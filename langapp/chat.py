import os

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.chat_history import BaseChatMessageHistory, InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.messages import AIMessage
from dotenv import load_dotenv
from colorama import init, Fore, Style

from langapp.llms import ChatContext
from langapp.prompts import custom_prompts

def create_directories(main: str, sub: str) -> None:
    os.makedirs(main, exist_ok=True)
    os.makedirs(os.path.join(main, sub), exist_ok=True)

# Initialize colorama
init()
# Load environment variables from .env file
load_dotenv()

class Llmlang():

    def __init__(self, openai: callable, model: callable, role: str, selected_model: str) -> None:
        self.openai = openai
        self.model = model
        self.role = role
        self.selected_model = selected_model
        self.store = {}
    
        print(f"\n{Fore.LIGHTBLUE_EX}{Style.NORMAL}Model: {self.selected_model}")
        print(f"{Fore.LIGHTBLUE_EX}{Style.NORMAL}Role: {self.role}")

        system_prompt = f" You are helpful, creative, clever, and very friendly assistant. {custom_prompts[self.role]}"

        prompt = ChatPromptTemplate.from_messages([
            ("user", system_prompt),  # Changed the role from system to user for the system prompt.
            MessagesPlaceholder(variable_name="history"),
            ("human", "{input}"),
        ])

        chain = prompt | self.model | StrOutputParser()
        
        def get_session_history(session_id: str) -> BaseChatMessageHistory:
            if session_id not in self.store:
                self.store[session_id] = InMemoryChatMessageHistory()
            return self.store[session_id]

        # Create a runnable that keeps track of the message history
        self.with_message_history = RunnableWithMessageHistory(
            chain,
            get_session_history,
            input_messages_key="input",
            history_messages_key="history",
        )
    # Chat on the command line
    async def chat_loop(self) -> None:

        print(f"{Style.RESET_ALL}\nI am your assistant. Give me a prompt according to my role!")

        while True:
            
            if prompt := input(f"\n{Fore.YELLOW}{Style.NORMAL}User: "):
                
                # Print the AI response
                print(f"{Fore.GREEN}{Style.NORMAL}AI: ", end='')
                
                # Stream the AI model response after prompting
                config = {"configurable": {"session_id": "chat"}}
                for response in self.with_message_history.stream({"input": prompt}, config=config):
                    print(response, end='', flush=True)
                
                # Translate the conversation to Hungarian if the role is correction
                if 'correct' in self.role or 'upgrade' in self.role:
                    print('\n')
                    latest_ai_message = self.store['chat'].messages[-1].content  # for message in store['chat'].messages: isinstance(message, AIMessage)
                    latest_human_message = self.store['chat'].messages[-2].content # ... isinstance(message, HumanMessage)
                    if 'is correct' in self.store['chat'].messages[-1].content:
                        translation = self.openai.invoke(f"Translate to Hungarian: {latest_human_message}").content
                    elif 'ist korrekt' in self.store['chat'].messages[-1].content:
                        translation = self.openai.invoke(f"Übersetze ins Ungarische: {latest_human_message}").content
                    else:
                        translation = self.openai.invoke(f"Translate to Hungarian: {latest_ai_message}").content
                    print(f"{Fore.CYAN}{Style.NORMAL}Translation: {translation}")

            else: 
                # Generate remarks if the role is 'correct ...'
                try:
                    conversation = self.store['chat'].messages
                except KeyError:  # This error occurs if the user provides an empty row as the first prompt.
                    break
                else:
                    if 'correct' in self.role or 'upgrade' in self.role:
                        remarks = ChatContext(conversation, 'provide remarks').generate()
                        print(f"\nRemarks:\n{remarks}")
                    else:
                        remarks = None
                
                # Ask a question to save or not to text file
                save = input("Do you want to save the conversation to a text file? (y/n): ")         
                
                if save.lower() == 'y':
                    
                    # Save the conversation to a text file
                    filename = ChatContext(conversation, "generate a filename").generate()
                    
                    # Make directories if not exists
                    dir = 'conversations'
                    create_directories(dir, self.role)
                    
                    with open(f"{dir}/{self.role}/{filename}.txt", 'w', encoding='UTF-8') as f:
                        f.write(f"Model: {self.selected_model}\n\n")
                        for message in conversation:
                            prefix = "AI" if isinstance(message, AIMessage) else "User"
                            f.write(f"{prefix}: {message.content}\n")
                        if remarks:
                            f.write(f"\nRemarks:\n{remarks}")
                    
                    print(f"Conversation saved to the file: {filename}.txt")
                
                break  # Exit the loop if the user enters an empty prompt
    


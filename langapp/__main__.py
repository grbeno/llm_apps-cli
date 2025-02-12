import argparse
import asyncio
from langapp.llms import Llms
import langapp.chat as chat

def main():
    
    parser = argparse.ArgumentParser(description="Script to process model and role")
    
    parser.add_argument(
        "--m",
        default="gpt-4o-mini",
        choices=[
            'gpt-4o-mini',
            'gpt-4o',
            'llama3.1',  # ollama
        ],
        help="The model to use (optional)"
    )

    # Add optional 'role' argument
    parser.add_argument(
        "--r",
        default="short and concise",
        choices=[
            'short and concise',
            'correct english',
            'correct german',
            'translate to english',
            'translate to german',
            'translate to spanish',
            'translate to french',
            'translate to hungarian',
            'generate a filename',
            'upgrade english',
            'remaster the conversation',
        ],
        help="The mode to response to the prompt (optional)"
    )

    # Parse arguments
    args = parser.parse_args()
    model = args.m
    role = args.r

    """ Apply the model """

    llm = Llms(model)
    openai = llm.openai_gpt()
    model = llm.get_model()
    selected_model = getattr(llm, 'model')

    model = chat.Llmlang(openai,model,role,selected_model)
    tool = model.chat_loop()

    try:
        # Call the async function to start the chat loop
        asyncio.run(tool)
    except EOFError or KeyboardInterrupt:  # ctrl + c
        print("\n\nGoodbye!")


if __name__ == "__main__":
    main()
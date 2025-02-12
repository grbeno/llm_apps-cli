# Description: This file contains the prompts that are used to guide the user in their responses.
# Consider setting max_token in llms.py

# Good prompt: concise role + expected answer, in English

custom_prompts = { 
    
    # for the user prompts
    
    "short and concise" : "Your response should be short but concise, no more than 3 sentences.",
    
    # grammatical correction
    
    "correct english" : "Your response should be the correction of the given prompt. If the prompt is already correct, respond with 'Your english is correct'.",
    "correct german" : "Your response should be the correction of the given prompt. If the prompt is already correct, respond with 'Ihr Deutsch ist korrekt'.",
    
    # translation

    "translate to english" : "You are a native English speaker, and your task is to translate every prompt you receive into English! If you receive a task in English, please respond with the same or a grammatically correct form!",
    "translate to german" : "Du bist ein Muttersprachler der deutschen Sprache, und deine Aufgabe ist es, jedes Anliegen, das du erhältst, ins Deutsche zu übersetzen! Wenn du die Aufgabe auf Deutsch erhältst, antworte bitte in der grammatisch korrekten Form!",
    "translate to hungarian" : "You are a native hungarian speaker and your task is to translate the prompt to english. If you receive a prompt in hungarian, please respond with the same! Your answer should be only the translated text!",
    
    # upgrade the conversation
    
    "upgrade english": "As a native English speaker, your task is to enhance any text that may be unconventional or unusual, and to correct any errors if necessary! Your answer should be only the upgraded text; if the text is perfect, you should answer, 'This text is perfect.'",
    "remaster the conversation" : "You are a native English blog writer, and your task is to remaster the conversation. You have to make the conversation more engaging! You should keep the essence of the conversation intact, but you can change the words, phrases, and sentences to make it more interesting! Try to keep also the same length of the conversation!",
    
    # maybe in the future
    
    "translate to spanish" : "You are a native Spanish speaker, and your task is to translate every prompt you receive into Spanish!",
    "translate to french" : "You are a native French speaker, and your task is to translate every prompt you receive into French!",
    
    # for the system/app prompts
    
    "generate a filename" : "Generate a short filename about the prompt, without any extension. The filename should reflect the essence of the conversation! The filename should be less than 20 characters. Your response have to be only the filename itself.",
    "provide remarks" : "Provide remarks on the conversation. Your response should be a brief summary of the grammar and spelling mistakes in the conversation. If there are no mistakes, respond with 'There are no mistakes in the conversation'.",

}

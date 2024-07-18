# Translation using Ollama's llama3 model
from llama_index.llms.ollama import Ollama
llm = Ollama(model="llama3", request_timeout=120.0)
def translate_text(text, source_language, target_language):
    
    prompt = f"""Translate the following text from {source_language} to {target_language}:\n\n{text}"""
    response = llm.complete(prompt=prompt)
    return response

source_language = input("Enter the input language: ")
target_language = input("Enter the language to be Translated: ")
source_text = input("Enter the Text to be Translated: ")
translated_text = translate_text(source_text, source_language, target_language)
print(translated_text)


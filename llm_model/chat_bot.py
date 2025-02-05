from langchain_groq import ChatGroq

from credentials import groq_creds

api_key = groq_creds.get("api_key")
model_name = groq_creds.get("model_name")


def chat_bot_llm():
    llm = ChatGroq(temperature=0, groq_api_key=api_key, model_name=model_name)
    return llm

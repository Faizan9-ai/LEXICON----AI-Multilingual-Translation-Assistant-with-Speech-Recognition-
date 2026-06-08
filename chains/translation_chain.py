
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0.2
)


def translate_text(text, source_language, target_language):
    prompt = ChatPromptTemplate.from_template("""
You are an expert multilingual translator.

Translate the text from {source_language} to {target_language}.
Preserve meaning, tone, grammar, and formatting.

Text:
{text}

Return only the translated text.
""")

    chain = prompt | llm
    response = chain.invoke({
        "text": text,
        "source_language": source_language,
        "target_language": target_language
    })

    return response.content
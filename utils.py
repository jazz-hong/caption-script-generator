import os

from dotenv import load_dotenv
from langfuse import Langfuse
from langfuse.callback import CallbackHandler
from langchain.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langchain_core.output_parsers import JsonOutputParser, StrOutputParser

load_dotenv()

# Initialize Langfuse client (prompt management)
langfuse = Langfuse(
    public_key=os.getenv("LANGFUSE_PUBLIC_KEY"),
    secret_key=os.getenv("LANGFUSE_SECRET_KEY"),
    host=os.getenv("LANGFUSE_HOST_URL"),
)

llama32_90b = ChatGroq(
                model="llama-3.2-90b-vision-preview",
                temperature=0.0,
                max_retries=2,
                api_key=os.getenv("GROQ_API_KEY")
                # other params...
            )

def generate_caption(theme):

    # ---CHAT PROMPT TEMPLATE---
    caption_generator_prompt = langfuse.get_prompt("caption-gen-chat", label="production", type="chat")
    caption_generator_prompt_langchain = ChatPromptTemplate.from_messages(caption_generator_prompt.get_langchain_prompt())
    
    caption_generator_chain = (
    caption_generator_prompt_langchain
    | llama32_90b
    | StrOutputParser()
    )
    # ---CHAT PROMPT TEMPLATE---

    result = caption_generator_chain.invoke({
        "theme": theme
    })
    return result

# ---------- TESTING ----------
# print(generate_caption("TANK 300越野车"))
# ---------- TESTING ----------
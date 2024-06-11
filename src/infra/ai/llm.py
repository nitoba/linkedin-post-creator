# from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI

from src.env import env

llm = ChatOpenAI(
    api_key=env.OPEN_AI_KEY,
    model=env.CHAT_MODEL,
    temperature=0.5,
    base_url=env.OPEN_AI_BASE_URL,
)

# llm = ChatGroq(
#     api_key=env.OPEN_AI_KEY,
#     model=env.CHAT_MODEL,
#     temperature=0.5,
# )

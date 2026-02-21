from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=32)

documents = [
    "A **large language model (LLM)** is a type of artificial‑intelligence system",
    "that learns to understand and generate human language by training on massive amounts of text data",
    "The “large” part refers to the sheer size of the model—tens of billions"
]

result = embedding.embed_documents(documents)
print(str(result))
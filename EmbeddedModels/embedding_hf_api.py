from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
import os

load_dotenv()

os.environ['HF_HOME'] = 'E:/huggingface_cache'

# It will download and run the model locally
embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

text = "A LLM is a type of artificial intelligence."

vector = embedding.embed_query(text)
print(str(vector))
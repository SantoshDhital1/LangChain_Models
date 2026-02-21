from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np  

load_dotenv()

embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

documents = [
    "Rohit Paudel, Nepal's cricket captain, anchors the batting with calm composure and tactical sharpness at just 23 years old.",
    "Dipendra Singh Airee, the explosive all-rounder, smashes quickfire 40s off 15 balls while taking crucial wickets.",
    "Sandeep Lamichhane, Nepal's mystery spinner, remains the go-to middle-overs wicket-taker with global league experience.",
    "Kushal Bhurtel, the aggressive opener, provides rapid starts blending timing and power at the top order.",
    "Gulshan Jha, 18-year-old prodigy, stuns with 5-wicket hauls and half-centuries, eyed for IPL all-rounder roles."
]

query = "Who is Rohit Lamichhane?"

doc_embedding = embedding.embed_documents(documents)
query_embedding = embedding.embed_query(query)

scores = cosine_similarity([query_embedding], doc_embedding)[0]


index, score = sorted(list(enumerate(scores)), key = lambda x: x[1])[-1]

print(query)
print(documents[index])
print("Similarity score is: ", score)
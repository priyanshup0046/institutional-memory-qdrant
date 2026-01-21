import google.generativeai as genai
import json
import os
from dotenv import load_dotenv
load_dotenv()
genai.configure(api_key=os.getenv("API_KEY"))

#embedding by google text embeddings
def build_embedding_text(memory):
    return " ".join(memory["core_reasoning"])

def embedd(text):
    response=genai.embed_content(model="text-embedding-004",content=text)
    return response["embedding"]




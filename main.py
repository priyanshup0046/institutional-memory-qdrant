import os
from dotenv import load_dotenv
import google.generativeai as genai

from memory.loader import load_memories
from memory.store import init_qdrant, store_memories
from search.query import search_memory
from memory.evolution import apply_dominance
from embeddings.embedd import embedd, build_embedding_text
from generation.answers import generate_answer


load_dotenv()
genai.configure(api_key=os.getenv("API_KEY"))


memories = load_memories()
client = init_qdrant()
store_memories(client, memories, embedd, build_embedding_text)


def call_llm(prompt):
    model = genai.GenerativeModel("gemini-2.5-flash")
    response = model.generate_content(prompt)
    return response.text


# User Query (Practical Case)

query = """
        I am a junior lawyer working on a case where a state government has been
        collecting mobile location data of citizens during protests through
        executive orders, without passing any legislation. The government is
        justifying this on grounds of national security.
        Based on current Supreme Court jurisprudence, is such surveillance
        constitutionally valid, and which judgments should I rely on?
        """


results = search_memory(client, query, embedd)
ranked = apply_dominance(results)


final_answer = generate_answer(
    call_llm,
    query,
    ranked_memories=ranked[:2]
)

print("\nFINAL ANSWER:\n")
print(final_answer)

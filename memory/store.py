from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance, PointStruct

def init_qdrant():
    client = QdrantClient(":memory:")
    client.recreate_collection(
        collection_name="institutional_memory",
        vectors_config=VectorParams(
            size=768,
            distance=Distance.COSINE
        )
    )
    return client

def store_memories(client, memories, embed_fn, build_text_fn):
    points = []
    for m in memories:
        vector = embed_fn(build_text_fn(m))
        points.append(
            PointStruct(
                id=m["memory_id"],
                vector=vector,
                payload={
                    "issue": m["issue"],
                    "stage": m["stage"],
                    "time_range": m["time_range"],
                    "dominance_score": 1.0,
                    "core_reasoning_text": " ".join(m["core_reasoning"]),

                    "linked_cases": m["linked_cases"]
                }
            )
        )
    client.upsert(
        collection_name="institutional_memory",
        points=points
    )

def search_memory(client, query_text, embed_fn, limit=3):
    return client.query_points(
        collection_name="institutional_memory",
        query=embed_fn(query_text),
        limit=limit,
        with_payload=True
    ).points

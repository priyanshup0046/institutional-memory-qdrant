def apply_dominance(results):
    """
    Re-rank retrieved memories using dominance_score.
    """
    return sorted(
        results,
        key=lambda r: r.score * r.payload.get("dominance_score", 1.0),
        reverse=True
    )


def reinforce_memory(client, memory_point, delta=0.3):
    """
    Increase dominance_score of a memory point.
    """
    old_score = memory_point.payload.get("dominance_score", 1.0)
    new_score = old_score + delta

    client.set_payload(
        collection_name="institutional_memory",
        payload={"dominance_score": new_score},
        points=[memory_point.id]
    )

    return new_score



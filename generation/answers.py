def build_prompt(query, ranked_memories):
    context_blocks = []

    for m in ranked_memories:
        cases = ", ".join(m.payload.get("linked_cases", []))

        context_blocks.append(
            f"""
Stage: {m.payload['stage']}
Time Period: {m.payload['time_range']}

Institutional Reasoning:
{m.payload.get('core_reasoning_text', '')}

Key Linked Cases:
{cases}
"""
        )

    context = "\n".join(context_blocks)

    prompt = f"""
You are a legal research assistant for Indian constitutional law.
IMPORTANT:
You are currently grounded only in institutional memory related to
the Right to Privacy under Article 21 of the Indian Constitution.

If the user’s question does NOT relate to privacy, surveillance,
personal liberty, or informational autonomy, you MUST clearly state
that the system is currently limited in scope and cannot provide a
reliable answer.


Below is the institutional memory of the Supreme Court,
ordered by current dominance (most influential first).

{context}

User Query:
{query}

TASK:
TASK:
1. Identify which institutional phase currently governs the legal outcome
   (not when the idea first appeared)
2. Explain the applicable constitutional reasoning
3. Cite the most relevant Supreme Court cases from the list above
4. Keep the answer practical, not academic
5.If the query is outside the scope of the available institutional memory,
respond with a clear limitation notice instead of guessing or generalizing.
"""

    return prompt



def generate_answer(llm_call_fn, query, ranked_memories):
    
    prompt = build_prompt(query, ranked_memories)
    return llm_call_fn(prompt)

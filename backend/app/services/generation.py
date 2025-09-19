from __future__ import annotations
from typing import List, Dict

DISCLAIMER = "This is general information for education only and not a medical diagnosis. Please consult a licensed clinician for personal medical advice."

def generate_answer_with_disclaimer(question: str, docs: List[Dict], temperature: float = 0.2):
    # Simple stub: concatenate top docs and echo a short answer for beginners.
    # Later, replace with Azure OpenAI call using the docs as context.
    context_bits = []
    for d in docs:
        context_bits.append(f"[Source: {d['id']}]\n{d['content']}")
    context = "\n\n".join(context_bits)[:1500]
    answer = f"Based on the available references, here are key points related to your question: '{question}'.\n\n"
    answer += "\n\n".join([f"- {line.strip()}" for line in context.splitlines() if line.strip().startswith("-")])
    citations = [{"title": d["id"], "url": None, "source": "kb"} for d in docs]
    return {"answer": answer, "citations": citations, "disclaimer": DISCLAIMER}

from __future__ import annotations
from pathlib import Path
import math

class InMemoryRetriever:
    """Very simple keyword retriever so beginners can run without Azure.
    Later you can swap with Azure AI Search by implementing the same interface.
    """
    def __init__(self, kb_dir: str | Path = None):
        self.kb_dir = Path(kb_dir or Path(__file__).parents[1] / "kb")
        self.docs = []
        for p in self.kb_dir.glob("*.md"):
            self.docs.append({"id": p.name, "content": p.read_text(encoding="utf-8")})
    
    def _score(self, query: str, content: str) -> float:
        tokens = query.lower().split()
        score = 0.0
        for t in tokens:
            score += content.lower().count(t)
        return score / math.sqrt(len(content) + 1)
    
    def retrieve(self, query: str, k: int = 5):
        ranked = sorted(self.docs, key=lambda d: self._score(query, d["content"]), reverse=True)
        return ranked[:k]

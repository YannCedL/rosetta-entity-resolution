def similarity_score(a: str, b: str) -> float:
    a, b = a.lower().strip(), b.lower().strip()
    if a == b:
        return 1.0
    common = set(a.split()) & set(b.split())
    total = set(a.split()) | set(b.split())
    return len(common) / len(total) if total else 0.0

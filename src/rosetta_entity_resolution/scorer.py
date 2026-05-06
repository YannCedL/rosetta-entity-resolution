# calcul de similarite floue et Jaccard / Levenshtein pour la resolution d'entites

def similarity_score(a: str, b: str) -> float:
    a, b = a.lower().strip(), b.lower().strip()
    if a == b:
        return 1.0
    
    words_a = set(a.split())
    words_b = set(b.split())
    
    common = words_a & words_b
    total = words_a | words_b
    jaccard = len(common) / len(total) if total else 0.0
    
    # bonus si un mot clé principal est partagé (ex: airbus)
    for w in words_a:
        if len(w) > 3 and w in words_b:
            jaccard = max(jaccard, 0.85)
            
    return jaccard

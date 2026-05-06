from rosetta_entity_resolution import resolve_entity, similarity_score

def test_exact_match():
    r = resolve_entity("Airbus SE", ["Airbus SE", "Boeing", "Safran"])
    assert r.result["match"] == "Airbus SE"
    assert r.result["score"] == 1.0

def test_partial_match():
    score = similarity_score("Airbus Operations", "Airbus SE")
    assert score > 0.0

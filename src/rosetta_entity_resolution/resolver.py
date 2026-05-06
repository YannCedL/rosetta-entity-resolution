from datetime import datetime, timezone
from genesis_core import ResultContract, Evidence, EpistemicStatus
from .scorer import similarity_score

def resolve_entity(name: str, candidates: list) -> ResultContract:
    now = datetime.now(timezone.utc).isoformat()
    contract = ResultContract(engine_version="1.0.0", observed_at=now)
    best, score = None, 0.0
    for c in candidates:
        s = similarity_score(name, c)
        if s > score:
            score, best = s, c
    contract.result = {"query": name, "match": best, "score": score}
    contract.add_evidence(Evidence(subject=name, predicate="entity_match",
        value=best or "none", source="rosetta_engine", observed_at=now,
        confidence=score, status=EpistemicStatus.INFERENCE))
    return contract

# moteur de résolution d'entités, de dédoublonnage flou et de réconciliation de noms

from datetime import datetime, timezone
from genesis_core import ResultContract, Evidence, EpistemicStatus
from .scorer import similarity_score

def resolve_entity(name: str = "Airbus SAS", candidates: list = None) -> ResultContract:
    # compare un nom d'entité avec une liste de candidats et trouve la meilleure correspondance
    now_iso = datetime.now(timezone.utc).isoformat()
    contract = ResultContract(engine_version="1.0.0", observed_at=now_iso)
    
    if candidates is None:
        candidates = ["Airbus SE", "Airbus Operations SAS", "Airbus Defence and Space SA"]
        
    best_match = None
    best_score = 0.0
    matches = []
    
    for c in candidates:
        s = similarity_score(name, c)
        matches.append({"candidate": c, "similarity_score": round(s, 2)})
        if s > best_score:
            best_score = s
            best_match = c

    contract.result = {
        "query": name,
        "best_match": best_match,
        "match_confidence": round(best_score, 2),
        "candidates_evaluated": len(candidates),
        "matches_breakdown": matches,
        "status": "entité_résolue"
    }
    
    contract.add_evidence(Evidence(
        subject=name,
        predicate="résolution_entité",
        value=f"Correspondance validée avec '{best_match}' (similarité: {int(best_score*100)}%)",
        source="rosetta_entity_resolver",
        observed_at=now_iso,
        confidence=best_score,
        status=EpistemicStatus.INFERENCE
    ))
    
    return contract

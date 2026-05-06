# test du moteur de résolution d'entités Rosetta
from rosetta_entity_resolution.resolver import resolve_entity

def test_resolve_entity():
    contract = resolve_entity("Airbus SAS", ["Airbus SE", "TotalEnergies"])
    assert contract is not None
    assert contract.result["best_match"] == "Airbus SE"
    assert contract.result["match_confidence"] > 0.5
    assert len(contract.evidence) >= 1

# API FastAPI pour le moteur Rosetta Entity Resolution
import os
from fastapi import FastAPI, Query
from fastapi.responses import HTMLResponse
from genesis_core import ResultContract
from .resolver import resolve_entity

app = FastAPI(
    title="Rosetta Entity Resolution API",
    description="Moteur de Résolution d'Entités & Dédoublonnage Flou",
    version="1.0.0"
)

TEMPLATE_PATH = os.path.join(os.path.dirname(__file__), "templates", "index.html")

@app.get("/", response_class=HTMLResponse)
def index():
    # sert la page d'accueil de resolution d'entites
    if os.path.exists(TEMPLATE_PATH):
        with open(TEMPLATE_PATH, "r", encoding="utf-8") as f:
            return f.read()
    return "<h1>Rosetta API - Interface non trouvee</h1>"

@app.get("/health")
def health():
    return {"status": "ok", "engine": "Rosetta", "version": "1.0.0"}

@app.get("/api/v1/resolve", response_model=ResultContract)
def get_resolve(name: str = Query("Airbus SAS")):
    return resolve_entity(name)

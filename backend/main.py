"""
Lumeval Backend: A FastAPI server that runs DeepEval evaluations on LLM-based projects and returns results as JSON. It currently evaluates MatchForge and Scoute, but it can support additional projects in the future.
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from evaluators.matchforge_evaluator import run_matchforge_evaluation
from evaluators.scoute_evaluator import run_scoute_evaluation

app = FastAPI(title="Lumeval API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://lumeval.vercel.app"],
    allow_methods=["*"],
    allow_headers=["*"],
)

_cache = {}

@app.get("/")
def root():
    return {"message": "Lumeval API is running"}

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.get("/evaluate/matchforge")
def evaluate_matchforge():
    if "matchforge" not in _cache:
        try:
            _cache["matchforge"] = run_matchforge_evaluation()
        except Exception as e:
            raise HTTPException(status_code=503, detail=str(e))
    return _cache["matchforge"]

@app.get("/evaluate/scoute")
def evaluate_scoute():
    if "scoute" not in _cache:
        try:
            _cache["scoute"] = run_scoute_evaluation()
        except Exception as e:
            raise HTTPException(status_code=503, detail=str(e))
    return _cache["scoute"]

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
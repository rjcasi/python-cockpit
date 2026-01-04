from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from db import Database

app = FastAPI()

# CORS so React (localhost:3000) can call FastAPI (localhost:8000)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

db = Database()

# -----------------------------
# Evolution Runs
# -----------------------------
@app.get("/evolution/runs")
def get_runs():
    query = "SELECT * FROM evolution_runs ORDER BY created_at DESC"
    return db.fetchall(query)


@app.get("/evolution/runs/{run_id}")
def get_run(run_id: int):
    query = "SELECT * FROM evolution_runs WHERE id = ?"
    return db.fetchone(query, (run_id,))


# -----------------------------
# Generations
# -----------------------------
@app.get("/evolution/runs/{run_id}/generations")
def get_generations(run_id: int):
    query = """
        SELECT * FROM evolution_generations
        WHERE run_id = ?
        ORDER BY generation_index ASC
    """
    return db.fetchall(query, (run_id,))


@app.get("/evolution/generations/{generation_id}")
def get_generation(generation_id: int):
    query = "SELECT * FROM evolution_generations WHERE id = ?"
    return db.fetchone(query, (generation_id,))


# -----------------------------
# Agents
# -----------------------------
@app.get("/evolution/generations/{generation_id}/agents")
def get_agents_for_generation(generation_id: int):
    query = """
        SELECT * FROM evolution_agents
        WHERE generation_id = ?
        ORDER BY fitness DESC
    """
    return db.fetchall(query, (generation_id,))


@app.get("/evolution/agents/{agent_id}")
def get_agent(agent_id: int):
    query = "SELECT * FROM evolution_agents WHERE id = ?"
    return db.fetchone(query, (agent_id,))

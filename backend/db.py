import sqlite3
from typing import Any, Dict, List, Optional


class Database:
    def __init__(self, path: str = "cyberarena.db"):
        self.path = path
        self.conn = sqlite3.connect(self.path)
        self.conn.row_factory = sqlite3.Row
        self.cur = self.conn.cursor()

    # ============================
    # Core Helpers
    # ============================
    def execute(self, query: str, params: tuple = ()) -> None:
        self.cur.execute(query, params)
        self.conn.commit()

    def fetchone(self, query: str, params: tuple = ()) -> Optional[sqlite3.Row]:
        self.cur.execute(query, params)
        return self.cur.fetchone()

    def fetchall(self, query: str, params: tuple = ()) -> List[sqlite3.Row]:
        self.cur.execute(query, params)
        return self.cur.fetchall()

    # ============================
    # Agents
    # ============================
    def create_agent(self, name: str, type: str) -> int:
        self.execute(
            "INSERT INTO agents (name, type) VALUES (?, ?)",
            (name, type),
        )
        return self.cur.lastrowid

    def get_agent(self, agent_id: int):
        return self.fetchone("SELECT * FROM agents WHERE id = ?", (agent_id,))

    # ============================
    # Memory Organ
    # ============================
    def add_memory_event(self, agent_id: int, event_type: str, content: str) -> int:
        self.execute(
            "INSERT INTO memory_events (agent_id, event_type, content, timestamp) "
            "VALUES (?, ?, ?, datetime('now'))",
            (agent_id, event_type, content),
        )
        return self.cur.lastrowid

    def add_memory_embedding(self, event_id: int, vector: bytes, model: str) -> int:
        self.execute(
            "INSERT INTO memory_embeddings (memory_event_id, vector, model) "
            "VALUES (?, ?, ?)",
            (event_id, vector, model),
        )
        return self.cur.lastrowid

    def link_memory_events(self, src: int, dst: int, relation: str, weight: float):
        self.execute(
            "INSERT INTO memory_links (source_event_id, target_event_id, relation, weight) "
            "VALUES (?, ?, ?, ?)",
            (src, dst, relation, weight),
        )

    # ============================
    # Replay Organ
    # ============================
    def start_replay_session(self, agent_id: int, scenario: str) -> int:
        self.execute(
            "INSERT INTO replay_sessions (agent_id, scenario_name, started_at) "
            "VALUES (?, ?, datetime('now'))",
            (agent_id, scenario),
        )
        return self.cur.lastrowid

    def end_replay_session(self, session_id: int):
        self.execute(
            "UPDATE replay_sessions SET ended_at = datetime('now') WHERE id = ?",
            (session_id,),
        )

    def add_replay_event(self, session_id: int, event_type: str, payload: str):
        self.execute(
            "INSERT INTO replay_events (session_id, event_type, payload, timestamp) "
            "VALUES (?, ?, ?, datetime('now'))",
            (session_id, event_type, payload),
        )

    def add_replay_snapshot(self, session_id: int, state_json: str):
        self.execute(
            "INSERT INTO replay_state_snapshots (session_id, state_json, timestamp) "
            "VALUES (?, ?, datetime('now'))",
            (session_id, state_json),
        )

    # ============================
    # Telemetry Organ
    # ============================
    def add_telemetry(
        self,
        agent_id: int,
        cpu: float,
        memory: float,
        net_in: float,
        net_out: float,
        custom_metrics: str = "",
    ):
        self.execute(
            "INSERT INTO telemetry_events "
            "(agent_id, cpu, memory, network_in, network_out, custom_metrics, timestamp) "
            "VALUES (?, ?, ?, ?, ?, ?, datetime('now'))",
            (agent_id, cpu, memory, net_in, net_out, custom_metrics),
        )

    def add_telemetry_rollup(
        self,
        agent_id: int,
        window_start: str,
        window_end: str,
        cpu_avg: float,
        mem_avg: float,
        net_in: float,
        net_out: float,
        custom_metrics: str = "",
    ):
        self.execute(
            "INSERT INTO telemetry_rollups "
            "(agent_id, window_start, window_end, cpu_avg, mem_avg, net_in, net_out, custom_metrics) "
            "VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
            (
                agent_id,
                window_start,
                window_end,
                cpu_avg,
                mem_avg,
                net_in,
                net_out,
                custom_metrics,
            ),
        )

    # ============================
    # Curriculum Organ
    # ============================
    def add_lesson(self, module: str, name: str, description: str, difficulty: int) -> int:
        self.execute(
            "INSERT INTO curriculum_lessons (module, lesson_name, description, difficulty) "
            "VALUES (?, ?, ?, ?)",
            (module, name, description, difficulty),
        )
        return self.cur.lastrowid

    def add_lab(self, lesson_id: int, name: str, instructions: str, expected_output: str) -> int:
        self.execute(
            "INSERT INTO curriculum_labs (lesson_id, lab_name, instructions, expected_output) "
            "VALUES (?, ?, ?, ?)",
            (lesson_id, name, instructions, expected_output),
        )
        return self.cur.lastrowid

    def update_progress(self, agent_id: int, lesson_id: int, status: str):
        self.execute(
            "INSERT INTO curriculum_progress (agent_id, lesson_id, status, updated_at) "
            "VALUES (?, ?, ?, datetime('now'))",
            (agent_id, lesson_id, status),
        )

    # ============================
    # Behavior Organ
    # ============================
    def add_behavior_event(self, agent_id: int, behavior_type: str, metadata: str):
        self.execute(
            "INSERT INTO behavior_events (agent_id, behavior_type, metadata, timestamp) "
            "VALUES (?, ?, ?, datetime('now'))",
            (agent_id, behavior_type, metadata),
        )

    def add_behavior_pattern(
        self, agent_id: int, name: str, description: str, severity: int
    ) -> int:
        self.execute(
            "INSERT INTO behavior_patterns (agent_id, pattern_name, description, severity, detected_at) "
            "VALUES (?, ?, ?, ?, datetime('now'))",
            (agent_id, name, description, severity),
        )
        return self.cur.lastrowid

    def link_behavior_pattern(self, pattern_id: int, event_id: int):
        self.execute(
            "INSERT INTO behavior_pattern_links (pattern_id, event_id) VALUES (?, ?)",
            (pattern_id, event_id),
        )

    # ============================
    # Graph Organ
    # ============================
    def add_graph_node(self, agent_id: int, label: str, properties: str) -> int:
        self.execute(
            "INSERT INTO graph_nodes (agent_id, label, properties) VALUES (?, ?, ?)",
            (agent_id, label, properties),
        )
        return self.cur.lastrowid

    def add_graph_edge(self, src: int, dst: int, relation: str, weight: float):
        self.execute(
            "INSERT INTO graph_edges (source_node_id, target_node_id, relation, weight) "
            "VALUES (?, ?, ?, ?)",
            (src, dst, relation, weight),
        )

    def add_graph_snapshot(self, snapshot_json: str):
        self.execute(
            "INSERT INTO graph_snapshots (snapshot_json, timestamp) "
            "VALUES (?, datetime('now'))",
            (snapshot_json,),
        )

    # ============================
    # SSH Organ
    # ============================
    def start_ssh_session(self, agent_id: int) -> int:
        self.execute(
            "INSERT INTO ssh_sessions (agent_id, started_at) VALUES (?, datetime('now'))",
            (agent_id,),
        )
        return self.cur.lastrowid

    def end_ssh_session(self, session_id: int):
        self.execute(
            "UPDATE ssh_sessions SET ended_at = datetime('now') WHERE id = ?",
            (session_id,),
        )

    def add_ssh_command(self, session_id: int, command: str, exit_code: int):
        self.execute(
            "INSERT INTO ssh_commands (session_id, command, exit_code, timestamp) "
            "VALUES (?, ?, ?, datetime('now'))",
            (session_id, command, exit_code),
        )

    def add_ssh_stream(self, session_id: int, stream_type: str, content: str):
        self.execute(
            "INSERT INTO ssh_stream (session_id, stream_type, content, timestamp) "
            "VALUES (?, ?, ?, datetime('now'))",
            (session_id, stream_type, content),
        )

    # ============================
    # Scoring Organ
    # ============================
    def add_rubric(self, name: str, description: str) -> int:
        self.execute(
            "INSERT INTO score_rubrics (rubric_name, description) VALUES (?, ?)",
            (name, description),
        )
        return self.cur.lastrowid

    def add_criterion(self, rubric_id: int, name: str, weight: float, description: str):
        self.execute(
            "INSERT INTO score_criteria (rubric_id, criterion_name, weight, description) "
            "VALUES (?, ?, ?, ?)",
            (rubric_id, name, weight, description),
        )

    def add_score(self, agent_id: int, rubric_id: int, score: float):
        self.execute(
            "INSERT INTO scores (agent_id, rubric_id, score, timestamp) "
            "VALUES (?, ?, ?, datetime('now'))",
            (agent_id, rubric_id, score),
        )


    # ============================
    # Evolution Organ
    # ============================

    def create_evolution_run(self, name: str, description: str) -> int:
        self.execute(
            "INSERT INTO evolution_runs (name, description, status) VALUES (?, ?, 'running')",
            (name, description),
        )
        return self.cur.lastrowid

    def complete_evolution_run(self, run_id: int):
        self.execute(
            "UPDATE evolution_runs SET status = 'completed' WHERE id = ?",
            (run_id,),
        )

    def create_generation(self, run_id: int, generation_index: int) -> int:
        self.execute(
            "INSERT INTO evolution_generations (run_id, generation_index) VALUES (?, ?)",
            (run_id, generation_index),
        )
        return self.cur.lastrowid

    def add_agent_instance(self, generation_id: int, agent_id: int, genome_json: str) -> int:
        self.execute(
            "INSERT INTO evolution_agent_instances (generation_id, agent_id, genome_json, fitness) "
            "VALUES (?, ?, ?, NULL)",
            (generation_id, agent_id, genome_json),
        )
        return self.cur.lastrowid

    def set_agent_fitness(self, instance_id: int, fitness: float):
        self.execute(
            "UPDATE evolution_agent_instances SET fitness = ? WHERE id = ?",
            (fitness, instance_id),
        )

    def get_generation_instances(self, generation_id: int):
        return self.fetchall(
            "SELECT * FROM evolution_agent_instances WHERE generation_id = ?",
            (generation_id,),
        )

    def get_best_instances(self, generation_id: int, top_k: int = 3):
        return self.fetchall(
            "SELECT * FROM evolution_agent_instances "
            "WHERE generation_id = ? AND fitness IS NOT NULL "
            "ORDER BY fitness DESC LIMIT ?",
            (generation_id, top_k),
        )

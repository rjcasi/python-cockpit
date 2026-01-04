-- ============================================
-- CyberArena Unified Schema (v1)
-- ============================================

PRAGMA foreign_keys = ON;

-- ============================
-- 1. Agents
-- ============================
CREATE TABLE agents (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    type TEXT,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP
);

-- ============================
-- 2. Memory Organ
-- ============================
CREATE TABLE memory_events (
    id INTEGER PRIMARY KEY,
    agent_id INTEGER,
    timestamp TEXT,
    event_type TEXT,
    content TEXT,
    FOREIGN KEY(agent_id) REFERENCES agents(id)
);

CREATE TABLE memory_embeddings (
    id INTEGER PRIMARY KEY,
    memory_event_id INTEGER,
    vector BLOB,
    model TEXT,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(memory_event_id) REFERENCES memory_events(id)
);

CREATE TABLE memory_links (
    id INTEGER PRIMARY KEY,
    source_event_id INTEGER,
    target_event_id INTEGER,
    relation TEXT,
    weight REAL,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(source_event_id) REFERENCES memory_events(id),
    FOREIGN KEY(target_event_id) REFERENCES memory_events(id)
);

-- ============================
-- 3. Replay Organ
-- ============================
CREATE TABLE replay_sessions (
    id INTEGER PRIMARY KEY,
    agent_id INTEGER,
    scenario_name TEXT,
    started_at TEXT,
    ended_at TEXT,
    notes TEXT,
    FOREIGN KEY(agent_id) REFERENCES agents(id)
);

CREATE TABLE replay_events (
    id INTEGER PRIMARY KEY,
    session_id INTEGER,
    timestamp TEXT,
    event_type TEXT,
    payload TEXT,
    FOREIGN KEY(session_id) REFERENCES replay_sessions(id)
);

CREATE TABLE replay_state_snapshots (
    id INTEGER PRIMARY KEY,
    session_id INTEGER,
    timestamp TEXT,
    state_json TEXT,
    FOREIGN KEY(session_id) REFERENCES replay_sessions(id)
);

-- ============================
-- 4. Telemetry Organ
-- ============================
CREATE TABLE telemetry_events (
    id INTEGER PRIMARY KEY,
    agent_id INTEGER,
    timestamp TEXT,
    cpu REAL,
    memory REAL,
    network_in REAL,
    network_out REAL,
    custom_metrics TEXT,
    FOREIGN KEY(agent_id) REFERENCES agents(id)
);

CREATE TABLE telemetry_rollups (
    id INTEGER PRIMARY KEY,
    agent_id INTEGER,
    window_start TEXT,
    window_end TEXT,
    cpu_avg REAL,
    mem_avg REAL,
    net_in REAL,
    net_out REAL,
    custom_metrics TEXT,
    FOREIGN KEY(agent_id) REFERENCES agents(id)
);

-- ============================
-- 5. Curriculum Organ
-- ============================
CREATE TABLE curriculum_lessons (
    id INTEGER PRIMARY KEY,
    module TEXT,
    lesson_name TEXT,
    description TEXT,
    difficulty INTEGER,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE curriculum_labs (
    id INTEGER PRIMARY KEY,
    lesson_id INTEGER,
    lab_name TEXT,
    instructions TEXT,
    expected_output TEXT,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(lesson_id) REFERENCES curriculum_lessons(id)
);

CREATE TABLE curriculum_progress (
    id INTEGER PRIMARY KEY,
    agent_id INTEGER,
    lesson_id INTEGER,
    status TEXT,
    updated_at TEXT DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(agent_id) REFERENCES agents(id),
    FOREIGN KEY(lesson_id) REFERENCES curriculum_lessons(id)
);

-- ============================
-- 6. Behavior Organ
-- ============================
CREATE TABLE behavior_events (
    id INTEGER PRIMARY KEY,
    agent_id INTEGER,
    timestamp TEXT,
    behavior_type TEXT,
    metadata TEXT,
    FOREIGN KEY(agent_id) REFERENCES agents(id)
);

CREATE TABLE behavior_patterns (
    id INTEGER PRIMARY KEY,
    agent_id INTEGER,
    pattern_name TEXT,
    description TEXT,
    severity INTEGER,
    detected_at TEXT,
    FOREIGN KEY(agent_id) REFERENCES agents(id)
);

CREATE TABLE behavior_pattern_links (
    id INTEGER PRIMARY KEY,
    pattern_id INTEGER,
    event_id INTEGER,
    FOREIGN KEY(pattern_id) REFERENCES behavior_patterns(id),
    FOREIGN KEY(event_id) REFERENCES behavior_events(id)
);

-- ============================
-- 7. Graph Organ
-- ============================
CREATE TABLE graph_nodes (
    id INTEGER PRIMARY KEY,
    agent_id INTEGER,
    label TEXT,
    properties TEXT,
    FOREIGN KEY(agent_id) REFERENCES agents(id)
);

CREATE TABLE graph_edges (
    id INTEGER PRIMARY KEY,
    source_node_id INTEGER,
    target_node_id INTEGER,
    relation TEXT,
    weight REAL,
    FOREIGN KEY(source_node_id) REFERENCES graph_nodes(id),
    FOREIGN KEY(target_node_id) REFERENCES graph_nodes(id)
);

CREATE TABLE graph_snapshots (
    id INTEGER PRIMARY KEY,
    timestamp TEXT,
    snapshot_json TEXT
);

-- ============================
-- 8. SSH Organ
-- ============================
CREATE TABLE ssh_sessions (
    id INTEGER PRIMARY KEY,
    agent_id INTEGER,
    started_at TEXT,
    ended_at TEXT,
    FOREIGN KEY(agent_id) REFERENCES agents(id)
);

CREATE TABLE ssh_commands (
    id INTEGER PRIMARY KEY,
    session_id INTEGER,
    timestamp TEXT,
    command TEXT,
    exit_code INTEGER,
    FOREIGN KEY(session_id) REFERENCES ssh_sessions(id)
);

CREATE TABLE ssh_stream (
    id INTEGER PRIMARY KEY,
    session_id INTEGER,
    timestamp TEXT,
    stream_type TEXT,
    content TEXT,
    FOREIGN KEY(session_id) REFERENCES ssh_sessions(id)
);

-- ============================
-- 9. Scoring Organ
-- ============================
CREATE TABLE score_rubrics (
    id INTEGER PRIMARY KEY,
    rubric_name TEXT,
    description TEXT,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE score_criteria (
    id INTEGER PRIMARY KEY,
    rubric_id INTEGER,
    criterion_name TEXT,
    weight REAL,
    description TEXT,
    FOREIGN KEY(rubric_id) REFERENCES score_rubrics(id)
);

CREATE TABLE scores (
    id INTEGER PRIMARY KEY,
    agent_id INTEGER,
    rubric_id INTEGER,
    score REAL,
    timestamp TEXT,
    FOREIGN KEY(agent_id) REFERENCES agents(id),
    FOREIGN KEY(rubric_id) REFERENCES score_rubrics(id)
);

-- ============================
-- 10. Evolution Organ
-- ============================

CREATE TABLE IF NOT EXISTS evolution_runs (
    id INTEGER PRIMARY KEY,
    name TEXT,
    description TEXT,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP,
    status TEXT
);

CREATE TABLE IF NOT EXISTS evolution_generations (
    id INTEGER PRIMARY KEY,
    run_id INTEGER,
    generation_index INTEGER,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(run_id) REFERENCES evolution_runs(id)
);

CREATE TABLE IF NOT EXISTS evolution_agent_instances (
    id INTEGER PRIMARY KEY,
    generation_id INTEGER,
    agent_id INTEGER,
    genome_json TEXT,
    fitness REAL,
    FOREIGN KEY(generation_id) REFERENCES evolution_generations(id),
    FOREIGN KEY(agent_id) REFERENCES agents(id)
);

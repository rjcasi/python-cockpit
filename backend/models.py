from sqlalchemy import (
    Column, Integer, String, Float, Text, ForeignKey, DateTime
)
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime

Base = declarative_base()


# ============================================
# 1. Agents
# ============================================
class Agent(Base):
    __tablename__ = "agents"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    type = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationships
    memory_events = relationship("MemoryEvent", back_populates="agent")
    replay_sessions = relationship("ReplaySession", back_populates="agent")
    telemetry_events = relationship("TelemetryEvent", back_populates="agent")
    curriculum_progress = relationship("CurriculumProgress", back_populates="agent")
    behavior_events = relationship("BehaviorEvent", back_populates="agent")
    behavior_patterns = relationship("BehaviorPattern", back_populates="agent")
    graph_nodes = relationship("GraphNode", back_populates="agent")
    ssh_sessions = relationship("SSHSession", back_populates="agent")
    scores = relationship("Score", back_populates="agent")


# ============================================
# 2. Memory Organ
# ============================================
class MemoryEvent(Base):
    __tablename__ = "memory_events"

    id = Column(Integer, primary_key=True)
    agent_id = Column(Integer, ForeignKey("agents.id"))
    timestamp = Column(DateTime, default=datetime.utcnow)
    event_type = Column(String)
    content = Column(Text)

    agent = relationship("Agent", back_populates="memory_events")
    embeddings = relationship("MemoryEmbedding", back_populates="event")
    outgoing_links = relationship(
        "MemoryLink", foreign_keys="MemoryLink.source_event_id", back_populates="source"
    )
    incoming_links = relationship(
        "MemoryLink", foreign_keys="MemoryLink.target_event_id", back_populates="target"
    )


class MemoryEmbedding(Base):
    __tablename__ = "memory_embeddings"

    id = Column(Integer, primary_key=True)
    memory_event_id = Column(Integer, ForeignKey("memory_events.id"))
    vector = Column(Text)  # store serialized list
    model = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

    event = relationship("MemoryEvent", back_populates="embeddings")


class MemoryLink(Base):
    __tablename__ = "memory_links"

    id = Column(Integer, primary_key=True)
    source_event_id = Column(Integer, ForeignKey("memory_events.id"))
    target_event_id = Column(Integer, ForeignKey("memory_events.id"))
    relation = Column(String)
    weight = Column(Float)
    created_at = Column(DateTime, default=datetime.utcnow)

    source = relationship("MemoryEvent", foreign_keys=[source_event_id], back_populates="outgoing_links")
    target = relationship("MemoryEvent", foreign_keys=[target_event_id], back_populates="incoming_links")


# ============================================
# 3. Replay Organ
# ============================================
class ReplaySession(Base):
    __tablename__ = "replay_sessions"

    id = Column(Integer, primary_key=True)
    agent_id = Column(Integer, ForeignKey("agents.id"))
    scenario_name = Column(String)
    started_at = Column(DateTime, default=datetime.utcnow)
    ended_at = Column(DateTime)
    notes = Column(Text)

    agent = relationship("Agent", back_populates="replay_sessions")
    events = relationship("ReplayEvent", back_populates="session")
    snapshots = relationship("ReplayStateSnapshot", back_populates="session")


class ReplayEvent(Base):
    __tablename__ = "replay_events"

    id = Column(Integer, primary_key=True)
    session_id = Column(Integer, ForeignKey("replay_sessions.id"))
    timestamp = Column(DateTime, default=datetime.utcnow)
    event_type = Column(String)
    payload = Column(Text)

    session = relationship("ReplaySession", back_populates="events")


class ReplayStateSnapshot(Base):
    __tablename__ = "replay_state_snapshots"

    id = Column(Integer, primary_key=True)
    session_id = Column(Integer, ForeignKey("replay_sessions.id"))
    timestamp = Column(DateTime, default=datetime.utcnow)
    state_json = Column(Text)

    session = relationship("ReplaySession", back_populates="snapshots")


# ============================================
# 4. Telemetry Organ
# ============================================
class TelemetryEvent(Base):
    __tablename__ = "telemetry_events"

    id = Column(Integer, primary_key=True)
    agent_id = Column(Integer, ForeignKey("agents.id"))
    timestamp = Column(DateTime, default=datetime.utcnow)
    cpu = Column(Float)
    memory = Column(Float)
    network_in = Column(Float)
    network_out = Column(Float)
    custom_metrics = Column(Text)

    agent = relationship("Agent", back_populates="telemetry_events")


class TelemetryRollup(Base):
    __tablename__ = "telemetry_rollups"

    id = Column(Integer, primary_key=True)
    agent_id = Column(Integer, ForeignKey("agents.id"))
    window_start = Column(DateTime)
    window_end = Column(DateTime)
    cpu_avg = Column(Float)
    mem_avg = Column(Float)
    net_in = Column(Float)
    net_out = Column(Float)
    custom_metrics = Column(Text)


# ============================================
# 5. Curriculum Organ
# ============================================
class CurriculumLesson(Base):
    __tablename__ = "curriculum_lessons"

    id = Column(Integer, primary_key=True)
    module = Column(String)
    lesson_name = Column(String)
    description = Column(Text)
    difficulty = Column(Integer)
    created_at = Column(DateTime, default=datetime.utcnow)

    labs = relationship("CurriculumLab", back_populates="lesson")


class CurriculumLab(Base):
    __tablename__ = "curriculum_labs"

    id = Column(Integer, primary_key=True)
    lesson_id = Column(Integer, ForeignKey("curriculum_lessons.id"))
    lab_name = Column(String)
    instructions = Column(Text)
    expected_output = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)

    lesson = relationship("CurriculumLesson", back_populates="labs")


class CurriculumProgress(Base):
    __tablename__ = "curriculum_progress"

    id = Column(Integer, primary_key=True)
    agent_id = Column(Integer, ForeignKey("agents.id"))
    lesson_id = Column(Integer, ForeignKey("curriculum_lessons.id"))
    status = Column(String)
    updated_at = Column(DateTime, default=datetime.utcnow)

    agent = relationship("Agent", back_populates="curriculum_progress")
    lesson = relationship("CurriculumLesson")


# ============================================
# 6. Behavior Organ
# ============================================
class BehaviorEvent(Base):
    __tablename__ = "behavior_events"

    id = Column(Integer, primary_key=True)
    agent_id = Column(Integer, ForeignKey("agents.id"))
    timestamp = Column(DateTime, default=datetime.utcnow)
    behavior_type = Column(String)
    metadata = Column(Text)

    agent = relationship("Agent", back_populates="behavior_events")


class BehaviorPattern(Base):
    __tablename__ = "behavior_patterns"

    id = Column(Integer, primary_key=True)
    agent_id = Column(Integer, ForeignKey("agents.id"))
    pattern_name = Column(String)
    description = Column(Text)
    severity = Column(Integer)
    detected_at = Column(DateTime, default=datetime.utcnow)

    agent = relationship("Agent", back_populates="behavior_patterns")
    links = relationship("BehaviorPatternLink", back_populates="pattern")


class BehaviorPatternLink(Base):
    __tablename__ = "behavior_pattern_links"

    id = Column(Integer, primary_key=True)
    pattern_id = Column(Integer, ForeignKey("behavior_patterns.id"))
    event_id = Column(Integer, ForeignKey("behavior_events.id"))

    pattern = relationship("BehaviorPattern", back_populates="links")
    event = relationship("BehaviorEvent")


# ============================================
# 7. Graph Organ
# ============================================
class GraphNode(Base):
    __tablename__ = "graph_nodes"

    id = Column(Integer, primary_key=True)
    agent_id = Column(Integer, ForeignKey("agents.id"))
    label = Column(String)
    properties = Column(Text)

    agent = relationship("Agent", back_populates="graph_nodes")
    outgoing_edges = relationship(
        "GraphEdge", foreign_keys="GraphEdge.source_node_id", back_populates="source"
    )
    incoming_edges = relationship(
        "GraphEdge", foreign_keys="GraphEdge.target_node_id", back_populates="target"
    )


class GraphEdge(Base):
    __tablename__ = "graph_edges"

    id = Column(Integer, primary_key=True)
    source_node_id = Column(Integer, ForeignKey("graph_nodes.id"))
    target_node_id = Column(Integer, ForeignKey("graph_nodes.id"))
    relation = Column(String)
    weight = Column(Float)

    source = relationship("GraphNode", foreign_keys=[source_node_id], back_populates="outgoing_edges")
    target = relationship("GraphNode", foreign_keys=[target_node_id], back_populates="incoming_edges")


class GraphSnapshot(Base):
    __tablename__ = "graph_snapshots"

    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
    snapshot_json = Column(Text)


# ============================================
# 8. SSH Organ
# ============================================
class SSHSession(Base):
    __tablename__ = "ssh_sessions"

    id = Column(Integer, primary_key=True)
    agent_id = Column(Integer, ForeignKey("agents.id"))
    started_at = Column(DateTime, default=datetime.utcnow)
    ended_at = Column(DateTime)

    agent = relationship("Agent", back_populates="ssh_sessions")
    commands = relationship("SSHCommand", back_populates="session")
    streams = relationship("SSHStream", back_populates="session")


class SSHCommand(Base):
    __tablename__ = "ssh_commands"

    id = Column(Integer, primary_key=True)
    session_id = Column(Integer, ForeignKey("ssh_sessions.id"))
    timestamp = Column(DateTime, default=datetime.utcnow)
    command = Column(Text)
    exit_code = Column(Integer)

    session = relationship("SSHSession", back_populates="commands")


class SSHStream(Base):
    __tablename__ = "ssh_stream"

    id = Column(Integer, primary_key=True)
    session_id = Column(Integer, ForeignKey("ssh_sessions.id"))
    timestamp = Column(DateTime, default=datetime.utcnow)
    stream_type = Column(String)
    content = Column(Text)

    session = relationship("SSHSession", back_populates="streams")


# ============================================
# 9. Scoring Organ
# ============================================
class ScoreRubric(Base):
    __tablename__ = "score_rubrics"

    id = Column(Integer, primary_key=True)
    rubric_name = Column(String)
    description = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)

    criteria = relationship("ScoreCriterion", back_populates="rubric")


class ScoreCriterion(Base):
    __tablename__ = "score_criteria"

    id = Column(Integer, primary_key=True)
    rubric_id = Column(Integer, ForeignKey("score_rubrics.id"))
    criterion_name = Column(String)
    weight = Column(Float)
    description = Column(Text)

    rubric = relationship("ScoreRubric", back_populates="criteria")


class Score(Base):
    __tablename__ = "scores"

    id = Column(Integer, primary_key=True)
    agent_id = Column(Integer, ForeignKey("agents.id"))
    rubric_id = Column(Integer, ForeignKey("score_rubrics.id"))
    score = Column(Float)
    timestamp = Column(DateTime, default=datetime.utcnow)

    agent = relationship("Agent", back_populates="scores")
    rubric = relationship("ScoreRubric")

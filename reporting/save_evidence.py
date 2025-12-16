# Save evidence
from src.reporting import evidence_collector

evidence_collector.save("sql_payload", "' OR 1=1--")
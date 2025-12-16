from src.reporting import report_generator, evidence_collector

# Generate Markdown report
findings = {"ports": [22, 80], "xss": ["<script>alert(1)</script>"]}
report_generator.create(findings, output="report.md")

# Save evidence
evidence_collector.save("sql_payload", "' OR 1=1--")
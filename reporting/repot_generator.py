# Generate PDF report
from src.reporting import report_generator

findings = {"ports": [22, 80], "xss": ["<script>alert(1)</script>"]}
report_generator.create(findings, output="report.pdf")
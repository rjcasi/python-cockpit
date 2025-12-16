# sample_use.py
from src.recon import port_scan, subdomain_scanner
from src.fuzzing import xss_fuzzer
from src.ml_detection import clustering
from src.reporting import report_generator

# Recon example
subs = subdomain_scanner.find("example.com")
for sub in subs:
    open_ports = port_scan.scan(sub, ports=[80, 443])
    print(f"{sub} -> {open_ports}")

# Fuzzing example
payloads = ["<script>alert(1)</script>", "' OR 1=1--"]
xss_fuzzer.run("http://testsite.com/search", payloads)

# ML detection example
logs = ["GET /index", "POST /login", "GET /admin"]
clusters = clustering.group_requests(logs)
print("Clusters:", clusters)

# Reporting example
findings = {"open_ports": [22, 80], "xss": payloads}
report_generator.create(findings, output="report.md")
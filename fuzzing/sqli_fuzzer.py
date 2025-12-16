# Chain fuzzers together
from src.fuzzing import xss_fuzzer, sqli_fuzzer

xss_fuzzer.run("http://testsite.com/search", ["<img src=x onerror=alert(1)>"])
sqli_fuzzer.test("http://testsite.com/login", {"user": "admin", "pass": "' OR 1=1--"})
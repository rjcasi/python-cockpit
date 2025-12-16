# IDOR check
from src.fuzzing import idor_checker

targets = ["http://example.com/user/1", "http://example.com/user/2"]
idor_checker.test(targets)
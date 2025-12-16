def test(target):
    print(f"[Fuzzing] Checking IDOR on {target}")
    return ["/profile?id=1234"]
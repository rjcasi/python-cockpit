def test(target):
    print(f"[Fuzzing] Running SQLi fuzz on {target}")
    return ["' OR 1=1 --"]
def run(target):
    print(f"[Fuzzing] Running XSS fuzz on {target}")
    return ["<script>alert(1)</script>"]
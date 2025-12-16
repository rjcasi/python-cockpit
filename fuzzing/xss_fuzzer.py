def run(target, payloads=None):
    print(f"[Fuzzing] Running XSS fuzz on {target}")
    return payloads or ["<script>alert(1)</script>"]

if __name__ == "__main__":
    results = run("http://testsite.com/search")
    print("XSS fuzz results:", results)
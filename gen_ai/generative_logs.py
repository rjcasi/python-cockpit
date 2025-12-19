"""
generative_logs.py
Python-Cockpit module for synthetic cybersecurity log generation using Generative AI.
"""

from transformers import pipeline
import random

class GenerativeLogSimulator:
    def __init__(self, model_name="gpt2"):
        # Load a text-generation pipeline (can swap with larger models if needed)
        self.generator = pipeline("text-generation", model=model_name)

    def generate_attack_log(self, prompt="Suspicious login attempt detected"):
        """
        Generate synthetic attack logs based on a given prompt.
        """
        result = self.generator(
            prompt,
            max_length=150,
            num_return_sequences=1,
            temperature=0.9,
            top_p=0.95
        )
        return result[0]["generated_text"]

    def random_fuzz_payload(self):
        """
        Create a randomized fuzzing payload for demo purposes.
        """
        payloads = [
            "' OR '1'='1",
            "<script>alert('XSS')</script>",
            "../../../../etc/passwd",
            "DROP TABLE users; --"
        ]
        return random.choice(payloads)

if __name__ == "__main__":
    cockpit = GenerativeLogSimulator()

    # Example recruiter-facing demo
    print("=== Synthetic Attack Log ===")
    print(cockpit.generate_attack_log("Unauthorized SSH attempt from 192.168.1.50"))

    print("\n=== Random Fuzz Payload ===")
    print(cockpit.random_fuzz_payload())
"""
rbapp_genai_panel.py
RB-App cockpit panel for recruiter-facing Generative AI demos.
"""

from flask import Flask, render_template, request
from generative_logs import GenerativeLogSimulator

app = Flask(__name__)
simulator = GenerativeLogSimulator()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    prompt = request.form.get("prompt", "Suspicious activity detected")
    log = simulator.generate_attack_log(prompt)
    payload = simulator.random_fuzz_payload()
    return render_template(
        "result.html",
        prompt=prompt,
        log=log,
        payload=payload
    )

if __name__ == "__main__":
    app.run(debug
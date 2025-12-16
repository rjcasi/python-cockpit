# Show fuzzing panel
from src.cockpit_panels import fuzzing_panel

payloads = ["<script>alert(1)</script>", "' OR 1=1--"]
responses = ["200 OK", "500 Error"]
fuzzing_panel.display(payloads, responses)
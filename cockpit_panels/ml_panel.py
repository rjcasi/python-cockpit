# Visualize ML anomalies
from src.cockpit_panels import ml_panel

scores = [0.01, 0.02, 0.95, 0.99]
ml_panel.plot(scores)
# Train anomaly detector
from src.ml_detection import anomaly_detector

logs = ["GET /index", "POST /login", "GET /admin"]
model = anomaly_detector.train(logs)
print("Model trained:", model)
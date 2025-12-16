from src.ml_detection import anomaly_detector, clustering, autoencoder

# Train anomaly detector
logs = ["GET /index", "POST /login", "GET /admin"]
model = anomaly_detector.train(logs)
print("Model trained:", model)

# Clustering requests
requests = ["GET /", "GET /admin", "POST /login", "DELETE /user/1"]
clusters = clustering.group_requests(requests)
print("Clusters:", clusters)

# Autoencoder anomaly detection
data = [[0.1, 0.2], [0.2, 0.3], [10.0, 12.0]]
scores = autoencoder.detect(data)
print("Anomaly scores:", scores)
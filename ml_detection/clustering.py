# Use clustering to group requests
from src.ml_detection import clustering

requests = ["GET /", "GET /admin", "POST /login", "DELETE /user/1"]
clusters = clustering.group_requests(requests)
print("Clusters:", clusters)
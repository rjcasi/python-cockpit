# models.py
from sklearn.linear_model import Lasso, LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.cluster import KMeans

def get_model(name):
    if name == "lasso":
        return Lasso(alpha=0.1)
    if name == "logistic":
        return LogisticRegression(max_iter=500)
    if name == "random_forest":
        return RandomForestClassifier(n_estimators=200, oob_score=True, n_jobs=-1)
    if name == "decision_tree":
        return DecisionTreeClassifier(max_depth=5)
    if name == "knn":
        return KNeighborsClassifier(n_neighbors=5)
    if name == "svm":
        return SVC(C=1.0, gamma="scale", probability=True)
    if name == "kmeans":
        return KMeans(n_clusters=3, random_state=42)
    raise ValueError(f"Unknown model: {name}")
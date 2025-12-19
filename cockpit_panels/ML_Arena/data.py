# data.py
from sklearn.datasets import load_iris, make_classification
from sklearn.model_selection import train_test_split

def load_iris_data(test_size=0.2, random_state=42):
    iris = load_iris()
    X_train, X_test, y_train, y_test = train_test_split(
        iris.data, iris.target,
        test_size=test_size,
        random_state=random_state,
        stratify=iris.target
    )
    return X_train, X_test, y_train, y_test, iris.feature_names, iris.target_names

def load_synthetic_data(n_samples=500, n_features=10, n_classes=2, test_size=0.2, random_state=42):
    X, y = make_classification(
        n_samples=n_samples,
        n_features=n_features,
        n_informative=5,
        n_redundant=2,
        n_classes=n_classes,
        random_state=random_state
    )
    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=test_size,
        random_state=random_state,
        stratify=y
    )
    return X_train, X_test, y_train, y_test
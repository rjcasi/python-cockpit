# selection.py
from sklearn.model_selection import GridSearchCV, StratifiedKFold

def run_cv(model, X, y, param_grid=None, scoring="accuracy"):
    cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
    search = GridSearchCV(model, param_grid or {}, cv=cv, scoring=scoring, n_jobs=-1)
    search.fit(X, y)
    return search.best_estimator_, search.best_score_, search.best_params_
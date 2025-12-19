# layout.py
import plotly.graph_objects as go
import plotly.express as px
from sklearn.metrics import confusion_matrix, roc_curve, auc
from .models import get_model
from .selection import run_cv
from .data import load_iris_data

def render_ml_panel(model_name="random_forest"):
    # Load sample dataset
    X_train, X_test, y_train, y_test, feature_names, target_names = load_iris_data()

    # Train + CV
    model = get_model(model_name)
    best_model, score, params = run_cv(model, X_train, y_train)

    # Fit on train, predict on test
    best_model.fit(X_train, y_train)
    y_pred = best_model.predict(X_test)

    # Confusion matrix
    cm = confusion_matrix(y_test, y_pred)
    cm_fig = px.imshow(cm,
                       text_auto=True,
                       x=target_names,
                       y=target_names,
                       color_continuous_scale="Blues",
                       title=f"{model_name} Confusion Matrix")

    # ROC curve (only for binary classifiers)
    roc_fig = None
    if len(set(y_test)) == 2 and hasattr(best_model, "predict_proba"):
        y_score = best_model.predict_proba(X_test)[:,1]
        fpr, tpr, _ = roc_curve(y_test, y_score)
        roc_auc = auc(fpr, tpr)
        roc_fig = go.Figure()
        roc_fig.add_trace(go.Scatter(x=fpr, y=tpr, mode="lines", name=f"AUC={roc_auc:.2f}"))
        roc_fig.add_trace(go.Scatter(x=[0,1], y=[0,1], mode="lines", line=dict(dash="dash"), name="Random"))
        roc_fig.update_layout(title=f"{model_name} ROC Curve", xaxis_title="False Positive Rate", yaxis_title="True Positive Rate")

    # Score indicator
    score_fig = go.Figure()
    score_fig.add_trace(go.Indicator(
        mode="number",
        value=score,
        title={"text": f"{model_name} CV Score (Iris dataset)"}
    ))
    score_fig.update_layout(title="ML Arena: Model Selection & Metrics")

    return {"score": score_fig, "confusion": cm_fig, "roc": roc_fig}
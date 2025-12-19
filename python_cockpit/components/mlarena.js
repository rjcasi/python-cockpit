// mlarena.js
import Plotly from "plotly.js-dist";

export function renderMLArena(containerId) {
  const container = document.getElementById(containerId);
  container.innerHTML = "";

  // Buttons for model selection
  const models = ["lasso", "logistic", "random_forest", "decision_tree", "knn", "svm", "kmeans"];
  const buttonBar = document.createElement("div");
  buttonBar.style.marginBottom = "10px";

  models.forEach(m => {
    const btn = document.createElement("button");
    btn.innerText = m;
    btn.style.marginRight = "5px";
    btn.onclick = () => updateCharts(m);
    buttonBar.appendChild(btn);
  });
  container.appendChild(buttonBar);

  // Chart containers
  const scoreDiv = document.createElement("div");
  scoreDiv.id = "ml-score";
  scoreDiv.style.display = "inline-block";
  scoreDiv.style.width = "30%";

  const cmDiv = document.createElement("div");
  cmDiv.id = "ml-confusion";
  cmDiv.style.display = "inline-block";
  cmDiv.style.width = "30%";

  const rocDiv = document.createElement("div");
  rocDiv.id = "ml-roc";
  rocDiv.style.display = "inline-block";
  rocDiv.style.width = "30%";

  container.appendChild(scoreDiv);
  container.appendChild(cmDiv);
  container.appendChild(rocDiv);

  function updateCharts(modelName) {
    // For now, mock values — backend will feed real JSON with score, confusion, roc
    const score = Math.random().toFixed(3);

    // Score indicator
    Plotly.newPlot("ml-score", [{
      type: "indicator",
      mode: "number",
      value: score,
      title: { text: `${modelName} CV Score` }
    }], { title: "Score" });

    // Confusion matrix placeholder
    Plotly.newPlot("ml-confusion", [{
      z: [[3,1],[0,4]],
      type: "heatmap",
      colorscale: "Blues"
    }], { title: "Confusion Matrix" });

    // ROC curve placeholder
    Plotly.newPlot("ml-roc", [{
      x: [0,0.2,0.4,0.6,0.8,1],
      y: [0,0.4,0.6,0.75,0.9,1],
      mode: "lines",
      name: "ROC"
    },{
      x: [0,1],
      y: [0,1],
      mode: "lines",
      line: { dash: "dash" },
      name: "Random"
    }], { title: "ROC Curve", xaxis:{title:"FPR"}, yaxis:{title:"TPR"} });
  }

  // Default load
  updateCharts("random_forest");
}
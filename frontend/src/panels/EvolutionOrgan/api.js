export async function getRuns() {
  const res = await fetch("/api/evolution/runs");
  return res.json();
}

export async function getRun(runId) {
  const res = await fetch(`/api/evolution/run/${runId}`);
  return res.json();
}

export async function getGenerations(runId) {
  const res = await fetch(`/api/evolution/run/${runId}/generations`);
  return res.json();
}

export async function getGeneration(runId, genIndex) {
  const res = await fetch(`/api/evolution/run/${runId}/generation/${genIndex}`);
  return res.json();
}

export async function getAgent(agentId) {
  const res = await fetch(`/api/evolution/agent/${agentId}`);
  return res.json();
}

export async function getGenome(agentId) {
  const res = await fetch(`/api/evolution/agent/${agentId}/genome`);
  return res.json();
}

export async function getFitnessHistory(runId) {
  const res = await fetch(`/api/evolution/run/${runId}/fitness-history`);
  return res.json();
}

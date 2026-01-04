import { useState } from "react";
import RunList from "./panels/EvolutionOrgan/RunList";
import RunDetail from "./panels/EvolutionOrgan/RunDetail";
import GenerationDetail from "./panels/EvolutionOrgan/GenerationDetail";
import AgentDetail from "./panels/EvolutionOrgan/AgentDetail";
import GenomeGraph from "./panels/EvolutionOrgan/GenomeGraph";
import TelemetryTrend from "./panels/EvolutionOrgan/TelemetryTrend";

export default function App() {
  const [selectedRunId, setSelectedRunId] = useState(null);
  const [selectedGeneration, setSelectedGeneration] = useState(null);
  const [selectedAgent, setSelectedAgent] = useState(null);
  const [viewGenome, setViewGenome] = useState(false);
  const [viewTrend, setViewTrend] = useState(false);

  // Reset navigation when switching runs
  function openRun(id) {
    setSelectedRunId(id);
    setSelectedGeneration(null);
    setSelectedAgent(null);
    setViewGenome(false);
    setViewTrend(false);
  }

  return (
    <div style={{ padding: 20 }}>
      {!selectedRunId && (
        <RunList onSelectRun={openRun} />
      )}

      {selectedRunId && !selectedGeneration && !viewTrend && (
        <RunDetail
          runId={selectedRunId}
          onBack={() => setSelectedRunId(null)}
          onSelectGeneration={(g) => setSelectedGeneration(g)}
          onViewTrend={() => setViewTrend(true)}
        />
      )}

      {selectedRunId && viewTrend && (
        <TelemetryTrend
          runId={selectedRunId}
          onBack={() => setViewTrend(false)}
        />
      )}

      {selectedRunId && selectedGeneration !== null && !selectedAgent && (
        <GenerationDetail
          runId={selectedRunId}
          genIndex={selectedGeneration}
          onBack={() => setSelectedGeneration(null)}
          onSelectAgent={(id) => setSelectedAgent(id)}
        />
      )}

      {selectedAgent && !viewGenome && (
        <AgentDetail
          agentId={selectedAgent}
          onBack={() => setSelectedAgent(null)}
          onViewGenome={() => setViewGenome(true)}
        />
      )}

      {selectedAgent && viewGenome && (
        <GenomeGraph
          agentId={selectedAgent}
          onBack={() => setViewGenome(false)}
        />
      )}
    </div>
  );
}

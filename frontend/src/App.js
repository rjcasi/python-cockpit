import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

import Dashboard from "./components/Dashboard";
import RecursionArena from "./components/RecursionArena";
import DPArena from "./components/DPArena";
import DSAArena from "./components/DSAArena";

export default function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Dashboard />} />
        <Route path="/recursion" element={<RecursionArena />} />
        <Route path="/dp" element={<DPArena />} />
        <Route path="/dsa" element={<DSAArena />} />
      </Routes>
    </Router>
  );
}
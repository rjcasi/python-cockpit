import React from "react";
import { Link } from "react-router-dom";

export default function Dashboard() {
  return (
    <div style={{ padding: "2rem" }}>
      <h1>BugBot Cockpit Dashboard</h1>

      <ul>
        <li><Link to="/recursion">Recursion Arena</Link></li>
        <li><Link to="/dp">Dynamic Programming Arena</Link></li>
        <li><Link to="/sorting">Sorting Arena</Link></li>
        <li><Link to="/graphs">Graph Arena</Link></li>
        <li><Link to="/dsa">DSA Arena</Link></li>
        <li><Link to="/ml">ML Arena</Link></li>
        <li><Link to="/cyber">Cyber Arena</Link></li>
        <li><Link to="/robotics">Robotics Arena</Link></li>
      </ul>
    </div>
  );
}
"""
Unified import hub for all cockpit panels.
Each arena exposes a `render_*` function for recruiter-facing dashboards.
"""

# Import arenas explicitly
from .CausalSetArena import render_causal_panel as CausalSetArena
from .SortingArena import render_sorting_panel as SortingArena
from .GraphArena import render_graph_panel as GraphArena

# Add new arenas here as you build them
# Example:
# from .DSAArena import render_dsa_panel as DSAArena

__all__ = [
    "CausalSetArena",
    "SortingArena",
    "GraphArena",
    # "DSAArena",  # uncomment when ready
]
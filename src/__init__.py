"""
AI Research Multi-Agent System

A Python module for multi-agent AI research using Microsoft Agent Framework.
"""

__version__ = "0.1.0"
__author__ = "AI Research Team"
__license__ = "MIT"

from .agents import create_research_agents, conduct_research
from .tools import bing_search

__all__ = [
    "create_research_agents",
    "conduct_research",
    "bing_search",
]

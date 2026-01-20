import pytest
from backend.agents.intake_agents import IntakeAgent

def test_intake_agent():
    agent = IntakeAgent()
    output = agent.run({"transcript": "Patient reports chest pain"})
    assert "chief_complaint" in output
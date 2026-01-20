from .base.py import BaseAgent

class IntakeAgent(BaseAgent):
    """Extracts chief complaint from patient transcript."""

    def run(self, input_data: dict) -> dict:
        transcript = input_data.get("transcript", "")
        # Simple example logic, replace with NLP/LLM pipeline
        chief_complaint = transcript.split(".")[0] if transcript else ""
        return {"chief_complaint": chief_complaint, "source": "voice", "confidence": 0.95}

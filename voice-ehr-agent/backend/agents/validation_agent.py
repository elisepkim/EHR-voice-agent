from .base import BaseAgent

class ValidationAgent(BaseAgent):
    """Validates reasoning output."""

    def run(self, input_data: dict) -> dict:
        reasoning = input_data.get("reasoning", {})
        issues = []
        if not reasoning.get("final_assessment"):
            issues.append("Missing final assessment")
        validated = len(issues) == 0
        return {"validated": validated, "issues": issues}

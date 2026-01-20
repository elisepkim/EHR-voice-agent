from .base import BaseAgent

class TriageAgent(BaseAgent):
    """Assigns acuity level based on symptoms."""

    def run(self, input_data: dict) -> dict:
        text = input_data.get("chief_complaint", "").lower()
        if "chest pain" in text or "shortness of breath" in text:
            acuity = "high"
            escalate = True
        else:
            acuity = "low"
            escalate = False
        return {"acuity": acuity, "escalate": escalate}

from agents.base import BaseAgent

class TriageAgent(BaseAgent):
    name = "triage"

    def run(self, input_data, context):
        symptoms = context.get("symptoms", "").lower()

        if "chest" in symptoms:
            decision = "high"
            confidence = 0.85
        else:
            decision = "low"
            confidence = 0.60

        context["triage"] = decision
        context.setdefault("trace", []).append(
            self.trace(decision, confidence)
        )
        return context
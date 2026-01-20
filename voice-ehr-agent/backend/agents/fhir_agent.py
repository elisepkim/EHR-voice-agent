from .base import BaseAgent

class FHIRWriteAgent(BaseAgent):
    """Converts final assessment to FHIR Condition."""

    def run(self, input_data: dict) -> dict:
        final_assessment = input_data.get("reasoning", {}).get("final_assessment", "")
        return {
            "resourceType": "Condition",
            "clinicalStatus": {"text": "active"},
            "code": {
                "coding": [
                    {"system": "http://hl7.org/fhir/sid/icd-10",
                     "code": "I24.9",
                     "display": final_assessment}
                ]
            }
        }

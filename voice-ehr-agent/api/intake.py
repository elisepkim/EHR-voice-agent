class IntakeAgent:
    def run(self, transcript: str) -> dict:
        return {
            "patient_transcript": transcript,
            "intake": {
                "symptoms": ["chest pain", "dizziness"],
                "summary": "Mocked intake analysis"
            }
        }
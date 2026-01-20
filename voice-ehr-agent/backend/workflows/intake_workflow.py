from backend.agents.intake_agents import IntakeAgent
from backend.agents.triage_agent import TriageAgent
from backend.agents.validation_agent import ValidationAgent
from backend.agents.fhir_agents import FHIRWriteAgent
from backend.agents.latent_agent import LatentAgent
from backend.services.memory_service import PatientMemory
from backend.services.audit_logger import log_event

class IntakeWorkflow:
    """
    Production-grade multi-agent EHR workflow with latent reasoning.
    """

    def __init__(self):
        self.intake_agent = IntakeAgent()
        self.triage_agent = TriageAgent()
        self.validation_agent = ValidationAgent()
        self.fhir_agent = FHIRWriteAgent()
        self.memory = PatientMemory()
        self.latent_agent = LatentAgent(memory=self.memory)

    def run(self, transcript: str) -> dict:
        # Step 1: Intake agent
        intake = self.intake_agent.run(transcript)
        log_event("intake", intake)

        # Step 2: Triage agent
        triage = self.triage_agent.run(intake)
        log_event("triage", triage)

        # Step 3: Latent agent performs internal planning + reasoning
        latent_output = self.latent_agent.run(transcript)
        log_event("latent_agent_output", latent_output)

        # Step 4: Validation agent
        validation = self.validation_agent.run(latent_output["reasoning"])
        log_event("validation", validation)

        # Step 5: FHIR write
        fhir_condition = self.fhir_agent.condition(
            latent_output["reasoning"]["final_assessment"]
        )
        log_event("fhir_write", fhir_condition)

        return {
            "intake": intake,
            "triage": triage,
            "latent_agent": latent_output,
            "validation": validation,
            "fhir": fhir_condition
        }
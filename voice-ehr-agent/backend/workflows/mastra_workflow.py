from mastra import Workflow
from backend.agents.mastra_agents import intake_agent, triage_agent, latent_agent, validation_agent, fhir_agent
from backend.services.audit_logger import log_event

class MastraIntakeWorkflow(Workflow):
    def __init__(self):
        super().__init__(name="mastra_intake_workflow")
        self.add_agent(intake_agent)
        self.add_agent(triage_agent)
        self.add_agent(latent_agent)
        self.add_agent(validation_agent)
        self.add_agent(fhir_agent)

    def run(self, transcript: str) -> dict:
        intake_result = intake_agent.run(transcript)
        log_event("intake", intake_result)
        triage_result = triage_agent.run(intake_result)
        log_event("triage", triage_result)
        latent_result = latent_agent.run(transcript)
        log_event("latent_agent", latent_result)
        validation_result = validation_agent.run(latent_result["reasoning"])
        log_event("validation", validation_result)
        fhir_result = fhir_agent.run(latent_result["reasoning"]["final_assessment"])
        log_event("fhir_write", fhir_result)
        return {"intake": intake_result, "triage": triage_result, "latent_agent": latent_result, "validation": validation_result, "fhir": fhir_result}

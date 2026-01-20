from mastra import Agent, Schema
from backend.agents.intake_agents import IntakeAgent
from backend.agents.triage_agent import TriageAgent
from backend.agents.validation_agent import ValidationAgent
from backend.agents.fhir_agents import FHIRWriteAgent
from backend.agents.latent_agent import LatentAgent
from backend.services.memory_service import PatientMemory

memory = PatientMemory()

intake_agent = Agent(
    name="intake_agent",
    schema=Schema(input={"transcript": str}, output={"intake": dict}),
    run=IntakeAgent().run
)

triage_agent = Agent(
    name="triage_agent",
    schema=Schema(input={"intake": dict}, output={"triage": dict}),
    run=TriageAgent().run
)

latent_agent = Agent(
    name="latent_agent",
    schema=Schema(input={"transcript": str}, output={"latent_plan": dict, "reasoning": dict, "memory_snapshot": str}),
    run=LatentAgent(memory=memory).run
)

validation_agent = Agent(
    name="validation_agent",
    schema=Schema(input={"reasoning": dict}, output={"validated": bool, "issues": list}),
    run=ValidationAgent().run
)

fhir_agent = Agent(
    name="fhir_agent",
    schema=Schema(input={"diagnosis": str}, output={"fhir_condition": dict}),
    run=FHIRWriteAgent().condition
)
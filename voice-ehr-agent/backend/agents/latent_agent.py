from typing import Any, Dict, Optional
from backend.agents.base import BaseAgent
from backend.services.memory_service import PatientMemory
from backend.services.hybrid_reasoner import HybridReasoner
from backend.services.audit_logger import log_event

class LatentAgent(BaseAgent):
    """
    Latent reasoning agent:
    - Generates internal latent plan
    - Uses memory context for guidance
    - Outputs final structured assessment
    """

    def __init__(self, memory: Optional[PatientMemory] = None, reasoner: Optional[HybridReasoner] = None):
        self.memory = memory or PatientMemory()
        self.reasoner = reasoner or HybridReasoner()

    def generate_latent_plan(self, transcript: str, history: str) -> Dict:
        """
        Create latent plan of action from transcript + memory.
        This is an internal reasoning step, not exposed externally.
        """
        # Simple example: latent states
        latent_state = {
            "needs_further_workup": "chest pain" in transcript.lower(),
            "risk_level": 0.8 if "shortness of breath" in transcript.lower() else 0.3,
            "history_summary": history
        }
        return latent_state

    def run(self, transcript: str) -> Dict:
        # Step 1: retrieve memory
        history = self.memory.retrieve(transcript)
        log_event("latent_memory_retrieved", {"transcript": transcript, "history": history})

        # Step 2: generate latent plan
        latent_plan = self.generate_latent_plan(transcript, history)
        log_event("latent_plan_generated", latent_plan)

        # Step 3: reason over transcript + latent plan
        reasoning_input = f"{transcript} | latent: {latent_plan}"
        reasoning = self.reasoner.reason(reasoning_input, history)
        log_event("latent_reasoning", reasoning)

        # Step 4: store transcript in memory
        self.memory.add_encounter(transcript)

        return {
            "latent_plan": latent_plan,
            "reasoning": reasoning,
            "memory_snapshot": history
        }
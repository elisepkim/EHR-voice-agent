from models.tiny_recursive_model import TinyRecursiveModel
from models.recurrent_depth_model import RecurrentDepthModel

class HybridReasoner:
    """
    Explicit hybrid reasoning engine with traceability.
    """

    def __init__(self):
        self.local_model = TinyRecursiveModel()
        self.longitudinal_model = RecurrentDepthModel()

    def reason(self, transcript: str, history=None) -> dict:
        local = self.local_model.reason(transcript)
        longitudinal = self.longitudinal_model.analyze(history or [])

        return {
            "final_assessment": local["diagnosis"],
            "confidence": local["confidence"],
            "reasoning_trace": {
                "local_reasoning": local,
                "longitudinal_context": longitudinal
            }
        }
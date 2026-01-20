from abc import ABC, abstractmethod

class BaseAgent(ABC):
    """Base class for all agents."""

    @abstractmethod
    def run(self, input_data: dict) -> dict:
        pass

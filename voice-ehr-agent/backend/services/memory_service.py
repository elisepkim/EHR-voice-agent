from llama_index.core import VectorStoreIndex, Document

class PatientMemory:
    """
    Persistent longitudinal memory using LlamaIndex.
    """

    def __init__(self):
        self.index = VectorStoreIndex([])

    def add_encounter(self, text: str):
        self.index.insert(Document(text=text))

    def retrieve(self, query: str) -> str:
        engine = self.index.as_query_engine()
        return str(engine.query(query))
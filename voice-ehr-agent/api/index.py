from fastapi import FastAPI
from pydantic import BaseModel
from workflows.mastra_workflow import MastraIntakeWorkflow

app = FastAPI(title="Mastra Voice-Enabled EHR Agent")
workflow = MastraIntakeWorkflow()

class IntakeRequest(BaseModel):
    transcript: str

@app.post("/api/v1/intake")
def intake(req: IntakeRequest):
    return workflow.run(req.transcript)

@app.get("/health")
def health():
    return {"status": "ok"}
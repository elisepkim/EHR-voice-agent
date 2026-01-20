from backend.workflows.intake_workflow import MastraIntakeWorkflow

def test_workflow():
    workflow = MastraIntakeWorkflow()
    output = workflow.run("Patient reports chest pain")
    assert "intake" in output
    assert "triage" in output
    assert "latent_agent" in output
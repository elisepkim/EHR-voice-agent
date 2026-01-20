from backend.workflows.intake_workflow import MastraIntakeWorkflow

workflow = MastraIntakeWorkflow()

test_transcripts = [
    "Patient reports chest pain and shortness of breath",
    "Patient has mild headache and nausea"
]

for t in test_transcripts:
    output = workflow.run(t)
    print(output)
from graphviz import Digraph

dot = Digraph(comment='Mastra Workflow')
dot.node('A', 'IntakeAgent')
dot.node('B', 'TriageAgent')
dot.node('C', 'LatentAgent')
dot.node('D', 'ValidationAgent')
dot.node('E', 'FHIRWriteAgent')

dot.edges(['AB','BC','CD','DE'])
dot.render('docs/workflow_graph', view=True)
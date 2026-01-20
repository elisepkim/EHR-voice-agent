# Mastra Voice-Enabled EHR Agent

## Overview
Production-grade, multi-agent EHR system using:
- Mastra multi-agent orchestration
- Latent reasoning agent
- Hybrid reasoning (TinyRecursive + RecurrentDepth models)
- Persistent patient memory
- FHIR-compliant outputs
- Audit logging

## Features
- Intake, triage, latent reasoning, validation, FHIR write
- Interactive frontend demo (`frontend/live_mastra_demo.html`)
- Simulation script (`scripts/simulate_intake.py`)
- Workflow visualization (`scripts/visualize_workflow.py`)
- Unit tests in `tests/`

## Run
```bash
pip install -r requirements.txt
uvicorn backend.main:app --reload
# Loan Approver Engine
## Project Summary
A deterministic, batch‑oriented underwriting engine delivered through staged milestones. The system generates synthetic applicant data, applies transparent rule logic, and produces a single authoritative decision ledger with strict data‑integrity guarantees.

## Milestone 1 - Batch Framework Established
- **Purpose:** Define the execution model and operational boundaries.
- **Deliverables:** Folder structure, deterministic batch conventions overwrite rules, logging format.
- **Outcome:** A reproducible, stateless pipeline foundation.

## Milestone 2 - Synthetic Data Generator Built 
- **Purpose:** Produce controlled, repeatable applicant batches.
- **Deliverables:** dataset_generator.py
    -  Ten CSV batches (10,000 rows each) with sequential application_id
    - Applicant fields: credit score, income, DTI, employment status, age, loan amount
- **Outcome:** Reliable input data for downstream evaluation.


## Milestone 3 - Underwriting Rules Engine Implemented
- **Purpose:** Encode transparent, auditable decision logic.
- **Deliverables:** rules_engine.py
    - Rule set: credit score, DTI, income, employment stability, age, affordability
    - Outputs: APPROVE/DECLINE, reason code, reason text
- **Outcome:** Deterministic, explainable decisions for every applicant.

## Milestone 4 - Batch Evaluator and Ledger Generator Completed
- **Purpose:** Apply rules across all batches and consolidate results.
- **Deliverables:** evaluator.py
    - Fail‑fast batch validation
    - Sorted, overwrite‑safe final ledger: outputs/decision_results.csv
- **Outcome:** A single authoritative decision artifact.

## Milestone 5 - End‑to‑End Pipeline Validated
- **Purpose:** Confirm deterministic behavior and data lineage.
- **Flow:** Generate batches → data/batch_01.csv … batch_10.csv
    - Evaluate batches → apply rules → aggregate
    - Produce final ledger → sorted, consolidated CSV
- **Outcome:** Predictable, audit‑ready DSS pipeline.

## Milestone 6 - Enterprise Design Principles Finalized
**Principles:**
- Deterministic batch structure
- Fail‑fast integrity enforcement
- Single source of truth
- Minimal, meaningful operational logs
- Modular, stateless components
- Clean separation of inputs (data/) and outputs (outputs/)
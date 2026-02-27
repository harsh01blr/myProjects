cat > README.md << 'EOF'
# Loan Approver Engine

## Executive Summary
The Loan Approver Engine is a deterministic, batch‑oriented Decision Support System designed to reflect enterprise‑grade underwriting pipelines. It produces a single authoritative decision ledger from structured applicant batches, applying transparent rule logic and enforcing strict data‑integrity guarantees. The system emphasizes reproducibility, operational clarity, and clean separation of responsibilities across generation, rule evaluation, and aggregation stages.

## System Overview
The engine processes synthetic applicant data through a modular pipeline consisting of three independent components: a dataset generator, a bottom‑up rules engine, and a batch evaluator. Each component is isolated, stateless, and deterministic, ensuring predictable behavior across runs and enabling straightforward auditability.

The design aligns with enterprise DSS principles:
- Deterministic batch processing with predictable file naming and ordering
- Fail‑fast integrity checks to prevent partial or inconsistent outputs
- A single source of truth for downstream consumption
- Transparent, explainable rule logic suitable for governance and audit review
- Operational logs that provide visibility without introducing side effects

## Repository Structure

loan-decision-engine/
├─ data/                     # Generated input batches (10 × 10,000 rows)
├─ outputs/                  # Final combined decision ledger
│  └─ decision_results.csv
├─ dataset_generator.py      # Creates synthetic applicant batches
├─ rules_engine.py           # Bottom-up underwriting rules
└─ evaluator.py              # Applies rules to all batches and produces final output

## Component Architecture

### Dataset Generator (`dataset_generator.py`)
Generates ten CSV batches (`batch_01.csv` … `batch_10.csv`), each containing 10,000 synthetic loan applications.

Key characteristics:
- Sequential `application_id` across all batches
- Overwrites existing files to maintain deterministic state
- Simple `[INFO]` logs for operational visibility
- Features include credit score, income, DTI, employment status, age, and loan amount

**Execution:**
```bash
python dataset_generator.py



 logs show progress.

Data includes credit score, income, DTI, employment status, age, and loan amount.

Run:

sh
python dataset_generator.py
This populates the data/ directory.

Rules Engine (rules_engine.py)
Implements bottom‑up underwriting logic. Each granular rule evaluates one eligibility dimension:

Minimum credit score

Maximum DTI

Minimum income

Employment stability

Age range

Loan‑to‑income affordability

The engine returns:

APPROVE or DECLINE

A reason code

A human‑readable reason text

Evaluator (evaluator.py)
Reads all 10 batches, applies the rules engine to each applicant, and produces a single combined output file:

Code
outputs/decision_results.csv
Key behaviors:

Fail‑fast if any expected batch file is missing.

Processes batches sequentially with [INFO] logs.

Sorts all results by application_id.

Overwrites the output file on each run.

Produces no intermediate or trace files.

Run:

sh
python evaluator.py
Data Flow
Generate batches  
dataset_generator.py → data/batch_01.csv … batch_10.csv

Evaluate batches  
evaluator.py → reads all batches → applies rules → aggregates results

Produce final ledger  
Sorted, combined output written to outputs/decision_results.csv

This mirrors how enterprise DSS pipelines produce daily or hourly decision artifacts.

Design Principles
Deterministic batch structure — predictable file naming and ordering.

Fail‑fast integrity — evaluation stops immediately if any batch is missing.

Single source of truth — only one final output file, overwritten each run.

Operational clarity — simple [INFO] logs for visibility.

Modular architecture — generator, rules engine, and evaluator are independent.

Enterprise alignment — clean separation between data/ and outputs/.
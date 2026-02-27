Loan Decision Engine
Overview
This project implements a modular, batch‑oriented Decision Support System (DSS) for loan underwriting. It includes a synthetic dataset generator, a bottom‑up rules engine, and an evaluator that processes all batches and produces a single authoritative decision ledger.

The system mirrors enterprise DSS patterns such as deterministic batch processing, fail‑fast integrity checks, simple operational logs, and clean separation between inputs and outputs.

Repository Structure
Code
loan-decision-engine/
├─ data/                     # Generated input batches (10 × 10,000 rows)
├─ outputs/                  # Final combined decision ledger
│  └─ decision_results.csv
├─ dataset_generator.py      # Creates synthetic applicant batches
├─ rules_engine.py           # Bottom-up underwriting rules
└─ evaluator.py              # Applies rules to all batches and produces final output

Components
Dataset Generator (dataset_generator.py)
Generates 10 CSV batches (batch_01.csv … batch_10.csv), each containing 10,000 synthetic loan applications.

Key characteristics:

application_id is the first column and strictly sequential across all batches.

Each batch overwrites any existing file with the same name.

Simple [INFO] logs show progress.

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
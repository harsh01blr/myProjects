import os
import csv

from rules_engine import apply_rules, DecisionResult

DATA_DIR = "data"
OUTPUT_DIR = "outputs"
OUTPUT_FILE = "decision_results.csv"
TOTAL_BATCHES = 10


def ensure_dirs():
    os.makedirs(OUTPUT_DIR, exist_ok=True)


def _fail_fast_if_missing_batches():
    for batch_num in range(1, TOTAL_BATCHES + 1):
        batch_path = os.path.join(DATA_DIR, f"batch_{batch_num:02d}.csv")
        if not os.path.exists(batch_path):
            raise FileNotFoundError(
                f"Missing expected batch file: {batch_path}. "
                "Fail-fast is enabled; aborting evaluation."
            )


def _read_batch_rows(batch_path: str):
    with open(batch_path, "r", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            yield row


def _evaluate_row(row: dict) -> DecisionResult:
    application_id = int(row["application_id"])
    credit_score = int(row["credit_score"])
    income = int(row["income"])
    dti = float(row["dti"])
    employment_status = row["employment_status"]
    age = int(row["age"])
    loan_amount = int(row["loan_amount"])

    return apply_rules(
        application_id=application_id,
        credit_score=credit_score,
        income=income,
        dti=dti,
        employment_status=employment_status,
        age=age,
        loan_amount=loan_amount,
    )


def evaluate_batches():
    print("[INFO] Starting evaluation...")
    ensure_dirs()
    _fail_fast_if_missing_batches()

    results = []

    for batch_num in range(1, TOTAL_BATCHES + 1):
        print(f"[INFO] Processing batch {batch_num:02d} of {TOTAL_BATCHES}...")
        batch_path = os.path.join(DATA_DIR, f"batch_{batch_num:02d}.csv")

        for row in _read_batch_rows(batch_path):
            decision_result = _evaluate_row(row)
            results.append(decision_result)

        print(f"[INFO] Batch {batch_num:02d} processed.")

    print("[INFO] Sorting combined results by application_id...")
    results.sort(key=lambda r: r.application_id)

    output_path = os.path.join(OUTPUT_DIR, OUTPUT_FILE)
    print(f"[INFO] Writing combined results to {output_path}...")

    # Overwrite behavior: open with "w"
    with open(output_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(
            [
                "application_id",
                "decision",
                "reason_code",
                "reason_text",
            ]
        )

        for r in results:
            writer.writerow(
                [
                    r.application_id,
                    r.decision,
                    r.reason_code,
                    r.reason_text,
                ]
            )

    print("[INFO] Evaluation complete.")


if __name__ == "__main__":
    evaluate_batches()
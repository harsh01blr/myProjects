import os
import csv
import random

DATA_DIR = "data"
TOTAL_BATCHES = 10
BATCH_SIZE = 10000


def ensure_dirs():
    os.makedirs(DATA_DIR, exist_ok=True)


def generate_applicant_row(application_id: int):
    credit_score = random.randint(300, 850)
    income = random.randint(20000, 200000)
    dti = round(random.uniform(0.1, 0.6), 2)
    employment_status = random.choice(["employed", "self-employed", "unemployed"])
    age = random.randint(21, 65)
    loan_amount = random.randint(5000, 500000)

    return [
        application_id,
        credit_score,
        income,
        dti,
        employment_status,
        age,
        loan_amount,
    ]


def generate_batches():
    print("[INFO] Starting dataset generation...")
    ensure_dirs()

    application_id = 1

    for batch_num in range(1, TOTAL_BATCHES + 1):
        print(f"[INFO] Generating batch {batch_num:02d} of {TOTAL_BATCHES}...")

        batch_path = os.path.join(DATA_DIR, f"batch_{batch_num:02d}.csv")
        # Overwrite behavior by default: open with "w"
        with open(batch_path, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(
                [
                    "application_id",
                    "credit_score",
                    "income",
                    "dti",
                    "employment_status",
                    "age",
                    "loan_amount",
                ]
            )

            for _ in range(BATCH_SIZE):
                row = generate_applicant_row(application_id)
                writer.writerow(row)
                application_id += 1

        print(f"[INFO] Batch {batch_num:02d} complete.")

    print("[INFO] All batches generated successfully.")


if __name__ == "__main__":
    generate_batches()
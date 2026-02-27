from dataclasses import dataclass


@dataclass
class DecisionResult:
    application_id: int
    decision: str
    reason_code: str
    reason_text: str


def _rule_min_credit_score(credit_score: int) -> bool:
    return credit_score >= 620


def _rule_max_dti(dti: float) -> bool:
    return dti <= 0.4


def _rule_min_income(income: int) -> bool:
    return income >= 30000


def _rule_employment_status(status: str) -> bool:
    return status in {"employed", "self-employed"}


def _rule_age(age: int) -> bool:
    return 21 <= age <= 65


def _rule_loan_to_income(income: int, loan_amount: int) -> bool:
    # Simple affordability: loan_amount <= 8 * monthly_income (approx)
    # monthly_income ~ income / 12
    return loan_amount <= 8 * (income / 12)


def apply_rules(
    application_id: int,
    credit_score: int,
    income: int,
    dti: float,
    employment_status: str,
    age: int,
    loan_amount: int,
) -> DecisionResult:
    """
    Bottom-up rule engine:
    - Evaluate granular rules
    - Aggregate into a single decision + reason
    """

    # Fail reasons in priority order
    if not _rule_min_credit_score(credit_score):
        return DecisionResult(
            application_id=application_id,
            decision="DECLINE",
            reason_code="CREDIT_SCORE_LOW",
            reason_text="Credit score below minimum threshold.",
        )

    if not _rule_max_dti(dti):
        return DecisionResult(
            application_id=application_id,
            decision="DECLINE",
            reason_code="DTI_HIGH",
            reason_text="Debt-to-income ratio above allowed maximum.",
        )

    if not _rule_min_income(income):
        return DecisionResult(
            application_id=application_id,
            decision="DECLINE",
            reason_code="INCOME_LOW",
            reason_text="Income below minimum required level.",
        )

    if not _rule_employment_status(employment_status):
        return DecisionResult(
            application_id=application_id,
            decision="DECLINE",
            reason_code="EMPLOYMENT_UNSTABLE",
            reason_text="Employment status not eligible.",
        )

    if not _rule_age(age):
        return DecisionResult(
            application_id=application_id,
            decision="DECLINE",
            reason_code="AGE_OUT_OF_RANGE",
            reason_text="Applicant age outside allowed range.",
        )

    if not _rule_loan_to_income(income, loan_amount):
        return DecisionResult(
            application_id=application_id,
            decision="DECLINE",
            reason_code="AFFORDABILITY_FAIL",
            reason_text="Requested loan amount not affordable given income.",
        )

    # If all rules pass, approve
    return DecisionResult(
        application_id=application_id,
        decision="APPROVE",
        reason_code="APPROVED",
        reason_text="All underwriting rules satisfied.",
    )
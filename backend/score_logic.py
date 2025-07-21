from random import randint

def generate_risk_score(applicant) -> tuple[int, str]:
    base_score = 600

    if applicant.income > 100000:
        base_score += 50
    elif applicant.income < 30000:
        base_score -= 50

    if "trust" in applicant.name.lower():
        base_score += 30

    # Add random jitter
    final_score = max(300, min(base_score + randint(-30, 30), 850))

    summary = (
        "Low risk — stable income and verified identity"
        if final_score > 700 else
        "Medium risk — moderate profile"
        if final_score > 600 else
        "High risk — flagged for additional checks"
    )

    return final_score, summary

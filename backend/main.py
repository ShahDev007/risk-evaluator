from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from score_logic import generate_risk_score

app = FastAPI()

class Applicant(BaseModel):
    loan_type: str
    name: str
    dob: str
    ssn: str
    zip: str
    income: float

@app.post("/score")
def get_score(applicant: Applicant):
    try:
        score, summary = generate_risk_score(applicant)
        return {
            "risk_score": score,
            "summary": summary
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

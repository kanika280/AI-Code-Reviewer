from fastapi import FastAPI, Body
from pydantic import BaseModel
from app.review import review_code

app = FastAPI(title="AI Code Reviewer", version="1.0")

# -----------------------------
# Input schema for JSON endpoint
# -----------------------------
class CodeInput(BaseModel):
    code: str

# -----------------------------
# Helper function
# -----------------------------
def contains_keywords(text_list, keywords):
    """
    Check if any of the keywords exist in the issues text.
    Returns True if at least one keyword is found.
    """
    combined = " ".join(text_list).lower()
    return any(word.lower() in combined for word in keywords)

def format_result(result):
    """
    Convert the review_code output into a dictionary for JSON response,
    including a semantic check.
    """
    critical_keywords = ["divide", "zero", "type", "string", "invalid"]
    semantic_passed = not contains_keywords(result.issues, critical_keywords)

    return {
        "issues": result.issues,
        "refactor_suggestions": result.refactor_suggestions,
        "test_suggestions": result.test_suggestions,
        "uncertainties": result.uncertainties,
        "semantic_passed": semantic_passed
    }

# -----------------------------
# Endpoint 1: JSON input
# -----------------------------
@app.post("/review/json")
async def review_json(input: CodeInput):
    """
    Review code sent as JSON: {"code": "..."}
    """
    code = input.code
    result = review_code(code)
    return format_result(result)

# -----------------------------
# Endpoint 2: Raw code input
# -----------------------------
@app.post("/review/raw")
async def review_raw(raw_code: str = Body(..., media_type="text/plain")):
    """
    Review raw code sent as plain text.
    """
    result = review_code(raw_code)
    return format_result(result)

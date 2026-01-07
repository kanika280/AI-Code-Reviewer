# AI Code Reviewer

**AI-powered Python code reviewer** built with **FastAPI**.  
Analyze Python code for issues, get refactor suggestions, test ideas, and detect uncertainties. Supports both **JSON input** and **raw Python code**.

---

## Features

- Detects common Python issues (type errors, division by zero, invalid inputs)
- Suggests code refactors and improvements
- Provides unit test suggestions
- Highlights uncertain or ambiguous code
- Two input methods:
  - `/review/json` → Send JSON: `{"code": "..."}`  
  - `/review/raw` → Send raw Python code directly

---

## Project Structure

ai-code-review-assistant/
├─ app/
│ ├─ main.py # FastAPI server with endpoints
│ └─ review.py # Code analysis logic
├─ evaluation/
│ └─ run_evaluation.py # CLI tool to test example code files
├─ tests/
│ └─ test_review.py # Pytest tests
├─ buggy_code1.py # Example code with issues
├─ buggy_code2.py # Example code with issues
├─ clean_code1.py # Example clean code
├─ requirements.txt # Dependencies
└─ README.md # This file

---

## Installation

```bash
git clone <repo-url>
cd ai-code-review-assistant
python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate
pip install -r requirements.txt

```
---

## Running the FastAPI Server

```bash
uvicorn app.main:app --reload
```
- Open http://127.0.0.1:8000/docs for Swagger UI
- Try /review/json or /review/raw

---

## Example Usage
JSON Input

{
  "code": "def divide(a, b): return a / b\nx = divide(10, 0)"
}

---

## Raw Python Input

def divide(a, b):
    return a / b

x = divide(10, 0)

---

## Sample Response

{
  "issues": ["Division by zero detected", "No type checks"],
  "refactor_suggestions": ["Add input validation", "Guard against zero division"],
  "test_suggestions": ["Test with zero denominator", "Test with invalid types"],
  "uncertainties": ["Intended behavior for zero denominator unclear"],
  "semantic_passed": false
}

---

## Running Evaluations
```bash
python evaluation/run_evaluation.py
```
- Evaluates example files in evaluation/
- Shows issues, refactor suggestions, test ideas, and semantic checks

---

## Running Tests

```bash
pytest -v
```

---

## Tech Stack

- Python 3.11+
- FastAPI
- Pydantic
- Uvicorn
- Pytest

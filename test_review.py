from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

BUGGY_CODE = """
def divide(a, b):
    return a / b

def add(a, b):
    return a + b

x = divide(10, 0)
"""

def test_review_returns_valid_schema():
    response = client.post(
        "/review",
        json={"code": BUGGY_CODE}
    )

    assert response.status_code == 200

    data = response.json()

    # Required top-level keys
    assert "issues" in data
    assert "refactor_suggestions" in data
    assert "test_suggestions" in data
    assert "uncertainties" in data

    # All fields must be lists
    assert isinstance(data["issues"], list)
    assert isinstance(data["refactor_suggestions"], list)
    assert isinstance(data["test_suggestions"], list)
    assert isinstance(data["uncertainties"], list)

    # Buggy code should produce at least one issue
    assert len(data["issues"]) > 0

def test_division_by_zero_detected():
    response = client.post(
        "/review",
        json={"code": BUGGY_CODE}
    )

    data = response.json()

    joined_issues = " ".join(data["issues"]).lower()

    assert "zero" in joined_issues or "divide" in joined_issues

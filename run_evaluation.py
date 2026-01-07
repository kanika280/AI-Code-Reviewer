import os
import sys
from app.review import review_code

# Make sure project root is on path
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, PROJECT_ROOT)

EVAL_FOLDER = os.path.dirname(__file__)

BUG_KEYWORDS = ["error", "exception", "crash", "zero", "invalid", "type", "fail"]

def contains_keywords(text_list, keywords):
    combined = " ".join(text_list).lower()
    return any(word.lower() in combined for word in keywords)

def evaluate_file(filename):
    path = os.path.join(EVAL_FOLDER, filename)

    with open(path, "r", encoding="utf-8") as f:
        code = f.read()

    print(f"\n=== Evaluating {filename} ===")
    result = review_code(code)

    print("Issues:", result.issues)
    print("Refactor:", result.refactor_suggestions)
    print("Tests:", result.test_suggestions)
    print("Uncertainties:", result.uncertainties)

    # --- Semantic evaluation for buggy files ---
    if filename == "buggy_code1.py":
        assert contains_keywords(result.issues, ["zero"]), "Did not detect division by zero"

    if filename == "buggy_code2.py":
        assert (
            contains_keywords(result.issues, ["type"])
            or contains_keywords(result.issues, ["string"])
            or contains_keywords(result.issues, ["number"])
        ), "Did not detect type error"

    # --- Clean code must NOT contain bug signals ---
    if filename == "clean_code1.py":
        assert not contains_keywords(result.issues, BUG_KEYWORDS), "Clean code incorrectly flagged as buggy"

    print("Semantic checks passed")

def main():
    for file in os.listdir(EVAL_FOLDER):
        if file.endswith(".py") and file != "run_evaluation.py":
            evaluate_file(file)

    print("\nAll evaluations passed")

if __name__ == "__main__":
    main()

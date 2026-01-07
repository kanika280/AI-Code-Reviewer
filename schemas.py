from pydantic import BaseModel
from typing import List


class CodeReviewResult(BaseModel):
    issues: List[str]
    refactor_suggestions: List[str]
    test_suggestions: List[str]
    uncertainties: List[str]

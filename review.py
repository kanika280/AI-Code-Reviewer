import os
import json
from groq import Groq
from app.prompts import SYSTEM_PROMPT
from app.schemas import CodeReviewResult

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def review_code(code: str) -> CodeReviewResult:
    response = client.chat.completions.create(
        model="groq/compound",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": code}
        ],
        temperature=0
    )

    # Groq response might need dict access
    content = response.choices[0].message.content

    # If AI returns a JSON string, parse it safely
    try:
        data = json.loads(content)
        return CodeReviewResult(**data)
    except json.JSONDecodeError:
        # Fallback if AI returns text instead of JSON
        return CodeReviewResult(
            issues=[content],
            refactor_suggestions=[],
            test_suggestions=[],
            uncertainties=[]
        )
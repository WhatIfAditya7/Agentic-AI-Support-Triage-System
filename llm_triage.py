from dotenv import load_dotenv
load_dotenv()

from openai import OpenAI
from pydantic import BaseModel, Field
from typing import Literal, List

client = OpenAI()

Category = Literal[
    "billing", "bug", "account", "feature_request", "performance", "how_to", "other"
]
Priority = Literal["low", "medium", "high"]
Path = Literal["self_help", "maintenance"]

class TriageResult(BaseModel):
    category: Category
    priority: Priority
    self_resolvable: bool
    recommended_path: Path
    summary: str
    next_action: str
    self_help_steps: List[str] = Field(default_factory=list)
    confidence: float = Field(ge=0.0, le=1.0)

def triage_with_llm(text: str) -> dict:
    response = client.responses.parse(
        model="gpt-4o-2024-08-06",
        input=[
            {
                "role": "system",
                "content": (
                    "You are a support triage agent. Decide whether the user can self-fix "
                    "or if it must be escalated to maintenance."
                ),
            },
            {
                "role": "user",
                "content": (
                    "Return JSON with: category, priority, self_resolvable, recommended_path, "
                    "summary (1 sentence), next_action (1 sentence), self_help_steps (0-3), "
                    "confidence (0-1).\n\n"
                    "Rules:\n"
                    "- If recommended_path='maintenance', self_help_steps must be [].\n"
                    "- If recommended_path='self_help', provide 1-3 simple steps.\n\n"
                    f"TICKET:\n{text}"
                ),
            },
        ],
        text_format=TriageResult,
    )

    return response.output_parsed.model_dump()

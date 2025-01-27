from pydantic import BaseModel
from typing import Optional, List


# Input schema for text generation
class GenerateRequest(BaseModel):
    prompt: str
    max_length: Optional[int] = 50
    temperature: Optional[float] = 1.0
    top_p: Optional[float] = 0.9


# Response schema for generated text
class GenerateResponse(BaseModel):
    generated_text: str


# Response schema for history
class HistoryItem(BaseModel):
    id: int
    prompt: str
    generated_text: str


# Response schema for history list
class HistoryResponse(BaseModel):
    history: List[HistoryItem]
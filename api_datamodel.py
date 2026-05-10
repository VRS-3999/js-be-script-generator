from pydantic import BaseModel


class AskDagRequest(BaseModel):
    dagCode: str
    prompt: str

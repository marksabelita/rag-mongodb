from pydantic import BaseModel


class QuestionParamsModel(BaseModel):
    question: str

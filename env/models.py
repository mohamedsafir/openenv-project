from pydantic import BaseModel


class Observation(BaseModel):
    task: str
    state: str
    message: str


class Action(BaseModel):
    action_type: str
    content: str


class Reward(BaseModel):
    score: float
    feedback: str

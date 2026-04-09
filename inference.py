import os
import sys
from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI

# ENV
API_BASE_URL = os.getenv("API_BASE_URL", "https://api.openai.com/v1")
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4o-mini")
HF_TOKEN = os.getenv("HF_TOKEN")

if HF_TOKEN is None:
    raise ValueError("HF_TOKEN is required")

client = OpenAI(base_url=API_BASE_URL, api_key=HF_TOKEN)

# Fix path
ROOT_DIR = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, ROOT_DIR)

from env.environment import OpenEnv

app = FastAPI()

env = OpenEnv()

# -------- REQUEST FORMAT --------
class ResetRequest(BaseModel):
    task: str

class StepRequest(BaseModel):
    action: str


# -------- RESET --------
@app.post("/reset")
def reset(req: ResetRequest):
    obs = env.reset(req.task)
    return {"message": obs.message}


# -------- STEP --------
@app.post("/step")
def step(req: StepRequest):
    class Action:
        def __init__(self, content):
            self.content = content

    obs, reward, done, info = env.step(Action(req.action))

    return {
        "message": obs.message,
        "reward": reward,
        "done": done
    }

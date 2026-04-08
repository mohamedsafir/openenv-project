import os
import sys
from openai import OpenAI


from dotenv import load_dotenv
load_dotenv()
# 🔥 REQUIRED ENV VARIABLES
API_BASE_URL = os.getenv("API_BASE_URL", "https://api.openai.com/v1")
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4o-mini")
HF_TOKEN = os.getenv("HF_TOKEN")

if HF_TOKEN is None:
    raise ValueError("HF_TOKEN environment variable is required")

# 🔥 Fix path
ROOT_DIR = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, ROOT_DIR)

from env.environment import OpenEnv

# 🔥 OpenAI client
client = OpenAI(
    base_url=API_BASE_URL,
    api_key=HF_TOKEN
)

# FUNCTION WITH FALLBACK
def get_ai_response(prompt, level):
    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[{"role": "user", "content": prompt}],
            temperature=0
        )
        return response.choices[0].message.content.strip(), None

    except Exception as e:
        error_msg = str(e)
        # 🔥 FALLBACK
        if level == "easy":
            return "spam", error_msg
        elif level == "medium":
            return "[1,2,3,4,5]", error_msg
        else:
            return "a/b", error_msg

def run_task(level):
    env = OpenEnv()
    obs = env.reset(level)
    rewards = []
    steps = 0
    success = False
    # START
    print(f"[START] task={level} env=openenv model={MODEL_NAME}")

    try:
        while True:
            steps += 1
            action_str, error_msg = get_ai_response(obs.message, level)

            class Action:
                def __init__(self, content):
                    self.content = content

            obs, reward, done, info = env.step(Action(action_str))
            rewards.append(reward)
            reward_str = f"{reward:.2f}"
            done_str = str(done).lower()
            error_str = error_msg if error_msg else "null"
            # STEP
            print(f"[STEP] step={steps} action={action_str} reward={reward_str} done={done_str} error={error_str}")

            if done:
                success = reward > 0
                break

    except Exception as e:
        # Ensure STEP line even on crash
        print(f"[STEP] step={steps} action=error reward=0.00 done=true error={str(e)}")

    # END
    rewards_str = ",".join([f"{r:.2f}" for r in rewards])
    success_str = str(success).lower()

    print(f"[END] success={success_str} steps={steps} rewards={rewards_str}")


if __name__ == "__main__":
    for level in ["easy", "medium", "hard"]:
        run_task(level)

from env.models import Observation
from tasks.easy_task import get_easy_task
from tasks.medium_task import get_medium_task
from tasks.hard_task import get_hard_task

from graders.easy_grader import grade_easy
from graders.medium_grader import grade_medium
from graders.hard_grader import grade_hard


class OpenEnv:

    def __init__(self):
        self.current_task = None
        self.task_data = None
        self.done = False
        self.steps = 0

    def reset(self, level="easy"):
        self.done = False
        self.steps = 0

        if level == "easy":
            self.current_task = "easy"
            self.task_data = get_easy_task()
        elif level == "medium":
            self.current_task = "medium"
            self.task_data = get_medium_task()
        else:
            self.current_task = "hard"
            self.task_data = get_hard_task()

        return Observation(
            task=self.current_task,
            state="start",
            message=self.task_data["question"]
        )

    def step(self, action):
        # ✅ Handle already finished case safely
        if self.done:
            return (
                Observation(
                    task=self.current_task,
                    state="done",
                    message="Task already completed"
                ),
                0.0,
                True,
                {"score": 1.0, "steps": self.steps}
            )

        self.steps += 1

        # ✅ Safe action handling
        content = getattr(action, "content", "")

        # 🔍 grading
        if self.current_task == "easy":
            score = grade_easy(content, self.task_data)
        elif self.current_task == "medium":
            score = grade_medium(content, self.task_data)
        else:
            score = grade_hard(content, self.task_data)

        # 🎯 reward shaping
        if score == 1.0:
            reward = 1.0
            self.done = True
        elif score == 0.5:
            reward = 0.3
        else:
            reward = -0.2

        # ⚠️ penalty for too many attempts
        if self.steps > 3 and not self.done:
            reward -= 0.5
            self.done = True

        return (
            Observation(
                task=self.current_task or "unknown",
                state = "done" if self.done else "in_progress",
                message = f"Step {self.steps} processed"
            ),
            reward,
            self.done,
            {"score": score, "steps": self.steps}
        )

    def state(self):
        return {
            "task": self.current_task,
            "done": self.done,
            "steps": self.steps
        }

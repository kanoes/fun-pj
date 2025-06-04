import os
from typing import List, Dict

try:
    import openai
except ImportError:  # pragma: no cover - optional dependency
    openai = None


class DungeonMaster:
    """Interact with the LLM acting as the game master."""

    def __init__(self, session_history: List[Dict[str, str]]):
        self._history = session_history

    def _call_openai(self) -> str:
        if openai is None:
            return "[OpenAI library missing]"
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            return "[OPENAI_API_KEY not set]"
        openai.api_key = api_key
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": h["role"], "content": h["content"]} for h in self._history],
        )
        return completion.choices[0].message.content

    def respond(self, prompt: str) -> str:
        self._history.append({"role": "user", "content": prompt})
        response = self._call_openai()
        self._history.append({"role": "assistant", "content": response})
        return response

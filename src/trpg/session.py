import json
import os
from typing import List, Dict

from .character import Character


class GameSession:
    """Manage session history and persistence."""

    def __init__(self, character: Character, log_file: str = "session.json"):
        self.character = character
        self.log_file = log_file
        self.history: List[Dict[str, str]] = []
        self._load()

    def _load(self) -> None:
        if os.path.exists(self.log_file):
            with open(self.log_file, "r", encoding="utf-8") as file:
                data = json.load(file)
                self.history = data.get("history", [])
                self.character = Character.from_dict(data.get("character", {}))

    def save(self) -> None:
        with open(self.log_file, "w", encoding="utf-8") as file:
            json.dump(
                {
                    "character": self.character.to_dict(),
                    "history": self.history,
                },
                file,
                ensure_ascii=False,
                indent=2,
            )

    def add_message(self, role: str, content: str) -> None:
        self.history.append({"role": role, "content": content})

    def chat_history(self) -> List[Dict[str, str]]:
        return self.history[:]

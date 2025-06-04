from dataclasses import dataclass, field
from typing import Dict, List


@dataclass
class Character:
    name: str
    race: str
    role: str
    level: int = 1
    inventory: List[str] = field(default_factory=list)
    stats: Dict[str, int] = field(
        default_factory=lambda: {
            "strength": 10,
            "dexterity": 10,
            "constitution": 10,
            "intelligence": 10,
            "wisdom": 10,
            "charisma": 10,
        }
    )

    def to_dict(self) -> Dict:
        return {
            "name": self.name,
            "race": self.race,
            "role": self.role,
            "level": self.level,
            "inventory": self.inventory,
            "stats": self.stats,
        }

    @classmethod
    def from_dict(cls, data: Dict) -> "Character":
        char = cls(
            name=data.get("name", "Unnamed"),
            race=data.get("race", "Human"),
            role=data.get("role", "Adventurer"),
            level=data.get("level", 1),
        )
        char.inventory = data.get("inventory", [])
        char.stats.update(data.get("stats", {}))
        return char

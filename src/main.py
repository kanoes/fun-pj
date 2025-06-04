import os
import json
from trpg.character import Character
from trpg.dm import DungeonMaster
from trpg.session import GameSession


def create_character() -> Character:
    name = input("角色名: ")
    race = input("种族: ")
    role = input("职业: ")
    return Character(name=name, race=race, role=role)


def run() -> None:
    if not os.path.exists("session.json"):
        print("创建新角色...")
        character = create_character()
    else:
        print("载入已有存档...")
        with open("session.json", "r", encoding="utf-8") as file:
            data = json.load(file)
            character = Character.from_dict(data.get("character", {}))
    session = GameSession(character)
    dm = DungeonMaster(session.history)
    print(f"欢迎, {session.character.name}! 输入 'quit' 退出.")
    while True:
        user_input = input("你: ")
        if user_input.lower() in {"quit", "exit"}:
            session.save()
            print("已保存进度，游戏结束.")
            break
        reply = dm.respond(user_input)
        session.add_message("assistant", reply)
        print("AI-DM:", reply)


if __name__ == "__main__":
    run()

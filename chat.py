from pydantic import BaseModel


class Chat(BaseModel):
    """Class representing a chat object."""
    player_slot: int
    type: str
    key: str

    def is_player_chat(self) -> bool:
        return self.type == "chat"

    def is_empty(self):
        return len(self.key) == 0

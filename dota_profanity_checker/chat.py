from pydantic import BaseModel


class Chat(BaseModel):
    """Class representing a chat object.

    WARNING! 'type' here does not refer to python type. It is an
    attribute name of the Chat class, defined by the format of the
    data the class is built on. The same goes for 'key', this does
    not refer to python dictionary keys.

    """
    player_slot: int
    type: str
    key: str

    def is_player_chat(self) -> bool:
        return self.type == "chat"

    def is_chatwheel_chat(self) -> bool:
        return self.type == "chatwheel"

    def is_empty(self):
        return len(self.key) == 0

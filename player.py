from pydantic import BaseModel, validator


class Player(BaseModel):
    """Class representing a player."""
    player_slot: int
    account_id: str = None
    hero_id: int
    chat_events: list = []

    class Config:
        validate_assignment = True

    @validator("chat_events")
    def set_chat_events(cls, chat_events):
        return chat_events or []

    def has_id(self) -> bool:
        return self.account_id is None

    def add_chat_event(self, chat_event):
        self.chat_events.append(chat_event)

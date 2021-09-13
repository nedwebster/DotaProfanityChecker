from pydantic import BaseModel


class Player(BaseModel):
    """Class representing a player."""
    player_slot: int
    account_id: str = None
    hero_id: int

    def has_id(self) -> bool:
        return self.account_id is None

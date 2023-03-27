from dataclasses import dataclass,field
from player import Player

@dataclass
class Party:
    players : list[Player]
    Map : list[list[str]]
    playercount : int = 1
    isGameStarted : bool = False
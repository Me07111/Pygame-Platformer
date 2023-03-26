from dataclasses import dataclass
import socket

@dataclass
class Party:
    sockets : list[socket.socket]
    map : list[list[str]]
    inputs : list[list[bool]] = [[False,False,False,False,False]]
    playerCount : int = 1
    isGameStarted : bool = False
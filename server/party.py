from dataclasses import dataclass,field
import socket

@dataclass
class Party:
    sockets : list[socket.socket]
    map : list[list[str]]
    inputs : list[list[bool]] = field(default_factory=[[False,False,False,False,False]])
    playerCount : int = 1
    isGameStarted : bool = False
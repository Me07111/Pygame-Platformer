from dataclasses import dataclass,field
import socket

@dataclass
class Player:
    socket : socket.socket
    inputs : list[bool] = field(default_factory=[False,False,False,False,False])
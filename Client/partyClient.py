import socket
import json

class PartyClient:
    def __init__(self, ipAddress, port):
        self.ipAddress = ipAddress
        self.port = port
        self.bufferSize = 4096
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.index = 0
        self.playerCount = 1
        self.socket.settimeout(5)
        self.map = []

    def connectToServer(self):
        print("nice")
        self.socket.connect((self.ipAddress, self.port))

    def disconnect(self):
        self.socket.close()
    
    def ping(self):
        try:
            self.socket.send("ping".encode())
            if(self.socket.recv(self.bufferSize).decode() == "pong"):
                return True
        except OSError:
            return False
    
    def sendCommand(self,command : str,**kwargs):
        if (self.ping()):
            string = command
            for key, value in kwargs.items():
                string += f"${value}"
            self.socket.send(string.encode())
            return self.socket.recv(self.bufferSize).decode()
        else:
            return False
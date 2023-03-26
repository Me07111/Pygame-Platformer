import socket
import json

class PartyClient:
    def __init__(self, ipAddress, port):
        self.ipAddress = ipAddress
        self.port = port
        self.bufferSize = 4096
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.index = 0
        self.socket.settimeout(5)

    def connectToServer(self):
        self.socket.connect((self.ipAddress, self.port))

    def disconnect(self):
        self.socket.close()

    def makeParty(self, partyName, map):
        jsonMap = json.dumps(map)
        self.socket.send(f"create${partyName}${jsonMap}".encode())
        response = self.socket.recv(self.bufferSize).decode()
        return response

    def connectToParty(self, partyName):
        self.socket.send(f"join${partyName}".encode())
        response = self.socket.recv(self.bufferSize).decode()
        self.index = int(response.split("$")[2])
        return response

    def sendLandupd(self,isGameStarted):
        response = self.socket.send(f"landUpd${isGameStarted}".encode())
        return int(response.decode())
    
    def sendUpdToServer(self, input):
        data = json.dumps(input)
        self.socket.send(f"upd${data}".encode())
        response = json.loads(self.socket.recv(self.bufferSize).decode())
        return response
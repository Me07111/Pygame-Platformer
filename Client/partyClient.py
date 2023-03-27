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
        self.map = []

    def connectToServer(self):
        print("nice")
        self.socket.connect((self.ipAddress, self.port))

    def disconnect(self):
        self.socket.close()

    def makeParty(self, partyName, map):
        self.map = map
        jsonMap = json.dumps(map)
        try:
            self.socket.send(f"create${partyName}${jsonMap}".encode())
            response = self.socket.recv(self.bufferSize).decode()
        except OSError:
            return False
        print(response)
        return response

    def connectToParty(self, partyName):
        try:
            self.socket.send(f"join${partyName}".encode())
            response = self.socket.recv(self.bufferSize).decode()
        except OSError:
            return False
        self.index = int(response.split("$")[2])
        self.map = json.loads(response.split("$")[1])
        return response

    def sendLandupd(self,isGameStarted):
        try:
            self.socket.send(f"landUpd${isGameStarted}".encode())
            response = self.socket.recv(self.bufferSize).decode()
        except OSError:
            return False
        return int(response.decode())
    
    def sendUpdToServer(self, input):
        try:
            data = json.dumps(input)
            self.socket.send(f"upd${data}".encode())
        except OSError:
            return False
        response = json.loads(self.socket.recv(self.bufferSize).decode())
        return response
    
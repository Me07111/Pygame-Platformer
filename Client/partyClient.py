import socket
import json

class PartyClient:
    def __init__(self, ipAddress, port):
        self.ipAddress = ipAddress
        self.port = port
        self.bufferSize = 1024
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.settimeout(5)
        self.connectToServer()

    def connectToServer(self):
        self.socket.connect((self.ipAddress, self.port))

    def makeParty(self, partyName, map):
        jsonMap = json.dumps(map)
        self.socket.send(f"create${partyName}${jsonMap}".encode())
        response = self.socket.recv(self.bufferSize).decode()
        return response

    def connectToParty(self, partyName):
        self.socket.send(f"join${partyName}".encode())
        response = self.socket.recv(self.bufferSize).decode()
        return response

    def sendUpdToServer(self, input):
        data = json.dumps(input)
        self.socket.send(f"upd${data}".encode())
        response = self.socket.recv(self.bufferSize).decode()
        return response
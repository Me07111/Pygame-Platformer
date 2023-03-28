import socket
from networkLib import sendMulti,recvMulti

class PartyClient:
    def __init__(self, ipAddress, port):
        self.ipAddress = ipAddress
        self.port = port
        self.bufferSize = 32768
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.index = 0
        self.playerCount = 1
        self.socket.settimeout(5)
        self.map = []

    def connectToServer(self):
        try:
            self.socket.connect((self.ipAddress, self.port))
            return True
        except OSError:
            return False

    def disconnect(self):
        self.socket.close()
    
    def ping(self):
        try:
            sendMulti("ping",self.socket)
            if  (self.socket,self.bufferSize) == "pong":
                return True
        except (OSError, socket.timeout):
            return False
    
    def sendCommand(self, command: str, **kwargs):
        if self.ping():
            string = command
            for key, value in kwargs.items():
                string += f"${value}"
            send_result = sendMulti(string, self.socket)
            if send_result is False:
                return False
            answer = recvMulti(self.socket, self.bufferSize)
            if answer is False:
                return False
            return answer
        else:
            return False

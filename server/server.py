import socket
import threading
import json
from party import Party
from player import Player
from sys import getsizeof

def getPartyInfo(clientSocket):
    i = 0
    for partyName, party in parties.items():
        for player in party.players:
            if player.socket == clientSocket:
                return partyName, i
        i += 1
    return None, None

# Set up constants
ipAddress = "192.168.1.197"
port = 12345
bufferSize = 16384
thread = None

# Create server socket
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind((ipAddress, port))
serverSocket.listen()
serverSocket.settimeout(0.5)

# Create dictionary of parties and their sockets
parties = {}

# Define function to handle client connections
def handleClient(clientSocket, clientAddress):
        while True:
            # Receive input from client
            data = clientSocket.recv(bufferSize)
            if not data:
                print("except")
                partyName, index = getPartyInfo(clientSocket)
                if partyName is not None and index == 0:
                    for player in parties[partyName].players:
                        player.socket.close()
                    del parties[partyName]
                elif(partyName is not None) and index != 0:
                    parties[partyName].plyercount -= 1
                    parties[partyName].players.pop(index)
                break
            
            # Parse input
            inputParts = data.decode().split("$")
            command = inputParts[0].lower()
            print(command)
            
            # Process command
            if command == "create":
                partyName = inputParts[1]
                if partyName not in parties:
                    host = Player(clientSocket,[False*5])
                    parties[partyName] = Party([host],inputParts[2])
                    print(parties[partyName].Map)
                    clientSocket.send(f"S${partyName}".encode())
                else:
                    clientSocket.send(f"Party {partyName} already exists".encode())
            elif command == "join":
                partyName = inputParts[1]
                if partyName in parties:
                    player = Player(clientSocket,[False*5])
                    parties[partyName].players.append(player)
                    partyName, index = getPartyInfo(clientSocket)
                    parties[partyName].playercount += 1
                    print(parties[partyName].Map)
                    jsonMap = json.dumps(parties[partyName].Map)
                    print(getsizeof(f"S${partyName}!${index}${jsonMap}".encode()))
                    print("sent",clientSocket.send(f"S${partyName}!${index}${jsonMap}".encode()),"bytes")
                else:
                    clientSocket.send(f"Party {partyName} does not exist".encode())
            elif command == "landupd":
                partyName, index = getPartyInfo(clientSocket)
                parties[partyName].isGameStarted = bool(inputParts[1])
                returnVal = str(parties[partyName].playercount)
                clientSocket.send(returnVal.encode()) 
            elif command == "upd":
                input = json.loads(inputParts[1])
                partyName, index = getPartyInfo(clientSocket)
                parties[partyName].players[index].input = input
                arr = []
                for i, player in enumerate(parties[partyName].players):
                    input = player.input
                    if(i != index):
                        arr.append(input)
                arr = json.dumps(arr)
                clientSocket.send(arr.encode())
            elif command == "ping":
                clientSocket.send("pong".encode())
            else:
                clientSocket.send("Invalid command".encode())

# Main loop to accept incoming connections
while True:
    # Accept incoming client connection
    try:
        clientSocket, clientAddress = serverSocket.accept()
        print("connection accepted")
        clientThread = threading.Thread(target=handleClient, args=(clientSocket, clientAddress))
        clientThread.start()
        thread = clientThread
    except OSError:
        continue
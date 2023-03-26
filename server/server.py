import socket
import threading
import json
from party import Party

def getPartyInfo(clientSocket):
    print(parties)
    for partyName, partys in parties.items():
        if clientSocket in partys.sockets:
            return partyName, partys.sockets.index(clientSocket)
    return None, None

# Set up constants
ipAddress = "192.168.1.197"
port = 12345
bufferSize = 1024

# Create server socket
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind((ipAddress, port))
serverSocket.listen()

# Create dictionary of parties and their sockets
parties = {}

# Define function to handle client connections
def handleClient(clientSocket, clientAddress):
    while True:
        # Receive input from client
        data = clientSocket.recv(bufferSize)
        if not data:
            break
        
        # Parse input
        inputParts = data.decode().split("$")
        print(inputParts)
        command = inputParts[0].lower()
        
        # Process command
        if command == "create":
            partyName = inputParts[1]
            if partyName not in parties:
                parties[partyName] = Party([clientSocket],inputParts[2])
                clientSocket.send(f"Created party {partyName}".encode())
            else:
                clientSocket.send(f"Party {partyName} already exists".encode())
        elif command == "join":
            partyName = inputParts[1]
            if partyName in parties:
                parties[partyName].sockets.append(clientSocket)
                partyName, index = getPartyInfo(clientSocket)
                parties[partyName].inputs.append([False,False,False,False,False])
                clientSocket.send(f"Succsessfully joined {partyName}!${parties[partyName].map}${index}".encode())
            else:
                clientSocket.send(f"Party {partyName} does not exist".encode())
        elif command == "landUpd":
            partyName, index = getPartyInfo(clientSocket)
            parties[partyName].isGameStarted = bool(inputParts[1])
            returnVal = str(parties[partyName].playerCount)
            clientSocket.send(returnVal.encode()) 
        elif command == "upd":
            input = json.loads(inputParts[1])
            partyName, index = getPartyInfo(clientSocket)
            parties[partyName].inputs[index] = input
            arr = []
            for i, input in enumerate(parties[partyName].inputs):
                if(i != index):
                    arr.append(input)
            arr = json.dumps(arr)
            clientSocket.send(arr.encode())
        else:
            clientSocket.send("Invalid command".encode())

# Main loop to accept incoming connections
while True:
    # Accept incoming client connection
    clientSocket, clientAddress = serverSocket.accept()
    
    # Create new thread to handle client
    clientThread = threading.Thread(target=handleClient, args=(clientSocket, clientAddress))
    clientThread.start()
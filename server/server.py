import socket
import threading
import json

def getPartyInfo(clientSocket):
    for partyName, partySockets in parties.items():
        if clientSocket in partySockets:
            return partyName, partySockets.index(clientSocket)
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
        command = inputParts[0].lower()
        
        # Process command
        if command == "create":
            partyName = inputParts[1]
            if partyName not in parties:
                parties[partyName] = [clientSocket]
                clientSocket.send(f"Created party {partyName}${inputParts[2]}".encode())
            else:
                clientSocket.send(f"Party {partyName} already exists".encode())
        elif command == "join":
            partyName = inputParts[1]
            if partyName in parties:
                parties[partyName].append(clientSocket)
                clientSocket.send(f"Joined party {partyName}".encode())
            else:
                clientSocket.send(f"Party {partyName} does not exist".encode())
        elif command == "upd":
            input = json.loads(inputParts[1])
            partyName, partyIndex = getPartyInfo(clientSocket)
            print(partyName)
            for i, socket in enumerate(parties[partyName]):
                if (i != partyIndex):
                    socket.send(f"{partyIndex} {input}")
        else:
            clientSocket.send("Invalid command".encode())

# Main loop to accept incoming connections
while True:
    # Accept incoming client connection
    clientSocket, clientAddress = serverSocket.accept()
    
    # Create new thread to handle client
    clientThread = threading.Thread(target=handleClient, args=(clientSocket, clientAddress))
    clientThread.start()
import socket
import time
import threading
from networkLib import recvMulti,sendMulti

def client():
    socket.setdefaulttimeout(1)
    start = time.perf_counter()
    ipAddress = "127.0.0.1"
    port = 12345
    client = socket.socket()
    client.connect((ipAddress,port))
    string = "hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh"
    print(sendMulti(string,client))
    end = time.perf_counter()
    print("client",end-start)
def server():
    start = time.perf_counter()
    ipAddress = "127.0.0.1"
    port = 12345
    bufferSize = 1024
    server = socket.socket()
    server.bind((ipAddress, port))
    server.listen(1)
    clientSocket, clientAddress = server.accept()
    print("rec",recvMulti(clientSocket))
    print("rec",recvMulti(clientSocket))
    print("rec",recvMulti(clientSocket))
    print("rec",recvMulti(clientSocket))
    print("rec",recvMulti(clientSocket))
    end = time.perf_counter()
    print("server",end-start)


servert = threading.Thread(target=server)
clientt = threading.Thread(target=client)
servert.start()
clientt.start()
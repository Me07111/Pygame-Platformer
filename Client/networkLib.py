import socket
import random

def sendMulti(message: str, sock: socket.socket) -> bool:
    #try:
    data = message.encode() + "#".encode()
    while data:
        sent = sock.send(data)
        print(sent)
        data = data[sent:]
        if not data:
            return
    #except (ConnectionResetError, TimeoutError):
        #return False
    #return True

def recvMulti(sock: socket.socket, buffer_size: int = 1024) -> str:
    chunks = []
    while True:
        chunk = sock.recv(buffer_size)
        if not chunk:
            break
        chunks.append(chunk)
        if(str(bytes(bytearray(chunk).pop())) == "#"):
            chunk = bytes(bytearray(chunk).pop())
            return b''.join(chunks).decode()
    #except (ConnectionResetError, TimeoutError):
        #return False


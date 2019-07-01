import socket

class IPSocket:

    def __init__(self, interface: str, type: int):
        self.socket = socket.socket(socket.PF_PACKET, socket.SOCK_RAW)
        self.socket.bind((interface, type))
    
    def send(self, data):
        self.socket.send(data)
    
    def read(self, buffer):
        self.socket.recv(buffer)
    
    
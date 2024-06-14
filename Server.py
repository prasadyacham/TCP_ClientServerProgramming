import socket
import threading

serverPort = 12000

SERVER = socket.gethostbyname((socket.gethostname()))

#print(SERVER)

ADDR = (SERVER, serverPort)
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind(ADDR)
serverSocket.listen(1)

print('The server is ready to receive')
while 1:
    connectionSocket,addr = serverSocket.accept()
    sentence = connectionSocket.recv(1024)
    capitalizedSentence = sentence.upper()
    connectionSocket.send(capitalizedSentence)
    connectionSocket.close()

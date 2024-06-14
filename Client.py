from socket import *
from pip._vendor.distlib.compat import raw_input

serverName = 'XXX.XXX.1.XXX'
serverPort = 5050
Format = 'utf-8'

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
sentence = raw_input('Input lowercase sentence:')
# sentenceencode = sentence.encode(Format)
clientSocket.send('Hi')
modifiedSentence = clientSocket.recv(1024)
print('From Server', modifiedSentence)
clientSocket.close()
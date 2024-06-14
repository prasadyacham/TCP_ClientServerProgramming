import socket

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = input("Enter the IP address of the server in XXX.XXX.X.XXX format: ")
Serverlist= SERVER.split(".")

#print (len(Serverlist))
#print (Serverlist)

Flag = True
while Flag == True:
    if (len(Serverlist) < 4 ):
        print ("Please enter valid IP Address in XXX.XXX.X.XXX format.")
        SERVER = input()
        Serverlist = SERVER.split(".")
    else:
        Flag = False

ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))


# send("Hello World!")
userinput = input("Type the command for set 'key' 'value' or get 'key' or just type Exit to disconnect: ")
while userinput.lower() != 'exit':
    send(userinput)
    userinput = input("Type the command for set and get or Exit to disconnect: ")
send(DISCONNECT_MESSAGE)

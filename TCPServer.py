#!/usr/bin/env python3
import socket
import threading

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


def handle_client(conn, addr):
    # print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        # print(msg_length)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)

            words = msg.split()

            if words[0] == 'get':
                Value = get(words[1])
                conn.send(Value.encode(FORMAT))

            elif words[0] == 'set':
                output = set(words[1], words[2])
                if output == 'STORED':
                    conn.send("STORED".encode(FORMAT))
                else:
                    conn.send(output.encode(FORMAT))
            elif msg == DISCONNECT_MESSAGE:
                conn.send("Connection Disconnected.. Bye Bye!".encode(FORMAT))
                connected = False
                print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")
            # print(f"[{addr}] {msg}")
            # conn.send("Msg received".encode(FORMAT))

            else:
                msg = "Received " + msg
                conn.send(msg.encode(FORMAT))

    conn.close()


def start( ):
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")


def set(Cachekey, Cachevalue):
    print("In Set")
    dict = {}
    file = open('Cache.txt')
    for eachline in file.readlines():
        key,value = eachline.split(":")
        if Cachekey == key:
            return 'NOT-STORED. DUPLICATE KEY!'
    try:
        with open("Cache.txt", "a") as fs2:
            str1 = Cachekey + ":" + Cachevalue + "\n"
            fs2.write(str1)
            fs2.close()
            return 'STORED'
    except:
        return 'NOT-STORED'

def get(CacheKey):
    print("In Get")
    with open("Cache.txt", "r") as fs1:
        for line1 in fs1:
            currentlinef1 = line1.split(":")
            if currentlinef1[0].lower() == CacheKey.lower():
                print(currentlinef1[1])
                return currentlinef1[1]
    return "Key Not Found!"


print("[Starting Server...")
start()

import os 
import socket 
import threading
import sys

Size = 1024 
Format = "utf-8"
Server_data_path = "server_data"

Host = socket.gethostbyname(socket.gethostname())
Port = 8080
if (len(sys.argv) ==1 and isinstance(sys.argv[0],int)):
    Port = sys.argv[0]
Addr = (Host, Port)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def handle_client(connection, addr):
    print(f"[NEW CONNECTION] {addr} connected")
    connection.send("Welcome to the File Server.".encode(Format))

    # Receiving the filename
    try:
        filename = connection.recv(Size).decode(Format)
        print(f"[RECV] Receiving the filename.")
        file = open(filename,"w")
        connection.send("HTTP/1.1 200 OK".encode(Format))
        connection.send("Filename Received".encode(Format))
    except FileNotFoundError:
        connection.send("HTTP/1.1 400 Bad Request".encode(Format))
    
    # Receiving the file data
    data = connection.recv(Size).decode(Format)
    print(f"[RECV] Receiving the file data.")
    file.write(data)
    connection.send("File data received.".encode(Format))
    file.close()

    Hosts=str(Host)
    ServerInfo = "HostName = " + Hosts + "\nsocketFamily = socket.AF_INET\nsocketType = socket.SOCK_STREAM" + "\nprotocol = TCP \nPort= "+ str(Port)
    # Send server details to Client
    connection.send("Receiving Server Details".encode(Format))
    connection.send(ServerInfo.encode(Format))

    #Receiving Client Details and print
    msgs = connection.recv(Size).decode(Format)
    print(f"[CLIENT]: {msgs} \n")
    ClientDetails = connection.recv(Size).decode(Format)
    print(f"[CLIENT]: Here are the Client details!\n{ClientDetails}")

    print(f"[DISCONNECTED] {addr} disconnected")
    connection.close()

def main():
    print("[STARTING] Server is starting.....")
    
    server.bind(Addr)
    server.listen(5)
    print(f"[LISTENING] Server is listening on IP={Host}: Port={Port}.")

    while True:
        connection, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(connection, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount()-1}")

if __name__ == "__main__":
    main()
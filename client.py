import socket 
import os
import sys
import time

Format = "utf-8"
Size = 1024

def main():
    Host = socket.gethostbyname(socket.gethostname())
    port = 8080 

    socket_family = socket.AF_INET
    socket_type = socket.SOCK_STREAM
    server = socket.socket(socket_family, socket_type)

    Addr = (Host, port)
    client = socket.socket(socket_family, socket_type)
    client.connect(Addr)

    t1 = time.time()
    # Welcome message
    r = client.recv(Size).decode(Format)
    print(f"[SERVER]: {r}")

    file = open("tempfile.txt","r")

    # Fetch from command line
    if (len(sys.argv)==3):
        host = sys.argv[0]
        port = sys.argv[1]
        filename = sys.argv[2]
        file = open(filename, "r")
    
    data = file.read()

    #Send filename and print server responses
    client.send("tempfile.txt".encode(Format))
    response = client.recv(Size).decode(Format)
    print(f"[SERVER]: {response}")
    msg = client.recv(Size).decode(Format)
    print(f"[SERVER]: {msg}")

    #Send data of file and print response from server
    client.send(data.encode(Format))
    datam = client.recv(Size).decode(Format)
    print(f"[SERVER]: {datam}")
    file.close()


    #Receiving Server Details and print
    m = client.recv(Size).decode(Format)
    print(f"\n[SERVER]: {m}")
    ServerDetails = client.recv(Size).decode(Format)
    print(f"[SERVER]: Here are the Server details!\n{ServerDetails}")
    
    Hosts=str(Host)
    ports = str(port)
    ClientInfo = "HostName = " + Hosts + "\nsocketFamily = socket.AF_INET\nsocketType = socket.SOCK_STREAM" + "\nprotocol = TCP \nPort= " + ports
    #Send server details to Client
    client.send("Receiving Client Details".encode(Format))
    client.send(ClientInfo.encode(Format))
    t2= time.time()

    #Calculate RTT
    print("\nTime in seconds: "+str(t2-t1)+"\n")

    print(f"Disconnected from the server.")
    client.close()

if __name__ == "__main__":
    main()


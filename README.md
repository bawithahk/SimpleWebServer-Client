# SimpleWebServer-Client
# Description 
    - To develop a multi-threaded Web server which interacts with any standard Web Clients
    - build a single thread web client that interacts with the web server and download from the server
    - display essential connection parameters of connection for both web client and web server

# Server Code Explanation
    1. Send welcome message to Client
    2. Receive the filename from client and send response 
        - if filename exist, then send send 200 OK HTTP response
        - else send 400 bad request
    3. Receive the file data from client and send the response to client
    4. Send server details to client
    5. Receive the client information and print

# Client Code Explanation
    1. get Host and Port number (default to 8080) 
    2. set up the server and bind the host and port to connect the client 
    3. Get the time for RTT 
    4. Print the Welcome message from server
    5. Get the host, port, or filename from the commandline 
    (This will reassign the previous values)
    6. Read the data from file and send the file name to server and print the responses from the server
    7. send the contents of the file to server and print response
    8. Receive the server informations from the server and print
    9. Send the Client information to server
    10. Calculate RTT and print

# Tools Used: 
    - VS Code
    - contains text file (tempfile.txt) for default file if not given by user
# Instructions to run code:
    ## Choice 1:
        - run server.py on vs code 
        - run client.py on vs code
    ## Choice 2: 
        - run server.py <port_number> on command line
        - run clinet.py <IP address> <port_number> <file_name>

# TIP: port 8080 has some issues with authorization with some locals and if you change the port number, this will run well!



    
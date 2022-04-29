# TCP or UDP server just to receive messages

Explanation:

1) The first line we import the librarie that we need, which is socket, the library that is going to allow us to connect to the port and listen

2) Then we setup the socket and bind to the host 0.0.0.0 (Means that we bind to all interfaces) and port 5000(tcp)

3) We listen and accept a connection, and we do clnt.recv(1024), which allows us to receive 1024 bytes from the client. I then print it to the screen using print()

4) We close all connections
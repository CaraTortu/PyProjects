import socket

try:
    # Setup the listening connection
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('0.0.0.0',5000))
    print("[+] Listening in port 5000")
    sock.listen(1)
x
    # Accept the connection and print the msg sent
    clnt, addr = sock.accept()
    print("[+] Received: " + clnt.recv(1024).decode().strip())
    
    # Cleanup
    clnt.close()
    sock.close()

except Exception as e:
    print("[-] ERROR")
    print(e)
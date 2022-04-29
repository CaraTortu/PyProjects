import socket, threading, termcolor

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 6000))
s.listen(1)
print("[+] Listening on port 5000")

clients = []

def broadcast(msg):
    global clients
    for client in clients:
        client.send(msg.encode())

def handle(username, clnt):
    global clients
    clients.append(clnt)
    clnt.send(termcolor.colored(f"Hello {username}!\n\n", 'blue').encode())
    broadcast(termcolor.colored("System", 'red')+f": {username} joined! Say hi!\n")

    while True:
        try:
            msg = clnt.recv(1024).decode().strip()
            broadcast(termcolor.colored(f"{username}", 'red')+f": {msg}\n")
        except:
            clients.remove(clnt)
            clnt.close()
            broadcast(termcolor.colored("System", 'red')+f": {username} left!\n")
            break



while True:
    clnt, addr = s.accept()
    clnt.send(termcolor.colored("Welcome to the chat server!. Please, enter your username: ", 'blue').encode())

    username = clnt.recv(1024).decode().strip()
    print(f"{addr} Connected to the server with the username {username}")

    thread = threading.Thread(target=handle, args=(username,clnt,))
    thread.start()
import socket, threading, random, string, json

def handle(clnt):
    global sendrecv2
    sendrecv = json.loads(sendrecv2)

    clnt.send(b"Do you want to receive [R] Or send [S] as file?: ")
    action = clnt.recv(64).decode().strip()



    if action == "R":

        id = ''.join(random.choice(string.ascii_lowercase) for i in range(32))
        sendrecv[id] = {"req": 0, "content": ""}
        sendrecv2 = json.dumps(sendrecv)
        clnt.send((f"Give this ID to the sender: {id}\n"+ "[+] Waiting for file...\n").encode())

        while True:
            sendrecv = json.loads(sendrecv2)
            if sendrecv[id]["req"] == 1:
                clnt.send(b"[+] File received!\n")
                clnt.send(sendrecv[id]["content"].encode())
                clnt.close()
                break

    elif action == "S":

        clnt.send(b"Please, enter the ID of the person: ")
        id = clnt.recv(1024).decode().strip()

        try:
            if sendrecv[id]:
                clnt.send(b"[+] ID IS VALID")
                contents = clnt.recv(4096)
                sendrecvjson = json.loads(sendrecv2)
                sendrecvjson[id]= {"content": contents.decode().strip(), "req": 1}
                sendrecv2 = json.dumps(sendrecvjson)
                clnt.send(b"[+] File sent successfully!")
                clnt.close()
        except KeyError:
            clnt.send(b"[-] ID WAS NOT VALID"); clnt.close()

    else: clnt.send(b"[-] Wrong action, rerun the script. Your options are [R] for receive and [S] for send!"); clnt.close()


if __name__ == "__main__":

    sendrecv2 = '{}'
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("0.0.0.0", 8000)); print("[+] Listening on port 8000")
    s.listen(1)

    while True:
        clnt, addr = s.accept()
        thread = threading.Thread(target=handle, args=(clnt,))
        thread.start()
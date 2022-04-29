import socket, os

ip = str(input("IP: "))
port = 8000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.connect((ip, port))
    print("[+] Connection was succesful!")
    action = str(input(s.recv(1024).decode()))
    if action == "S" or action == "R":
        if action == "R":
            s.send(b"R")
            print(s.recv(1024).decode().strip())
            s.recv(1024).decode().strip()
            file = str(input("Output filename: "))

            with open(file, 'a') as f:
                content = s.recv(4096).decode()
                f.write(content)
        else:
            s.send(b"S")
            s.send(str(input(s.recv(1024).decode())).encode())
            res = s.recv(1024).decode().strip()
            if "NOT" not in res:
                print("[+] ID is valid")
                
                with open(str(input("File path that you wanna send: "))) as f:
                    s.send(f.read().encode())
                    print(s.recv(1024).decode().strip())

except Exception as e:
    print("[-] Error: " + e)
#server 1
import time
import tkinter as tk
import socket
key="hello123"



from Des import encrypt_text , decrypt_text  # 

server=socket.socket(socket.AF_INET , socket.SOCK_STREAM)
server.bind(('localhost', 5001))

server.listen(1)
print("Waiting connection")

conn,addres=server.accept()

def sendmessage(address,posrt,client):
    while True:
        message=input("me : ")
        encryptmessage=encrypt_text(message,key).encode()
        client.sendto(encryptmessage, (address, posrt))
def recivemwssage(client):
    while True:
        data, addr = client.recvfrom(1024)
        decrypted = decrypt_text(data.decode(), key)
        print(f"[{addr}] => {decrypted}")


if conn:
    print(f"conniction with {addres}")
    print("Enter End or exit to close the connection")
    while conn:
        repaly=""
        data=conn.recv(1024).decode()
        decryptmessage=decrypt_text(data,key)
        print(f"Client: {decryptmessage}")
             
        repaly=input("me: ")
        if repaly.lower() == 'exit' or repaly.lower() == 'end':
            print("Closing connection.")
            break
        else:
            repaly=encrypt_text(repaly,key).encode()
        conn.send(repaly)
        print(f"Sent, waiting for reply...")
else:
    print("No Connictions : ")

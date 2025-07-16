import socket
from Des import encrypt_text , decrypt_text
key="hello123"


client=socket.socket(socket.AF_INET , socket.SOCK_STREAM)
client.connect(('localhost', 5001))

print("Enter End or exit to close the connection")

mes=input("me : ")
encypMessage=encrypt_text(mes,key)
client.send(encypMessage.encode()) 
print("Message sent, waiting for reply...")

def chat():
    end=False
    while(not end):
        a=""
        data=client.recv(1024).decode()
        data = decrypt_text(data, key)
        print(f"server: {data}")
        a=input("me ")
        if a !="end" and  client:
            a=encrypt_text(a,key).encode()
            if a:
                print(f"Sent, waiting for reply...")
                client.send(a)
        else:
            end=True
            client.close()
chat()
client.close()
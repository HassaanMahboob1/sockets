import socket
import  json
host = socket.gethostname()
port = 5555
BUFFER = 1000
server_socket = socket.socket()  
server_socket.bind((host, port))  
dict_data = {"message" : "input"}
print("Server started successfully\nWaiting for client to connect") 
server_socket.listen(1)
conn, address = server_socket.accept() 
print("Connection with: " + str(address) + "created")
print("Waiting for response from client ! ")
while True:
    data = conn.recv(BUFFER).decode()
    if not data:
        break
    data = json.loads(data)
    print("from connected user: " + data['message'])
    data = input("Enter Message : ") 
    dict_data["message"] = data
    json_data = json.dumps(dict_data)
    conn.send(bytes(json_data,encoding="utf-8"))  

conn.close() 



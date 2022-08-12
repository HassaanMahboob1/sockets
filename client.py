import socket
import json
host = socket.gethostname() 
port = 5555
BUFFER = 1000
client_socket = socket.socket() 
client_socket.connect((host, port)) 
dict_data = {"message" : "input"}
message = input("Enter Message : ")  
dict_data["message"] = message
while message.lower().strip() != 'end':
    json_data = json.dumps(dict_data)
    client_socket.send(bytes(json_data,encoding="utf-8"))  
    print("Waiting for response from server ! ")
    data = client_socket.recv(BUFFER).decode() 
    data = json.loads(data)
    print('Received from server: ' + data['message'])  
    message = input("Enter Message : ") 

client_socket.close() 


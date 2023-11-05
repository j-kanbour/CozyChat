from socket import *
from threading import Thread, Condition
import sys, select, json
import User_auth

# acquire server host and port from command line parameter
HOST = '192.168.1.210'
PORT = 5050
serverAddress = (HOST, PORT)

# define socket for the server side and bind address
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(serverAddress)

# List to store client connections
clients = {}

class ClientThread(Thread):
    def __init__(self, clientAddress, clientSocket):
        Thread.__init__(self)
        self.clientAddress = clientAddress
        self.client_socket = clientSocket
        self.clientAlive = False
        
        print("===== New connection created for: ", clientAddress)
        self.clientAlive = True

    def new_user(self, username, email, password):
        query = User_auth.new_user(username, email, password)
        if  query == 1:
            return 'FAIL: Username'
        elif query == 2:
            return 'FAIL: Email'
        elif query == 3:
            return 'SUCCESS'
        else:
            return 'INTERNAL ERROR'

    def sendmessage(self, message, receiver):
        global clients
        client = clients[receiver]
        try:
            client.send(message)
        except Exception as e:
            print(f"Error broadcasting message: {e}")

    def handle_client(self, client_socket, recipient):
        while True:
            try:
                message = self.client_socket.recv(1024)
                if not message:
                    break
                self.sendmessage(message, recipient)
            except Exception as e:
                print(f"Error: {e}")
                break

    def run(self):
        global clients
        global connections
        while self.clientAlive:
        
            data = self.client_socket.recv(1024)
            data = data.decode()
            data = json.loads(data)
            action = data["action"]
            
            if action == 'new user':
                print("[recv] New user request")
                message = self.new_user(data['username'], data['email'], data['password'])
                if message == "SUCCESS": 
                    clients[data['username']] = self.client_socket
                    username = data['username']
                print('[send] ' + message)
                self.client_socket.send(message.encode())
                continue

            elif action == 'login':
                print("[recv] login request")
                print(clients, data['username'])
                if data['username'] in clients:
                    message = 'FAIL'
                elif not User_auth.auth_login(data['username'], data['password']):
                    message = 'FAIL'
                else:
                    message = 'SUCCESS'
                    clients[data['username']] = self.client_socket
                    username = data['username']
                
                print('[send] ' + message)
                self.client_socket.send(message.encode())
                continue

            elif action == 'open_chat':
                #get receipient
                recipient = data['username']
                if recipient not in clients:
                    message = "USER NOT ACTIVE"

                    print('[send] ' + message)
                    self.client_socket.send(message.encode())
                else: 
                    message = "SUCCESS"

                    print('[send] ' + message)
                    self.client_socket.send(message.encode())

                    client_handler = Thread(target=self.handle_client, args=(self.client_socket, recipient))
                    client_handler.start()

print("\n===== Server is running =====")
print("===== Waiting for connection request from clients...=====")

while True:
    serverSocket.listen()
    clientSockt, clientAddress = serverSocket.accept()
    clientThread = ClientThread(clientAddress, clientSockt)
    clientThread.start()
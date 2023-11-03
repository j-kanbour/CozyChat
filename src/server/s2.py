from socket import *
from threading import Thread, Condition
import sys, select, json
import User_auth

# acquire server host and port from command line parameter
if len(sys.argv) != 2:
    print("\n===== Error usage, python3 TCPServer3.py SERVER_PORT ======\n")
    exit(0)
serverHost = "192.168.0.183"
serverPort = int(sys.argv[1])
serverAddress = (serverHost, serverPort)

# define socket for the server side and bind address
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(serverAddress)

t_lock = Condition()

class ClientThread(Thread):
    def __init__(self, clientAddress, clientSocket):
        Thread.__init__(self)
        self.clientAddress = clientAddress
        self.clientSocket = clientSocket
        self.clientAlive = False
        
        print("===== New connection created for: ", clientAddress)
        self.clientAlive = True
    
    def checkCMD(cmd,msg):
        try:
            if(msg[0:len(cmd.lower())]==cmd.lower()):
                return True
        except:
            return False
        return False
        
    def run(self):
        message = ''
        
        while self.clientAlive:
            # use recv() to receive message from the client
            data = self.clientSocket.recv(1024)
            if not data: exit(0)

            data = data.decode()
            data = json.loads(data)
            action = data["action"]

            # get lock as we might me accessing some shared data structures
            with t_lock:
            
                # if the message from client is empty, the client would be off-line then set the client as offline (alive=Flase)
                if action == 'exit':
                    self.clientAlive = False
                    print("===== the user disconnected - ", clientAddress)
                    break
                
                # handle message from the client
                if action == 'new user':
                    print("[recv] New user request")
                    if User_auth.new_user(data['Username'], data['password']):
                        message = 'Username taken, try another one'
                    else:
                        message = f'Welcome {action["Username"]}'
                    
                    print('[send] ' + message)
                    self.clientSocket.send(message.encode())
                    continue

                elif action == 'login':
                    print("[recv] New user request")
                    if User_auth.auth_login(data['Username'], data['password']):
                        message = 'Incorrect username or password'
                    else:
                        message = f'Welcome {action["Username"]}'
                    
                    print('[send] ' + message)
                    self.clientSocket.send(message.encode())
                    continue
                    
                else:
                    print("[recv] " + message)
                    print("[send] Cannot understand this message")
                    message = 'Cannot understand this message'
                    self.clientSocket.send(message.encode())

    def process_login(self):
        message = 'user credentials request'
        print('[send] ' + message)
        self.clientSocket.send(message.encode())

        # use recv() to receive message from the client
        data = self.clientSocket.recv(1024)
        message = data.decode()

    


print("\n===== Server is running =====")
print("===== Waiting for connection request from clients...=====")


while True:
    serverSocket.listen()
    clientSockt, clientAddress = serverSocket.accept()
    clientThread = ClientThread(clientAddress, clientSockt)
    clientThread.start()

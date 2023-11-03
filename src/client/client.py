from socket import *
import sys, json, time

#Server would be running on the same host as Client

serverHost = '192.168.1.210'
serverPort = 5050
serverAddress = (serverHost, serverPort)

# define a socket for the client side, it would be used to communicate with the server
clientSocket = socket(AF_INET, SOCK_STREAM)

# build connection with the server and send message to it
clientSocket.connect(serverAddress)

fail_log_count = 0

def log_in(): 
    while True:
        global fail_log_count
        if fail_log_count >= 5:
            print("Too many failed attempts: access locked for 1 minute")
            time.sleep(60)

        username = input("Username: ")
        password = input("Password: ")

        message = json.dumps({
            "action": "login",
            "username": username,
            "password": password,
        })

        clientSocket.send(message.encode())

        # wait for the reply from the server
        login_result = clientSocket.recv(1024)
        login_result = login_result.decode()

        if login_result == "SUCCESS":
            print(f"Welcome {username}")
            fail_log_count = 0
            break
        elif login_result == "FAIL":
            print("Uncessful Login")
            fail_log_count += 1
            continue

def new_acc():
    while True:
        username = input("Username: ")
        email = input("Email: ")
        password = input("Password: ")
        

        message = json.dumps({
            "action": "new user",
            "username": username,
            'email': email,
            "password": password,
        })

        clientSocket.send(message.encode())

        # wait for the reply from the server
        login_result = clientSocket.recv(1024)
        login_result = login_result.decode()

        if login_result == "SUCCESS":
            print(f"Welcome {username}")
            break
        elif login_result == "FAIL: Email":
            print("Email already registered, try aain")
            continue
        elif login_result == "FAIL: Username":
            print("Username already taken, try again")
            continue
        elif login_result == "INTERNL ERROR":
            print("Internal error, try again")
            continue

print("Welcome: please log in(1) or create a new account (2)")
while True:
    try:
        opt = int(input())
        break
    except ValueError:
        print("Enter (1) for login, or (2) for new account")
        continue

if opt == 1: log_in()
elif opt == 2: new_acc()

while True:
    message = input("===== Please type any messsage you want to send to server: =====\n")
    clientSocket.sendall(message.encode())

    # receive response from the server
    # 1024 is a suggested packet size, you can specify it as 2048 or others
    data = clientSocket.recv(1024)
    receivedMessage = data.decode()

    print()
        
    ans = input('\nDo you want to continue(y/n) :')
    if ans == 'y':
        continue
    else:
        break



# close the socket
clientSocket.close()
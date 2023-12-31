import socket
import threading, sys, json, time

# Server configuration
SERVER_HOST = '192.168.1.210'
SERVER_PORT = 5050

fail_log_count = 0

curr_chat = ''

def log_in(clientSocket):
    global fail_log_count
    while True:
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

        # Wait for the reply from the server
        login_result = clientSocket.recv(1024)
        login_result = login_result.decode()

        if login_result == "SUCCESS":
            print(f"Welcome {username}")
            fail_log_count = 0
            return True
        elif login_result == "FAIL":
            print("Unsuccessful Login")
            fail_log_count += 1
            continue

def new_acc(clientSocket):
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

        # Wait for the reply from the server
        login_result = clientSocket.recv(1024)
        login_result = login_result.decode()

        if login_result == "SUCCESS":
            print(f"Welcome {username}")
            return True
        elif login_result == "FAIL: Email":
            print("Email already registered, try again")
            continue
        elif login_result == "FAIL: Username":
            print("Username already taken, try again")
            continue
        elif login_result == "INTERNAL ERROR":
            print("Internal error, try again")
            continue

def receive_messages(client_socket):
    global curr_chat
    while True:
        try:
            message = client_socket.recv(1024)
            if not message:
                break
            print(f"{curr_chat}: {message.decode('utf-8')}")
        except Exception as e:
            print(f"Error receiving message: {e}")
            break

def authentication(clientSocket):
    print("Welcome: please log in (1) or create a new account (2)")
    while True:
        try:
            opt = int(input())
            break
        except ValueError:
            print("Enter (1) for login, or (2) for a new account")
            continue

    if opt == 1:
        if log_in(clientSocket): return True
    elif opt == 2:
        if new_acc(clientSocket): return True

def main():
    global curr_chat
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSocket.connect((SERVER_HOST, SERVER_PORT))
    
    #authenitcate the user
    while True:
        if authentication(clientSocket): break

    #try to connection with other user
    while True:
        receiver = input("Enter a username to open a secure connection: ")

        message = json.dumps({
            "action": "open_chat",
            "username": receiver,
        })

        clientSocket.sendall(message.encode())

        # Wait for the reply from the server
        chat_response = clientSocket.recv(1024)
        chat_response = chat_response.decode()

        if chat_response == "USER NOT ACTIVE":
            print('User not active, try again')
            continue
        else: 
            curr_chat = receiver
            break

    #establish secure connection with user
    

    #comunicating with other
    receive_thread = threading.Thread(target=receive_messages, args=(clientSocket,))
    receive_thread.start()
    while True:
        message = input("You: ")
        clientSocket.send(message.encode('utf-8'))

        if message.lower() == 'exit':
            clientSocket.send(message.encode('utf-8'))
            break
        clientSocket.send(message.encode('utf-8'))

if __name__ == "__main__":
    main()

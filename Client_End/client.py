import socket, os
from turtle import down
from helper_functions import substitute, transpose

def cwd(cmd):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    client_socket.send(cmd.encode())
    response = client_socket.recv(4096).decode()
    print('Current Working Directory is: ', response)
    client_socket.close()
        

def ls(cmd):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    client_socket.send(cmd.encode())
    response = client_socket.recv(1024).decode()
    response = eval(response)
    print('All files in this directory are:')
    print(*response, sep = "\n")
    client_socket.close()

def cd(cmd):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    client_socket.send(cmd.encode())
    response = client_socket.recv(1024).decode()
    print('Status: ', response)
    if (response == 'OK'):
        curr = client_socket.recv(1024).decode()
        print('Path is changed to: ', curr)
    else:
        curr = client_socket.recv(1024).decode()
        print("Path isn't changed. It is still: ", curr)
    client_socket.close()

def dwd(cmd):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    client_socket.send(cmd.encode())
    response = client_socket.recv(1024).decode()
    cmd = cmd.split(' ')
    print("Status: ", response)
    if (response == "OK"):
        with open('dwd_'+cmd[1], 'wb') as downloaded_file:
            while True:
                data = client_socket.recv(1024)
                if (cmd[2] == 'plain'):
                    downloaded_file.write(data)
                elif (cmd[2] == 'substitute'):
                    downloaded_file.write(substitute(data.decode(), -2).encode())
                elif (cmd[2] == 'transpose'):
                    downloaded_file.write(transpose(data.decode()).encode())
                print(data)
                if not data:
                    break
            downloaded_file.close()
    client_socket.close()

def upd(cmd):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    client_socket.send(cmd.encode())
    cmd = cmd.split(' ')
    try:
        with open(cmd[1], 'rb') as file_to_upload:
            client_socket.send("OK".encode())
            print("Status: OK")
            data = file_to_upload.read(1024)
            while(data):
                client_socket.send(data)
                data = file_to_upload.read(1024)
                file_to_upload.close()
    except:
        client_socket.send("NOK".encode())
        print("Status: NOK")
    client_socket.close()

def client_program():
    global host, port
    host = socket.gethostname()
    port = 5000
    print("Connecting to the server with HOST: ", host)
    cmd = str(input('>> '))   
    while cmd.lower().strip() != 'exit':
        cmd_list = cmd.split(' ')
        if (cmd_list[0] == 'cwd'):
            cwd(cmd)
        elif (cmd_list[0] == 'ls'):
            ls(cmd)
        elif (cmd_list[0] == 'cd'):
            cd(cmd)
        elif (cmd_list[0] == 'dwd'):
            dwd(cmd)
        elif (cmd_list[0] == 'upd'):
            upd(cmd)

        cmd = str(input('>> '))

if __name__ == '__main__':
    client_program()
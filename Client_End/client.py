import socket, os

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
    cmd = cmd.split(' ')
    with open(cmd[2] + '_dwd_' + cmd[1], 'wb') as downloaded_file:
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            downloaded_file.write(data)
        downloaded_file.close()
    client_socket.close()

def upd(cmd):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    client_socket.send(cmd.encode())
    cmd = cmd.split(' ')
    with open(cmd[1], 'rb') as file_to_upload:
        data = file_to_upload.read(1024)
        while(data):
            client_socket.send(data)
            data = file_to_upload.read(1024)
            file_to_upload.close()
    client_socket.close()

def client_program():
    global host, port
    host = socket.gethostname()
    port = 5000

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

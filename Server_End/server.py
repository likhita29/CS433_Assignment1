import socket, os
from pathlib import Path
from helper_functions import encrypt, reverse

def cwd(cmd):
    conn.send(os.getcwd().encode())

def ls(cmd):
    files = str(os.listdir())
    conn.send(files.encode())
    
def cd(cmd):
    try:
        path = Path(cmd[1])
        os.chdir(path)
        conn.send('OK'.encode())
        conn.send(os.getcwd().encode())
    except OSError:
        conn.send('NOK'.encode())
        conn.send(os.getcwd().encode())

def dwd(cmd):
    with open(cmd[1], 'rb') as file_to_download:
        for word in file_to_download:
            if (cmd[2] == 'plain'):
                conn.sendall(word)
            elif (cmd[2] == 'substitute'):
                conn.sendall(encrypt(word.decode(), 2).encode())
                conn.sendall("\n".encode())
            elif (cmd[2] == 'reverse'):
                conn.sendall(reverse(word.decode()).encode())
                conn.sendall("\n".encode())

def upd(cmd):
    with open('uploaded_'+cmd[1], 'wb') as uploaded_file:
        cmdv= conn.recv(1024)
        while True:
            if not cmd:
                break
            else:
                uploaded_file.write(cmd)
                cmd = conn.recv(1024)
            uploaded_file.close()
            break

def server_program():
    host = socket.gethostname()
    port = 5000
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)

    while True:
        global conn
        conn, address = server_socket.accept()
        cmd = conn.recv(1024).decode()
        if (cmd == 'exit'):
            conn.close()
            break
        cmd = cmd.split(' ')
        if (cmd[0] == 'cwd'):
            cwd(cmd)
        elif (cmd[0] == 'ls'):
            ls(cmd)
        elif (cmd[0] == 'cd'):
            cd(cmd)
        elif (cmd[0] == 'dwd'):
            dwd(cmd)
        elif (cmd[0] == 'upd'):
            upd(cmd)
        conn.close()


if __name__ == '__main__':
    server_program()

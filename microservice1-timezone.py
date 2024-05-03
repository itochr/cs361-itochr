# Based on code from https://realpython.com/python-sockets/
# this microservice takes a 2-char state code and returns the time zone to the main program

import socket

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 5478  # Port to listen on (non-privileged ports are > 1023)

while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
    
            while True:
                
                data = conn.recv(1024).decode()
                
                if not data:
                    break
                
                if data == 'OR':
                    conn.sendall("PT".encode())
               
                if data == 'CO':
                    conn.sendall("MT".encode())

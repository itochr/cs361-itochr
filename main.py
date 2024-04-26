import socket
import typer
import threading
from rich.console import Console
from rich.table import Table

HEADER = 64
PORT = 5050
#SERVER = "10.0.0.103"
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MSG = "DISCONNECT!"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
   print("[NEW CONNECTION] {addr} connected.")
   connected = True
   while connected:
      msg_length = conn.recv(HEADER).decode(FORMAT)
      if msg_length:
         msg_length = int(msg_length)
         msg = conn.recv(msg_length).decode(FORMAT)
         if msg == DISCONNECT_MSG:
            connected = False
         print(f"[{addr}] {msg}")
   conn.close()

def start():
   server.listen()
   print(f"[LISTENING] server is listening on {SERVER}")
   while True:
      conn, addr = server.accept()
      thread = threading.Thread(target = handle_client, args = (conn, addr))
      thread.start()
      print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")


print("[STARTING] server is starting...")
start()



# console = Console()
# app = typer.Typer()

# @app.command(short_help = 'Add new appointment')
# def add(appt: str, category: str):
#    typer.echo(f"adding {appt}, {category}")


# if __name__ == "__main__":
#     app()

import socket 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(5)

while True: 
  clientsocket, address = s.accept()
  print(f"Connection from vice: {address} has been established")
  clientsocket.send(bytes("Welcome to Venus Server!", "utf-8"))
  clientsocket.close()
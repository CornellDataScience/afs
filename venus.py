import socket 
import select 

HEADER_LENGTH = 10
IP = "127.0.0.1"
PORT = 1234

# Initialize and bind socket for stream and resuse same socket for 
# reconnection if it goes down
venus_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
venus_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
venus_socket.bind((IP,PORT))

#All sockets including venus
sockets_list = [venus_socket]
#client socket is key and data is value 
vices = {}

def receive_message(vice_socket):
  try:
    message_header = vice_socket.recv(HEADER_LENGTH)
    #If no data is given
    if not len(message_header):
      return False
    else: 
        message_length = int(message_header.decode("utf-8"))
        #Problematic because this assumes small messages, not the case for files
        # Have to figure out buffering system 
        return {"header":message_header, "data":vice_socket.recv(message_length)}
  except:
    pass


while True: 
  

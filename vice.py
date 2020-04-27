import socket
import select
import json
import enum
import pickle


#SERVER 


HEADER_LENGTH = 10
IP = "127.0.0.1"
PORT = 1234
class message_type(enum.Enum):
  file_request = 1
  file_update = 2



with open('parameter.json') as f:
    data = json.load(f)
HEADER_LENGTH = data['HEADER_LENGTH']
IP = data["IP"]
PORT = data['PORT']
CONNECTION = data['CONNECTION']

HEADER_LENGTH = data['HEADER_LENGTH']
IP = data["IP"]
PORT = data['PORT']
CONNECTION = data['CONNECTION']


# Initialize and bind socket for stream and resuse same socket for
# reconnection if it goes down
venus_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
venus_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
venus_socket.bind((IP,PORT))

#All sockets including venus
sockets_list = [venus_socket]
#client socket is key and data is value
vice_data = {}

def receive_message(vice_socket):
  try:
    message_header = vice_socket.recv(HEADER_LENGTH)
    #If no data is given
    if not len(message_header):
      return False
    else:
        message_length = int(message_header.decode("utf-8"))
        message = pickle.load(vice_socket.recv(message_length))
        #Problematic because this assumes small messages, not the case for files
        # Have to figure out buffering system 
        return {"length":message_length, "type":message['type'], 
        "time":message['time'], data:message['data']}
  except:
    return False

while True:
  #select.select takes first a read list and a write list
  read_sockets, _, exception_sockets = select.select(sockets_list, [], sockets_list)
  for incoming_socket in read_sockets:
    if incoming_socket == venus_socket:
      vice_socket, vice_address = venus_socket.accept()
      client_data = receive_message(vice_socket)

      if client_data is False:
        continue

      sockets_list.append(vice_socket)
      vice_data[vice_socket] = client_data
      print("Message received")
    else: 
      message = receive_message(incoming_socket)
      if message is False:
        print(f"Closed Connection from {vice_data[incoming_socket]['data'].decode('utf-8')}")
        sockets_list.remove(incoming_socket)
        del vice_data[incoming_socket]
        continue
      user = vice_data[incoming_socket]
      print(f"Received message from {user['data'].decode('utf-8')}")
      #Below here is where you place message handling/protocols/propogation 
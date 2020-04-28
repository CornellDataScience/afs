import socket
import select
import time
import json
import pickle
import venusfs
from fuse import FUSE, FuseOSError, Operations


#CLIENT


HEADER_LENGTH = 4
IP = "127.0.0.1"
PORT = 1234
# all the files stored locally
venus_data = {}

venus_file = FUSE(venusfs.VenusFilesystem(root), "/", nothreads=True,
         foreground=True, **{'allow_other': True})

class myMessage:
    def __init__(self, file_name, type, change):
        self.message = file_name
        #type can be open, close, or request
        self.type = type
        #whether the file has been changed(0 means no change)
        self.change = change
    #create a json message to send
    def msg(self):
        msg = {}
        msg['length'] = len(file_name)
        msg['type'] = self.type
        msg['time'] = time.time()
        msg['data'] = str(self.file_name)
        return json.dump(msg)
    def covertStr(self):
        return str(self.messages)

#Initialize and connect socket
vice_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
vice_socket.connect((socket.gethostname(),PORT))

def receive_message(vice_socket):
  try:
    message_header = venus_socket.recv(HEADER_LENGTH)
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

#can move this into venusfs and just use venus_file.open(file_name.convertStr())
def open(file_name):
    if file_name.convertStr() in venus_data.key():
        #check whether the file is stored locally
        file = venus_data.get[file_name]
        print ("file in local cache")
        return False
    else:
        # if not, make it a request message and run the request func
        file_name.type = "request"

def request(request_msg):
    #establish connection with server
    venus_socket, address = vice_socket.accept()
    #create dic for the message
    message = request_msg.msg()
    serversocket.send(bytes(message, "utf-8")) #should this be vice_socket
    print("file not in local cache, request sent")


while True:
    input_type = input("Please enter the type of action you would like to do ('open', 'close'):")
    input_message = input("Please enter the file name:")
    # initialize the input message as myMessage class
    message = myMessage(input_message, input_type)
    if message.type == "open":
        open(message)
    if message.type == "request":
        request(message)
        server_data = receive_message(venus_socket)
        if server_data is False:
            continue
        print(f"Received message from the server")
        server_message = myMessage(server_data['body'], server_data['type'])
        venus_data[server_message.convertStr()] = None #not sure how to express the content of the file

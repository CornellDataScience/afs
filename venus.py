import socket
import select
import time
import json
import pickle

#CLIENT


with open('parameter.json') as f:
    data = json.load(f)
HEADER_LENGTH = data['HEADER_LENGTH']
IP = data["IP"]
PORT = data['PORT']
CONNECTION = data['CONNECTION']
# all the files stored locally
venus_data = {}

#Initialize and connect socket
vice_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def open(file_name):
    if file_name in venus_data.key():
        #check whether the file is stored locally
        file = venus_data.get[file_name]
        return False
    else:
        request_msg = file_name
        type = "open"

while True:
    venus_socket, address = s.accept()
    tstamp = time.time()
    msg = str(len(request_msg)) + type + str(tstamp)
    venus_socket.sned(bytes(msg, "utf-8"))

import socket
import select
import time
import json
import pickle

#CLIENT


HEADER_LENGTH = 4
IP = "127.0.0.1"
PORT = 1234
# all the files stored locally
venus_data = {}

#Initialize and connect socket
vice_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
vice_socket.connect((socket.gethostname(),PORT))
def open(file_name):
    if file_name in venus_data.key():
        #check whether the file is stored locally
        file = venus_data.get[file_name]
        return False
    else:
        request_msg = file_name
        type = "open"

def request(file_name): 
    if file_name in venus_data.key():
        #get file from data and dont' send message
        print ("file in local cache");
    else:
        # send message request
        print ("file not in local cache");

while True:
    user_input = input("Please enter the action you would like to do (actions include" +
    "request 'file_name' open 'file_name'):")
    

import socket
import select
import time

#creating a hashtable of files
dict = {}
dict['a'] = 'alpha.txt'
dict['g'] = 'gamma.txt'
dict['o'] = 'omega.txt'

HEADER_LENGTH = 10
PORT = 1234
#our server will receive up to 5 connections
CONNECTION = 5
# fetch request of the file
reuqested_file = 'a'

#Initialize and connect socket
vice_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
vice_socket.bind((socket.gethostname(),PORT))
vice_socket.listen(CONNECTION)

while True:
    clientsocket, address = vice_socket.accept()
    print(f"Connection from {address} has been established")

    msg = dict[reuqested_file]
    msg = f'{len(msg):<{HEADERSIZE}}' + time.time() + msg
    clientsocket.send(bytes(msg, "tuf-8"))

#question: how to differentiate which files to send to different clients

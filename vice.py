import socket

vice_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
vice_socket.connect((socket.gethostname(),1234))
#think about the directories are array of arrays
home_directory = [[],[],[]]
#the first index in the array is the hashed name of the directory
home_directory[0][0] = hash('desired_directory')

def open(file_name):
  s.send(file_name)
  while True:
    msg = s.recv(1024)
    print(msg.decode("utf-8"))



def send_message(directoryFID, desired_directory):
    if directoryFID.equals(homeFID):
        desired_d = hash(desired_directory)
        for i in home_directory:
            if home_directory[i][0] == desired_d:
                #set up callbacks on the directory and the client
                #how to generate FID or what is the FID of each directories and files
                return home_directory[i][1:]

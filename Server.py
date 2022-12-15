# Server
import os
import socket

from cryptography.fernet import Fernet

import Config


# Server connection
def connect_server(self):
    s = socket.socket()
    print('Socket created')
    s.bind((Config.server_address, Config.port_number))
    s.listen(3) # take it out or put it into the config file (config.timeout(3))
    print('Waiting for connections')
    while self.running:
        c, addr = s.accept()
        name = c.recv(1024).decode() # put the number into the config file 
        print("connected with ", addr, name)
        data = c.recv(1024).decode()
        c.send(bytes('Welcome to the dictionary', 'utf-8')) # messages into the config file


# Server disconnection
def disconnect_server(self):
    self.running = False
    if self.s_socket is not None:
        self.s_socket.close()
        self.s_socket = None


# Decoding file from client
# send the information we received directly - the same as the client
def decode_file(filename, key):
    f = Fernet(key)
    with open(filename, "rb") as file:
        # read the encrypted data
        encrypted_data = file.read()
    # decrypt data
    decrypted_data = f.decrypt(encrypted_data)
    # write the original file
    with open(filename, "wb") as file:
        file.write(decrypted_data)

# Save file from client
# do not save file - only write to a file if it is in the config file. DO NOT USE FILES unless it is in the config file!!! print a screen or write to file
# config option
def save_file(self, encrypted_data, filename):
    directory_name = 'received_files'
    if not os.path.exists(directory_name):
        os.makedirs(directory_name)
    with open(directory_name + '/' + filename, "wb") as f:
        # Save the file in the directory
        f.write(encrypted_data)
        f.close()
        print('The file has been saved')

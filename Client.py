import json
import os
import pickle
import dict2xml as dict2xml
import Config
import socket
from dict2xml import dict2xml
from cryptography.fernet import Fernet
COUNTRIES = Config.countries

# Server connection
def connect_to_server(self):
    s = socket.socket()
    client = socket.socket()
    client.connect((Config.server_address, Config.port_number))
    name = input("Enter your name, please: ")
    client.send(bytes(name, 'utf-8'))
    data = input("Please type dictionary: ")
    client.send(bytes(data, 'utf-8'))
    print("Welcome to the dictionary:")

    for key, value in COUNTRIES.items():
      print(key, value, '\n')

# Server disconnect
def disconnect(self):
    if self.client_socket is not None:
        self.client_socket.send(f"EXIT".encode())
        self.client_socket.close()

# Edit dictionary
def edit(self, key, value):
    self.dictionary[key] = value

# Create new dictionary
 def create_new_dictionary(self):
     self.dictionary = {}

# File encryption
def encrypt(filename, key):
    #pass an extra variable containing the info we are sending .dumps
    f = Fernet(key)
    with open(filename, "rb") as file: 
        # read all file data
        file_data = file.read()
    # encrypt data
    encrypted_data = f.encrypt(file_data)
    # write the encrypted file
    with open(filename, "wb") as file:
        file.write(encrypted_data)

# Serialization/ pickle file
def serialise_dictionary(self, serialization):
    if Config.serialization_option == "JSON":
        with open('dico.json', 'w') as f:
            json.dump(self.dictionary, f)
            print('Dictionary serialised. Filename: JSON')
    elif Config.serialization_option == "BINARY":
        with open('dico.bin', 'wb') as f:
            pickle.dump(self.dictionary, f)
            print('Dictionary serialised. Filename: Binary')
    elif format == "XML":
        xml_content = dict2xml(self.dictionary, wrap="dictionary", indent="  ")
        with open('dico.xml', 'w') as f:
            f.write(xml_content)
            f.close()
            print('Dictionary serialised as XML. Filename: xml')
            #we do not need to write to files, we can return either JSON, pickle or XML

def display_dictionary(self):
    print(self.dictionary)

# Send file to server
# instead of filename, we pass the information directly to that function
def send_file(self, filename, encrypted_data):
    filesize = os.path.getsize(filename)
    self.client.send(f"{filename} \ {filesize} \ {encrypted_data}".encode())
    with open(filename, "rb") as file:
        while True:
            bytes_read = file.read(Config.Buffer_size)
            if not bytes_read:
                break
            self.client_socket.sendall(bytes_read)
    print(filename + ' was successfully sent to the server.')






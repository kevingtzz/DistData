#Client code
"""
August 1, 2021
Created by: Sebastian Loaiza Correa
"""
#Import socket library
import socket
import constants
import os

#Variables for connection
host = constants.SERVER_ADDRESS
port = constants.PORT

def runClientSocket():
    #Create client socket
    clientSocket = socket.socket()

    #Connection with server. first parameter = IP address, second parameter = Connection Port
    clientSocket.connect((host, port))
    print("Connected to server")


    #Maintain connection with the server
    while True:
        #Client command
        command = input("Enter the command you want to send >> ")
        informationToSend = ""
        if command == constants.PUT:
            key = input("Enter the key >> ")
            value = input("Enter the value >> ")
            informationToSend = command+","+key+","+value
        elif command == constants.GET:
            key = input("Enter the key >> ")
            informationToSend = command+","+key
        elif command == constants.UPDATE:
            key = input("Enter the key >> ")
            currentValue = input("Enter the current value >> ")
            newValue = input("Enter the new value >> ")
            informationToSend = command+","+key+","+currentValue+","+newValue
        elif(command == constants.DELETE):
            key = input("Enter the key >> ")
            informationToSend = command+","+key
        elif(command == constants.EXIT):
            break
        else:
            print("Non-existent command, try again")
            continue
        #Send message
        clientSocket.send(bytes(informationToSend, constants.ENCODING_FORMAT))
        #Server response
        response = clientSocket.recv(constants.BUFFER_SIZE)
        print(response.decode())
    #Close connection to the server
    clientSocket.close()
    print("Connection closed")

#Iniatialize client socket
runClientSocket()

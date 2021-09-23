#!/usr/bin/env python
"""
August 1, 2021
Created by: Sebastian Loaiza Correa
"""


import socket
import os
import constants
import shutil
import sys
import string
from _thread import *

minusculas = string.ascii_lowercase   # O si prefieres pones "abcde...z" que es lo mismo

def handleConecction(client):
	while True:
		request = client.recv(constants.BUFFER_SIZE).decode('ascii')
		options = request.split(',')
		checkStatus(options)

def letra_a_codigo(letra):
    return minusculas.index(letra) + 97

def getNode(key): 
# (negro, azul, marrón, gris, verde, naranja, rosa, púrpura, rojo, blanco y amarillo) 
# y los 28 adicionales 
# (turquesa, verde oliva, verde menta, borgoña, lavanda, magenta, salmón, cian, beige, 
# rosado, verde oscuro, verde oliva, lila, amarillo pálido, fucsia, mostaza, ocre, 
# trullo, malva, púrpura oscuro, verde lima, verde claro, ciruela, azul claro, melocotón, 
# violeta, tan y granate.
# A a F, G a L, M a S, T a Z
	keyVerification = letra_a_codigo(key[0])
	if (keyVerification >= 97 and keyVerification <= 102):
		return host, port
	elif (keyVerification >= 103 and keyVerification <= 108):
		return host, port
	elif (keyVerification >= 109 and keyVerification <= 115):
		return host, port
	elif (keyVerification >= 116 and keyVerification <= 122):
		return host, port
	else:
		return "0",0
    
    

def checkStatus(options):
	key = options[0]
	host, port = getNode(key)
	#TO DO connect to node and send data
	#sendToNode(host, port)


def sendToNode(options, host, port):
	clientSocket = socket.socket()
	clientSocket.connect((host, port))
	print("Connected to node")
	clientSocket.send(bytes(informationToSend, constants.ENCODING_FORMAT))
	response = clientSocket.recv(constants.BUFFER_SIZE)
	print(response.decode())
	clientSocket.close()

try:
	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server.bind(("172.31.1.2", constants.PORT))
	server.listen(5)
	threadCount = 0
	try:
		test_db = sys.argv[1]
	except:
		test_db = input("Enter buckets path >> ")

	if not os.path.exists(test_db):
		os.makedirs(test_db)
	print("SERVER UP!\nlistening...")

	while True:
		client, address = server.accept()
		print('Connected to: ' + address[0] + ':' + str(address[1]))
		start_new_thread(handleConecction, (client, ))
		threadCount += 1
		print('Thread Number: ' + str(threadCount))
except Exception as error:
	print("Server error")
	print(error)
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
from _thread import *


def handleConecction(client):
	while True:
		request = client.recv(constants.BUFFER_SIZE).decode('ascii')
		options = request.split(',')
		checkStatus(options)


def checkStatus(options):
	key = options[0]
	#host, port = getNode(key)
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

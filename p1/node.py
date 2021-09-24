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


data = dict()

def handleConecction(client):
	while True:
		request = client.recv(constants.BUFFER_SIZE).decode('ascii')
		options = request.split(',')
		checkStatus(options)


def checkStatus(options):
	if options[0] == constants.PUT:
		createBucket(options[1])
	elif options[0] == constants.GET:
		get(options[1])
	elif options[0] == constants.UPDATE:
		getFileList(options[1])
	elif options[0] == constants.DELETE:
		deleteFile(options[1], options[2])

def put(key, value):
    list = []
    if data[key]:
        list = data[key].append(value)
    else:
        list = [value]
    data[key] = list

def get(key):
    if data[key]:
        list = '\n'.join(data[key])
        client.send(list.encode('ascii'))
    else:
        client.send('key not found'.encode('ascii'))

try:
	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server.bind(("172.31.1.2", constants.PORT))
	server.listen(5)
	threadCount = 0
	print("NODE UP!\nlistening...")

	while True:
		client, address = server.accept()
		print('Connected to: ' + address[0] + ':' + str(address[1]))
		start_new_thread(handleConecction, (client, ))
		threadCount += 1
		print('Thread Number: ' + str(threadCount))
except Exception as error:
	print("Server error")
	print(error)

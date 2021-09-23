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
	if options[0] == constants.HELLO:
		#createBucket(options[1])
	elif options[0] == constants.PUT:
		#createFile(options[1], options[2])
	elif options[0] == constants.GET:
		getKeyList(options[1])
	elif options[0] == constants.UPDATE:
		#deleteFile(options[1], options[2])
	elif options[0] == constants.DELETE:
		#downloadFile(options[1], options[2])




def getKeyList(bucketName):
	fileList = os.listdir(os.path.join(test_db, bucketName))
	if len(fileList) > 0:
		strList = '\n'.join([str(e) for e in fileList])
	else:
		strList = "Empty bucket."
	client.send(strList.encode('ascii'))



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


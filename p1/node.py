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

import pickle

nombre_archivo= '/home/database.txt'
#dataToSave = [("Negro", 1, "7:06"), ("Anaconda", 32, "6:3")]

data = dict()

def handleConecction(client):
	data = callData(nombre_archivo)
	while True:
		request = client.recv(constants.BUFFER_SIZE).decode('ascii')
		options = request.split(',')
		checkStatus(options)


def checkStatus(options):
	if options[0] == constants.PUT:
		put(options[1], options[2])
	elif options[0] == constants.GET:
		get(options[1])
	elif options[0] == constants.UPDATE:
		update(options[1], options[2], options[3])
	elif options[0] == constants.DELETE:
		delete(options[1])

"""
saveData(nombre_archivo, dataToSave):
	nombre_archivo -> Name of the file (with the address)
	dataToSave -> could be the options (is the data that we going to save early)
"""
def saveData(nombre_archivo, dataToSave):
    archivo = open(nombre_archivo, "wb")
    pickle.dump(dataToSave, archivo)
    archivo.close()

"""
callData(nombre_archivo)
	nombre_archivo -> Call the file (same address)
	Use the pickle library to unicode the data saved and return it
"""
def callData(nombre_archivo):
    archivo = open(nombre_archivo, "rb")
    dataToSave = pickle.load(archivo)
    archivo.close()
    return dataToSave


def put(key, value):
    list = []
    if key in data.keys():
        data[key].append(value)
    else:
        list = [value]
        data[key] = list
    msg = key + ": " + value + " saved"
    client.send(msg.encode('ascii'))
    saveData(nombre_archivo, data)

def get(key):
    if key in data.keys():
        list = '\n'.join(data[key])
        client.send(list.encode('ascii'))
    else:
        client.send('key not found'.encode('ascii'))

def update(key, current, new):
	if key in data.keys():
		list = data[key]
		index = -1
		try:
			index = list.index(current)
		except:
			client.send('Current value not found in key'.encode('ascii'))
		if index > -1:
			list[index] = new
		data[key] = list
		client.send('Update action finished'.encode('ascii'))
	else:
		client.send('key not found'.encode('ascii'))
	saveData(nombre_archivo, data)

def delete(key):
	remove_key = data.pop(key, "None")
	msg = ','.join(remove_key) + ' deleted'
	client.send(msg.encode('ascii'))
	saveData(nombre_archivo, data)

try:
	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server.bind(("0.0.0.0", constants.PORT))
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

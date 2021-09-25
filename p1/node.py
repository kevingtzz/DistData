#!/usr/bin/env python
"""
August 1, 2021
Created by: Sebastian Loaiza Correa, Kevin Gutierrez, Cristian Ceballos
"""


import socket
import constants
from _thread import *
import json

#dataToSave = [("Negro", 1, "7:06"), ("Anaconda", 32, "6:3")]

data = dict()

def handleConecction(client):
	try:
		data = callData(constants.FILENAME)
	except:
		print('holi')
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
def saveData(fileName, dataToSave):
    file = open(fileName, "w")
    json.dump(dataToSave, file)
    file.close()

"""
callData(nombre_archivo)
	nombre_archivo -> Call the file (same address)
	Use the pickle library to unicode the data saved and return it
"""
def callData(fileName):
    file = open(fileName, "r")
    dataToSave = file.read()
    file.close()
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
    saveData(constants.FILENAME, data)

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
	saveData(constants.FILENAME, data)

def delete(key):
	remove_key = data.pop(key, "None")
	msg = ','.join(remove_key) + ' deleted'
	client.send(msg.encode('ascii'))
	saveData(constants.FILENAME, data)

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

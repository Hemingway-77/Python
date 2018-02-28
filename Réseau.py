# !/usr/bin/python3
# coding: utf-8
'''
import socket # Socket est un point d'entree

ip = socket.gethostbyname(socket.gethostname()) # ip local

print (ip)
'''


import os

subnet = "192.168.0."

for i in range(1,255):
	hostname = subnet + str(i)

	response = os.system("ping -n 1 "+ hostname)

	if response == 0:

		print (hostname, 'is up !')

#!/usr/bin/python3

import socket

serversocket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.settimeout(5)

host = input("please enter the ip address you want to sacan ")
port = int(input("please enter the port you want to sacan "))

def portscanner(port):
    if serversocket.connect_ex((host,port)):
       print("this port is closed")
    else:
        print("this port is open")

portscanner(port)

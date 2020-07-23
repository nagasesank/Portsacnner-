#!/usr/bin/python3

import socket

serversocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#host = '192.168.1.151'
host = socket.gethostname()
port = 444

serversocket.bind(('191.168.1.151', port))

serversocket.listen(3)

while True:
    clientsocket , Address = serversocket.accept()
    print("Connection Established %s " % str (Address))

    message = 'Thank you for conncetion to the server ' + "\r\n"

    clientsocket.send(message.encode('ascii'))

    clientsocket.close()

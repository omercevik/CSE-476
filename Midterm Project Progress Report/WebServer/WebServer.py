"""
CSE 476 Mobile Communication Networks
Midterm Project
Web Server

WebServer.py
@author Omer CEVIK
161044004
"""
#import socket module
from socket import *

serverSocket = socket(AF_INET, SOCK_STREAM)

#Prepare a server socket
#Fill in start

HOST = '0.0.0.0'
PORT = 6789
serverSocket.bind((HOST, PORT))
serverSocket.listen(1)

#Fill in end

while True:

    #Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()

    try:
        message = connectionSocket.recv(1024)

        filename = message.split()[1]
        f = open(filename[1:])

        outputdata = f.read()

        #Send one HTTP header line into socket
        #Fill in start

        connectionSocket.send('HTTP/1.1 200 OK\r\n\r\n'.encode())

        #Fill in end

        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i])
        connectionSocket.close()
    except IOError:
        #Send response message for file not found
        #Fill in start

        connectionSocket.send('404 Not Found')

        #Fill in end

        #Close client socket
        #Fill in start

        connectionSocket.close()

        #Fill in end
serverSocket.close()

"""
CSE 476 Mobile Communication Networks
Midterm Project
UDP Pinger Client

UDPPingerClient.py
@author Omer CEVIK
161044004
"""

# Import time, socket, UDP protocol
from socket import AF_INET, SOCK_DGRAM
import time
import socket

# Init host as localhost, port, buffersize as 1024 and server address.
HOST = "127.0.0.1"
PORT = 12000
bufferSize = 1024
serverAddressPort = (HOST, PORT)

# Initialize simple ping message of client and encode it.
pingMsg = "Ping Message "
bytedPingMsg = pingMsg.encode()

# Message counter initialization with 1.
messageCounter = 1

# Creating UDP client socket.
UDPClientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Setting the wait time to 1 second.
UDPClientSocket.settimeout(1)

# Creating a loop for 10 messages of client.
while messageCounter <= 10:

    # RTT time begin.
    start_rtt = time.time()

    # Sending client byted message to server.
    UDPClientSocket.sendto(bytedPingMsg, serverAddressPort)

    try:
        # Waiting response of server on UDP socket.
        msgFromServer = UDPClientSocket.recvfrom(bufferSize)

        # RTT time end and distinct of start-end time of message trip.
        end_rtt = time.time()
        distinct_rtt = end_rtt - start_rtt

        # Printing the message which is upper cased by server, message counter and RTT time.
        msg = str(msgFromServer[0]) + str(messageCounter) + " " + str(distinct_rtt)
        print(msg)
    except socket.timeout:
        # If time out is generated about 1 second then printing the information.
        print("Request timed out")

    # Increasing message counter.
    messageCounter += 1

# Closing socket.
UDPClientSocket.close()

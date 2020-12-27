"""
CSE 476 Mobile Communication Networks
Midterm Project
Mail Client

MailClient.py
@author Omer CEVIK
161044004
"""

from socket import *
import base64
import sys
import ssl

msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"

# Choose a mail server (e.g. Google mail server) and call it mailserver

# Choose mailserver as live or gmail.
# mailserver = ("smtp.live.com", 587)
mailserver = ("smtp.gmail.com", 587)

# Create socket called clientSocket and establish a TCP connection with mailserver
#Fill in start

# Creating socket TCP protocoled.
clientSocket = socket(AF_INET, SOCK_STREAM)

# Connecting to mail server and printing the response.
clientSocket.connect(mailserver)

recvConnect = clientSocket.recv(1024)
recvConnect = recvConnect.decode()
print("RECV CONNECT : " + recvConnect)
if recvConnect[:3] != '220':
    print('220 reply not received from server.')

#Fill in end


# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode())

recvHelloCommand = clientSocket.recv(1024)
recvHelloCommand = recvHelloCommand.decode()
print("RECV HELLO COMMAND : " + recvHelloCommand)

if recvHelloCommand[:3] != '250':
    print('250 reply not received from server.')

# Send MAIL FROM command and print server response.
# Fill in start

# Start TLS sending STARTTLS command and printing the response.
startTlsMsg = 'STARTTLS\r\n'
clientSocket.send(startTlsMsg.encode())
recvTls = clientSocket.recv(1024)
print("RECV STARTTLS : " + recvTls.decode())

# Wraps the client socket using SSL.
wrappedClientSocket = ssl.wrap_socket(clientSocket, ssl_version=ssl.PROTOCOL_SSLv23)

# If hotmail/outlook/live server is used then it sends hello command again.
if "live" in mailserver[0]:
    wrappedClientSocket.send(heloCommand.encode())

# Sending wrapped socket AUTH LOGIN command.
authLoginMsg = 'AUTH LOGIN\r\n'
wrappedClientSocket.send(authLoginMsg.encode())
recvAuthLogin = wrappedClientSocket.recv(1024)
print("RECV AUTH LOGIN : " + recvAuthLogin.decode())

# Test mail username and password.
username = "omerceviktest@gmail.com"
password = "KjhdveB7CMqwH7r"

# Encode the username and password.
encodedUserName = (base64.b64encode(username.encode()))+('\r\n').encode()
encodedPassword = (base64.b64encode(password.encode()))+('\r\n').encode()

# Sending encoded username and printing the response.
wrappedClientSocket.send(encodedUserName)
recvUserName = wrappedClientSocket.recv(1024)
print("RECV USER NAME : " + recvUserName.decode())

# Sending encoded password and printing the response.
wrappedClientSocket.send(encodedPassword)
recvPassword = wrappedClientSocket.recv(1024)
print("RECV PASSWORD : " + recvPassword.decode())

# Sending MAIL FROM command with username and printing the response.
mailFromMsg = "MAIL FROM: <"+ username +">\r\n"
wrappedClientSocket.send(mailFromMsg.encode())
recvMailFrom = wrappedClientSocket.recv(1024)
print("RECV MAIL FROM : " + recvMailFrom.decode())

# Fill in end


# Send RCPT TO command and print server response.
# Fill in start

# Using rcpt to mail with itself or other one.
rcptToMail = username
# rcptToMail = "omer.cevik2016@gtu.edu.tr"

# Sending RCPT TO command with rcpt to mail and printing the response.
rcptToMsg = "RCPT TO: <"+ rcptToMail +">\r\n"
wrappedClientSocket.send(rcptToMsg.encode())
recvRcptTo = wrappedClientSocket.recv(1024)
print("RECV RCPT TO : " + recvRcptTo.decode())

# Fill in end


# Send DATA command and print server response.
# Fill in start

# Sending DATA command and printing the response.
dataMsg = "DATA\r\n"
wrappedClientSocket.send(dataMsg.encode())
recvData = wrappedClientSocket.recv(1024)
print("RECV DATA : " + recvData.decode())

# Fill in end


# Send message data.
# Fill in start

# Sending message.
wrappedClientSocket.send(msg.encode())

# Fill in end

# Message ends with a single period.
# Fill in start

# Sending end of message and printing the response.
wrappedClientSocket.send(endmsg.encode())

recvMsg = wrappedClientSocket.recv(1024)
print("RECV MSG : " + recvMsg.decode())

# Fill in end

# Send QUIT command and get server response.
# Fill in start

# Sending QUIT command and printing the response.
quitMsg = "QUIT\r\n"

wrappedClientSocket.send(quitMsg.encode())
recvQuit = wrappedClientSocket.recv(1024)
print("RECV QUIT : " + recvQuit.decode())

# Closing wrapper socket and client socket.
wrappedClientSocket.close()
clientSocket.close()

# Fill in end
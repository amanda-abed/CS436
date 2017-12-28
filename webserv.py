import sys
from socket import *

if len(sys.argv) != 3:
    print 'python <filename> <ipaddr> <port>'
    sys.exit(1)
serverSocket = socket(AF_INET, SOCK_STREAM)
host = '127.0.0.1'
port = 7060
serverSocket.bind((host, port))
serverSocket.listen(1)

while True:
    print 'Ready to serve...'
    connectionSocket, addr = serverSocket.accept() 

    try:
        message = connectionSocket.recv(1024).decode()
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()
        connectionSocket.send('HTTP/1.1 200 OK\n')
        print 'Success opening file'
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i])
        connectionSocket.close()
        pass
    except IOError: 
        print 'Error. 404 Not Found'
        connectionSocket.send('HTTP/1.1 404 Not Found\n')
        connectionSocket.close()
        pass
serverSocket.close()

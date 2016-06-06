import socket

serv = socket.socket()
host = socket.gethostname()
port = 12345

serv.connect((host,port))
print serv.recv(1024)
serv.close()


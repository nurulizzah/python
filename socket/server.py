import socket

#creating socket. create INET, STREAMing socket
serv= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 12345

#bind the socket
serv.bind((host,port))

#bcm a server socket
serv.listen(5)
while 1:
	#accept connection
	(c,addr)= serv.accept()
	print 'Connection from ',addr
	c.send('Thank you for connecting')
	c.close()


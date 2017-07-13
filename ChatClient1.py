import socket
addr = input("Enter an address:")
prot = int("Enter a Port:")
s = socket.socket()
s.connect((addr,port))
while True:
	message = input("Enter a message:")
	s.sendall(message.encode("utf-8")

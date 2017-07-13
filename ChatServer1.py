import socket
import thread
addr = ""
port = int(input("Enter a port to host on:"))
s = socket.socket()
s.bind((addr,port))
s.listen(8)
while True:
	conn, addr = s.accept()
	_thread.start_new_thread(handle_connection, (conn, addr, ))

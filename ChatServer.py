import socket
phone = socket.socket()
addr = (socket.gethostname(), 6000)
#phone.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
phone.bind(addr)
phone.listen(17)
while True:
	try:
		conn, cid = phone.accept()
		msg = bytes.decode(conn.recv(1024))
		conn.send("r".encode("UTF-8"))
		conn.close()
		print("Call from {0}: {1}.".format(cid, msg))
		phone.close()
	except ConnectionRefusedError:
		print("They appear to be offline.")
	except KeyboardInterrupt:
		print("Shutting Down")
		phone.close()
		break

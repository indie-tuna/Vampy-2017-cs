import socket
while True:
	N = input("Who do you want to call? ")
	msg = "(UrMum)" + input("What do you want to say? ")
	data = msg.encode("UTF-8")
	addr = ("Vampy-CS-"+N,8080)
	phone = socket.socket()
	try:
		phone.connect(addr)
		phone.send(data)
		resp = bytes.decode(phone.recv(1024))
		if resp !="r":
			print("Whoops.")
		phone.close()
		time.sleep(.1)
	except ConnectionRefusedError:
		print("They appear to be offline.")

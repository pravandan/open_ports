import socket


port_for_ex_connection_open = []
port_for_ex_connection_closed = []
port_for_new_server = []


def check_port_for_ex_connection(ip,port):
	global port_for_ex_connection_open,port_for_ex_connection_closed
	sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	#sock.settimeout(0.02) #as no one will wait for more than 2 seconds
	result = sock.connect_ex((ip,port))
	if result == 0:
		print("The port " +str(port) + " is open of " + ip + " for external connections")
		port_for_ex_connection_open.append(port)
	else:
		print("The port " +str(port) + " is open of " + ip + " for external connections")
		port_for_ex_connection_closed.append(port)
#the problem with the following function can be - this script should run from outside
#otherise firewall will be also blocking the connections to OPEN PORTS
def check_port_for_new_server(ip,port):
	global port_for_new_server
	try:
		sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		sock.bind((ip,port))
		sock.listen(5)
		sock.close()
	except socket.error as e:
		#print("The port " + str(port) + " is already occupied")
		return False
		raise RuntimeError("The server is already listening at port " + str(port))
	# print("The port " + str(port) + " is open")
	port_for_new_server.append(port)
	return True


def check_ip(ip):
	port = 1000
	while port<9999:
		check_port_for_new_server(ip,port)
		port += 1
	print("The following ports are open to be occupied")
	print(port_for_new_server)

ip = input("Enter the IP ")
port = int(input("Enter the custom port "))


#check_port_for_ex_connection(ip,port)
#check_port_for_new_server(ip,port)

check_ip(ip)

print("\n")
print("\n")

already_occupied = check_port_for_new_server(ip,port)
if already_occupied:
	print("The port " + str(port) + " is not occupied.")
else:
	print("The port " + str(port) + " is already occupied.")

print("\n")
print("\n")

hostname = input("Enter website to try to test external ports which are open ")
ip_hostname = socket.gethostbyname(hostname)
print("\n\n")

print("For " + hostname +" : " )
check_ip(ip_hostname)
print("\n\n Also for " + hostname + " the status of the port " + str(port) + " is ")


already_occupied = check_port_for_new_server(ip_hostname,port)
if already_occupied:
	print("The port " + str(port) + " is not occupied.")
else:
	print("The port " + str(port) + " is already occupied.")


#check_ip('35.224.103.178')

#check_port_for_ex_connection('35.224.103.178',1358)
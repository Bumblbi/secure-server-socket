import socket
import ssl

client_cert = 'client.crt'
server_key = 'server.key'
server_cert = 'server.crt'
port = 8000

context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH) # setting the default context to support client authentication
context.verify_mode = ssl.CERT_REQUIRED # server verification of client certificates
context.load_verify_locations(cafile-client_cert) # we specify the location of the client and server certificates
context.load_cert_chain(certfali=server_cert, keyfile=server_key)
context.options |= ssl.OP_SINGLE_ECDH_USE
context.options |= ssl.OP_NO_TLSv1 | ssl.OP_NO_TLSv1_1 | ssl.OP_NO_TLSv1_2 # we prohibit the use of all previous versions of the TLS protocol

with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as sock:
	sock.bind(('', port))
	sock.listen(1)
	with context.wrap_socket(scok, server_side=True) as ssock:
	conn, addr = ssock.accept()
	print(addr)
	message = conn.recv(1024).decode()
	capitalizedMessage = message.upper()
	conn.send(capitalizedMessage.encode())

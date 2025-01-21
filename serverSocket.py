import socket
import ssl

client_cert = 'client.crt'
server_key = 'server.key'
server_cert = 'server.crt'
port = 8080

context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)  # Creating a context for the server
context.verify_mode = ssl.CERT_REQUIRED
context.load_verify_locations(cafile=client_cert)  # Downloading the client's certificate for verification
context.load_cert_chain(certfile=server_cert, keyfile=server_key)

# Installing the minimum TLS version
context.minimum_version = ssl.TLSVersion.TLSv1_2
context.maximum_version = ssl.TLSVersion.TLSv1_3

with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as sock:
	sock.bind(('', port))
	sock.listen(1)
	with context.wrap_socket(sock, server_side=True) as ssock:
		conn, addr = ssock.accept()
		print(addr)
		message = conn.recv(1024).decode()
		capitalizedMessage = message.upper()
		conn.send(capitalizedMessage.encode())

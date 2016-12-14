import socket

s = socket.socket()
host = socket.gethostname()
port = 12345

print(host)
print(port)

s.connect((host,port))
print(s.recv(1024))
s.close()
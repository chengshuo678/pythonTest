import socket

s = socket.socket()
host = socket.gethostname()
port = 12345
s.bind((host,port))

s.listen(5)  # 可以挂起的最大连接数量为5
while True:
    c, addr = s.accept()
    print("连接地址：", addr)
    c.send()
    c.close()
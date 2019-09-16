#1 python3

from socket import *

HOST = '127.0.0.1' # or 'localhost'
POST = 21567
BUFSIZ = 1024
ADDR = (HOST, POST)

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)  # 连接到服务器

while True:
    data = input('>')
    if not data:
        break
    tcpCliSock.send(data.encode())  # 发送数据
    data = tcpCliSock.recv(BUFSIZ).decode()  # 接收服务器发来的数据
    if not data:
        break
    print(data)  # 转码

tcpCliSock.close()

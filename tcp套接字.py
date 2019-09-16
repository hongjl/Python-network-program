#！ python3
from socket import *
from time import ctime

HOST = ''  # 表示可以使用任何可用的地址
PORT = 21567  # 端口
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)  # 创建TCP套接字
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

connect_num = 0

while connect_num <=1:
    print('waiting for connection...')
    tcpCliSock, addr = tcpSerSock.accept()
    print('...connected from:',addr)

    while True:
        data = tcpCliSock.recv(BUFSIZ)
        if not data:
            break
        tcpCliSock.send(('[%s] %s' % (ctime(),data)).encode())
    tcpCliSock.close()
    connect_num += 1

print('完成两次连接，正常退出。')
tcpSerSock.close()

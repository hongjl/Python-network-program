#! python3

from socket import *
from time import ctime  # ctime是返回时间戳的字符串形式

HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

udpSerSock = socket(AF_INET, SOCK_DGRAM)
udpSerSock.bind(ADDR)

while True:
    print('waiting for message...')
    data, addr = udpSerSock.recvfrom(BUFSIZ)
    udpSerSock.sendto(('[%s] %s' % (ctime(),data)).encode(),addr)  # 按照addr发送
    print('...received from and returned to:',addr)

udpSerSock.close()

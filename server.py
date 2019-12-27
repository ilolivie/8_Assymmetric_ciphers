import socket
import pickle
from random import randint

def numb(g,l,p):
    return g**l%p

def crypt(msg, k):
    crypt_msg=''
    for i in range(len(msg)):
        crypt_msg+=chr(ord(msg[i])^k)
    return crypt_msg

def send_msg(conn, msg, k):
	conn.send(pickle.dumps(crypt(msg, k)))

def recv_msg(conn, k):
	msg=crypt(pickle.loads(conn.recv(1024)), k)
	return msg

HOST = '127.0.0.1'
sock = socket.socket()         
sock.bind((HOST,9090))
print('Номер порта:',port)


sock.listen(0)			
sock.setblocking(1)
conn, addr = sock.accept()

b = randint(1, 256)

msg = conn.recv(1024)
p, g, Aa = pickle.loads(msg)

Bb = numb(g,b,p)
conn.send(pickle.dumps(Bb))

K = numb(Aa,b,p)
print('K=',K)
while True:
	try:
		msg = recv_msg(conn, K)
		print(msg)
		send_msg(conn, 'Сервер получил и расшифровал', K)
	except:
		break

conn.close()

import socket
import pickle

def numb(g,l,p):
    return g**l%p

def crypt(msg, k):
    crypt_msg=''
    for i in range(len(msg)):
        crypt_msg+=chr(ord(msg[i])^k)
    return crypt_msg

def send_msg(conn, msg, k):
	sock.send(pickle.dumps(crypt(msg, k)))

def recv_msg(conn, k):
	msg=crypt(pickle.loads(sock.recv(1024)), k)
	return msg

HOST = '127.0.0.1'
sock = socket.socket()


sock.connect((HOST, 9090))
print('Соединение установлено')
print('Для отсоединения введите "disconnect"')	


p = 3
g = 7
a = 3
Aa =  chis(g,a,p)
sock.send(pickle.dumps((p, g, Aa)))

B = pickle.loads(sock.recv(1024))

K = chis(B,a,p)
print('K=',K)

msg = input('Отправляем на сервер: ')
while True: 
	try:
		while msg!='disconnect':
			send_msg(sock, msg, K)
			print(' ' + recv_msg(sock, K))
			msg=input(':')
		break
	except:
		break

sock.close()

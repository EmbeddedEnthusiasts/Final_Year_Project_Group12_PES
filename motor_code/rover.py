import socket 
from wheel import Wheels

#socket setup
s=socket.socket()
ip="192.168.0.29"
port=9999
s.connect((ip,port))

#speed declaration
speed=25

#wheel setup
left=Wheels(13,15,33,0)
right=Wheels(18,16,12,0)

while True:
	d=str(s.recv(1024),"utf-8")
	print(d)
	if d=='w':
		left.control(1,0,speed)
		right.control(1,0,speed)
	elif d=='s':
		left.control(0,1,speed)
		right.control(0,1,speed) 
	elif d=='w+a' or d=='a+w':
		left.control(1,0,speed/2)
		right.control(1,0,speed*2)
	elif d=='w+d' or d=='d+w':
		left.control(1,0,speed*2)
		right.control(1,0,speed/2)
	elif d=='s+a' or d=='a+s':
		left.control(0,1,speed/2)
		right.control(0,1,speed*2)
	elif d=='s+d' or d=='d+s':
		left.control(0,1,speed*2)
		right.control(0,1,speed/2)
	elif d=='a':
		left.control(0,1,speed)
		right.control(1,0,speed)
	elif d=='d':
		left.control(1,0,speed)
		right.control(0,1,speed)	
	elif d=='e':
		break
	else:
		left.control(0,0,0)
		right.control(0,0,0)

left.hault()
right.hault()

s.close()

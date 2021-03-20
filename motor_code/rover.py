import socket 
from wheel import Wheels

#socket setup
s=socket.socket()
ip="192.168.0.173"
port=9999
s.connect((ip,port))


#wheel setup
fl=Wheels(13,15,33,0)
fr=Wheels(16,18,12,0)
bl=Wheels(29,31,35,0)
br=Wheels(22,36,32,0)

while True:
	d=str(s.recv(1024),"utf-8")
	print(d)
	if d=='w':
		fl.control(1,0,speed)
		fr.control(1,0,speed)
		bl.control(1,0,speed)
		br.control(1,0,speed) 
	elif d=='s':
		fl.control(0,1,speed)
		fr.control(0,1,speed)
		bl.control(0,1,speed)
		br.control(0,1,speed) 
	elif d=='w+a' or d=='a+w':
		fl.control(1,0,speed/2)
		fr.control(1,0,speed)
		bl.control(1,0,speed/2)
		br.control(1,0,speed) 
	elif d=='w+d' or d=='d+w':
		fl.control(1,0,speed)
		fr.control(0,0,speed/2)
		bl.control(1,0,speed)
		br.control(0,0,speed/2) 
	elif d=='s+a' or d=='a+s':
		fl.control(0,0,speed/2)
		fr.control(0,1,speed)
		bl.control(0,0,speed/2)
		br.control(0,1,speed) 
	elif d=='s+d' or d=='d+s':
		fl.control(0,1,speed)
		fr.control(0,0,speed/2)
		bl.control(0,1,speed)
		br.control(0,0,speed/2) 
	elif d=='a':
		fl.control(0,1,speed)
		fr.control(1,0,speed)
		bl.control(0,1,speed)
		br.control(1,0,speed) 
	elif d=='d':
		fl.control(1,0,speed)
		fr.control(0,1,speed)
		bl.control(1,0,speed)
		br.control(0,1,speed) 		
	elif d=='e':
		break
	else:
		fl.control(0,0,0)
		fr.control(0,0,0)
		bl.control(0,0,0)
		br.control(0,0,0) 

fl.hault()
fr.hault()
br.hault()
bl.hault()
s.close()

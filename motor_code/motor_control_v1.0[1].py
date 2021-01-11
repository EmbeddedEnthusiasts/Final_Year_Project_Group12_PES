import RPi.GPIO as gpio
import socket 

#socket setup
s=socket.socket()
ip="192.168.0.100"
port=9999
s.connect((ip,port))

#gpio setup
gpio.setmode(gpio.BOARD)
gpio.setup(32,gpio.OUT)#RIGHT
gpio.setup(16,gpio.OUT)#RIGHT
gpio.setup(18,gpio.OUT)#RIGHT

gpio.setup(33,gpio.OUT)#LEFT
gpio.setup(13,gpio.OUT)#LEFT
gpio.setup(15,gpio.OUT)#LEFT


left=gpio.PWM(33,50)
right=gpio.PWM(32,50)
left.start(60)
right.start(60)

#gpio.output(16,0)
#gpio.output(18,0)
#gpio.output(13,0)
#gpio.output(15,0)

while True:
	d=str(s.recv(1024),"utf-8")
	print(d)
	if d=='w':
		gpio.output(16,1)
		gpio.output(18,0)
		gpio.output(13,1)
		gpio.output(15,0)
	elif d=='s':
		gpio.output(16,0)
		gpio.output(18,1)
		gpio.output(13,0)
		gpio.output(15,1)
	elif d=='w+a' or d=='a+w':
		gpio.output(16,0)
		gpio.output(18,0)
		gpio.output(13,1)
		gpio.output(15,0)
	elif d=='w+d' or d=='d+w':
		gpio.output(16,1)
		gpio.output(18,0)
		gpio.output(13,0)
		gpio.output(15,0)
	elif d=='s+a' or d=='a+s':
		gpio.output(16,0)
		gpio.output(18,0)
		gpio.output(13,0)
		gpio.output(15,1)
	elif d=='s+d' or d=='d+s':
		gpio.output(16,0)
		gpio.output(18,1)
		gpio.output(13,0)
		gpio.output(15,0)
	elif d=='e':
		break
	else:
		gpio.output(16,0)
		gpio.output(18,0)
		gpio.output(13,0)
		gpio.output(15,0)

gpio.cleanup()
s.close()

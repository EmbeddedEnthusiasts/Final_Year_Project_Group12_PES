from wheel import Wheels
from time import sleep

front=Wheels(13,15,32,0)

front.control(0,0,0)
sleep(2)
front.control(0,1,100)
sleep(2)
front.control(1,0,0)
sleep(2)
front.control(1,1,100)
sleep(2)
front.hault()

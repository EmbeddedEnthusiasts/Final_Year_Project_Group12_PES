import RPi.GPIO as GPIO
class Wheels():
    def __init__(self,inx,iny,pwm_pin,duty_cycle):
        GPIO.setmode(GPIO.BOARD)
        self.inx=inx
        self.iny=iny
        self.pwm_pin=pwm_pin
        self.duty_cycle=duty_cycle
        GPIO.setup(self.inx,GPIO.OUT)
        GPIO.setup(self.iny,GPIO.OUT)
        GPIO.setup(self.pwm_pin,GPIO.OUT)
        self.pwm_obj=GPIO.PWM(self.pwm_pin,50)
        self.pwm_obj.start(self.duty_cycle)
	
    def control(self,o1,o2,speed):
        self.pwm_obj.ChangeDutyCycle(speed)
        GPIO.output(self.inx,o1)
        GPIO.output(self.iny,o2)

    def hault(self):
        GPIO.cleanup()

        
        

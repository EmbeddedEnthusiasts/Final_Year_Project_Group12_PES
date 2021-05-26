import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
class Ultrasonic:
    
    def __init__(self,TRIG,ECHO):
        self.TRIG=TRIG
        self.ECHO=ECHO
        GPIO.setup(self.TRIG,GPIO.OUT)
        GPIO.setup(self.ECHO,GPIO.IN)
        GPIO.output(self.TRIG, False)
    
    def getDistance(self):
        try:
            GPIO.output(self.TRIG, True)
            time.sleep(0.00001)
            GPIO.output(self.TRIG, False)

            while GPIO.input(self.ECHO)==0:
                pulse_start = time.time()

            while GPIO.input(self.ECHO)==1:
                pulse_end = time.time()

            pulse_duration = pulse_end - pulse_start
            distance = pulse_duration * 17150
            return distance
        
        except:
            GPIO.cleanup()
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

class Ultrasonic:
    def __init__(self,TRIG,ECHO):
        self.TRIG=TRIG
        self.ECHO=ECHO
        GPIO.setup(TRIG,GPIO.OUT)
        GPIO.setup(ECHO,GPIO.IN)
        GPIO.output(TRIG, False)
    
    def getDistance():
        try:
            GPIO.output(TRIG, True)
            time.sleep(0.00001)
            GPIO.output(TRIG, False)

            while GPIO.input(ECHO)==0:
                pulse_start = time.time()

            while GPIO.input(ECHO)==1:
                pulse_end = time.time()

            pulse_duration = pulse_end - pulse_start
            distance = pulse_duration * 17150
            return distance
        
        except:
            GPIO.cleanup()
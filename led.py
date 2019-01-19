import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
list_GPIO=[17,27,21]
GPIO.setup(list_GPIO,GPIO.OUT)
while(1):
    GPIO.output(list_GPIO,GPIO.LOW)
    time.sleep(0.5)
    GPIO.output(list_GPIO,GPIO.HIGH)
    time.sleep(0.5)

    

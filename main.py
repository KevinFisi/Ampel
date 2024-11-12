import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

RED_PIN = 17                                                                                                                                                                                                                                                                                            
YELLOW_PIN = 27
GREEN_PIN = 22

GPIO.setup(RED_PIN, GPIO.OUT)
GPIO.setup(YELLOW_PIN, GPIO.OUT)
GPIO.setup(GREEN_PIN, GPIO.OUT)

while True:
	    GPIO.output(RED_PIN, GPIO.HIGH)
	    print("Rot an")
	    time.sleep(2)
	    GPIO.output(RED_PIN, GPIO.LOW)
	    
	    GPIO.output(YELLOW_PIN, GPIO.HIGH)
	    GPIO.output(RED_PIN, GPIO.HIGH)
	    time.sleep(1)
	    GPIO.output(RED_PIN, GPIO.LOW)
	    
	    GPIO.output(YELLOW_PIN, GPIO.HIGH)
	    print("Gelb  an")
	    time.sleep(2)
	    GPIO.output(YELLOW_PIN, GPIO.LOW)

	    GPIO.output(GREEN_PIN, GPIO.HIGH)
	    print("Gruen an")
	    time.sleep(2)
	    GPIO.output(GREEN_PIN, GPIO.LOW)

	    GPIO.output(YELLOW_PIN, GPIO.HIGH)
	    print("Gelb  an")
	    time.sleep(2)
	    GPIO.output(YELLOW_PIN, GPIO.LOW)

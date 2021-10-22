import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.IN)
time.sleep(1)

while True:
	result = GPIO.input(2)
	if result == 1:
		print("down")
		time.sleep(1)
		
	else:
		print("normal")
		time.sleep(1)

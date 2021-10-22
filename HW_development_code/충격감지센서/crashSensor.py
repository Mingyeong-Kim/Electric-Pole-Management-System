import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(3, GPIO.IN)
time.sleep(1)

while True:
	result = GPIO.input(3)
	if result != 1:
		print("click")
	time.sleep(0.5)


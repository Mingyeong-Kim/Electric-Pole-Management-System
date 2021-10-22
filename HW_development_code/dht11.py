from time import sleep
import wiotp.sdk
import psutil
import Adafruit_DHT
import RPi.GPIO as GPIO
import time

"""

"""
sensor = Adafruit_DHT.DHT11
pin = 4


#"""
GPIO.setmode(GPIO.BCM)
time.sleep(1)
#"""


# ibm iot platform device credential here
deviceOptions = {
    "identity": {"orgId": "aua984", "typeId": "vDev", "deviceId": "dht11"},
    "auth": {"token": "password"},
}


def commandProcessor(cmd):
    print(cmd.data["d"])
    if cmd.data["d"]["info"]:
        data = {"d": {}}

        data["d"]["cpu_count"] = psutil.cpu_count()
        data["d"]["cpu_freq"] = psutil.cpu_freq().current
        data["d"]["memory"] = psutil.virtual_memory().total

        deviceCli.publishEvent("status", "json", data, qos=0)


deviceCli = wiotp.sdk.device.DeviceClient(deviceOptions)
deviceCli.commandCallback = commandProcessor
deviceCli.connect()




while True:
    

    #result = GPIO.input(7)

    h, t = Adafruit_DHT.read_retry(sensor, pin)

    if h is not None and t is not None:
        #print("Temperature = {0:0.1f}*C Humidity = {1:0.1f}%".format(t, h))
        
        
        temp = t
        humi = h
        
    else:
        print('Read error')
    

    time.sleep(2)

    data = {"d": {}}
    data["d"]["temp"] = t;
    data["d"]["humi"] = h;

    deviceCli.publishEvent("status", "json", data, qos=0)
    sleep(10)


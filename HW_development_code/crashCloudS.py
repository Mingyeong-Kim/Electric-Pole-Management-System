from time import sleep
import wiotp.sdk
import psutil
import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)
GPIO.setup(3, GPIO.IN)
time.sleep(1)



# ibm iot platform device credential here
deviceOptions = {
    "identity": {"orgId": "aua984", "typeId": "vDev", "deviceId": "vCrash"},
    "auth": {"token": "password"},
}

def commandProcessor(cmd):
    print(cmd.data["d"])
    if cmd.data["d"]["info"]:
        data = {"d":{}}

        data["d"]["cpu_count"] = psutil.cpu_count()
        data["d"]["cpu_freq"] = psutil.cpu_freq().current
        data["d"]["memory"] = psutil.virtual_memory().total

        deviceCli.publishEvent("status", "json", data, qos=0)

deviceCli = wiotp.sdk.device.DeviceClient(deviceOptions)
deviceCli.commandCallback = commandProcessor
deviceCli.connect()


while True:

    result = GPIO.input(3)
    if result == 1:
        
        crash = 0

    else:
        crash=30
        print("crashed")
        
    data = {"d":{}}
    data["d"]["sense_impact"] = crash;

    deviceCli.publishEvent("status", "json", data, qos=0)
    sleep(2)


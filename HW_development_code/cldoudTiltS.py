from time import sleep
import wiotp.sdk
import psutil
import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.IN)
time.sleep(1)



# ibm iot platform device credential here
deviceOptions = {
    "identity": {"orgId": "aua984", "typeId": "vDev", "deviceId": "vinclination"},
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
#
    result = GPIO.input(2)
    if result == 1:
        print("down")
        tilt = "30"
        time.sleep(1)

    else:
        print("low")
        tilt="0"
        time.sleep(1)
#
    data = {"d":{}}
    data["d"]["inclination"] = tilt;

    deviceCli.publishEvent("status", "json", data, qos=0)
    sleep(2)
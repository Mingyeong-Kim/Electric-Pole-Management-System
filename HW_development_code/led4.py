from time import sleep
import wiotp.sdk
import psutil
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(27, GPIO.OUT)


# ibm iot platform device credential here
deviceOptions = {
    "identity": {"orgId": "aua984", "typeId": "vDev", "deviceId": "led2"},
    "auth": {"token": "password"},
}

lamp = 'off'
sangsu=False

def commandProcessor(cmd):
    global lamp
    global sangsu
    # print("hi")
    if cmd.data["d"]["switch_state"]:
        data = {}
        if cmd.data["d"]["switch_state"] == "on":
            lamp = 'on'

            print(lamp)
            #bulb.bulbOn()
            data = {"d": {"switch_state": "on"}}
            sangsu = True
        else:
            lamp = 'off'
            print(lamp)
            #bulb.bulbOff()
            data = {"d": {"switch_state": "off"}}
            sangsu = False
    deviceCli.publishEvent("status", "json", data, qos=0)

deviceCli = wiotp.sdk.device.DeviceClient(deviceOptions)
deviceCli.commandCallback = commandProcessor
deviceCli.connect()

while True:
    data = {"d":{}}
    data["d"]["switch_state"] = lamp

    if sangsu == True :
        GPIO.output(27,True)
    else:
        GPIO.output(27, False)
    
    deviceCli.publishEvent("status", "json", data, qos=0)
    sleep(1)



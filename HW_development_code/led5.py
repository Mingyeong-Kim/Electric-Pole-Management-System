import RPi.GPIO as GPIO
import wiotp.sdk
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(27, GPIO.OUT)
# ibm iot platform device credential here
deviceOptions = {
    "identity": {"orgId": "aua984", "typeId": "vDev", "deviceId": "led2"},
    "auth": {"token": "password"},
}

GPIO.output(27,False)

switch_state = 'off'


def commandProcessor(cmd):
    global switch_state
    if cmd.data["d"]["switch_state"]:
        data = {}
        if cmd.data["d"]["switch_state"] == "on":
            switch_state = 'on'
            GPIO.output(27,True)
            print("Lamp is On")
            data = {"d": {"switch_state": "on"}}
        else:
            switch_state = 'off'
            GPIO.output(27,False)
            print("Lamp is Off")
            data = {"d": {"switch_state": "off"}}
        deviceCli.publishEvent("status", "json", data, qos=0)


deviceCli = wiotp.sdk.device.DeviceClient(deviceOptions)
deviceCli.commandCallback = commandProcessor
deviceCli.connect()


def periodicPublish():
    data = {"d": {"switch_state": switch_state}}
    deviceCli.publishEvent("status", "json", data, qos=0)
    print("        Periodic update : Lamp is " + switch_state)


while True:
    periodicPublish()
    sleep(4)

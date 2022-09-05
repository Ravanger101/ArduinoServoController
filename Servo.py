from pyfirmata import Arduino ,SERVO,util
from time import sleep

port = 'COM6'
pin=10
board=Arduino(port)

board.digital[pin].mode=SERVO

def rotateservo(pin,angle):
    board.digital[pin].write(angle)
    sleep(0.015)
    
while True:
    x=input("Input :  ")
    if x =="10":
        for i in range(0,10):
            rotateservo(pin,i)
    elif x=="20":
        for i in range(0,20):
            rotateservo(pin,i)
    elif x=="30":
        for i in range(0,30):
            rotateservo(pin,i)
    elif x=="40":
        for i in range(0,40):
            rotateservo(pin,i)
    elif x=="50":
        for i in range(0,50):
            rotateservo(pin,i)
    elif x=="60":
        for i in range(0,60):
            rotateservo(pin,i)
    elif x=="70":
        for i in range(0,70):
            rotateservo(pin,i)
    elif x=="80":
        for i in range(0,80):
            rotateservo(pin,i)
    elif x=="90":
        for i in range(0,90):
            rotateservo(pin,i)
    elif x=="100":
        for i in range(0,100):
            rotateservo(pin,i)
    elif x=="110":
        for i in range(0,110):
            rotateservo(pin,i)
    elif x=="120":
        for i in range(0,120):
            rotateservo(pin,i)
    elif x=="130":
        for i in range(0,130):
            rotateservo(pin,i)
    elif x=="140":
        for i in range(0,140):
            rotateservo(pin,i)
    elif x=="150":
        for i in range(0,150):
            rotateservo(pin,i)
    elif x=="160":
        for i in range(0,160):
            rotateservo(pin,i)
    elif x=="170":
        for i in range(0,170):
            rotateservo(pin,i)
    elif x=="180":
        for i in range(0,180):
            rotateservo(pin,i)

            
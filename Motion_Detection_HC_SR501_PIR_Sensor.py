import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
SENSOR_PIR_PIN = 23
GPIO.setup(SENSOR_PIR_PIN, GPIO.IN)

def callback_func(output):
    if output == 1:
        print('Motion Detected!!')
    # else output == 0:
    #     print("Motion Not Detected!!")

try:
    print("PIR Module Test (CTRL+C to exit)")
    time.sleep(2)
    print("Ready")
    while True:
        time.sleep(5)
        output = GPIO.input(SENSOR_PIR_PIN)
        callback_func(output)
except KeyboardInterrupt:
    print("Quit")
    GPIO.cleanup()
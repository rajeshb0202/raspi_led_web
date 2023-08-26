import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
LED_PIN = 18
GPIO.setup(LED_PIN, GPIO.OUT)


def control_led(status):
    if status == 'on':
        GPIO.output(LED_PIN, GPIO.HIGH)
    elif status == 'off':
        GPIO.output(LED_PIN, GPIO.LOW)
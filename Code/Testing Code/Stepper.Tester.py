# Install the GPIO code: https://learn.adafruit.com/adafruits-raspberry-pi-lesson-4-gpio-setup/configuring-gpio
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

class Stepper (object):
        def __init__ (self, pin1, pin2, pin3, pin4, enable):
                self.enable = enable
                self.pin1 = pin1
                self.pin2 = pin2
                self.pin3 = pin3
                self.pin4 = pin4

                GPIO.setup(enable, GPIO.OUT)
                GPIO.setup(pin1, GPIO.OUT)
                GPIO.setup(pin2, GPIO.OUT)
                GPIO.setup(pin3, GPIO.OUT)
                GPIO.setup(pin4, GPIO.OUT)

                GPIO.output(enable, 1)

#512 steps= full rotation
        def forward(delay, steps):
                for i in range(0, steps):
                        setStep(1, 0, 1, 0)
                        time.sleep(delay)
                        setStep(0, 1, 1, 0)
                        time.sleep(delay)
                        setStep(0, 1, 0, 1)
                        time.sleep(delay)
                        setStep(1, 0, 0, 1)
                        time.sleep(delay)

        def backwards(delay, steps):
                for i in range(0, steps):
                        setStep(1, 0, 0, 1)
                        time.sleep(delay)
                        setStep(0, 1, 0, 1)
                        time.sleep(delay)
                        setStep(0, 1, 1, 0)
                        time.sleep(delay)
                        setStep(1, 0, 1, 0)
                        time.sleep(delay)


        def setStep(w1, w2, w3, w4):
                GPIO.output(coil_A_1_pin, w1)
                GPIO.output(coil_A_2_pin, w2)
                GPIO.output(coil_B_1_pin, w3)
                GPIO.output(coil_B_2_pin, w4)


def main():
        stepper1 = Stepper(4, 17, 23, 24, 18)
        stepper1.forward(10, 512)
        

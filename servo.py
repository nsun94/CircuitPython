# CircuitPython Demo - Cap Touch Multiple Pins
# Example does NOT work with Trinket M0!

import time
import pulsio
import board
import touchio
from adafruit_motor import servo
pwm = pulseio.PWMOut(board.A3,duty_cycle=2 **15 frequency=50)
my_servo = servo.Servo(pwm)

angle = 90

touch_A1 = touchio.TouchIn(board.A1)  # Not a touch pin on Trinket M0!
touch_A2 = touchio.TouchIn(board.A2)  # Not a touch pin on Trinket M0!

while True:
    if touch_A1.value:
        angle +=1
    if touch_A2.value:
        angle -=1
        if angle >180
        angle = 180
    if angle <0
        angle = 0
my_servo.angle = angle
#
# โปรแกรม Lab 6_1 - หลอด LED กระพริบ
#

import RPi.GPIO as GPIO
import time

LED = 12
GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED, GPIO.OUT)

while True :
  GPIO.output (LED, True)
  time.sleep(0.1)
  GPIO.output(LED, False)
  time.sleep(1) 

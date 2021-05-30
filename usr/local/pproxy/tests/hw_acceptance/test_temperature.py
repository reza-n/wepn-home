import time
import os
import sys
import board
import adafruit_pct2075
up_dir = os.path.dirname(os.path.abspath(__file__))+'/../../'
sys.path.append(up_dir)
from oled import OLED as OLED
LED = OLED()
LED.set_led_present(1)

i2c = board.I2C()

pct = adafruit_pct2075.PCT2075(i2c, address=0x48)
print("Temperature is %.2f C" % pct.temperature)
LED.display([(1,"Temperature:",0,"white"), (2,str(pct.temperature),0,"white"),], 20)

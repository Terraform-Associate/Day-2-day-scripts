# A small python script to move your mouse, press the shift key, and keep your PC awake when 
# you're away Uses command line arguments to set the number of minutes between movements and requires Python3 or higher. 
# Default timer is 3 minutes, but can be 1 or more.


import pyautogui
import time
import sys
from datetime import datetime
pyautogui.FAILSAFE = False
numMin = None
if ((len(sys.argv)<2) or sys.argv[1].isalpha() or int(sys.argv[1])<1):
    numMin = 3
else:
    numMin = int(sys.argv[1])
while(True):
    x=0
    while(x<numMin):
        time.sleep(60)
        x+=1
    for i in range(0,200):
        pyautogui.moveTo(0,i*4)
    pyautogui.moveTo(1,1)
    for i in range(0,3):
        pyautogui.press("shift")
    print("Movement made on sashank konduru screen {}".format(datetime.now().time()))

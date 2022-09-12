#!/usr/bin/env python3
# Arm startup code
# Don't touch this!

import sys
import math
import time
import datetime
import random
import traceback
import threading

#import Robot as Robot
import requests
import transformer
#import keyboard
from upgradedArm import upgradedArm
import tempFinder
import Stepper_Motor_Code
try:
    from xarm.tools import utils
except:
    pass
from xarm import version
from xarm.wrapper import XArmAPI

def pprint(*args, **kwargs):
    try:
        stack_tuple = traceback.extract_stack(limit=2)[0]
        print('[{}][{}] {}'.format(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), stack_tuple[1], ' '.join(map(str, args))))
    except:
        print(*args, **kwargs)

pprint('xArm-Python-SDK Version:{}'.format(version.__version__))

arm = upgradedArm('192.168.1.207', baud_checkset=False)
arm.clean_warn()
arm.clean_error()
arm.motion_enable(True)
arm.set_mode(0)
arm.set_state(0)

# Arm setup complete

#arm = XArmAPI(ip)
arm.motion_enable(enable=True)


arm.reset(wait=True)

#Stepper_Motor_Code.stepper_motor(10, 100)

arm.set_cgpio_digital(1, 1, 1000)

arm.reset(wait=True)
arm.disconnect()

#print(tempFinder.temperatureFinder(676, adcBits = 12, adcMaxVoltage = 10))



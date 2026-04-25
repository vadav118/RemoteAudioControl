from pycaw.pycaw import *
from comtypes import *
from ctypes import *
import warnings
import json
import requests

def GetDevices():
    devices = AudioUtilities.GetAllDevices()
    return devices


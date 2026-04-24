from pycaw.pycaw import *
from comtypes import *
from ctypes import *
import warnings
import json


devices=AudioUtilities.GetSpeakers()
volume = devices.EndpointVolume
sessions = AudioUtilities.GetAllSessions()

def ListAllSessions():
    sessionlist = []
    for session in sessions:
        if session.Process is not None:
            sessionlist.append(session.Process.name())
    return sessionlist

def SetASessionsVolume(sessionName, neededVolume,):
    sessionfound = False
    for session in sessions:
        if session.Process is not None:
            appvolume = session.SimpleAudioVolume
            if session.Process.name() == sessionName and session.Process is not None:
                sessionfound = True

    if sessionfound:
        appvolume.SetMasterVolume(neededVolume, None)
        print(appvolume.GetMasterVolume())
    else:
        print("Session not found")

warnings.filterwarnings("ignore", category=UserWarning)




if __name__ == "__main__":
    SetASessionsVolume("brave.exe",1.0)
    print(ListAllSessions())
    # devices = AudioUtilities.GetAllDevices()
    # for device in devices:
    #
    #     name = str(device.FriendlyName) if device.FriendlyName else ""
    #     if "Mikrofon" in name or "Input" in name:
    #         print("MIKROFONOK:")
    #         print(name)
    #         print("\n")
    #     elif "Hangszóró" in name or "Fejhallgató" in name:
    #         print("Hangszórók:")
    #         print(name)
    #         print("\n")
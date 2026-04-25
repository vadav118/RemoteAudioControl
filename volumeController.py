from pycaw.pycaw import *
from comtypes import *
from ctypes import *
import warnings
import json
import requests

def GetSessions():
    sessions = AudioUtilities.GetAllSessions()
    return sessions

def PostAllSessions():
    sessions = GetSessions()
    sessionlist=[]
    for session in sessions:
        if session.Process is not None:
            name = session.Process.name()
            pid = session.Process.pid
            volume = session.SimpleAudioVolume.GetMasterVolume()

            sessionlist.append({
                "name":name,
                "volume":volume,
            })
    requests.post("http://localhost:8080", data=json.dumps(sessionlist))


def SetASessionsVolume(sessionName, neededVolume):
    sessions = GetSessions()
    sessionfound = False
    for session in sessions:
        if session.Process is not None:
            if session.Process.name == sessionName:
                sessionfound = True
                appvolume = session.SimpleAudioVolume

    if sessionfound:
        appvolume.SetMasterVolume(neededVolume, None)
        print(appvolume.GetMasterVolume())
    else:
        print("Session not found")

warnings.filterwarnings("ignore", category=UserWarning)


if __name__ == "__main__":
    SetASessionsVolume("brave.exe",0.25)
    sessione= GetSessions()
    for session in sessione:
        if session.Process is not None:

            print(session.Process.name()+":"+ str(session.Process.pid))


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
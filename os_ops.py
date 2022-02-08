import os
import subprocess as sp


paths = {
    'notepad' : "C:\\Windows\\System32\\Notepad.exe",
    "calculator" : "C:\\Windows\System32\\calc.exe",
    "spotify" : "C:\\Users\\user\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Spotify.lnk",
    "visual_studio_code": "C:\\Users\\user\\AppData\\Local\\Programs\\Microsoft VS Code\\Code"
}

def open_notepad():
    sp.Popen(paths['notepad'])

def open_calculator():
    sp.Popen(paths['calculator'])

def open_cmd():
    os.system('start cmd')

def open_camera():
    sp.run('start microsoft.windows.camera:' , shell=True)

def open_spotify():
    os.startfile(paths['spotify'])

def open_visual_studio_code():
    os.startfile(paths['visual_studio_code'])

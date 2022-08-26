from __future__ import print_function
import ctypes
import ctypes.wintypes as w

import win32com.client

from gtts import gTTS

from io import BytesIO

################ Copy Selected ###################
import pyautogui as pya
import pyperclip  # handy cross-platform clipboard text handler
import time

def copy_clipboard():
    pya.hotkey('ctrl', 'c')
    time.sleep(.01)  # ctrl-c is usually very fast but your program may execute faster
    return pyperclip.paste()

# double clicks on a position of the cursor
# pya.doubleClick(pya.position())

list = []
var = copy_clipboard()
list.append(var) 
print(list)



########################## GET ######################
CF_UNICODETEXT = 13

u32 = ctypes.WinDLL('user32')
k32 = ctypes.WinDLL('kernel32')

OpenClipboard = u32.OpenClipboard
OpenClipboard.argtypes = w.HWND,
OpenClipboard.restype = w.BOOL
GetClipboardData = u32.GetClipboardData
GetClipboardData.argtypes = w.UINT,
GetClipboardData.restype = w.HANDLE
GlobalLock = k32.GlobalLock
GlobalLock.argtypes = w.HGLOBAL,
GlobalLock.restype = w.LPVOID
GlobalUnlock = k32.GlobalUnlock
GlobalUnlock.argtypes = w.HGLOBAL,
GlobalUnlock.restype = w.BOOL
CloseClipboard = u32.CloseClipboard
CloseClipboard.argtypes = None
CloseClipboard.restype = w.BOOL

def get_clipboard_text():
    text = ""
    if OpenClipboard(None):
        h_clip_mem = GetClipboardData(CF_UNICODETEXT)
        text = ctypes.wstring_at(GlobalLock(h_clip_mem))
        GlobalUnlock(h_clip_mem)
        CloseClipboard()
    return text

# print(get_clipboard_text())



######################### Off-Line SPEEK ###################
# speaker = win32com.client.Dispatch("SAPI.SpVoice")
# speaker.Speak(get_clipboard_text())

#### On-Line SPEEK:
#my_tts = "Text you want to process"
#tts = gTTS(text=my_tts, lang='en')
# tts.save("Absolute/path/to/file.mp3")
#mp3_fp = BytesIO()
# tts = gTTS('hello', lang='en')
#tts.write_to_fp(mp3_fp)


import pyttsx3
engine = pyttsx3.init()
# engine.say("Hello")
engine.say(get_clipboard_text())
engine.runAndWait()
# exit()


######## Print pithon location
# import sys
# locate_python = sys.exec_prefix
# print(locate_python)
#!/usr/bin/env python3
import os
from google_speech import Speech
import psutil

# Prog name
process_to_kill = "sox"

# Get PID of the current process
my_pid = os.getpid()

for p in psutil.process_iter():
    # if it's process we're looking for...
    if process_to_kill in p.name():
        if not p.pid == my_pid:
            p.kill()
            exit()

# say "Hello World"
text = os.popen('xsel').read()
lang = "en"
speech = Speech(text, lang)
speech.play()
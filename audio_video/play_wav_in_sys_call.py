#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
play audio via system call

Test environment:
    Mac OS X 10.6.8
    Linux 3.0 KDE 4.6.5

alsa-utils: /usr/bin/aplay
"""
import os
import threading
import subprocess
import sys


if sys.platform == "darwin":
    player_name = "afplay"
elif sys.platform == "linux2":
    player_name = "aplay"


def _play_audio_t(path):
    path = os.path.realpath(path)

    if sys.platform == "darwin":
        cmd = '%s -q 1 "%s"' % (player_name, path)
    elif sys.platform == "linux2":    
        cmd = '%s "%s"' % (player_name, path)

    os.system(cmd)

def play_audio_t(path):
    t = threading.Thread(target = _play_audio_t, kwargs = {"path" : path})
    t.start()

def play_audio_p(path):
    path = os.path.realpath(path)
    subprocess.call([player_name, path])


if __name__ == "__main__":
#    path = 'if_you_go_away.mp3'
#    play_audio_t(path)

#    path = 'wow.wav'
#    play_audio_p(path)

    from timeit import Timer

    t = Timer("play_audio_p('wow.wav')", "from __main__ import play_audio_p")
    print t.timeit(number=3)

    t = Timer("play_audio_t('wow.wav')", "from __main__ import play_audio_t")
    print t.timeit(number=3)

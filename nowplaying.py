#!/usr/bin/python
import pywintypes
import win32gui
import hexchat
import re

__module_name__        = "now_playing"
__module_version__     = "0.1"
__module_description__ = "Now playing plugin for HexChat"

red = "\x034"
blue = "\x0312"
yellow = "\x038"
green = "\x039"


def check_spotify():
    try:
        hwnd = win32gui.FindWindow("SpotifyMainWindow", None)
        return hwnd
    except Exception as err:
        hexchat.prnt("Error: %s" % (err))
        return None


def check_winamp():
    try:
        hwnd = win32gui.FindWindow("Winamp v1.x", None)
        return hwnd
    except Exception as err:
        hexchat.prnt("Error: %s" % (err))
        return None


def now_playing(word, wordeol, userdata):
    win_title = ""
    hwnd = ""

    try:
        if check_spotify():
            hwnd = check_spotify()
        elif check_winamp():
            hwnd = check_winamp()
        else:
            raise Exception("No player found...")
        try:
            win_title = win32gui.GetWindowText(hwnd)
            if win_title.startswith("Spotify") or win_title.startswith("Winamp"):
                raise Exception("Nothing playing...")
            else:
                try:
                    if "Winamp" in win_title:
                        no_num = re.sub('[0-9]{1,2}\. ', '', win_title)
                        song_title = re.sub(' - Winamp', '', no_num)
                    else:
                        song_title = win_title
                    artist,title = song_title.split(" - ", 1)
                    hexchat.command("say %s♫ %sNow playing:%s %s %s-%s %s %s♫" % (red, blue, yellow, artist, blue, green, title, red))
                except Exception as err:
                    hexchat.prnt("Error: %s" % (err))
        except Exception as err:
            hexchat.prnt("Error: %s" % (err))
    except Exception as err:
        hexchat.prnt("Error: %s" % (err))


def main():
    hexchat.hook_command("music",now_playing,"")


if __name__ == "__main__":
    main()
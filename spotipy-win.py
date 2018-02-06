#!/usr/bin/python
import pywintypes
import win32gui
import hexchat

__module_name__        = "spotipy"
__module_version__     = "0.1"
__module_description__ = "Spotify now playing plugin for HexChat"

red = "\x034"
blue = "\x0312"
yellow = "\x038"
green = "\x039"


def get_win_title():
	win_title = ""

	try:
		hwnd = win32gui.FindWindow("SpotifyMainWindow", None)
		win_title = win32gui.GetWindowText(hwnd)
	except Exception as err:
		hexchat.prnt("Error: %s" % (err))

	return win_title


def spotify(word, wordeol, userdata):
	try:
		win_title = get_win_title()
		if win_title.startswith("Spotify"):
			raise Exception("Nothing playing...")
		else:
			artist,title = win_title.split(" - ", 1)
			hexchat.command("say %s♫ %sNow playing:%s %s %s-%s %s %s♫" % (red, blue, yellow, artist, blue, green, title, red))
	except Exception as err:
		hexchat.prnt("Error: %s" % (err))


def main():
	hexchat.hook_command("spotify",spotify,"")


if __name__ == "__main__":
	main()
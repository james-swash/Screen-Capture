import mss
import numpy
from win32api import GetSystemMetrics


def screen_capture():
	screen_width = GetSystemMetrics(0)
	screen_height = GetSystemMetrics(1)
	mon = {"top": 0, "left": 0, "width": screen_width, "height": screen_height}
	sct = mss.mss()
	arr = numpy.asarray(sct.grab(mon))
	return str(arr)
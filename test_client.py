import websocket
import _thread
import time
from pynput import keyboard
from pynput import mouse
import coding_test as ct
import test_server

def on_error(ws, error):
	print (error)

def on_close(ws):
	print ("### closed ###")

def on_open(ws):
	def run(*args):
		while True:
			time.sleep(5)
			def on_move(x, y):
				ws.send(ct.screen_capture())			
			
			def on_click(x, y, button, pressed):
				ws.send(ct.screen_capture())
			
			def on_scroll(x, y, dx, dy):
				ws.send(ct.screen_capture())
			
			def on_press(key):
				try:
					ws.send(ct.screen_capture())
				except AttributeError:
					print('special key {0} pressed'.format(
						key))
			
			def on_release(key):
				ws.send(ct.screen_capture())

			listener_mouse = mouse.Listener(
					   on_move=on_move,
					   on_click=on_click,
					   on_scroll=on_scroll)
			listener_key = keyboard.Listener(
						on_press=on_press,
						on_release=on_release)
			listener_mouse.start()
			listener_key.start()
			listener_mouse.join()
			listener_key.join()
		time.sleep(1)
		ws.close()
	_thread.start_new_thread(run, ())


if __name__ == "__main__":
	websocket.enableTrace(True)
	ws = websocket.WebSocketApp("ws://localhost:8765/",
						  on_error = on_error,
						  on_close = on_close,
						  on_open = on_open)
	ws.run_forever()

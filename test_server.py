from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket
import numpy as np
import _thread

class SimpleEcho(WebSocket):

    def handleMessage(self):
    	recv = np.asarray(self.data)
    	# print(recv)

    def handleConnected(self):
        print(self.address, 'connected')

    def handleClose(self):
        print(self.address, 'closed')

def run_server():
	server = SimpleWebSocketServer('', 8765, SimpleEcho)
	server.serveforever()

_thread.start_new_thread(run_server, ())
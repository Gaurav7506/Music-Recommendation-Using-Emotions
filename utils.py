''' Class for using separate thread for video streaming through web camera'''
import cv2
from threading import Thread
class WebcamVideoStream:
    	
		def __init__(self, src=0):
			self.stream = cv2.VideoCapture(src,cv2.CAP_DSHOW)
			(self.grabbed, self.frame) = self.stream.read()
			self.stopped = False

		def start(self):
				
			Thread(target=self.update, args=()).start()
			return self
			
		def update(self):
		
			while True:
				
				if self.stopped:
					return
				
				(self.grabbed, self.frame) = self.stream.read()

		def read(self):
			
			return self.frame
		def stop(self):
			
			self.stopped = True

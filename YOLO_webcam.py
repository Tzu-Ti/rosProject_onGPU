from yoloPydarknet import pydarknetYOLO
import cv2
import imutils
import time

yolo = pydarknetYOLO(obdata="/home/titi/darknet/cfg/coco.data", weights="/home/titi/darknet/yolov3.weights", cfg="/home/titi/darknet/cfg/yolov3.cfg")

start_time = time.time()

if __name__ == "__main__":
	VIDEO_IN = cv2.VideoCapture(0)
	frameID = 0
	while True:
		hasFrame, frame = VIDEO_IN.read()
		if not hasFrame:
			print("Done precessing !!!")
			print("— %s seconds —" % (time.time() - start_time))
			break
			
		yolo.getObject(frame, labelWant="", drawBox=True, bold=1, textsize=0.6, bcolor=(0,0,255), tcolor=(255,255,255))
		print("Object counts:", yolo.objCounts)
		cv2.imshow("Frame", imutils.resize(frame, width=850))
		if cv2.waitKey(1) == 0xFF & ord('q'):
			VIDEO_IN.release()
			cv2.destroyAllWindows()
			break

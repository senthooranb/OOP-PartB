import cv2 as cv

def resize(frame, factor=0.5):
    width =  int(frame.shape[1] * factor)
    height = int(frame.shape[0] * factor)
    dimensions = (width, height)
    newFrame = cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)
    
    return newFrame

videoFeed = cv.VideoCapture(0, cv.CAP_DSHOW)


while True:
    isReceiving, frame = videoFeed.read()
    cv.imshow("Original webcam feed", frame)
    cv.imshow("Resized webcam feed", resize(frame, 0.4))

    if(cv.waitKey(20) & 0xFF==ord('d')):
        break
videoFeed.release()
cv.destroyAllWindows

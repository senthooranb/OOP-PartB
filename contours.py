import cv2 as cv
import numpy
#can use canny to find contours or binarize to find contours
img = cv.imread("Python/Opencv/Ferrari.jpg")
blank = numpy.zeros(img.shape, dtype="uint8")
cv.imshow("blank", blank)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#canny = cv.Canny(img, 200, 400)
ret, thresh = cv.threshold(gray, 125, 180, cv.THRESH_BINARY)
contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
cv.drawContours(blank, contours, -1, (0,255,0), 1)
cv.imshow("Contours drawn", blank)
cv.imshow("Greyscale", gray)
#cv.imshow("Canny", canny)
cv.imshow("Threshold", thresh)
print(len(contours), "Contours found")
cv.waitKey(0)
cv.destroyAllWindows()

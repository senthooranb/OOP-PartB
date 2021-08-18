import cv2 as cv
import numpy
img = cv.imread("Python/Opencv/Ferrari.jpg")
b, g, r = cv.split(img)
cv.imshow("original", img)
cv.imshow("blue", b)
cv.imshow("green", g)
cv.imshow("Red", r)

merged = cv.merge([b,g,r])
cv.imshow("Merged", merged)

blank = numpy.zeros(img.shape[:2], dtype="uint8")
blue = cv.merge([b, blank, blank])
red = cv.merge([blank, blank, r])
green = cv.merge([blank, g, blank])

cv.imshow("Red CS", red)
cv.imshow("Blue CS", blue)
cv.imshow("Green CS", green)
print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)
cv.waitKey(0)
cv.destroyAllWindows()

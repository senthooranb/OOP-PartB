import time
import cv2 as cv
import numpy as np
import imutils
import tkinter as tk
from PIL import Image
from PIL import ImageTk
root = tk.Tk()
root.title("Theft detection using computer vision")
count = 3
width= root.winfo_screenwidth() 
height= root.winfo_screenheight()
#setting tkinter window size
root.geometry("%dx%d" % (width, height))
topFrame = tk.Frame(root, bg="misty rose")
topFrame.place(rely=0, relx=0.33, relheight=0.45, relwidth=0.67)
bottomFrame = tk.Frame(root, bg="light yellow")
leftFrame = tk.Frame(root, bg="PeachPuff2")
leftFrame.place(rely=0, relx=0, relheight=1, relwidth=0.33,)
bottomFrame.place(rely=0.45, relx=0.33, relheight=0.45, relwidth=0.67)

cameraFrame1 = tk.Label(topFrame, bg="black")
cameraFrame1.place(relx=0.05, relwidth=0.425, relheight=0.9, rely=0.05)

cameraFrame2 = tk.Label(topFrame, bg="black")
cameraFrame2.place(relx=0.525, relwidth=0.425, relheight=0.9, rely=0.05)

cameraFrame3 = tk.Label(bottomFrame, bg="black")
cameraFrame3.place(relx=0.05, relwidth=0.425, relheight=0.9, rely=0.05)

cameraFrame4 = tk.Label(bottomFrame, bg="black")
cameraFrame4.place(relx=0.525, relwidth=0.425, relheight=0.9, rely=0.05)

""" def detect():
button1 = tk.Button(leftFrame, text="Detect",fg="green", relheight=0.3, relwidth=0.7, command=detect()) """

""" videoFeed = cv.VideoCapture(0)
ret, initialFrame = videoFeed.read()
initialFrameCopy1 = initialFrame
initialFrameCopy2 = initialFrame
videoFeed.release()
while True:
    videoFeed = cv.VideoCapture(0)
    ret, frame = videoFeed.read()
    videoFeed.release()        
    initialFrame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    initialFrame = imutils.resize(initialFrame, 438, 342)
    initialFrame = cv.blur(initialFrame, (27,27))
    frame = cv.cvtColor(frame, cv.COLOR_RGB2GRAY)
    frame = imutils.resize(frame, 438, 342)
    frame = cv.blur(frame, (27,27))
    frameDelta = cv.absdiff(initialFrame, frame)
    ret, thresh = cv.threshold(frameDelta, 125, 180, cv.THRESH_BINARY)
    contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
    for c in contours:
        x,y,w,h = cv.boundingRect(c)
        cv.rectangle(initialFrameCopy2, (x,y), (x+w, y+h), (255, 0, 0), 4)

    img1 = Image.fromarray(initialFrameCopy1)
    imgtk1 = ImageTk.PhotoImage(image=img1)
    cameraFrame1.imgtk = imgtk1
    cameraFrame1.configure(image=imgtk1)

    img2 = Image.fromarray(frame)
    imgtk2 = ImageTk.PhotoImage(image=img2)
    cameraFrame2.imgtk = imgtk2
    cameraFrame2.configure(image=imgtk2)

    img3 = Image.fromarray(initialFrameCopy2)
    imgtk3 = ImageTk.PhotoImage(image=img3)
    cameraFrame3.imgtk = imgtk3
    cameraFrame3.configure(image=imgtk3)
    cameraFrame3.after(50, detect)

    if(len(contours)):
        break """

def stop():
    exit(0)

def show_frame():
    initialFrame = cv.imread("Hello.jpg")
    initialFrame = imutils.resize(initialFrame, 438, 342)
    initialFrameCopy2 = initialFrame
    videoFeed = cv.VideoCapture(0)
    while True:
        ret, frame = videoFeed.read()
        frameCopy = frame
        videoFeed.release()
        
        initialFrame = cv.cvtColor(initialFrame, cv.COLOR_BGR2GRAY)
        initialFrame = cv.blur(initialFrame, (7,7))
        frame = cv.cvtColor(frame, cv.COLOR_RGB2GRAY)
        frame = imutils.resize(frame, 438, 342)
        frame = cv.blur(frame, (7,7))
        frameDelta = cv.absdiff(initialFrame, frame)
        ret, thresh = cv.threshold(frameDelta, 45, 255, cv.THRESH_BINARY)
        contours, hierarchies = cv.findContours(thresh, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
        for c in contours:
            x,y,w,h = cv.boundingRect(c)
            cv.rectangle(initialFrameCopy2, (x,y), (x+w, y+h), (255, 0, 0), 4)

        img2 = Image.fromarray(thresh)
        imgtk2 = ImageTk.PhotoImage(image=img2)
        cameraFrame2.imgtk = imgtk2
        cameraFrame2.configure(image=imgtk2)

        frameCopy = cv.cvtColor(frameCopy, cv.COLOR_BGR2RGB)
        img3 = Image.fromarray(frameCopy)
        imgtk3 = ImageTk.PhotoImage(image=img3)
        cameraFrame3.imgtk = imgtk3
        cameraFrame3.configure(image=imgtk3)
        
        initialFrameCopy2 = cv.cvtColor(initialFrameCopy2, cv.COLOR_BGR2RGB)
        img4 = Image.fromarray(initialFrameCopy2)
        imgtk4 = ImageTk.PhotoImage(image=img4)
        cameraFrame4.imgtk = imgtk4
        cameraFrame4.configure(image=imgtk4)
        cameraFrame4.after(15, show_frame)


videoFeed = cv.VideoCapture(0)
ret, initialFrame = videoFeed.read()
videoFeed.release()
cv.imwrite("Hello.jpg", initialFrame)

initialFrame = cv.cvtColor(initialFrame, cv.COLOR_BGR2RGB)
img1 = Image.fromarray(initialFrame)
imgtk1 = ImageTk.PhotoImage(image=img1)
cameraFrame1.imgtk = imgtk1
cameraFrame1.configure(image=imgtk1)

button1 = tk.Button(leftFrame, text="Detect",fg="black", bg = "pale green",  command=show_frame)
button1['font'] = 'serif'
button1.place(relx=0.1, relwidth=0.8, relheight=0.15, rely=0.7)
button2 = tk.Button(leftFrame, text="Stop",fg="black", bg = "salmon", command=stop, )
button2['font'] = 'serif'
button2.place(relx=0.1, relwidth=0.8, relheight=0.15, rely=0.5)
Label1 = tk.Label(leftFrame, text="Object Detection", fg="black")
Label1['font'] = 'serif'
Label1.place(relx=0.1, relwidth=0.8, relheight=0.15, rely=0.1)
root.mainloop()
""" img1 = cv.imread("C:\\Sen\\Codes\\Python\\Opencv\\bottle.jpg")
img1 = imutils.resize(img1, 438, 342)
im1 = Image.fromarray(img1)
imgtk1 = ImageTk.PhotoImage(image=im1)
cameraFrame1.imgtk = imgtk1
cameraFrame1.configure(image=imgtk1)
cameraFrame1.update()
print("width:", cameraFrame1.winfo_width(), "\tHeight:", cameraFrame1.winfo_height())

img2 = cv.imread("C:\\Sen\\Codes\\Python\\Opencv\\no_bottle.jpg")
img2 = imutils.resize(img2, 438, 342)
im2 = Image.fromarray(img2)
imgtk2 = ImageTk.PhotoImage(image=im2)
cameraFrame2.imgtk = imgtk2
cameraFrame2.configure(image=imgtk2)
img1 = cv.cvtColor(img1, cv.COLOR_BGR2GRAY)
img2 = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)
img1 = cv.blur(img1, (3,3))
img2 = cv.blur(img2, (3,3))

diff = cv.absdiff(img1, img2)
thresh = cv.threshold(diff, 30, 255, cv.THRESH_BINARY_INV)[1]

blank = np.zeros(img1.shape, dtype="uint8")
contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(len(contours), "Found")
cv.drawContours(blank, contours, -1, (0,255,0), 1)
for c in contours:
    (x,y,w,h) = cv.boundingRect(c)
    cv.rectangle(img1, (x,y), (x+w, y+h), (0,255,0), 2)

cv.imshow("Demp", blank)
root.mainloop() """



""" img1 = cv.imread("C:\\Sen\\Codes\\Python\\Opencv\\bottle.jpg")
img2 = cv.imread("C:\\Sen\\Codes\\Python\\Opencv\\no_bottle.jpg")
img1 = cv.blur(img1, (27,27))
img2 = cv.blur(img2, (27, 27))

frameDelta = cv.absdiff(img1, img2)
frameDelta = cv.cvtColor(frameDelta, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(frameDelta, 125, 180, cv.THRESH_BINARY)
contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
for c in contours:
    x,y,w,h = cv.boundingRect(c)
    cv.rectangle(img1, (x,y), (x+w, y+h), (255, 0, 0), 4)

cv.imshow("Demo",img1)
cv.waitKey(0) """

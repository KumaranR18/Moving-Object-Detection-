import cv2
import imutils  # for resizing

cam = cv2.VideoCapture(0)  # open default camera
firstFrame = None
area = 500  # minimum contour area to detect

while True:
    _, img = cam.read()  # capture frame
    text = "Normal"
    img = imutils.resize(img, width=1000)  # resize frame for consistency
    grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # convert to grayscale
    gaussianImg = cv2.GaussianBlur(grayImg, (21, 21), 0)  # blur to reduce noise

    if firstFrame is None:
        firstFrame = gaussianImg  # set initial background frame
        continue

    imgDiff = cv2.absdiff(firstFrame, gaussianImg)  # compute difference with background
    threshImg = cv2.threshold(imgDiff, 25, 255, cv2.THRESH_BINARY)[1]  # threshold difference
    threshImg = cv2.dilate(threshImg, None, iterations=2)  # fill gaps

    cnts = cv2.findContours(threshImg.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)  # handle different OpenCV versions

    for c in cnts:
        if cv2.contourArea(c) < area:  # ignore small contours
            continue

        (x, y, w, h) = cv2.boundingRect(c)  # get bounding box
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)  # draw rectangle
        text = "Moving Object detected"
        print(text)

    cv2.putText(img, text, (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)  # overlay text
    cv2.imshow("cameraFeed", img)  # show frame

    key = cv2.waitKey(10)  # wait for key press
    print(key)

    if key == ord("q"):  # quit on 'q' key
        break

cam.release()
cv2.destroyAllWindows()

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import os

def callback(input):
    pass

def cannyEdge():
    print("This is the main function of the canny module.")
    img = cv.imread("images/cat.jpg", cv.IMREAD_GRAYSCALE)
    if img is None:
        print("Error: Image not found.")
        return

    winname = "Canny Edge Detection"
    cv.namedWindow(winname)
    cv.createTrackbar("Min Threshold", winname, 0, 255, callback)
    cv.createTrackbar("Max Threshold", winname, 0, 255, callback)
    
    while True:
        if cv.waitKey(1) == ord('q'):
            break
        
        min_threshold = cv.getTrackbarPos("Min Threshold", winname)
        max_threshold = cv.getTrackbarPos("Max Threshold", winname)
        
        cannyEdge = cv.Canny(img, min_threshold, max_threshold)
        
        display = np.hstack((img, cannyEdge))
        cv.imshow(winname, display)
    cv.destroyAllWindows()

if __name__ == "__main__":
    cannyEdge()
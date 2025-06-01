import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
import os

def main():
    img = cv.imread("images/cat.jpg", cv.IMREAD_GRAYSCALE)
    
    # Explain the lines below:
    plt.figure()
    plt.subplot(221) # 2 rows, 2 columns, first subplot
    plt.imshow(img, cmap='gray')
    
    laplacian = cv.Laplacian(img, cv.CV_64F, ksize=7)
    plt.subplot(222) # 2 rows, 2 columns, second subplot
    plt.imshow(laplacian, cmap='gray')
    
    kx, ky = cv.getDerivKernels(1, 0, 3)
    print(ky@kx.T)
    
    sobelX = cv.Sobel(img, cv.CV_64F, 1, 0, ksize=3)
    plt.subplot(223) # 2 rows, 2 columns, third subplot
    plt.imshow(sobelX, cmap='gray')
    
    sobelY = cv.Sobel(img, cv.CV_64F, 0, 1, ksize=3)
    plt.subplot(224) # 2 rows, 2 columns, fourth subplot
    plt.imshow(sobelY, cmap='gray')
        
    plt.show()

if __name__ == "__main__":
    main()
    
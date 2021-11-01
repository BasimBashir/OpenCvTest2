try:
    from cv2 import cv2
except ImportError:
    pass                          # Another method to use assist in cv2 module except direct import cv2

import numpy as np

kernel = np.ones((5, 5), np.uint8)

img = cv2.imread("Resources/Sample.png")  # reading image from directory
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # converting that image to gray and assigning new name
imgBlur = cv2.GaussianBlur(imgGray, (5, 5), 0)  # Making image blur and assigning it a name
imgCanny = cv2.Canny(imgBlur, 80, 80)  # Creating Pencil Drawing Like effect
imgBold = cv2.dilate(imgCanny, kernel, iterations=1)  # Creating Bold effect on Pencil Art
imgUnBold = cv2.erode(imgBold, kernel, iterations=1)  # Creating unBold effect on Bolded Pencil Art

# cv2.imshow("Colorful", img)  # displaying colorful image
#cv2.imshow("Gray", imgGray)  # displaying grey image
# cv2.imshow("blur", imgBlur)  # displaying Blur image
cv2.imshow("Pencil Art", imgCanny)  # displaying pencil art effect
cv2.imshow("Bold Effect ", imgBold)  # displaying Bold pencil art effect
cv2.imshow("Unbold Effect", imgUnBold)  # displaying unBold pencil art effect
cv2.waitKey(0)

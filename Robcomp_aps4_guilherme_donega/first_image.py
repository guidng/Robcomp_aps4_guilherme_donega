import cv2


print("OpenCV Version : %s " % cv2.__version__)

grid = cv2.imread("img/img9x9_aumentada.png")

cv2.imshow("Imagem BGR", grid)
cv2.waitKey()
cv2.destroyAllWindows()

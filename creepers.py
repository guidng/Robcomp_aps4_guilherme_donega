import cv2 as c
import numpy as np
import matplotlib.pyplot as plt

class ProcessImage:
    def __init__(self):
        self.bgr = None

    def run_image(self, image):
        self.bgr = image
        self.hsv = c.cvtColor(self.bgr, c.COLOR_BGR2HSV)

        #Verde
        g_low = np.array([35, 50, 50])
        g_high = np.array([85, 255, 255])
        self.mask_green = c.inRange(self.hsv, g_low, g_high)

        #Vermelho
        r_low = np.array([0, 50, 50])
        r_high = np.array([10, 255, 255])
        self.mask_red = c.inRange(self.hsv, r_low, r_high)

        #Azul
        b_low = np.array([90, 50, 50])
        b_high = np.array([140, 255, 255])
        self.mask_blue = c.inRange(self.hsv, b_low, b_high)

        self.mask = self.mask_red + self.mask_blue + self.mask_green

    def show_image(self):
        c.imshow("BGR", self.bgr)
        c.imshow("MASK", self.mask)
        
     


def main():
    imagem = ProcessImage()
    webcam = c.VideoCapture(0)
    while True:
        val, image = webcam.read()
        imagem.run_image(image)
        imagem.show_image()
        if c.waitKey(1) == 13:
            break

    webcam.release()
    c.destroyAllWindows()



    
    
if __name__ == "__main__":
    main()   


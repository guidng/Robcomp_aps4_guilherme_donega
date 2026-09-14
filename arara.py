import cv2 as c
import numpy as np
import time as t

class ProcessImage:
    def __init__(self):
        self.bgr = None

    def run_image(self, image):
        self.bgr = c.imread(image)
        height, width, channels = self.bgr.shape
        self.bgr[int(height/2):,int((width/3)*2):] = 0
        self.bgr[int(height/2):,:int(width/3)] = 0
        self.bgr[:int(height/2), int(width/3):int((width/3)*2)] = 0

    def show_image(self):
        c.imshow("imagem",self.bgr)
        c.waitKey()
        c.destroyAllWindows()
        


def main():
    imagem = ProcessImage()
    imagem.run_image("img/arara.jpg")
    imagem.show_image()

if __name__ == "__main__":
    main()

        



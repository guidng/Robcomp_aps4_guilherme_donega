import cv2 as c
import numpy as np
class ProcessImage():
    def __init__(self):
        self.bgr = None

    def run_image(self, image):
        self.bgr = image
        self.gray = c.cvtColor(self.bgr, c.COLOR_BGR2GRAY)
        self.gray[self.gray >= 128] = 255
        self.gray[self.gray < 128] = 0

    def show_image(self):
        c.imshow("imagem", self.gray)
        
        

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





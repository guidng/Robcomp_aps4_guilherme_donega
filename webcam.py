import cv2 as c
class ProcessImage:
    def __init__(self):
        self.bgr = None

    def run_image(self, image):
        self.bgr = image
        B,G,R = c.split(self.bgr)
        self.bgr = c.merge([R,G,B])
        self.bgr = c.transpose(self.bgr)

    def show_image(self):
        c.imshow("Imagem transposta", self.bgr)
        
        

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
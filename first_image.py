import cv2 as c
class ProcessImage():
    def __init__(self):
        self.bgr = None

    def load_image(self, image):
        self.bgr = c.imread(image)

        
    def show_image(self):
        c.imshow("Imagem Processada", self.bgr)
        c.waitKey()
        c.destroyAllWindows()

    def show_channels(self):
        B,G,R = c.split(self.bgr)
        c.imshow("B", B)
        c.imshow("G", G)
        c.imshow("R", R)
        c.waitKey()
        c.destroyAllWindows()

def main():
    imagem = ProcessImage()
    imagem.load_image("img/arara.jpg")
    imagem.show_image()
    imagem.show_channels()

if __name__ == "__main__":
    main()
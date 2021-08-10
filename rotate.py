from PIL import Image
import os

def rotate(img):
    print(img)
    pic = Image.open(img)
    zdjecie = pic.transpose(Image.ROTATE_270)
    zdjecie.save(img)

if __name__ == "__main__":
    images = os.listdir()
    images.remove("rotate.py")
    for img in images:
        rotate(img)
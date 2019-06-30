from PIL import Image
import os

zdjecia = os.listdir()
#print(zdjecia)
for c in zdjecia:
    if ".py" in c:
        pass
    else:
        print(c)
        pic = Image.open(c)
        print(pic)
        zdjecie = pic.transpose(Image.ROTATE_270)
        zdjecie.save(c)
        
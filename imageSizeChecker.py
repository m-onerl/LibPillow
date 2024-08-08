from PIL import Image
import os, sys
import os
from PIL import Image

"""
im = Image.open("C:/Users/moner/Desktop/tapeta/tapeta10.jpg")
print(im.format, im.size, im.mode)
im.show()
"""
os.chdir('/Users/moner/Documents/Projekty_github/LibPillow')
current_dir = os.getcwd()

for filename in os.listdir(current_dir):
    if filename.endswith != (".jpeg"):
        try:
            with Image.open(filename) as im:
                print(im.format, im.size, im.mode)
                if im.format != "JPEG":
                    print("Converting to JPEG")
                    im = im.convert("RGB")
                    new_filename = os.path.splitext(filename)[0] + ".jpeg"
                    im.save(new_filename, "JPEG")
                    im.show()
                else:
                    print("Image is already a JPEG file")
        except OSError:
            print("Is not a image file", filename)
    else:
        print("Skipping non-JPEG file:", filename)
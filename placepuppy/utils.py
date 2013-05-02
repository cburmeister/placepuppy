import glob
from random import choice
import PIL
from PIL import Image

def resize_da_puppeh(width, height):

    images = glob.glob('placepuppy/static/img/300.png')
    img = Image.open(choice(images))

    img_ratio = img.size[0] / float(img.size[1])
    ratio = width / float(height)

    if ratio > img_ratio:
        img = img.resize((width, width * img.size[1] / img.size[0]),
                Image.ANTIALIAS)
        box = (0, 0, img.size[0], height)
        img = img.crop(box)
    elif ratio < img_ratio:
        img = img.resize((height * img.size[0] / img.size[1], height),
                Image.ANTIALIAS)
        box = (0, 0, width, img.size[1])
        img = img.crop(box)
    else:
        img = img.resize((width, height), Image.ANTIALIAS)
    
    img.save('placepuppy/static/img/resized_img.png')

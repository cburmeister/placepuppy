import glob
from random import choice
import PIL
from PIL import Image

def resize_da_puppeh(width, height, crop='middle'):
    images = glob.glob('placepuppy/static/img/*')
    img = Image.open(choice(images))
    img_ratio = img.size[0] / float(img.size[1])
    ratio = width / float(height)
    if ratio > img_ratio:
        img = img.resize((width, width * img.size[1] / img.size[0]),
                Image.ANTIALIAS)
        if crop == 'top':
            box = (0, 0, img.size[0], height)
        elif crop == 'middle':
            box = (0, (img.size[1] - height) / 2, img.size[0],
                    (img.size[1] + height) / 2)
        else:
            box = (0, img.size[1] - height, img.size[0], img.size[1])
        img = img.crop(box)
    elif ratio < img_ratio:
        img = img.resize((height * img.size[0] / img.size[1], height),
                Image.ANTIALIAS)
        if crop == 'top':
            box = (0, 0, width, img.size[1])
        elif crop == 'middle':
            box = ((img.size[0] - width) / 2, 0, (img.size[0] + width) / 2,
                    img.size[1])
        else:
            box = (img.size[0] - width, 0, img.size[0], img.size[1])
        img = img.crop(box)
    else:
        img = img.resize((width, height), Image.ANTIALIAS)
    img.save('placepuppy/static/img/resized_img.png')

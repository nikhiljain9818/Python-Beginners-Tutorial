''' Install pillow library
    change the image extension
    resize image files
    resize multiple images using for loop
    Sharpness     -----|
    Brightness         |
    Color              |------> import ImageEnhance module
    Contrast      -----|
    Image blur, GaussianBlur  ------> import ImageFilter module'''

from PIL import Image, ImageEnhance, ImageFilter
import os
# making instance of image
# img1 = Image.open('nik.jpg')

# creating new file with different extension
# img1.save('nik1.png')

# showing file 
# img1.show('nik.jpg')

# resizing file
# MAX_SIZE = (250,250)
# img1.thumbnail(MAX_SIZE)
# img1.save('dognew.jpg')

# resizing multiple image at time using loop
# for item in os.listdir():
#     if item.endswith('.jpg'):
#         img1 = Image.open(item)
#         filename,extension = os.path.splitext(item)
#         img1.save(f'{filename}.png')

# Sharpness = ImageEnhance.Sharpness()
# img1 = Image.open('dog.jpg')
# enhancer = ImageEnhance.Sharpness(img1)
# enhancer.enhance(4).save('dogsharpness.jpg')

# Color = ImageEnhance.Color()
# img1 = Image.open('dog.jpg')
# enhancer = ImageEnhance.Color(img1)
# enhancer.enhance(3).save('dogcolor.jpg')

# Brightness = ImageEnhance.Brightness()
# img1 = Image.open('dog.jpg')
# enhancer = ImageEnhance.Brightness(img1)
# enhancer.enhance(2).save('dogbright.jpg')

# Contrast = ImageEnhance.Cntrast()
# img1 = Image.open('dog.jpg')
# enhancer = ImageEnhance.Contrast(img1)
# enhancer.enhance(2).save('dogcontrast.jpg')

# Blur  
# img1 = Image.open('dog.jpg')
# img1.filter(ImageFilter.GaussianBlur(radius=2)).save('dogblur.jpg')







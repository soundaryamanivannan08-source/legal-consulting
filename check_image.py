from PIL import Image
img = Image.open('Assest/stackly_071.webp')
img = img.convert('RGBA')
print('Image size:', img.size)
print('Top-left pixel:', img.getpixel((0,0)))

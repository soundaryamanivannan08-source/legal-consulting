from PIL import Image, ImageChops

def process_image(input_path, output_path, bg_color=(247, 247, 247), tolerance=30):
    img = Image.open(input_path).convert('RGBA')
    datas = img.getdata()
    
    new_data = []
    for item in datas:
        # Check if the pixel is close to the bg_color
        if (abs(item[0] - bg_color[0]) <= tolerance and
            abs(item[1] - bg_color[1]) <= tolerance and
            abs(item[2] - bg_color[2]) <= tolerance):
            new_data.append((255, 255, 255, 0)) # transparent
        else:
            new_data.append(item)
            
    img.putdata(new_data)
    
    # Get bounding box of non-transparent pixels
    bbox = img.getbbox()
    if bbox:
        img = img.crop(bbox)
        
    img.save(output_path, 'WEBP')

process_image('Assest/stackly_071.webp', 'Assest/stackly_071_transparent.webp')
print('Image processed and saved.')

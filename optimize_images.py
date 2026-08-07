import os
import glob
from PIL import Image

ASSET_DIR = "Assest"
MAX_SIZE = 100 * 1024  # 100KB

image_files = []
for ext in ('*.jpg', '*.jpeg', '*.png', '*.jfif'):
    image_files.extend(glob.glob(os.path.join(ASSET_DIR, ext)))

replacement_map = {}

for img_path in image_files:
    filename = os.path.basename(img_path)
    name, ext = os.path.splitext(filename)
    new_filename = f"{name}.webp"
    new_path = os.path.join(ASSET_DIR, new_filename)
    
    img = Image.open(img_path)
    if img.mode in ("RGBA", "P"):
        img = img.convert("RGB")
        
    quality = 90
    scale = 1.0
    
    while True:
        if scale < 1.0:
            new_size = (int(img.width * scale), int(img.height * scale))
            if new_size[0] == 0 or new_size[1] == 0:
                break
            temp_img = img.resize(new_size, Image.Resampling.LANCZOS)
        else:
            temp_img = img
            
        temp_img.save(new_path, "WEBP", quality=quality)
        size = os.path.getsize(new_path)
        
        if size <= MAX_SIZE:
            break
            
        if quality > 30:
            quality -= 10
        else:
            scale *= 0.8
            
    print(f"Optimized {filename} to {new_filename} (Size: {size / 1024:.1f} KB)")
    replacement_map[filename] = new_filename
    
    os.remove(img_path)

web_files = glob.glob('*.html') + glob.glob('*.css')
for file in web_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
        
    for old_file, new_file in replacement_map.items():
        content = content.replace(f"Assest/{old_file}", f"Assest/{new_file}")
        content = content.replace(f"Assest\\\\{old_file}", f"Assest/{new_file}")
        
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Finished updating assets and references.")

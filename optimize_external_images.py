import os
import re
import urllib.request
from PIL import Image

ASSET_DIR = "Assest"
MAX_SIZE = 100 * 1024

files_to_process = ['index.html', 'pricing.html']
url_pattern = re.compile(r'(https://images\.unsplash\.com/[^\s"\'<>]+)')

url_map = {}

for file in files_to_process:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    urls = url_pattern.findall(content)
    for url in urls:
        if url not in url_map:
            url_map[url] = f"unsplash_{len(url_map) + 1}.webp"

print(f"Found {len(url_map)} unique images to download.")

for url, new_filename in url_map.items():
    print(f"Downloading {new_filename}...")
    temp_path = os.path.join(ASSET_DIR, "temp_download.jpg")
    
    req = urllib.request.Request(url.replace('&amp;', '&'), headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req) as response, open(temp_path, 'wb') as out_file:
            out_file.write(response.read())
    except Exception as e:
        print(f"Failed to download {url}: {e}")
        continue
        
    new_path = os.path.join(ASSET_DIR, new_filename)
    
    img = Image.open(temp_path)
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
            
    print(f"Optimized {new_filename} (Size: {size / 1024:.1f} KB)")
    os.remove(temp_path)

for file in files_to_process:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
        
    for url, new_filename in url_map.items():
        content = content.replace(url, f"Assest/{new_filename}")
        
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Finished updating external links.")

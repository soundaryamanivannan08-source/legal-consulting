import os
import re

files = [f for f in os.listdir('.') if f.endswith('.html')]
logo_pattern = re.compile(r'(<(?:div|a)[^>]*class="logo[^"]*"[^>]*>)\s*<svg.*?</svg>\s*STACKLY\s*(</(?:div|a)>)', re.IGNORECASE | re.DOTALL)

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = logo_pattern.sub(r'\1\n            <img src="Assest/stackly_071.webp" alt="Stackly Logo" style="height: 32px; width: auto;">\n        \2', content)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(new_content)
        
print("Replaced in all files.")

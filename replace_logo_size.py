import os

files = [f for f in os.listdir('.') if f.endswith('.html')]
old_str = '<img src="Assest/stackly_071.webp" alt="Stackly Logo" style="height: 32px; width: auto;">'
new_str = '<img src="Assest/stackly_071_transparent.webp" alt="Stackly Logo" style="height: 44px; width: auto;">'

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if old_str in content:
        new_content = content.replace(old_str, new_str)
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
print("Updated logo source and size in all files.")

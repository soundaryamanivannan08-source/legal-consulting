import glob, os, re

html_files = glob.glob('*.html')
for f in html_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Replace exact href="#"
    new_content = content.replace('href=\"#\"', 'href=\"404.html\"')
    
    # Also find buttons or anchor tags that might need it? 
    # The user said "wherever # is there in our project"
    # What about href='#0' ? Let's just do href="#" for now.

    if new_content != content:
        with open(f, 'w', encoding='utf-8') as file:
            file.write(new_content)
        print(f"Updated {f}")

print("Done updating unused links.")

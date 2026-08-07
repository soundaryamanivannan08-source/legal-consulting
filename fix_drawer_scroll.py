import glob

html_files = glob.glob('*.html')

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the mobile menu toggle line and add body overflow toggle
    old_line = "navLinks.classList.toggle('active');"
    new_line = "navLinks.classList.toggle('active');\n            document.body.style.overflow = navLinks.classList.contains('active') ? 'hidden' : '';"
    
    if old_line in content and "document.body.style.overflow" not in content:
        content = content.replace(old_line, new_line)

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print('Fixed drawer background scrolling across all HTML files.')

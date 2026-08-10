import glob

html_files = glob.glob('*.html')

replacements = {
    '123 Business Blvd, NY 10001': 'MMR Complex, Chinna Thirupathi, near Chinna Muniyappan Kovil, Salem, Tamil Nadu 636008',
    'One Battery Park Plaza, NY': 'MMR Complex, Chinna Thirupathi, near Chinna Muniyappan Kovil, Salem, Tamil Nadu 636008',
    'hello@stackly.com': 'info@stackly.com',
    '+1 (555) 000-0000': '9876543210',
    'Stackly, Salem, Tamil Nadu, India': 'MMR Complex, Chinna Thirupathi, near Chinna Muniyappan Kovil, Salem, Tamil Nadu 636008',
    'john@example.com': 'info@stackly.com'
}

for f in html_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    new_content = content
    for old, new in replacements.items():
        new_content = new_content.replace(old, new)
    
    if new_content != content:
        with open(f, 'w', encoding='utf-8') as file:
            file.write(new_content)
        print(f"Updated {f}")

print("Done updating contact details.")

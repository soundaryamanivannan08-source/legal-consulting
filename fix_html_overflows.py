import glob
import re

html_files = glob.glob('*.html')

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Eradicate problematic min-widths that cause overflow on 320px screens
    content = re.sub(r'min-width:\s*320px;?', 'min-width: 100%; max-width: 100%;', content)
    content = re.sub(r'min-width:\s*300px;?', 'min-width: 100%; max-width: 100%;', content)
    content = re.sub(r'width:\s*250px;?', 'width: 100%; max-width: 250px;', content)
    
    # Ensure any stray flex items don't overflow
    content = re.sub(r'flex:\s*1;\s*min-width:\s*\d+px;?', 'flex: 1 1 100%;', content)

    # In dashboards, min-width: 600px on tables is okay IF they are in overflow-x: auto containers
    # We will add a wrapper in CSS for dashboard grids/tables instead of replacing inline

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print('Updated HTML files to eliminate rigid inline widths.')

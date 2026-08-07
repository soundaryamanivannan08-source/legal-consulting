import glob
import re

html_files = glob.glob('*.html')

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # The button looks like: <a href="#" class="btn btn-primary btn-sm">Book Consultation</a>
    # Or variations thereof. We can just target the innerHTML and the surrounding tag.
    # It might have a different href or slightly different classes.
    pattern = r'<a[^>]*class="[^"]*btn-primary[^"]*"[^>]*>\s*Book Consultation\s*</a>'
    
    # Wait, we only want to remove it from the navbar!
    # Let's target the nav-actions block.
    # Since the button is specific enough and mostly only exists in nav-actions or hero (hero is "Book Your Consultation"),
    # we can just use the pattern exactly. Let's make sure it's inside <div class="nav-actions"> to be safe.
    
    # A safer approach: find the nav-actions div and replace inside it.
    def replace_in_nav(match):
        inner = match.group(1)
        # Remove the book consultation button
        inner = re.sub(r'<a[^>]*>\s*Book Consultation\s*</a>\s*', '', inner)
        return '<div class="nav-actions">' + inner + '</div>'
        
    content = re.sub(r'<div class="nav-actions">(.*?)</div>', replace_in_nav, content, flags=re.DOTALL)

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print('Removed Book Consultation button from navbar in all HTML files.')

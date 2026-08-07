import glob

html_files = glob.glob('*.html')

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the entire block from mobileHeader.innerHTML down to navLinks.insertBefore
    # and replace it with clean JS using single quotes or valid backticks.
    
    # Let's just use string concatenation to be absolutely safe from string literal parsers
    safe_js = (
        "            mobileHeader.innerHTML = "
        "'<button class=\"mobile-close-btn\" id=\"mobileCloseBtn\" aria-label=\"Close menu\">&times;</button>' + "
        "'<img src=\"Assest/stackly_071_transparent.webp\" alt=\"Stackly Logo\" class=\"mobile-menu-logo\">';"
    )
    
    # We need to find whatever broken mess is currently there and replace it
    import re
    # Match from mobileHeader.innerHTML = up to navLinks.insertBefore
    pattern = r'mobileHeader\.innerHTML\s*=\s*(?:\\n)?.*?<button.*?</button>.*?<img.*?>.*?(?:\\;|;)\s*(?=\n\s*navLinks\.insertBefore)'
    
    new_content = re.sub(pattern, safe_js, content, flags=re.DOTALL)
    
    if new_content != content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)

print('JS fully fixed.')

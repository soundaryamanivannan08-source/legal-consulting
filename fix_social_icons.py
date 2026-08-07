import glob

html_files = glob.glob('*.html')

svg_ln = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"/><rect x="2" y="9" width="4" height="12"/><circle cx="4" cy="4" r="2"/></svg>'
svg_tw = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M23 3a10.9 10.9 0 0 1-3.14 1.53 4.48 4.48 0 0 0-7.86 3v1A10.66 10.66 0 0 1 3 4s-4 9 5 13a11.64 11.64 0 0 1-7 2c9 5 20 0 20-11.5a4.5 4.5 0 0 0-.08-.83A7.72 7.72 0 0 0 23 3z"/></svg>'
svg_fb = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"/></svg>'

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace ln, tw, fb with SVGs. We look for ">ln</a>", etc to avoid matching random text.
    # Note: in about.html it's literally <a href="#">ln</a>
    
    if '>ln</a>' in content or '>tw</a>' in content or '>fb</a>' in content:
        content = content.replace('>ln</a>', '>' + svg_ln + '</a>')
        content = content.replace('>tw</a>', '>' + svg_tw + '</a>')
        content = content.replace('>fb</a>', '>' + svg_fb + '</a>')
        # Also handle uppercase variants if they exist
        content = content.replace('>LN</a>', '>' + svg_ln + '</a>')
        content = content.replace('>TW</a>', '>' + svg_tw + '</a>')
        content = content.replace('>FB</a>', '>' + svg_fb + '</a>')

        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {file}")

print('Finished updating social icons.')

import glob
import re

html_files = glob.glob('*.html')

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Fix grid minmax
    content = re.sub(r'minmax\(300px', 'minmax(250px', content)
    content = re.sub(r'minmax\(280px', 'minmax(250px', content)

    # Fix large font sizes in inline styles
    content = re.sub(r'font-size:\s*3rem;?', 'font-size: clamp(2rem, 5vw, 3rem);', content)
    content = re.sub(r'font-size:\s*2\.5rem;?', 'font-size: clamp(1.8rem, 4vw, 2.5rem);', content)
    content = re.sub(r'font-size:\s*2\.2rem;?', 'font-size: clamp(1.5rem, 3.5vw, 2.2rem);', content)

    # Fix large inline paddings
    content = re.sub(r'padding:\s*120px\s*0\s*80px;?', 'padding: clamp(60px, 10vw, 120px) 0 clamp(40px, 5vw, 80px);', content)
    content = re.sub(r'padding:\s*80px\s*0;?', 'padding: clamp(40px, 8vw, 80px) 0;', content)
    
    # Fix info-card max-width on contact page (if 1100px is too rigid, make it 100%)
    content = re.sub(r'max-width:\s*1100px;', 'max-width: 100%;', content)

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print('Updated HTML files.')

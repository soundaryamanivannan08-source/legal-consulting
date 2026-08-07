import os, glob, re

aos_css = '\n    <link href="https://unpkg.com/aos@2.3.1/dist/aos.css" rel="stylesheet">\n</head>'
aos_js = """
    <!-- AOS Animation -->
    <script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>
    <script>
        document.addEventListener("DOMContentLoaded", function() {
            AOS.init({
                duration: 800,
                once: true,
                offset: 100
            });
        });
    </script>
</body>"""

for filepath in glob.glob('*.html'):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Add AOS CSS if not present
    if 'aos.css' not in content:
        content = content.replace('</head>', aos_css)
        
    # 2. Add AOS JS if not present
    if 'aos.js' not in content:
        content = content.replace('</body>', aos_js)
        
    # 3. Replace gsap-* classes with data-aos="..."
    def replace_gsap_class(match):
        tag_str = match.group(0)
        
        # Find all gsap-xxx classes
        gsap_classes = re.findall(r'gsap-([a-zA-Z0-9-]+)', tag_str)
        if not gsap_classes:
            return tag_str
            
        aos_val = gsap_classes[0] # Usually there's only one
        
        # Remove the gsap-xxx class
        tag_str = re.sub(r'\s*gsap-[a-zA-Z0-9-]+', '', tag_str)
        
        # Remove empty class attributes if they exist
        tag_str = tag_str.replace('class=""', '')
        tag_str = tag_str.replace("class=''", "")
        
        # Add data-aos attribute right before the closing >
        if tag_str.endswith('/>'):
            tag_str = tag_str[:-2] + f' data-aos="{aos_val}"/>'
        else:
            tag_str = tag_str[:-1] + f' data-aos="{aos_val}">'
            
        return tag_str
        
    # Regex to find opening tags containing 'gsap-'
    content = re.sub(r'<[^>]+class="[^"]*gsap-[^"]*"[^>]*>', replace_gsap_class, content)
    content = re.sub(r"<[^>]+class='[^']*gsap-[^']*'[^>]*>", replace_gsap_class, content)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Restored AOS animations globally.")

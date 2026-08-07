import os, glob, re

gsap_cdn = """
    <!-- GSAP & ScrollTrigger -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/ScrollTrigger.min.js"></script>
    <script src="animations.js"></script>
</body>"""

for filepath in glob.glob('*.html'):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Remove AOS links
    content = re.sub(r'<link[^>]*href="[^"]*aos\.css"[^>]*>\s*', '', content)
    content = re.sub(r'<script[^>]*src="[^"]*aos\.js"[^>]*></script>\s*', '', content)
    
    # Remove AOS initialization block
    content = re.sub(r'<script>\s*AOS\.init\(\{.*?\}\);\s*</script>\s*', '', content, flags=re.DOTALL)
    
    # Process all opening tags with data-aos
    def replace_aos_tag(match):
        tag_str = match.group(0)
        
        # Extract data-aos value
        aos_match = re.search(r'data-aos="([^"]+)"', tag_str)
        if not aos_match:
            return tag_str
        
        aos_val = aos_match.group(1)
        new_class = f"gsap-{aos_val}"
        
        # Remove all data-aos related attributes
        tag_str = re.sub(r'\s*data-aos(-duration|-delay|-offset)?="[^"]+"', '', tag_str)
        
        # Inject into class
        if 'class="' in tag_str:
            tag_str = re.sub(r'class="([^"]*)"', rf'class="\1 {new_class}"', tag_str, count=1)
        else:
            # If no class exists, add it after the tag name
            tag_name_match = re.match(r'<([a-zA-Z0-9]+)', tag_str)
            if tag_name_match:
                tag_name = tag_name_match.group(1)
                tag_str = tag_str.replace(f'<{tag_name}', f'<{tag_name} class="{new_class}"', 1)
                
        return tag_str

    content = re.sub(r'<[^>]+data-aos="[^"]+"[^>]*>', replace_aos_tag, content)
    
    # Add GSAP scripts before closing body
    content = content.replace('</body>', gsap_cdn)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Migration completed.")

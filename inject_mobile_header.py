import glob

html_files = glob.glob('*.html')

js_injection = """
        // Inject Mobile Header
        if (!document.getElementById('mobileHeader')) {
            const mobileHeader = document.createElement('div');
            mobileHeader.id = 'mobileHeader';
            mobileHeader.className = 'mobile-menu-header';
            mobileHeader.innerHTML = 
                <button class="mobile-close-btn" id="mobileCloseBtn" aria-label="Close menu">&times;</button>
                <img src="Assest/stackly_071_transparent.webp" alt="Stackly Logo" class="mobile-menu-logo">
            ;
            navLinks.insertBefore(mobileHeader, navLinks.firstChild);

            document.getElementById('mobileCloseBtn').addEventListener('click', () => {
                navLinks.classList.remove('active');
                document.body.style.overflow = '';
            });
        }
"""

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Avoid double injection
    if 'id="mobileHeader"' not in content:
        # Insert right after const navLinks = document.getElementById('navLinks');
        old_line = "const navLinks = document.getElementById('navLinks');"
        new_line = old_line + "\n" + js_injection
        
        content = content.replace(old_line, new_line)

        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)

print('Injected mobile header JS into all HTML files.')

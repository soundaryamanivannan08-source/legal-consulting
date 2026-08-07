import re

files = ['user-dashboard.html', 'admin-dashboard.html']

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update .top-header for desktop (fixed instead of sticky)
    top_header_desktop = '''
        .top-header {
            display: flex;
            align-items: center;
            justify-content: flex-end;
            gap: 16px;
            padding: 16px 40px;
            background: white;
            border-bottom: 1px solid var(--border-color);
            position: fixed;
            top: 0;
            width: calc(100% - var(--sidebar-width));
            left: var(--sidebar-width);
            z-index: 40;
            transition: left 0.3s ease, width 0.3s ease;
        }'''
    
    # We will regex replace the old .top-header entirely
    content = re.sub(r'\.top-header\s*\{[^}]*position:\s*sticky;[^}]*\}', top_header_desktop, content)
    
    # 2. Add padding-top to desktop .main-content-inner
    # Find .main-content-inner { padding: 0 40px 40px; } and replace it
    content = re.sub(r'\.main-content-inner\s*\{\s*padding:\s*0\s*40px\s*40px;\s*\}', '.main-content-inner {\n            padding: 90px 40px 40px;\n        }', content)
    # Also handle admin-dashboard format if it's different (it's the same or similar)
    content = re.sub(r'\.main-content-inner\s*\{\s*padding:\s*32px\s*40px\s*40px;\s*\}', '.main-content-inner {\n            padding: 90px 40px 40px;\n        }', content)

    # 3. Update mobile queries
    if '@media (max-width: 768px)' in content:
        # Inject mobile fixes
        mobile_header_fix = '''
            .top-header {
                width: 100% !important;
                left: 0 !important;
                padding: 12px 20px !important;
            }
            .main-content-inner {
                padding: 80px 16px 16px 16px !important;
            }
'''
        content = content.replace('@media (max-width: 768px) {', '@media (max-width: 768px) {' + mobile_header_fix)

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Updated top header to be strictly fixed.")

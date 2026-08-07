import re

files = ['user-dashboard.html', 'admin-dashboard.html']

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Add overflow-x: hidden to body
    if 'overflow-x: hidden;' not in content:
        content = content.replace('body {', 'body {\n            overflow-x: hidden;\n            max-width: 100vw;')

    # Make page-title word break
    if '.page-title {' in content:
        content = content.replace('.page-title {', '.page-title {\n            word-wrap: break-word;\n            word-break: break-word;\n            overflow-wrap: break-word;\n            hyphens: auto;')
    
    # Also add it to h1 globally in the dashboard if .page-title is not found
    if 'h1, h2, h3 {' in content:
        content = content.replace('h1, h2, h3 {', 'h1, h2, h3 {\n            word-wrap: break-word;\n            word-break: break-word;\n            overflow-wrap: break-word;')

    # Fix stats grid on mobile
    # Let's ensure padding is not pushing it out
    mobile_query = '@media (max-width: 768px)'
    
    if mobile_query in content:
        mobile_css_fixes = '''
            .main-content-inner {
                padding: 16px !important;
                max-width: 100vw;
                box-sizing: border-box;
            }
            .page-title {
                font-size: 1.5rem !important;
            }
            .stats-grid {
                display: flex;
                flex-direction: column;
            }
            .stat-card {
                width: 100%;
                box-sizing: border-box;
            }
'''
        content = content.replace('        @media (max-width: 768px) {', '        @media (max-width: 768px) {' + mobile_css_fixes)

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Applied responsiveness fixes to dashboards.")

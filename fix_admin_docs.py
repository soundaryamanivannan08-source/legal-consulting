import re

file = 'admin-dashboard.html'

with open(file, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace inline styles for page-header
content = content.replace('class="section-header" style="display: flex; justify-content: space-between; align-items: center;"', 'class="section-header header-flex"')
content = content.replace('class="page-header" style="display: flex; justify-content: space-between; align-items: center;"', 'class="page-header header-flex"')

if '.header-flex {' not in content:
    content = content.replace('.section-header {', '.header-flex {\n            display: flex;\n            justify-content: space-between;\n            align-items: center;\n        }\n        .section-header {')
    # If .section-header is not found, fallback to adding to body
    if '.header-flex {' not in content:
        content = content.replace('body {', '.header-flex {\n            display: flex;\n            justify-content: space-between;\n            align-items: center;\n        }\n        body {')

mobile_fixes = '''
            .header-flex {
                flex-direction: column;
                align-items: flex-start;
                gap: 16px;
            }
            .doc-item {
                flex-direction: column;
                align-items: flex-start;
                gap: 12px;
            }
            .doc-icon {
                margin-bottom: 4px;
                margin-right: 0;
            }
            .doc-meta {
                flex-wrap: wrap;
                gap: 8px !important;
            }
            .doc-meta span {
                background: #F3F4F6;
                padding: 4px 8px;
                border-radius: 4px;
            }
            .btn-download {
                width: 100%;
                margin-top: 8px;
            }
'''

if '.doc-item {' not in content.split('@media (max-width: 768px) {')[1]:
    content = content.replace('@media (max-width: 768px) {', '@media (max-width: 768px) {' + mobile_fixes)

with open(file, 'w', encoding='utf-8') as f:
    f.write(content)

print("Applied responsive fixes to Admin Documents section.")

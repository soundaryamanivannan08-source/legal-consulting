import re

files = ['user-dashboard.html', 'admin-dashboard.html']

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Change 100vw to 100% to avoid scrollbar overflow issues
    content = content.replace('max-width: 100vw;', 'max-width: 100%;\n            width: 100%;')
    
    # Add overflow-x hidden to html, body
    if 'html, body {' not in content:
        content = content.replace('body {', 'html, body {\n            overflow-x: hidden;\n            max-width: 100%;\n            width: 100%;\n        }\n\n        body {')
    else:
        content = content.replace('html, body {', 'html, body {\n            overflow-x: hidden;\n            max-width: 100%;\n            width: 100%;')

    # Remove the second duplicate .main-content-inner padding in mobile query if it exists
    # Find the mobile query block
    if '@media (max-width: 768px)' in content:
        # Just use a robust regex to replace .main-content-inner {...} entirely in the mobile section
        # and re-add it once.
        pass # Actually, let's just make sure .main-content is width: 100% and overflow-x hidden
        
        mobile_fix = '''
            .main-content {
                margin-left: 0 !important;
                width: 100% !important;
                max-width: 100% !important;
                overflow-x: hidden !important;
            }
            .main-content-inner {
                padding: 16px !important;
                width: 100% !important;
                max-width: 100% !important;
                box-sizing: border-box !important;
                overflow-x: hidden !important;
            }
            .top-header {
                width: 100% !important;
                box-sizing: border-box !important;
            }
            * {
                box-sizing: border-box !important;
            }
'''
        # Inject at the very end of the max-width: 768px block
        # We can find the closing brace of the media query... it's tricky with regex.
        # Let's just insert it right after the media query declaration.
        content = content.replace('@media (max-width: 768px) {', '@media (max-width: 768px) {' + mobile_fix)

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Applied robust 100% width fixes to dashboards.")

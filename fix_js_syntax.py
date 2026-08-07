import glob

html_files = glob.glob('*.html')

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # The broken JS block
    broken_str = "            mobileHeader.innerHTML = \n                <button"
    fixed_str = "            mobileHeader.innerHTML = \\n                <button"
    
    if broken_str in content:
        content = content.replace(broken_str, fixed_str)
        
    broken_str2 = "class=\"mobile-menu-logo\">\n            ;"
    fixed_str2 = "class=\"mobile-menu-logo\">\n            \;"
    
    if broken_str2 in content:
        content = content.replace(broken_str2, fixed_str2)

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print('Fixed JS syntax in HTML files.')

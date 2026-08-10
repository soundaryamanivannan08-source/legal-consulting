import os

css_file = 'styles.css'
with open(css_file, 'a', encoding='utf-8') as f:
    f.write('\n/* Fix for fixed navbar overlapping hero sections */\n.navbar + * {\n    margin-top: 90px;\n}\n')

print("Added margin-top to hero sections in styles.css")

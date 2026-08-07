import re

files = ['user-dashboard.html', 'admin-dashboard.html']

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Remove the floating toggle if it exists (only in user-dashboard.html)
    toggle_pattern = r'\s*<button class="mobile-toggle" onclick="toggleSidebar\(\)">\s*<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\s*<line x1="3" y1="12" x2="21" y2="12"></line>\s*<line x1="3" y1="6" x2="21" y2="6"></line>\s*<line x1="3" y1="18" x2="21" y2="18"></line>\s*</svg>\s*</button>'
    content = re.sub(toggle_pattern, '', content)

    # 2. Update sidebar-header to include the close button and flex justification
    header_pattern = r'(<div class="sidebar-header">)\s*(<img src="Assest/stackly_071_transparent\.webp" alt="Stackly" style="height: 44px; width: auto;">)\s*(</div>)'
    new_header = r'''<div class="sidebar-header" style="justify-content: space-between; width: 100%;">
            \2
            <button class="sidebar-close-btn" onclick="toggleSidebar()" aria-label="Close sidebar">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>
            </button>
        </div>'''
    content = re.sub(header_pattern, new_header, content)

    # 3. Add CSS for sidebar-close-btn (before closing </style>)
    css_to_add = '''
        .sidebar-close-btn {
            display: none;
            background: none;
            border: none;
            color: #9CA3AF;
            cursor: pointer;
            padding: 4px;
            transition: color 0.3s;
        }
        .sidebar-close-btn:hover {
            color: white;
        }
'''
    if '.sidebar-close-btn {' not in content:
        # Find the last closing brace of the main CSS, right before media queries
        content = content.replace('        @media (max-width: 768px) {', css_to_add + '        @media (max-width: 768px) {')

        # And add to the mobile query
        mobile_css_to_add = '''
            .sidebar-close-btn {
                display: block;
            }
'''
        content = content.replace('            .sidebar {', mobile_css_to_add + '            .sidebar {')

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Updated dashboard sidebars successfully.")

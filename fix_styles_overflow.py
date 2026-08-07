import re

css_appends = """
/* === Global Anti-Overflow Safeguards === */
html, body {
    overflow-x: hidden;
    width: 100%;
    margin: 0;
    padding: 0;
}

* {
    box-sizing: border-box;
    overflow-wrap: break-word; /* Prevent long links/emails from blowing out containers */
    word-wrap: break-word;
}

/* Ensure flex containers wrap natively on small screens if they aren't already */
@media (max-width: 480px) {
    .container, .contact-main, .hero-content, .auth-container {
        flex-direction: column !important;
        flex-wrap: wrap !important;
    }
    
    /* Allow charts or wide tables in dashboard to scroll horizontally instead of breaking layout */
    .dashboard-table-wrapper, .dashboard-grid, .recent-activity {
        overflow-x: auto;
        -webkit-overflow-scrolling: touch;
        width: 100%;
    }
}
"""

with open('styles.css', 'a', encoding='utf-8') as f:
    f.write(css_appends)

print('Updated styles.css.')

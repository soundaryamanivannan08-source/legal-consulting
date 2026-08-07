import re

css_appends = """
/* === Comprehensive Responsive Overhaul === */
/* Global Media */
img, picture, video, iframe, figure {
    max-width: 100%;
    height: auto;
}
iframe {
    border: 0;
}

/* Fluid Typography Base for H1/H2 (if not overridden inline) */
h1 {
    font-size: clamp(2rem, 5vw, 4rem);
}
h2 {
    font-size: clamp(1.8rem, 4vw, 3rem);
}

/* Mobile Tables */
@media (max-width: 600px) {
    .hours-table {
        display: block;
        width: 100%;
        overflow-x: auto;
        -webkit-overflow-scrolling: touch;
    }
    .hours-table tbody {
        display: block;
        width: 100%;
    }
    .hours-table tr {
        display: flex;
        flex-direction: column;
        padding: 10px 0;
    }
    .hours-table td {
        padding: 5px 0 !important;
        text-align: left !important;
    }
    .hours-time {
        text-align: left !important;
    }
}

/* Form Container */
@media (max-width: 480px) {
    .contact-form-container {
        padding: 20px !important;
    }
    .cta-banner {
        padding: 40px 20px !important;
    }
    .info-card {
        padding: 20px !important;
    }
}

/* Fix flex containers that don't wrap */
@media (max-width: 768px) {
    .contact-main {
        flex-direction: column;
    }
}
"""

with open('styles.css', 'a', encoding='utf-8') as f:
    f.write(css_appends)

print('Updated styles.css.')

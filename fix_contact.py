import re

with open('about.html', 'r', encoding='utf-8') as f:
    about = f.read()

nav_match = re.search(r'(<nav class="navbar">.*?</nav>)', about, re.DOTALL)
footer_match = re.search(r'(<footer class="footer">.*?</footer>)', about, re.DOTALL)
js_match = re.search(r'(<script>.*?</script>.*?)</body>', about, re.DOTALL)

nav_html = nav_match.group(1) if nav_match else ""
footer_html = footer_match.group(1) if footer_match else ""
js_html = js_match.group(1) if js_match else ""

with open('contact.html', 'r', encoding='utf-8') as f:
    contact = f.read()
    
# Find where body starts
body_start = contact.find('<body>') + 6
head_html = contact[:body_start]

contact_body = """
    <!-- Navbar -->
""" + nav_html + """

    <!-- Contact Hero -->
    <section class="contact-hero">
        <div class="container">
            <h1>Get in Touch</h1>
            <p>Our experts are ready to assist you. Reach out today for a confidential consultation and discover how we can help your business thrive.</p>
        </div>
    </section>

    <!-- Info Cards -->
    <section class="info-cards container">
        <div class="info-card">
            <div class="info-icon">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg>
            </div>
            <h3>Phone</h3>
            <p>+1 (555) 000-0000</p>
        </div>
        <div class="info-card">
            <div class="info-icon">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path><polyline points="22,6 12,13 2,6"></polyline></svg>
            </div>
            <h3>Email</h3>
            <p>hello@stackly.com</p>
        </div>
        <div class="info-card">
            <div class="info-icon">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle cx="12" cy="10" r="3"></circle></svg>
            </div>
            <h3>Headquarters</h3>
            <p>One Battery Park Plaza, NY</p>
        </div>
    </section>

    <!-- Main Content: Form & Map -->
    <section class="contact-main container">
        <div class="contact-form-container">
            <h2>Send us a message</h2>
            <form>
                <div style="margin-bottom: 20px;">
                    <label style="display:block; margin-bottom: 5px; color:#64748B;">Full Name</label>
                    <input type="text" style="width:100%; padding: 12px; border: 1px solid #E2E8F0; border-radius: 8px;" placeholder="John Doe">
                </div>
                <div style="margin-bottom: 20px;">
                    <label style="display:block; margin-bottom: 5px; color:#64748B;">Email Address</label>
                    <input type="email" style="width:100%; padding: 12px; border: 1px solid #E2E8F0; border-radius: 8px;" placeholder="john@example.com">
                </div>
                <div style="margin-bottom: 20px;">
                    <label style="display:block; margin-bottom: 5px; color:#64748B;">Message</label>
                    <textarea style="width:100%; padding: 12px; border: 1px solid #E2E8F0; border-radius: 8px;" rows="5" placeholder="How can we help you?"></textarea>
                </div>
                <button type="button" class="btn btn-primary" style="width: 100%;">Send Message</button>
            </form>
        </div>
        <div style="flex: 1; min-width: 320px;">
            <div class="location-pills">
                <div class="location-pill active">Salem</div>
            </div>
            <div class="map-card">
                <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d15632.748110595995!2d78.16522501066779!3d11.685002599999999!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3babefef7fd970bb%3A0xe11aef1a71994f9!2sStackly!5e0!3m2!1sen!2sin!4v1715000000000!5m2!1sen!2sin" width="100%" height="350" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
                <div class="map-info">
                    <div class="map-info-text">
                        <h4>Stackly Legal Consulting</h4>
                        <p>Stackly, Salem, Tamil Nadu, India</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

""" + footer_html + """
""" + js_html + """
</body>
</html>
"""

with open('contact.html', 'w', encoding='utf-8') as f:
    f.write(head_html + contact_body)

print('contact.html restored')

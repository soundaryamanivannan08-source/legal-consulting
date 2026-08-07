import re

new_html = """

    <!-- 1. Global Offices Grid -->
    <section class="global-offices" style="padding: 80px 0; background: #F8FAFC;">
        <div class="container">
            <div class="section-header text-center" style="margin-bottom: 40px;">
                <div class="tag-blue">Global Presence</div>
                <h2 style="font-size: 2.2rem; color: #0F172A; margin-top: 15px;">Our Offices Worldwide</h2>
            </div>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 30px;">
                <div class="info-card">
                    <h3 style="font-size: 1.25rem; margin-bottom: 15px;">New York (Headquarters)</h3>
                    <p style="margin-bottom: 10px;"><strong>Address:</strong> One Battery Park Plaza, NY 10004</p>
                    <p style="margin-bottom: 10px;"><strong>Phone:</strong> +1 (212) 555-0100</p>
                    <p><strong>Email:</strong> ny@stackly.com</p>
                </div>
                <div class="info-card">
                    <h3 style="font-size: 1.25rem; margin-bottom: 15px;">London</h3>
                    <p style="margin-bottom: 10px;"><strong>Address:</strong> 30 St Mary Axe, London EC3A 8EP</p>
                    <p style="margin-bottom: 10px;"><strong>Phone:</strong> +44 20 7946 0958</p>
                    <p><strong>Email:</strong> london@stackly.com</p>
                </div>
                <div class="info-card">
                    <h3 style="font-size: 1.25rem; margin-bottom: 15px;">Singapore</h3>
                    <p style="margin-bottom: 10px;"><strong>Address:</strong> 8 Marina Boulevard, Singapore 018981</p>
                    <p style="margin-bottom: 10px;"><strong>Phone:</strong> +65 6555 0199</p>
                    <p><strong>Email:</strong> sg@stackly.com</p>
                </div>
            </div>
        </div>
    </section>

    <!-- 2. Department Contacts -->
    <section class="department-contacts" style="padding: 80px 0; background: white;">
        <div class="container">
            <div class="section-header" style="margin-bottom: 40px; text-align: center;">
                <h2 style="font-size: 2.2rem; color: #0F172A;">Direct Department Access</h2>
                <p style="color: #64748B; max-width: 600px; margin: 15px auto 0;">Reach out directly to the practice area that suits your needs.</p>
            </div>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 20px;">
                <div style="padding: 25px; border-bottom: 2px solid #E2E8F0; text-align: center;">
                    <h4 style="font-size: 1.1rem; color: #0F172A; margin-bottom: 10px;">Corporate Law</h4>
                    <a href="mailto:corporate@stackly.com" style="color: var(--primary); font-weight: 600; text-decoration: none;">corporate@stackly.com</a>
                </div>
                <div style="padding: 25px; border-bottom: 2px solid #E2E8F0; text-align: center;">
                    <h4 style="font-size: 1.1rem; color: #0F172A; margin-bottom: 10px;">M&A Advisory</h4>
                    <a href="mailto:mna@stackly.com" style="color: var(--primary); font-weight: 600; text-decoration: none;">mna@stackly.com</a>
                </div>
                <div style="padding: 25px; border-bottom: 2px solid #E2E8F0; text-align: center;">
                    <h4 style="font-size: 1.1rem; color: #0F172A; margin-bottom: 10px;">Tax Advisory</h4>
                    <a href="mailto:tax@stackly.com" style="color: var(--primary); font-weight: 600; text-decoration: none;">tax@stackly.com</a>
                </div>
                <div style="padding: 25px; border-bottom: 2px solid #E2E8F0; text-align: center;">
                    <h4 style="font-size: 1.1rem; color: #0F172A; margin-bottom: 10px;">Compliance</h4>
                    <a href="mailto:compliance@stackly.com" style="color: var(--primary); font-weight: 600; text-decoration: none;">compliance@stackly.com</a>
                </div>
            </div>
        </div>
    </section>

    <!-- 3. Business Hours -->
    <section class="office-hours-section">
        <div class="hours-container container">
            <div class="hours-header text-center">
                <h2>Business Hours</h2>
                <p style="margin: 0 auto;">Our dedicated team operates across time zones to ensure you always have the support you need.</p>
            </div>
            <div style="background: white; border: 1px solid #E2E8F0; border-radius: 16px; padding: 40px; box-shadow: 0 4px 6px rgba(0,0,0,0.05);">
                <table class="hours-table">
                    <tr>
                        <td class="hours-day">Monday - Friday</td>
                        <td class="hours-time open">8:00 AM - 6:00 PM (EST)</td>
                    </tr>
                    <tr>
                        <td class="hours-day">Saturday</td>
                        <td class="hours-time">10:00 AM - 2:00 PM (EST)</td>
                    </tr>
                    <tr style="border-bottom: none;">
                        <td class="hours-day">Sunday</td>
                        <td class="hours-time">Closed</td>
                    </tr>
                </table>
            </div>
        </div>
    </section>

    <!-- 4. Consultation Process -->
    <section class="consultation-process" style="padding: 80px 0; background: white;">
        <div class="container">
            <div class="section-header text-center" style="margin-bottom: 50px;">
                <div class="tag-blue">What to Expect</div>
                <h2 style="font-size: 2.2rem; color: #0F172A; margin-top: 15px;">Your Journey With Us</h2>
            </div>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 30px;">
                <div style="text-align: center; padding: 20px;">
                    <div style="width: 60px; height: 60px; background: var(--primary); color: white; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 1.5rem; font-weight: bold; margin: 0 auto 20px;">1</div>
                    <h3 style="font-size: 1.25rem; color: #0F172A; margin-bottom: 15px;">Initial Review</h3>
                    <p style="color: #64748B;">Submit your details. We review your requirements and assign the right specialist.</p>
                </div>
                <div style="text-align: center; padding: 20px;">
                    <div style="width: 60px; height: 60px; background: var(--primary); color: white; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 1.5rem; font-weight: bold; margin: 0 auto 20px;">2</div>
                    <h3 style="font-size: 1.25rem; color: #0F172A; margin-bottom: 15px;">Strategy Session</h3>
                    <p style="color: #64748B;">A deep dive consultation to outline potential legal and consulting avenues.</p>
                </div>
                <div style="text-align: center; padding: 20px;">
                    <div style="width: 60px; height: 60px; background: var(--primary); color: white; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 1.5rem; font-weight: bold; margin: 0 auto 20px;">3</div>
                    <h3 style="font-size: 1.25rem; color: #0F172A; margin-bottom: 15px;">Action Plan</h3>
                    <p style="color: #64748B;">We draft a comprehensive roadmap tailored specifically to your objectives.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- 5. Contact FAQ -->
    <section class="contact-faq cs-faq" style="padding: 80px 0; background: #F8FAFC;">
        <div class="container">
            <div class="section-header text-center" style="margin-bottom: 40px;">
                <h2 style="font-size: 2.2rem; color: #0F172A;">Frequently Asked Questions</h2>
            </div>
            <div class="faq-list">
                <div class="faq-item">
                    <div class="faq-question">What should I bring to my first consultation? <span class="icon">+</span></div>
                    <div class="faq-answer"><p>Please bring any relevant legal documents, contracts, or business records pertaining to your case. A brief summary of your goals is also helpful.</p></div>
                </div>
                <div class="faq-item">
                    <div class="faq-question">Are initial consultations free? <span class="icon">+</span></div>
                    <div class="faq-answer"><p>We offer a complimentary 30-minute initial discovery call. Detailed strategy sessions are billed at our standard advisory rates.</p></div>
                </div>
                <div class="faq-item">
                    <div class="faq-question">How quickly will someone get back to me? <span class="icon">+</span></div>
                    <div class="faq-answer"><p>Our team strives to respond to all inquiries within 24 business hours. Urgent matters should be directed to our phone line.</p></div>
                </div>
            </div>
        </div>
    </section>

    <!-- 6. Final CTA Banner -->
    <section class="cta-banner-wrapper container">
        <div class="cta-banner">
            <h2>Ready to protect and grow your business?</h2>
            <p>Schedule a confidential consultation with our industry experts today.</p>
            <a href="#" class="btn btn-primary" style="background: white; color: var(--primary);">Book Your Consultation</a>
        </div>
    </section>

"""

with open('contact.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Insert before <footer class="footer">
new_content = content.replace('<footer class="footer">', new_html + '\n<footer class="footer">')

with open('contact.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print('Added 6 sections.')

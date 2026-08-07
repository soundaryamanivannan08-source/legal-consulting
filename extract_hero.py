import json
import re

with open(r'C:\Users\Dell\.gemini\antigravity\brain\37c7d971-592d-477b-8036-96d84b536e2b\.system_generated\logs\transcript_full.jsonl', 'r', encoding='utf-8') as f:
    for line in f:
        data = json.loads(line)
        content = data.get('content', '')
        if 'class="contact-hero"' in content:
            print("FOUND CONTACT-HERO IN LOG!")
            # Extract the block around contact-hero
            idx = content.find('class="contact-hero"')
            print(content[max(0, idx-1000):idx+3000])
            break

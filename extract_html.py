import json

with open(r'C:\Users\Dell\.gemini\antigravity\brain\37c7d971-592d-477b-8036-96d84b536e2b\.system_generated\logs\transcript_full.jsonl', 'r', encoding='utf-8') as f:
    for line in f:
        data = json.loads(line)
        if data.get('type') == 'VIEW_FILE' and 'contact.html' in data.get('content', ''):
            print('--- FOUND VIEW_FILE ---')
            print(data.get('content', '')[:1000])
        elif data.get('type') == 'REPLACE_FILE_CONTENT' and 'contact.html' in data.get('content', ''):
            print('--- FOUND REPLACE_FILE_CONTENT ---')
            print(data.get('content', '')[:1000])

import re

with open('aplikacje-mobilne.html', 'r', encoding='utf-8') as f:
    text = f.read()

# fetch features header
features_header = re.search(r'<div class="max-w-[^>]*mb-16[^>]*>.*?</div>', text, flags=re.DOTALL)
if features_header: print(features_header.group(0))
    

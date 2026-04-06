import re

with open('aplikacje-mobilne.html', 'r', encoding='utf-8') as f:
    text = f.read()

faq_match = re.search(r'<section [^>]*id="faq"[^>]*>', text)
if faq_match: print("FAQ:", faq_match.group(0))

grid_match = re.search(r'(<div class="col-span-full md:col-start-1 md:col-span-2 md:row-start-4 md:row-span-1[^>]*>.*?</div>\s*</div>)', text, flags=re.DOTALL)
if grid_match:
    with open('grid.html', 'w', encoding='utf-8') as g:
        g.write(grid_match.group(1))
    print("Exported grid")

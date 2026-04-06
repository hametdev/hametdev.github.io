import re

with open('aplikacje-mobilne.html', 'r', encoding='utf-8') as f:
    text = f.read()

# find the main layout containing these svgs
match = re.search(r'(<div class="col-span-full md:col-start-1 md:col-span-2 md:row-start-4 md:row-span-1 rounded-\[2rem\] flex items-center justify-center p-8 bg-charcoal">)(.*?)(</div>\s*</div>\s*</div>)', text, flags=re.DOTALL)
if match:
    grid_html = match.group(0)

    for f in ['ru/mobilnye-prilozheniya.html', 'hr/mobilne-aplikacije.html', 'en/mobile-apps.html']:
        with open(f, 'r', encoding='utf-8') as fh:
            c = fh.read()
        c_match = re.search(r'(<div class="col-span-full md:col-start-1 md:col-span-2 md:row-start-4 md:row-span-1 rounded-\[2rem\] flex items-center justify-center p-8 bg-charcoal">)(.*?)(</div>\s*</div>\s*</div>)', c, flags=re.DOTALL)
        if c_match:
            c = c[:c_match.start()] + grid_html + c[c_match.end():]
            with open(f, 'w', encoding='utf-8') as fh:
                fh.write(c)
            print("Replaced grid in", f)
        else:
            print("Could not find grid in", f)

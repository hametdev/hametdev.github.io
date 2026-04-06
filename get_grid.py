import re

with open('aplikacje-mobilne.html', 'r', encoding='utf-8') as f:
    text = f.read()

# fetch grid
grid_match = re.search(r'(<div class="grid grid-cols-2 gap-4 lg:gap-8 max-w-lg w-full">.*?</div>\s*</div>)', text, flags=re.DOTALL)
if grid_match:
    with open('grid.html', 'w', encoding='utf-8') as g:
        g.write(grid_match.group(1))
    print("Exported grid")

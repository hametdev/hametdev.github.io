import re

with open('aplikacje-mobilne.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Extract from 
start = text.find('<!-- Card 4:')
end = text.find('</section>', start)
if start != -1:
    with open('grid.html', 'w', encoding='utf-8') as f:
        f.write(text[start:end])
    print("Exported grid chunk")

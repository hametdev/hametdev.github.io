import os

m_html = open('aplikacje-mobilne.html', 'r', encoding='utf-8').read()

# Get new config block
config_start = m_html.find('        tailwind.config = {')
config_end = m_html.find('        }') + 9

new_config = m_html[config_start:config_end]

for f in ['ru/mobilnye-prilozheniya.html', 'hr/mobilne-aplikacije.html', 'en/mobile-apps.html']:
    c = open(f, 'r', encoding='utf-8').read()
    c_start = c.find('        tailwind.config = {')
    c_end = c.find('        }', c_start) + 9
    
    if c_start > -1 and c_end > -1:
        c = c[:c_start] + new_config + c[c_end:]
        open(f, 'w', encoding='utf-8').write(c)
        print("Updated config for", f)

import os
import sys

ref = open('aplikacje-mobilne.html', 'r', encoding='utf-8').read()
ref_s = ref.find('tailwind.config = {')
ref_e = ref.find('</script>', ref_s)
new_config = ref[ref_s:ref_e]

for f in ['ru/mobilnye-prilozheniya.html', 'hr/mobilne-aplikacije.html', 'en/mobile-apps.html']:
    c = open(f, 'r', encoding='utf-8').read()
    c_s = c.find('tailwind.config = {')
    c_e = c.find('</script>', c_s)
    if c_s > -1 and c_e > -1:
        c = c[:c_s] + new_config + c[c_e:]
        open(f, 'w', encoding='utf-8').write(c)
        print(f"Updated config for {f}")

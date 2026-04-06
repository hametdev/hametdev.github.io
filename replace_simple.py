import os

files = ['ru/mobilnye-prilozheniya.html', 'hr/mobilne-aplikacije.html', 'en/mobile-apps.html']

replacements = {
    '#A78BFA': '#7C3AED',
    '167,139,250': '124,58,237',
    '#F472B6': '#DB2777',
    '244,114,182': '219,39,119',
    '#34D399': '#059669',
    '52,211,153': '5,150,105',
    '#60A5FA': '#2563EB',
    '96,165,250': '37,99,235',
    '#FCD34D': '#D97706',
    '252,211,77': '217,119,6',
    '#F87171': '#DC2626',
    '248,113,113': '220,38,38',
    'class="flex flex-col gap-4 pb-8 max-w-7xl"': 'class="flex flex-col gap-4 pb-8 max-w-[1000px] mx-auto w-full items-center text-center"',
    'class="relative py-28 px-4 md:px-20 bg-[#EDEDED]" id="faq"': 'class="relative py-28 px-4 md:px-20 bg-neutral-50" id="faq"',
    'class="text-charcoal text-4xl mb-4"': 'class="text-charcoal text-4xl mb-4 text-center self-center"',
    'class="text-charcoal text-4xl mb-8"': 'class="text-charcoal text-4xl mb-8 text-center self-center"',
    'class="max-w-3xl flex flex-col gap-4 w-full text-left"': 'class="max-w-3xl flex flex-col gap-4 w-full text-left mx-auto"',
    'class="max-w-3xl flex flex-col gap-4 w-full text-left bg-white"': 'class="max-w-3xl flex flex-col gap-4 w-full text-left mx-auto"',
}

for f in files:
    with open(f, 'r', encoding='utf-8') as fh:
        c = fh.read()
    for k, v in replacements.items():
        c = c.replace(k, v)
    with open(f, 'w', encoding='utf-8') as fh:
        fh.write(c)
    print("Replaced colors and classes in", f)

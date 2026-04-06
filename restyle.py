import re

# File path
filepath = r"c:\Users\mkham\Projects\hamet\hamet.agency\aplikacje-mobilne.html"

with open(filepath, "r", encoding="utf-8") as f:
    text = f.read()

# 1. Update fonts link
old_fonts = r"icon_names=attach_file,close,devices,expand_more,keyboard_arrow_down,mail,menu,payments,smart_toy,smartphone"
new_fonts = r"icon_names=arrow_outward,attach_file,close,devices,expand_more,keyboard_arrow_down,mail,menu,payments,send,smart_toy,smartphone"
text = text.replace(old_fonts, new_fonts)

# 2. Update overall background/blobs
old_bg = r"""<div class="fixed inset-0 z-0 overflow-hidden pointer-events-none">
        <div class="absolute inset-0 bg-cream/80 z-0"></div>
        <div class="absolute top-[-20%] left-[-10%] w-[80vw] h-[80vw] max-w-[1000px] max-h-[1000px] bg-neutral-200/70 rounded-full mix-blend-multiply filter blur-[120px] animate-blob opacity-80"></div>
        <div class="absolute top-[10%] right-[-10%] w-[60vw] h-[60vw] max-w-[800px] max-h-[800px] bg-accent/40 rounded-full mix-blend-multiply filter blur-[100px] animate-blob animation-delay-2000 opacity-60"></div>
        <div class="absolute top-[40%] left-[20%] w-[50vw] h-[50vw] max-w-[600px] max-h-[600px] bg-[#d9dde3]/60 rounded-full mix-blend-multiply filter blur-[80px] animate-drift animation-delay-4000 opacity-70"></div>
        <div class="absolute bottom-[-20%] right-[10%] w-[70vw] h-[70vw] max-w-[900px] max-h-[900px] bg-taupe/10 rounded-full mix-blend-multiply filter blur-[120px] animate-breathe animation-delay-2000 opacity-50"></div>
        <div class="absolute bottom-[20%] left-[-10%] w-[40vw] h-[40vw] max-w-[500px] max-h-[500px] bg-clay/20 rounded-full mix-blend-multiply filter blur-[90px] animate-float animation-delay-6000 opacity-40"></div>
        <div class="absolute inset-0 bg-noise opacity-[0.07] mix-blend-overlay z-10"></div>
    </div>"""

new_bg = r"""<div class="fixed inset-0 z-0 overflow-hidden pointer-events-none">
        <div class="absolute inset-0 bg-neutral-100 z-0"></div>
    </div>"""
text = text.replace(old_bg, new_bg)

# 3. Update Header
# The header layout is mostly fine but we need to update the button styles, mobile menu toggle, and inner div
old_header_inner = '<div class="flex flex-1 w-full px-6 py-3 items-center justify-between bg-white rounded-full pointer-events-auto border border-charcoal/10 shadow-sm">'
new_header_inner = '<div class="flex flex-1 w-full px-6 py-3 items-center justify-between bg-white rounded-full border border-charcoal/10 pointer-events-auto shadow-sm">'
text = text.replace(old_header_inner, new_header_inner)

old_btn = r"""<a href="#contact" class="hidden sm:flex items-center justify-center overflow-hidden rounded-full h-10 px-6 glass-button-dark text-white text-sm font-bold">"""
new_btn = r"""<a href="#contact" class="hidden sm:flex items-center justify-center rounded-full h-10 px-6 bg-charcoal text-white text-sm font-bold hover:bg-black transition-colors">"""
text = text.replace(old_btn, new_btn)

# Language text links
old_lang_mobile = r"""<a href="/en/mobile-apps.html" class="hidden md:inline-flex items-center text-[11px] font-mono tracking-widest border border-taupe/20 rounded-full px-3 py-1.5 text-taupe hover:text-charcoal transition-colors">EN</a>
                        <div class="hidden">
                            <span class="text-charcoal font-bold">PL</span>
                            <span class="text-taupe/40 select-none">?</span>
                            <a href="/en/mobile-apps.html" class="text-taupe hover:text-charcoal transition-colors">EN</a>
                            <span class="text-taupe/40 select-none">?</span>
                            <a href="/hr/mobilne-aplikacije.html" class="text-taupe hover:text-charcoal transition-colors">HR</a>
                            <span class="text-taupe/40 select-none">?</span>
                            <a href="/ru/mobilnye-prilozheniya.html" class="text-taupe hover:text-charcoal transition-colors">RU</a>
                        </div>"""
new_lang_mobile = r"""<a href="/en/mobile-apps.html" class="text-sm font-bold text-charcoal hover:text-taupe transition-colors px-2">EN</a>"""
text = text.replace(old_lang_mobile, new_lang_mobile)

# mobile menu toggle
old_menu_toggle = r"""<button id="mobile-menu-toggle" class="md:hidden flex items-center justify-center w-10 h-10 rounded-full bg-white/10 text-charcoal backdrop-blur-md border border-white/20">"""
new_menu_toggle = r"""<button id="mobile-menu-toggle" class="md:hidden flex items-center justify-center w-10 h-10 rounded-full bg-black/5 text-charcoal backdrop-blur-md border border-charcoal/10">"""
text = text.replace(old_menu_toggle, new_menu_toggle)

# 4. Hero image section
# For now we'll keep the app image, but change dark buttons on hero page
# text = text.replace('class="flex h-12 md:h-14 px-6 md:px-8 items-center justify-center rounded-full bg-white text-charcoal border border-charcoal/12 hover:bg-neutral-50 text-sm md:text-base font-medium transition-colors"', 'class="flex h-12 md:h-14 px-6 md:px-8 items-center justify-center rounded-full bg-white text-charcoal border border-charcoal/12 hover:bg-neutral-50 shadow-sm transition-colors text-sm md:text-base font-medium"')

# 5. Background replacements
text = text.replace('style="background-color: #f2f4f7;"', 'class="relative py-28 px-4 md:px-10 bg-[#EDEDED]"')
# Wait, there are sections that have both class="..." and style="background-color...
# Let's use regex
text = re.sub(r'class="([^"]*?)"\s+style="background-color:\s*#f2f4f7;"\s*id="features"', r'class="\1 bg-[#EDEDED]" id="features"', text)
text = re.sub(r'class="([^"]*?)"\s+style="background-color:\s*#f2f4f7;"\s*id="pricing"', r'class="\1 bg-[#EDEDED]" id="pricing"', text)
text = re.sub(r'class="([^"]*?)"\s+style="background-color:\s*#f2f4f7;"\s*id="faq"', r'class="\1 bg-neutral-50" id="faq"', text)
text = re.sub(r'class="([^"]*?)"\s+style="background-color:\s*#f2f4f7;"\s*id="contact"', r'class="\1 bg-[#EDEDED]" id="contact"', text)

# 6. Pricing bottom button
old_pricing_btn = '<a href="#contact" class="inline-flex h-14 px-10 items-center justify-center rounded-full glass-button-dark text-base font-medium">'
new_pricing_btn = '<a href="#contact" class="inline-flex h-14 px-10 items-center justify-center rounded-full bg-charcoal text-white hover:bg-black text-sm md:text-base font-medium transition-colors">'
text = text.replace(old_pricing_btn, new_pricing_btn)

# 7. Contact WhatsApp SVG and send button SVG (wait, main page uses mail / whatsapp instead of chat input, let's keep the contact section as is but with new styling if needed).
# In aplikacje-mobilne, contact is similar to main page. 

# 8. Footer replacement
footer_pattern = re.compile(r'<footer.*?</footer>', re.DOTALL)
new_footer = r"""<footer class="bg-[#111111]/50 border-t border-white/5 relative z-20">  
    <div class="layout-container flex justify-center w-full px-4 md:px-10 py-8">
        <div class="flex flex-col w-full max-w-[1000px] gap-1 md:gap-2 text-white/50 text-sm">

            <!-- Первая строка (Адрес с флагом слева, Языки справа) -->
            <div class="flex flex-col md:flex-row justify-between items-center gap-1 w-full">
                <!-- Адрес -->
                <div class="flex items-center gap-2.5">
                    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="15" viewBox="0 0 16 12" class="rounded-[2px] shadow-sm border border-white/10"><rect width="16" height="12" fill="#fff"/><rect width="16" height="6" y="6" fill="#dc143c"/></svg>
                    <span class="tracking-wide text-white/50">Polska, Warszawa, Korotyńskiego 20</span>
                </div>
                <!-- Языки -->
                <div class="flex items-center opacity-80 hover:opacity-100 transition-opacity">
                    <nav class="flex items-center gap-3 md:gap-4" aria-label="Languages">
                                        <a href="https://hamet.agency/en/" class="text-xs font-bold tracking-wide text-white/50 hover:text-white transition-colors">EN</a>
                                        <a href="https://hamet.agency/" class="text-xs font-bold tracking-wide text-white/50 hover:text-white transition-colors">PL</a>
                                        <a href="https://hamet.agency/hr/" class="text-xs font-bold tracking-wide text-white/50 hover:text-white transition-colors">HR</a>
                                        <a href="https://hamet.agency/ru/" class="text-xs font-bold tracking-wide text-white/50 hover:text-white transition-colors">RU</a>
                                    </nav>
                </div>
            </div>

            <!-- Вторая строка (Копирайт слева, Политика справа) -->
            <div class="flex flex-col md:flex-row justify-between items-center gap-1 w-full">
                <!-- Copyright -->
                <p>© 2026 Hamet Agency. All rights reserved.</p>
                <!-- Privacy Policy -->
                <a class="hover:text-white transition-colors" href="privacy-policy.html">Polityka Prywatności</a>
            </div>

        </div>
    </div>
</footer>"""
text = footer_pattern.sub(new_footer, text)


with open(filepath, "w", encoding="utf-8") as f:
    f.write(text)

print("Done")
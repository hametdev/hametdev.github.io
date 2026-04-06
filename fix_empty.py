import os
import re

files = ['ru/mobilnye-prilozheniya.html', 'hr/mobilne-aplikacije.html', 'en/mobile-apps.html']

empty_icons_html = r'''
                        <!-- Empty Grid Icons -->
                        <div class="hidden md:flex md:col-start-2 md:col-span-1 md:row-start-1 md:row-span-1 items-center justify-center p-8">
                            <svg viewBox="0 0 384 512" fill="currentColor" class="w-full max-w-[100px] max-h-[100px] text-neutral-100 hover:scale-105 transition-transform duration-500"><path d="M318.7 268.7c-.2-36.7 16.4-64.4 50-84.8-18.8-26.9-47.2-41.7-84.7-44.6-35.5-2.8-74.3 20.7-88.5 20.7-15 0-49.4-19.7-76.4-19.7C63.3 141.2 4 184.8 4 273.5q0 39.3 14.4 81.2c12.8 36.7 59 126.7 107.2 125.2 25.2-.6 43-17.9 75.8-17.9 31.8 0 48.3 17.9 76.4 17.9 48.6-.7 90.4-82.5 102.6-119.3-65.2-30.7-61.7-90-61.7-91.9zm-56.6-164.2c27.3-32.4 24.8-61.9 24-72.5-24.1 1.4-52 16.4-67.9 34.9-17.5 19.8-27.8 44.3-25.6 71.9 26.1 2 49.9-11.4 69.5-34.3z"/></svg>
                        </div>
                        <div class="hidden md:flex md:col-start-4 md:col-span-1 md:row-start-2 md:row-span-1 items-center justify-center p-8">
                            <svg viewBox="0 0 512 512" fill="currentColor" class="w-full max-w-[100px] max-h-[100px] text-neutral-100 hover:scale-105 transition-transform duration-500"><path d="M325.3 234.3c-13.7 0-24.9-11.9-24.9-26.4s11.1-26.4 24.9-26.4 24.9 11.9 24.9 26.4-11.2 26.4-24.9 26.4zm-143 0c-13.7 0-24.9-11.9-24.9-26.4s11.1-26.4 24.9-26.4 24.9 11.9 24.9 26.4-11.1 26.4-24.9 26.4zm229.4-106l34.8-59c2.8-4.8 1-11-3.9-13.8-4.9-2.9-11.1-1.2-13.9 3.7l-35.3 59.8C352.4 97.4 306.9 84 256 84s-96.4 13.4-137.4 35.1L83.3 59.3c-2.9-4.8-9.1-6.5-13.9-3.7-4.9 2.8-6.6 9-3.9 13.8l34.8 59C42.8 158 4 213 4 277.6h504c0-64.6-38.8-119.6-96.3-149.3zM4 316.4h504V428c0 15.5-12.6 28-28.1 28H32.1C16.6 456 4 443.5 4 428v-111.6z"/></svg>
                        </div>
                        <div class="hidden md:flex md:col-start-3 md:col-span-1 md:row-start-3 md:row-span-1 items-center justify-center p-8 pl-12 pb-10">
                            <svg viewBox="0 0 512 512" fill="currentColor" class="w-full max-w-[100px] max-h-[100px] text-neutral-100 hover:scale-105 transition-transform duration-500"><path d="M325.3 234.3L104.6 13l280.8 161.2-60.1 60.1zM47 0C34 6.8 25.3 19.2 25.3 35.3v441.3c0 16.1 8.7 28.5 21.7 35.3l256.6-256L47 0zm425.2 225.6l-58.9-34.1-65.7 64.5 65.7 64.5 60.1-34.1c18-14.3 18-46.5-1.2-60.8zM104.6 499l280.8-161.2-60.1-60.1L104.6 499z"/></svg>
                        </div>
                        <div class="hidden md:flex md:col-start-1 md:col-span-1 md:row-start-4 md:row-span-1 items-center justify-center p-8">
                            <svg viewBox="0 0 32 32" fill="currentColor" xmlns="http://www.w3.org/2000/svg" class="w-full max-w-[100px] max-h-[100px] text-neutral-100 hover:scale-105 transition-transform duration-500">
                                <circle cx="16" cy="16" r="14" fill="currentColor"/>
                                <path d="M18.4468 8.65403C18.7494 8.12586 18.5685 7.45126 18.0428 7.14727C17.5171 6.84328 16.8456 7.02502 16.543 7.55318L16.0153 8.47442L15.4875 7.55318C15.1849 7.02502 14.5134 6.84328 13.9877 7.14727C13.462 7.45126 13.2811 8.12586 13.5837 8.65403L14.748 10.6864L11.0652 17.1149H8.09831C7.49173 17.1149 7 17.6089 7 18.2183C7 18.8277 7.49173 19.3217 8.09831 19.3217H18.4324C18.523 19.0825 18.6184 18.6721 18.5169 18.2949C18.3644 17.7279 17.8 17.1149 16.8542 17.1149H13.5997L18.4468 8.65403Z" fill="white"/>
                                <path d="M11.6364 20.5419C11.449 20.3328 11.0292 19.9987 10.661 19.8888C10.0997 19.7211 9.67413 19.8263 9.45942 19.9179L8.64132 21.346C8.33874 21.8741 8.51963 22.5487 9.04535 22.8527C9.57107 23.1567 10.2425 22.975 10.5451 22.4468L11.6364 20.5419Z" fill="white"/>
                                <path d="M22.2295 19.3217H23.9017C24.5083 19.3217 25 18.8277 25 18.2183C25 17.6089 24.5083 17.1149 23.9017 17.1149H20.9653L17.6575 11.3411C17.4118 11.5757 16.9407 12.175 16.8695 12.8545C16.778 13.728 16.9152 14.4636 17.3271 15.1839C18.7118 17.6056 20.0987 20.0262 21.4854 22.4468C21.788 22.975 22.4594 23.1567 22.9852 22.8527C23.5109 22.5487 23.6918 21.8741 23.3892 21.346L22.2295 19.3217Z" fill="white"/>
                            </svg>
                        </div>'''

for f in files:
    with open(f, 'r', encoding='utf-8') as fh:
        content = fh.read()
    if "Empty Grid Icons" not in content:
        # replace the last closing tags of the grid before pricing
        content = re.sub(r'(                        </div>\s*</div>\s*</div>\s*</div>\s*</section>)', empty_icons_html + r'\n\1', content)
        with open(f, 'w', encoding='utf-8') as fh:
            fh.write(content)
        print("Injected empty grid icons in", f)

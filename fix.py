import glob
import re
import os

files = ['tworzenie-stron.html', 'ru/razrabotka-saytov.html', 'ru/mobilnye-prilozheniya.html', 'hr/mobilne-aplikacije.html', 'en/mobile-apps.html']

def apply_fixes():
    for f in files:
        if not os.path.exists(f): continue
        with open(f, 'r', encoding='utf-8') as fh:
            content = fh.read()
        
        # update tailwind config
        old_config = r'''        tailwind.config = {
            theme: {
                extend: {
                    colors: {
                        charcoal: '#1c1c1c',
                        taupe:    '#595552',
                        cream:    '#f9f8f4',
                        sand:     '#eae8e4',
                        accent:   '#d1ccc2',
                        clay:     '#9e958a',
                    },
                    fontFamily: {
                        display: ['Manrope', 'sans-serif'],
                    },
                }
            }
        }'''
        new_config = r'''        tailwind.config = {
            theme: {
                extend: {
                    colors: {
                        charcoal: '#1c1c1c',
                        taupe:    '#595552',
                        cream:    '#f9f8f4',
                        sand:     '#eae8e4',
                        accent:   '#d1ccc2',
                        clay:     '#9e958a',
                    },
                    fontFamily: {
                        display: ['Manrope', 'sans-serif'],
                    },
                    animation: {
                        'float': 'float 6s ease-in-out infinite',
                        'breathe': 'breathe 8s ease-in-out infinite',
                        'drift': 'drift 5s ease-in-out infinite',
                    },
                    keyframes: {
                        float: {
                            '0%, 100%': { transform: 'translateY(0)' },
                            '50%': { transform: 'translateY(-10px)' },
                        },
                        breathe: {
                            '0%, 100%': { transform: 'scale(1)' },
                            '50%': { transform: 'scale(1.05)' },
                        },
                        drift: {
                            '0%, 100%': { transform: 'translate(0, 0) rotate(0deg)' },
                            '33%': { transform: 'translate(10px, -15px) rotate(3deg)' },
                            '66%': { transform: 'translate(-15px, 10px) rotate(-3deg)' },
                        }
                    }
                }
            }
        }'''
        if old_config in content:
            content = content.replace(old_config, new_config)
            
        with open(f, 'w', encoding='utf-8') as fh:
            fh.write(content)
        print("Updated config for", f)

apply_fixes()

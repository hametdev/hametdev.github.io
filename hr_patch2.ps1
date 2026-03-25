$text = [IO.File]::ReadAllText("hr/index.html", [System.Text.Encoding]::UTF8)

# Header
$text = $text.Replace('>Services<', '>Usluge<')
$text = $text.Replace('>Process<', '>Proces<')
$text = $text.Replace('>Valuation<', '>Procjena<')
$text = $text.Replace('>Let''s Talk<', '>Kontakt<')
$text = $text.Replace('px-2">PL<', 'px-2">HR<')
$text = $text.Replace('href="/" class="text-sm font-bold', 'href="/hr/" class="text-sm font-bold')

# Hero text
$text = $text.Replace('We Build <br />', 'Izrađujemo <br />')
$text = $text.Replace('id="text-cycler">Websites · Mobile Apps · AI Integrations</span>', 'id="text-cycler">Web stranice · Mobilne aplikacije · AI integracije</span>')
$text = $text.Replace('Premium web development, mobile applications, AI integration, and workflow automation. We craft digital experiences that feel natural, intuitive, and profoundly effective.', 'Izrada vrhunskih web stranica, mobilnih aplikacija i AI integracija. Stvaramo digitalna iskustva koja su prirodna, intuitivna i iznimno učinkovita.')
$text = $text.Replace('>Get Quote<', '>Zatraži ponudu<')

# Services
$text = $text.Replace('Our Expertise', 'Naša Stručnost')
$text = $text.Replace('Software development and<br class="hidden md:block" />', 'Razvoj softvera i<br class="hidden md:block" />')
$text = $text.Replace('AI tools for your company', 'AI alati za vašu tvrtku')
$text = $text.Replace('Trusted by:', 'Vjeruju nam:')
$text = $text.Replace('Websites & Web Apps', 'Web stranice i web aplikacije')
$text = $text.Replace('Mobile Apps', 'Mobilne aplikacije')
$text = $text.Replace('AI Tools', 'AI alati')

$text = $text.Replace('Stunning landing pages, complex websites, and web applications tailored to any device and business goal.', 'Privlačne landing stranice, složene web stranice i web aplikacije prilagođene svakom uređaju i poslovnom cilju.')
$text = $text.Replace('Cross-platform solutions - one app for both platforms. Fast development, testing, and publishing for iOS and Android.', 'Cross-platform rješenja – jedna aplikacija za obje platforme. Brz razvoj, testiranje i objava za iOS i Android.')
$text = $text.Replace('Integrating language models, deploying chatbots, and implementing intelligent automation tools for your workflows.', 'Integracija jezičnih modela, implementacija chatbotova i pametnih alata za automatizaciju vaših poslovnih procesa.')

$text = $text.Replace('from</span>', 'od</span>')
$text = $text.Replace('Learn more</span>', 'Saznaj više</span>')

$text = $text.Replace('Didn''t find what you''re looking for?', 'Niste pronašli ono što tražite?')
$text = $text.Replace('We''ll help regardless of the challenge. For us, nothing is impossible!', 'Pomoći ćemo vam bez obzira na izazov. Za nas ništa nije nemoguće!')
$text = $text.Replace('>Contact us<', '>Javite nam se<')

[IO.File]::WriteAllText("hr/index.html", $text, [System.Text.Encoding]::UTF8)

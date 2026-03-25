$text = [IO.File]::ReadAllText("hr/index.html", [System.Text.Encoding]::UTF8)

# SEO and Head
$text = $text.Replace('lang="en"', 'lang="hr"')
$text = $text.Replace('<link rel="canonical" href="https://hamet.agency/en/" />', '<link rel="canonical" href="https://hamet.agency/hr/" />')
$text = $text.Replace('content="Hamet Agency - We build premium websites, mobile applications, and integrate AI & automation solutions. Digital experiences engineered for growth."', 'content="Hamet Agency - Izrađujemo vrhunske web stranice, mobilne aplikacije i integriramo AI rješenja. Digitalna iskustva dizajnirana za rast vaše tvrtke."')
$text = $text.Replace('content="digital agency, web development, mobile apps, artificial intelligence, AI integration, process automation, software house"', 'content="digitalna agencija, izrada web stranica, mobilne aplikacije, umjetna inteligencija, AI integracija, automatizacija procesa, software house"')
$text = $text.Replace('content="Hamet Agency | Web Development, Mobile Apps, AI"', 'content="Hamet Agency | Izrada Web Stranica, Mobilne Aplikacije, AI"')
$text = $text.Replace('content="We craft digital experiences that feel natural, intuitive, and profoundly effective for your business growth."', 'content="Stvaramo digitalna iskustva koja su prirodna, intuitivna i iznimno učinkovita za rast vašeg poslovanja."')
$text = $text.Replace('content="en_US"', 'content="hr_HR"')
$text = $text.Replace('<title>Hamet Agency | Web, Mobile apps, AI</title>', '<title>Hamet Agency | Izrada web stranica, mobilne aplikacije i AI</title>')

# JSON LD
$text = $text.Replace('"url": "https://hamet.agency/"', '"url": "https://hamet.agency/hr/"')
$text = $text.Replace('"description": "Hamet Agency - Premium web development, mobile applications, AI integration, and workflow automation."', '"description": "Hamet Agency - Izrada vrhunskih web stranica, mobilnih aplikacija, AI integracija i automatizacija poslovanja."')
$text = $text.Replace('"priceRange": "PLN"', '"priceRange": "EUR"')

# FAQ JSON
$text = $text.Replace('"name": "How long does it take to create a website or app?"', '"name": "Koliko traje izrada web stranice ili aplikacije?"')
$text = $text.Replace('"text": "The timeline depends on project complexity. Website development usually takes up to 1 week. Developing more complex mobile and web apps takes up to 1 month."', '"text": "Rok ovisi o složenosti projekta. Izrada web stranice obično traje do 1 tjedna, a kompleksnije web i mobilne aplikacije do 1 mjeseca."')

$text = $text.Replace('"name": "Do you offer post-launch support?"', '"name": "Nudite li podršku nakon lansiranja?"')
$text = $text.Replace('"text": "Yes, we provide comprehensive technical support after launch. We ensure security updates and the stability of the created apps."', '"text": "Da, pružamo sveobuhvatnu tehničku podršku nakon lansiranja. Brinemo o sigurnosnim nadogradnjama i stabilnosti izrađenih aplikacija."')

$text = $text.Replace('"name": "How much does a mobile app or website cost?"', '"name": "Koliko košta mobilna aplikacija ili web stranica?"')
$text = $text.Replace('"text": "Our professionally built websites start from 199 €, and mobile apps from 749 €. The final cost is calculated individually based on the scope."', '"text": "Profesionalno izrađene web stranice počinju od 199 €, a mobilne aplikacije od 749 €. Konačna cijena ovisi o opsegu projekta."')

$text = $text.Replace('"name": "Do you help with AI integration in my company?"', '"name": "Pomažete li s AI integracijom u mojoj tvrtki?"')
$text = $text.Replace('"text": "Absolutely! We handle language model integration, chatbot deployment, and business process automation to save your time."', '"text": "Apsolutno! Uvodimo integraciju jezičnih modela, implementaciju chatbotova te automatizaciju poslovnih procesa kako bismo vam uštedjeli vrijeme."')

$text = $text.Replace('"name": "Do you help publish the app on Google Play and the App Store?"', '"name": "Pomažete li s objavom aplikacije na Google Playu i App Storeu?"')
$text = $text.Replace('"text": "Yes, upon the client''s request we provide the app in the leading stores: Apple App Store and Google Play. Before publishing, we also conduct necessary testing."', '"text": "Da, na zahtjev klijenta objavljujemo aplikaciju u vodećim trgovinama: Apple App Store i Google Play. Prije objave provodimo sva potrebna testiranja."')

[IO.File]::WriteAllText("hr/index.html", $text, [System.Text.Encoding]::UTF8)

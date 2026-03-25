$text = [IO.File]::ReadAllText("hr/index.html", [System.Text.Encoding]::UTF8)

# Process
$text = $text.Replace('How We Work', 'Kako Radimo')
$text = $text.Replace('From concept to launch in three steps', 'Od ideje do lansiranja u tri koraka')

$text = $text.Replace('>Discovery &amp; Quote<', '>Analiza i procjena<')
$text = $text.Replace('>Discovery & Quote<', '>Analiza i procjena<')
$text = $text.Replace('We analyze your requirements, select appropriate technologies, and precisely estimate the budget and schedule.', 'Analiziramo vaše zahtjeve, biramo odgovarajuće tehnologije te precizno procjenjujemo proračun i raspored.')
$text = $text.Replace('>Development<', '>Razvoj<')
$text = $text.Replace('We build a dedicated solution, ensuring the highest code quality and regularly consulting progress to meet your expectations.', 'Razvijamo jedinstveno rješenje, osiguravajući najvišu kvalitetu koda i redovito savjetovanje o napretku kako bismo ispunili vaša očekivanja.')
$text = $text.Replace('>Launch<', '>Lansiranje<')
$text = $text.Replace('We comprehensively deploy the finished product, configure the production environment, and ensure a stable, trouble-free start for your application.', 'Sveobuhvatno uvodimo gotov proizvod, konfiguriramo produkcijsko okruženje i osiguravamo stabilan početak bez problema za vašu aplikaciju.')

# Valuation
$text = $text.Replace('Have a specification<br>or idea?', 'Imate specifikaciju<br>ili ideju?')
$text = $text.Replace('Evaluate your project within two hours.', 'Procijenite svoj projekt unutar dva sata.')
$text = $text.Replace('Send a message directly via WhatsApp. It''s the fastest way to get a precise quote for your project.', 'Pošaljite poruku izravno putem WhatsAppa. To je najbrži način da dobijete preciznu ponudu za svoj projekt.')
$text = $text.Replace('Message us on WhatsApp...', 'Pošaljite nam poruku na WhatsApp...')
$text = $text.Replace('>or<', '>ili<')
$text = $text.Replace('Send an email inquiry', 'Pošaljite upit e-mailom')

# FAQ
$text = $text.Replace('Knowledge<', 'Znanje<')
$text = $text.Replace('Frequently Asked Questions (FAQ)', 'Često postavljana pitanja (FAQ)')

# Footer
$text = $text.Replace('Get in Touch', 'Kontaktirajte Nas')
$text = $text.Replace('Reach out to us directly to discuss your project.', 'Obratite nam se izravno kako bismo razgovorali o vašem projektu.')
$text = $text.Replace('All rights reserved.', 'Sva prava pridržana.')
$text = $text.Replace('Privacy Policy', 'Politika privatnosti')

$text = $text.Replace('Contact<', 'Kontakt<')

[IO.File]::WriteAllText("hr/index.html", $text, [System.Text.Encoding]::UTF8)

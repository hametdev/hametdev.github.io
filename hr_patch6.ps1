$text = [IO.File]::ReadAllText("hr/index.html", [System.Text.Encoding]::UTF8)

# FAQ HTML Text
$text = $text.Replace('<span>How long does it take to create a website or app?</span>', '<span>Koliko traje izrada web stranice ili aplikacije?</span>')
$text = $text.Replace('The timeline depends on project complexity. Website development usually takes up to 1 week. Developing more complex mobile and web apps takes up to 1 month.', 'Rok ovisi o složenosti projekta. Izrada web stranice obično traje do 1 tjedna, a kompleksnije web i mobilne aplikacije do 1 mjeseca.')

$text = $text.Replace('<span>Do you offer post-launch support?</span>', '<span>Nudite li podršku nakon lansiranja?</span>')
$text = $text.Replace('Yes, we provide comprehensive technical support after launch. We ensure security updates and the stability of the created apps.', 'Da, pružamo sveobuhvatnu tehničku podršku nakon lansiranja. Brinemo o sigurnosnim nadogradnjama i stabilnosti izrađenih aplikacija.')

$text = $text.Replace('<span>How much does a mobile app or website cost?</span>', '<span>Koliko košta mobilna aplikacija ili web stranica?</span>')
$text = $text.Replace('Our professionally built websites start from 199 €, and mobile apps from 749 €. The final cost is calculated individually based on the scope.', 'Profesionalno izrađene web stranice počinju od 199 €, a mobilne aplikacije od 749 €. Konačna cijena ovisi o opsegu projekta.')

$text = $text.Replace('<span>Do you help with AI integration in my company?</span>', '<span>Pomažete li s AI integracijom u mojoj tvrtki?</span>')
$text = $text.Replace('Absolutely! We handle language model integration, chatbot deployment, and business process automation to save your time.', 'Apsolutno! Uvodimo integraciju jezičnih modela, implementaciju chatbotova te automatizaciju poslovnih procesa kako bismo vam uštedjeli vrijeme.')

$text = $text.Replace('<span>Do you help publish the app on Google Play and the App Store?</span>', '<span>Pomažete li s objavom aplikacije na Google Playu i App Storeu?</span>')
$text = $text.Replace('Yes, upon the client''s request we provide the app in the leading stores: Apple App Store and Google Play. Before publishing, we also conduct necessary testing.', 'Da, na zahtjev klijenta objavljujemo aplikaciju u vodećim trgovinama: Apple App Store i Google Play. Prije objave provodimo sva potrebna testiranja.')

[IO.File]::WriteAllText("hr/index.html", $text, [System.Text.Encoding]::UTF8)

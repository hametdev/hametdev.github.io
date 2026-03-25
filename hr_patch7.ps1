$text = [IO.File]::ReadAllText("hr/index.html", [System.Text.Encoding]::UTF8)

$text = $text.Replace('Attractive landing pages, complex websites, and web applications adapted to any device and business needs.', 'Privlačne landing stranice, složene web stranice i web aplikacije prilagođene svakom uređaju i poslovnim potrebama.')
$text = $text.Replace('Cross-platform mobile solutions, one app - two platforms. Fast deployment, testing, and publishing on iOS and Android.', 'Cross-platform mobilna rješenja, jedna aplikacija za obje platforme. Brz razvoj, testiranje i objava na iOS i Android uređajima.')
$text = $text.Replace('Integration of language models, implementation of chatbots and intelligent automation tools supporting company workflows.', 'Integracija jezičnih modela, implementacija chatbotova i pametnih alata za automatizaciju koji podržavaju poslovne procese.')

[IO.File]::WriteAllText("hr/index.html", $text, [System.Text.Encoding]::UTF8)

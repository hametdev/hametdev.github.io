$text = [IO.File]::ReadAllText("hr/index.html", [System.Text.Encoding]::UTF8)

$text = $text.Replace('<link rel="alternate" hreflang="pl-PL" href="https://hamet.agency/en/" />', '<link rel="alternate" hreflang="pl-PL" href="https://hamet.agency/" />')
$text = $text.Replace('<link rel="alternate" hreflang="en" href="https://hamet.agency/en/" />', '<link rel="alternate" hreflang="en" href="https://hamet.agency/en/" />')
# wait, my previous script made hreflang="en" into hreflang="hr" because I replaced 'en' with 'hr' - ah right! Look at `<html lang="hr"` which replaced `lang="en"`. And it messed up hreflang="en" to "hr" !

$text = $text.Replace('<link rel="alternate" hreflang="hr" href="https://hamet.agency/hr/" />', '<link rel="alternate" hreflang="en" href="https://hamet.agency/en/" />')
$text = $text.Replace('<link rel="alternate" hreflang="hr" href="https://hamet.agency/en/" />', '<link rel="alternate" hreflang="en" href="https://hamet.agency/en/" />')

[IO.File]::WriteAllText("hr/index.html", $text, [System.Text.Encoding]::UTF8)

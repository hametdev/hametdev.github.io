$text = [IO.File]::ReadAllText("hr/index.html", [System.Text.Encoding]::UTF8)

# replace the entire hreflang block
$block = @"
    <link rel="canonical" href="https://hamet.agency/hr/" />
    <link rel="alternate" hreflang="pl-PL" href="https://hamet.agency/" />
    <link rel="alternate" hreflang="hr-HR" href="https://hamet.agency/hr/" />
    <link rel="alternate" hreflang="en" href="https://hamet.agency/en/" />
    <link rel="alternate" hreflang="ru" href="https://hamet.agency/ru/" />
    <link rel="alternate" hreflang="x-default" href="https://hamet.agency/en/" />
"@

$text = $text -replace '(?s)<link rel="canonical".*?href="https://hamet\.agency/en/" />', $block

# Also, language switcher at the bottom
$footerBlock = @"
<nav class="flex items-center gap-3 md:gap-4" aria-label="Languages">
                                        <a href="https://hamet.agency/en/" class="text-xs font-bold tracking-wide text-white/65 hover:text-cream transition-colors">EN</a>
                                        <a href="https://hamet.agency/" class="text-xs font-bold tracking-wide text-white/65 hover:text-cream transition-colors">PL</a>
                                        <a href="https://hamet.agency/hr/" class="text-xs font-bold tracking-wide text-white/65 hover:text-cream transition-colors">HR</a>
                                        <a href="https://hamet.agency/ru/" class="text-xs font-bold tracking-wide text-white/65 hover:text-cream transition-colors">RU</a>
                                    </nav>
"@
$text = $text -replace '(?s)<nav class="flex items-center gap-3 md:gap-4" aria-label="Languages">.*?</nav>', $footerBlock

[IO.File]::WriteAllText("hr/index.html", $text, [System.Text.Encoding]::UTF8)

$text = [IO.File]::ReadAllText('index.html', [Text.Encoding]::UTF8)
$pattern = '(?s)(<a class="nav-link[^>]+href="#faq"[\s\S]*?</a>)(\s*)(<a class="nav-link[^>]+href="#([a-zA-Z]+)"[\s\S]*?</a>)'
$text = [Regex]::Replace($text, $pattern, "$3$2$1")
[IO.File]::WriteAllText('index.html', $text, [Text.Encoding]::UTF8)

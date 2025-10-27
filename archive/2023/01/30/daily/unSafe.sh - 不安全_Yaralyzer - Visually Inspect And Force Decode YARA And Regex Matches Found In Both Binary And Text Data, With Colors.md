---
title: Yaralyzer - Visually Inspect And Force Decode YARA And Regex Matches Found In Both Binary And Text Data, With Colors
url: https://buaq.net/go-147070.html
source: unSafe.sh - 不安全
date: 2023-01-30
fetch_date: 2025-10-04T05:09:43.020391
---

# Yaralyzer - Visually Inspect And Force Decode YARA And Regex Matches Found In Both Binary And Text Data, With Colors

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/b02fc3eac2a9b5d6263ef93d05049b42.jpg)

Yaralyzer - Visually Inspect And Force Decode YARA And Regex Matches Found In Both Binary And Text Data, With Colors

Visually inspect all of the regex matches (and their sexier, more cloak and dagger cousins,
*2023-1-29 19:30:0
Author: [www.kitploit.com(查看原文)](/jump-147070.htm)
阅读量:33
收藏*

---

[![](https://blogger.googleusercontent.com/img/a/AVvXsEjAog6oWRmXKmapz7kx-IjCUpxiu1kZFqGawD_JLGEmLgU3dbwFKUYMY7SOR3oSy1N2SyEWoh-3C-JcPJI0IRxCjNa1r4KUSCHpZrQEL8F_w-O4q5T0c2qDy532zFs9d4REMcr0DTaf_IJ8whxupFrlpc0aBcg6aFYAx9JFWUpZvbMmTsO2JoK0GtdtbA=w640-h442)](https://blogger.googleusercontent.com/img/a/AVvXsEjAog6oWRmXKmapz7kx-IjCUpxiu1kZFqGawD_JLGEmLgU3dbwFKUYMY7SOR3oSy1N2SyEWoh-3C-JcPJI0IRxCjNa1r4KUSCHpZrQEL8F_w-O4q5T0c2qDy532zFs9d4REMcr0DTaf_IJ8whxupFrlpc0aBcg6aFYAx9JFWUpZvbMmTsO2JoK0GtdtbA)

Visually inspect all of the regex matches (and their sexier, more cloak and dagger cousins, the [YARA](https://github.com/VirusTotal/yara-python "YARA") matches) found in binary data and/or text. See what happens when you force various character encodings upon those matched bytes. [With colors](https://github.com/michelcrypt4d4mus/yaralyzer#example-output "With colors").

#### Quick Start

```
pipx install yaralyzer

# Scan against YARA definitions in a file:

# Scan against an arbitrary regular expression:
yaralyze --regex-pattern 'good and evil.*of\s+\w+byte' the_crypto_archipelago.exe

# Scan against an arbitrary YARA hex pattern
yaralyze --hex-pattern 'd0 93 d0 a3 d0 [-] 9b d0 90 d0 93' one_day_in_the_life_of_ivan_cryptosovich.bin
```

#### What It Do

1. **See the actual bytes your YARA rules are matching.** No more digging around copy/pasting the start positions reported by YARA into your favorite hex editor. Displays both the bytes matched by YARA as well as a configurable number of bytes before and after each match in [hexadecimal](https://www.kitploit.com/search/label/Hexadecimal "hexadecimal") and "raw" python string representation.
2. **Do the same for byte patterns and [regular expressions](https://www.kitploit.com/search/label/Regular%20Expressions "regular expressions") without writing a YARA file.** If you're too lazy to write a YARA file but are trying to determine, say, whether there's a [regular expression](https://www.kitploit.com/search/label/Regular%20Expression "regular expression") hidden somewhere in the file you could scan for the pattern `'/.+/'` and immediately get a window into all the bytes in the file that live between front slashes. Same story for quotes, BOMs, etc. Any regex YARA can handle is supported so the sky is the limit.
3. **Detect the possible encodings of each set of matched bytes.** [The `chardet` library](https://github.com/chardet/chardet "The") is a sophisticated library for guessing character encodings and it is leveraged here.
4. **Display the result of forcing various character encodings upon the matched areas.** Several default character encodings will be *forcibly* attempted in the region around the match. [`chardet`](https://github.com/chardet/chardet "Visually inspect and force decode YARA and regex matches found in both binary and text data. With Colors. (11)") will also be leveraged to see if the bytes fit the pattern of *any* known encoding. If `chardet` is confident enough (configurable), an attempt at decoding the bytes using that encoding will be displayed.
5. **Export the matched regions/decodings to SVG, HTML, and colored text files.** Show off your ASCII art.

#### Why It Do

The Yaralyzer's functionality was extracted from [The Pdfalyzer](https://github.com/michelcrypt4d4mus/pdfalyzer "The Pdfalyzer") when it became apparent that visualizing and decoding pattern matches in binaries had more utility than just in a PDF analysis tool.

[YARA](https://github.com/VirusTotal/yara-python "YARA"), for those who are unaware[1](https://github.com/michelcrypt4d4mus/yaralyzer#user-content-fn-1-07cabfeda204600d7c803b332fc4d0cd "1"), is branded as a malware analysis/alerting tool but it's actually both a lot more and a lot less than that. One way to think about it is that YARA is a regular expression matching engine on steroids. It can locate regex matches in binaries like any regex engine but it can also do far wilder things like combine regexes in logical groups, compare regexes against all 256 XORed versions of a binary, check for `base64` and other encodings of the pattern, and more. Maybe most importantly of all YARA provides a standard text based format for people to *share* their 'roided regexes with the world. All these features are particularly useful when analyzing or [reverse engineering](https://www.kitploit.com/search/label/Reverse%20Engineering "reverse engineering") malware, whose authors tend to invest a great deal of time into making stuff hard to find.

But... that's also all YARA does. Everything else is up to the user. YARA's just a match engine and if you don't know what to match (or even what character encoding you might be able to match in) it only gets you so far. I found myself a bit frustrated trying to use YARA to look at all the matches of a few critical patterns:

1. Bytes between escaped quotes (`\".+\"` and `\'.+\'`)
2. Bytes between front slashes (`/.+/`). Front slashes demarcate a regular expression in many implementations and I was trying to see if any of the bytes matching this pattern were *actually* regexes.

YARA just tells you the byte position and the matched string but it can't tell you whether those bytes are UTF-8, UTF-16, Latin-1, etc. etc. (or none of the above). I also found myself wanting to understand what was going *in the region* of the matched bytes and not just *in* the matched bytes. In other words I wanted to scope the bytes immediately before and after whatever got matched.

Enter **The Yaralyzer**, which lets you quickly scan the regions around matches while also showing you what those regions would look like if they were forced into various character encodings.

It's important to note that **The Yaralyzer** isn't a full on malware reversing tool. It can't do all the things a tool like [CyberChef](https://gchq.github.io/CyberChef/ "CyberChef") does and it doesn't try to. It's more intended to give you a quick visual overview of suspect regions in the binary so you can hone in on the areas you might want to inspect with a more serious tool like [CyberChef](https://gchq.github.io/CyberChef/ "CyberChef").

Install it with [`pipx`](https://pypa.github.io/pipx/ "Visually inspect and force decode YARA and regex matches found in both binary and text data. With Colors. (18)") or `pip3`. `pipx` is a marginally better solution as it guarantees any packages installed with it will be isolated from the rest of your local python environment. Of course if you don't really have a local python environment this is a moot point and you can feel free to install with `pip`/`pip3`.

Run `yaralyze -h` to see the [command line](https://www.kitploit.com/search/label/Command%20Line "command line") options (screenshot below).

[![](https://blogger.googleusercontent.com/img/a/AVvXsEhhTVoKs1Ynnu71NXgC9RVNhwRYw4Q_5fUW9z5qWgVMsHcCo3Zap86cn2FuVnVTp-xCRhixghl2VZA_lyCGSkevCjOWVEmzDQsN6O3OTFEXHSIl39-7Wy1MFz8lIbVInbBdIr_3SqEkM3CODltOOqZw3_bIRyogXEfAkWXTsoBCBmsY9_wcuJ1ClcFphg=w636-h640)](https://blogger.googleusercontent.com/img/a/AVvXsEhhTVoKs1Ynnu71NXgC9RVNhwRYw4Q_5fUW9z5qWgVMsHcCo3Zap86cn2FuVnVTp-xCRhixghl2VZA_lyCGSkevCjOWVEmzDQsN6O3OTFEXHSIl39-7Wy1MFz8lIbVInbBdIr_3SqEkM3CODltOOqZw3_bIRyogXEfAkWXTsoBCBmsY9_wcuJ1ClcFphg)

For info on exporting SVG images, HTML, etc., see [Example Outp...
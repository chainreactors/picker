---
title: Yara rules pageant
url: https://www.hexacorn.com/blog/2023/01/21/yara-rules-pageant/
source: Hexacorn
date: 2023-01-22
fetch_date: 2025-10-04T04:33:13.553737
---

# Yara rules pageant

[Skip to primary content](#content)

# [Hexacorn](https://www.hexacorn.com/blog/)

## Hexacorn

Search

### Main menu

* [Home](https://www.hexacorn.com/)
* [Services](https://www.hexacorn.com/services.html)
* [Products & Freebies](https://www.hexacorn.com/products_and_freebies.html)
* [Case Studies](https://www.hexacorn.com/case_studies.html)
* [Contact Us](https://www.hexacorn.com/contact.html)

### Post navigation

[← Previous](https://www.hexacorn.com/blog/2023/01/13/decrypting-shell-compiled-shc-elf-files/)
[Next →](https://www.hexacorn.com/blog/2023/01/22/excelling-at-excel-part-3/)

# Yara rules pageant

Posted on [2023-01-21](https://www.hexacorn.com/blog/2023/01/21/yara-rules-pageant/ "12:12 am")  by  [adam](https://www.hexacorn.com/blog/author/adam/ "View all posts by adam")

A few days ago I posted a very specific question on [Twitter](https://twitter.com/Hexacorn/status/1613297961189998592) and [Mastodon](https://infosec.exchange/%40hexacorn/109672869110224161):

> You’ve got gazillion of random yara rules stored inside many random .yar files scattered around many folders. What do you use to read them all, remove duplicates, ensure all rule names are unique, and all the unique rules end up in a ‘merged’ final .yar file (or files)? I am aware of these projects & gists:
> <https://github.com/plyara/plyara>
> <https://github.com/lsoumille/Yara_Merger>
> <https://gist.github.com/Neo23x0/577926e34183b4cedd76aa33f6e4dfa3>
> <https://gist.github.com/Neo23x0/81990b8e5eb351a118dca1d5f2a2a86b>
> [https://gist.github.com/notareverser/7](https://gist.github.com/notareverser/7e76c122d82ec455278640f4948a3e11)

I got 2 interesting answers:

* <https://github.com/VirusTotal/gyp>
* <https://github.com/PUNCH-Cyber/YaraGuardian>

Thanks [AllenSwackhamer](https://twitter.com/AllenSwackhamer) and [bmmaloney97](https://twitter.com/bmmaloney97)!

Still, I wanted something simpler. I just want to build a single, ‘megalopolis’ type of yara file that includes all yara rules I have ever saved.

I am a hoarder, so anytime I come across some interesting code (f.ex. c, idapython, idc, etc.), signatures and rules (flirt, yara, capa, etc.), file formats, compression, exploitation bits, bobs and PoCs, info on new attacks, any info really posted on social media, web sites, advertised via rss feeds, whatever, I just bookmark it, or download it, and I don’t really spend much time categorizing, deduplicating and organizing it. Despite many attempts over the years to make it ‘easier on me’ I always end up having it stored all over the place. I really wish I was more Marie Kondo, but it’s a mess.

I literally have a pile of different yara rules collected over last 8+ years, many of them written by me of course, all scattered across many folders, and with my aforementioned question on social media I simply wanted to achieve one thing: walk through all of these yara files, deduplicate, remove all the poor quality rules (f.ex. many PEiD rules), remove all complex rules (f.ex. where one rule depends on another), and also remove any rules related to Android malware, because I really don’t have much interest in this topic.

Many of the approaches presented by very mature projects and gists listed above focus on yara rules seen from a source code perspective. That is, you can use existing libraries to parse these yara rules, maybe calculate hashes of their bodies, and do a lot of interesting things. But then again, I wanted something simpler.

So I devised a cunning plan aka THE YARA PAGEANT ALGORITHM:

* manual step: find all yara rules on my system, copy them all to one place, use subfolders where applicable, but don’t care for duplicates, multiple versions of the same github repo, file, just drop them all in one place… it is… all okay… etc.
* now I have a single place where I have stored ALL rules I have ever collected (this is mainly to improve performance – easier to scan one directory with a script than scanning all drives)
* now I can run a script that will comb through all these yara rule files, parse them all, and extract every single atomic yara rule into a separate file; that is — if a file stores one yara rule, only one output yara rule file will be saved, but if we have a collection, we export every single unique yara rule into a separate file
* while doing so, we remove all the meta data; that is, we leave strings and/or conditions only; still, we should copy the body of the original rule into the final file, just commented out — this is not only for troubleshooting, but it also helps to preserve a crucial info about the rule — the info we will need if the rule ends up in a final ‘mega’ file and we want to understand where it came from and what other meta data info is available for it
* to ensure names do not collide, we can add a prefix in a form of f.ex. ‘h\_<counter>\_’ to every single rule name where counter increases for every single rule file written to disk
* while processing them in bulk, we can exclude many rules that rely on external information: filename, extension, or known macros f.ex. IS\_PE; who cares… it’s a small percentage, ROI is low, let’s just ditch them
* to ensure it actually works, we add a universal prologue to every single output yara file created; the prologue consists of:

```
import "console"
import "elf"
import "hash"
import "math"
import "pe"
import "dotnet"
```

This ensures all the module dependencies are resolved (except for androguard, but I ignored it ‘by design’)

* Note that it may help to use a RAM disk for this exercise!
* once we go through every single source file, we end up with a gazillion single-rule yara files
* we now use yarac to compile every single one of these yara files, yes, one by one
* we ignore these that don’t compile — it’s a small percentage of all rules
* with no metadata, many of them are just atomic detections that compile to a very specific, binary form
* once all of them are compiled, we remove all compiled files that are duplicates; that is, these where binary output of yarac is identical to a yarac output produced for another rule
* we know have a directory with a gazillion of individual yara rules, plus, for these that are unique, we also have them compiled
* for every single yara file where there exists its compiled version, we add it to the final ‘mega’ yara file
* once the ‘mega’ file is completed, we run it via yarac to create a ‘mega’ compiled version of all unique rules

That’s it.

Going forward, we simply run ‘yara -w -C <compiled mega yara file> <malware file>’ to have all these rules applied to the target file. If you have many yara files in your ‘mega’ pack you may see rules hitting on file properties, features, and if you are lucky – specific TA or malware family may sometimes hit too. It helps to use ‘-s’ argument so see the exact strings that are extracted from the sample that hit the rule so you can quickly tweak the ‘mega’ source file, recompile and avoid FPs in next runs.

I wish I could share the source code of my script and commands doing all the stuff I described above, or even my own mega yara pack. But I can’t. It’s a spaghetti code, some of the rules are super private, and in the end, your needs may be different from mine. Still, nothing can stop you from starting your own Yara pageant today…

This entry was posted in [Yara sigs](https://www.hexacorn.com/blog/category/yara-sigs/) by [adam](https://www.hexacorn.com/blog/author/adam/). Bookmark the [permalink](https://www.hexacorn.com/blog/2023/01/21/yara-rules-pageant/ "Permalink to Yara rules pageant").

[Privacy Policy](https://www.hexacorn.com/blog/privacy-policy/) [Proudly powered by WordPress](https://wordpress.org/ "Semantic Personal Publishing Platform")
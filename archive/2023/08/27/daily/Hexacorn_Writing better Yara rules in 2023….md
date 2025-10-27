---
title: Writing better Yara rules in 2023…
url: https://www.hexacorn.com/blog/2023/08/26/writing-better-yara-rules-in-2023/
source: Hexacorn
date: 2023-08-27
fetch_date: 2025-10-04T11:59:26.465440
---

# Writing better Yara rules in 2023…

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

[← Previous](https://www.hexacorn.com/blog/2023/08/25/lolbins-for-connoisseurs/)
[Next →](https://www.hexacorn.com/blog/2023/09/03/the-secret-of-961c151d2e87f2686a955a9be24d316f1362bf21/)

# Writing better Yara rules in 2023…

Posted on [2023-08-26](https://www.hexacorn.com/blog/2023/08/26/writing-better-yara-rules-in-2023/ "12:15 am")  by  [adam](https://www.hexacorn.com/blog/author/adam/ "View all posts by adam")

**Update**

This post has been featured in Josh Hammond’s [video](https://www.youtube.com/watch?v=fu71CljrxsU)! Yay, thanks Josh!

Also, you should know that there are many other great resources online focusing on Yara performance improvements, efficiency, etc. f.ex:

* <https://github.com/InQuest/awesome-yara>
* <https://engineering.avast.io/category/know-your-yara-rules/>
* <https://engineering.avast.io/yaramod-inspect-analyze-and-modify-your-yara-rules-with-ease/>
* <https://docs.google.com/presentation/d/1efe57L44WHZFJLNX2Ir-E4SOMFGK6eUzVsFiBOgOF-U/edit?usp=sharing>
* <https://help.stairwell.com/en/knowledge/what-are-yara-rule-best-practices>
* <https://github.com/nbareil/yara-dedup>

**Old Post**

In my [previous post](https://www.hexacorn.com/blog/2023/01/21/yara-rules-pageant/) I mused about an impossible task – how to consolidate a large, unorganized yara ruleset (that lots of us, admittedly, collect and hoard – just downloading it all, randomly, from all the corners of the internet w/o much thinking…) into a single, monolith, ready-to-use-for-a-quick-triage yara rule set…

Trust me: it’s not easy, but still doable, and in my previous post I kinda outlined a process that extracts, isolates and classifies each rule one by one, so that once they are all in separate files, we strip their metadata, deduplicate them, check their syntax for errors, find hidden duplicates (via compilation), and finally merge the surviving ones into a one, gigantic rule set that can be used directly with yara.exe (or compiled with yarac.exe for faster processing).

Yup, it’s not perfect, but this is one of these “it kinda worked for me” situations…

Since my last post I made lots of improvements to that idea and I can now painlessly merge any set of random yara rules with a minimal manual input, but with a caveat that I brutally ditch many of the ‘bad rules’ ‘in the process’… It’s their authors’ fault though 😉 Yup, I am serious – if your rule is kinda over-engineered – no one wants it, and this is why I also kill it at source cuz I don’t want it either 😉

Anyway… this post is not about automation. It’s about quality. A subject close to my heart, because this is my second post on yara rule writing ‘best practices’ – the first one was a disaster, because I was wrong on many fronts, and was corrected by the actual Yara devs… It was an eye-opening experience, for sure. That old post – I took it down.

And I do hope this post will be a bit better!

Reviewing many Yara rules written by others is a great researching adventure… You learn a lot not only about various optimization tricks, but also Yara syntax that you were not even aware existed… And yes, nothing works better for learning than a corpora of good examples… You can RTFM all day long and then someone breaks the rules (sic!) and uses the language syntax in a way no one ever thought of before… And yes, looking at all these rules you find mistakes too 🙂 Not only bad strings, but also wrong assumptions, bad copypasta, and sometimes a certain level of laziness…

So, let’s cover a few things that I learned from eyeballing of these 40K+ yara rules:

* ditch PEiD-based yara rules – they are truly obsolete in 2023 and many of them are simply naive; also, 32-bit packers and protectors prevalent in 1990s and 2000s are not interesting anymore
* ditch file properties and feature extraction-oriented rules – better tools exist today f.ex. [DiE](https://github.com/horsicq/Detect-It-Easy), [capa](https://github.com/mandiant/capa); detecting that a file is a PE, PE.NET, ELF, MSI or DOC/X, or XLS/X via yara is simply NOT the best use of yara and IT IS AN ALREADY SOLVED PROBLEM on a modular level (see f.ex. *dotnet.is\_dotnet* discussion below)
* separate specific (client-specific, scope-specific, threat actor-specific, etc) and generic rules – the generic ones may be useful for scoped DFIR/loose triage/sweeps, or targeted VM assessment engagements, but you don’t want these FP-prone rules to be used on every ‘light’ scan across the fleet of many endpoints, and for many customers; there simply is a really high cost associated with reviewing results of many of these wishy-washy ‘detections’, and I guarantee you – you will find a lot of results… nowadays many DF/IR companies rely on yara-based scanners for their triage activities and trust me, reviewing the results that these tools produce is a very time-consuming task — notably, most of the hits are False Positives
* separate public rules you want to share and private rules you want to keep to yourself
* separate in-memory and file-specific yara rules; memory-only rules are great, but when ran against a file system, even on a clean installation of Windows 10 or 11 they may produce FPs; I have seen that happening; and then you have your TEMP and CACHE directories of your browsers; they will store snapshots of pages including websites/blogs/social media pages hosted by security vendors, yourself, etc. and if there is no file-specific conditions in your yara rule, you will get hits (FPs!); last, but not least – if your yara rule hits on itself, it is probably not a good yara rule at all, so add this self-check to your test routine!
* ditch rules dependent on other rules – it’s really hard to process these in bulk; to merge these with a larger yara rules corpora w/o breaking something is impossible; yara rule dependencies are nothing but a fancy-pantsy show-off of one’s skillset, and – while they will surely find some local appeal – the moment you share them widely… such monstrosities will surely break many yara rules aggregating builds… that is – simple is BETTER, use KISS principle and avoid nesting conditions
* keep rules high-fidelity, as much as you can…
* but then again, for DFIR, Threat Hunting/Triage, and often incident-, or even client-, or scope-specific rules, keep them very wide-open and allow low-fidelity, if needed – in such cases it is actually acceptable and welcome, because the scope and objective is different… I must confess I literally wrote a very controversial yara rule for a very specific APT case — it was then published online and all hell broke loose when people started b\*g about its quality; I still stand by it though, it was a beautiful example of a targeted yara rule that was detecting ‘surgical’ patches to a code introducing a skeleton key functionality to a logon request processing binary – it was horrendous on a grand scheme of things though, so it would produce a lot of FPs if you wanted to use it in retroscans on VT, but on systems of interest — it was detecting patches beautifully, and with 100% accuracy
* if you can, keep a list of sample hashes you used for writing the rule inside the rule meta section; your internal QC process can use them for verification, and… you can also use an external QC process relying on [yara-ci](https://yara-ci.cloud.virustotal.com/) that can extract these for automated QC…; it takes care of both False Positives (via NSRL set) and False Negatives (via hashes you pass in the meta data)
* having said that, remember that I [exposed the NSRL set](https://www.hexacorn.com/blog/2022/02/04/analysing-nsrl-d...
---
title: Beyond good ol’ Run key, Part 141
url: https://www.hexacorn.com/blog/2023/02/25/beyond-good-ol-run-key-part-141/
source: Hexacorn
date: 2023-02-26
fetch_date: 2025-10-04T08:08:31.681900
---

# Beyond good ol’ Run key, Part 141

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

[← Previous](https://www.hexacorn.com/blog/2023/01/22/excelling-at-excel-part-3/)
[Next →](https://www.hexacorn.com/blog/2023/03/10/threat-hunting-localization-issues/)

# Beyond good ol’ Run key, Part 141

Posted on [2023-02-25](https://www.hexacorn.com/blog/2023/02/25/beyond-good-ol-run-key-part-141/ "11:55 pm")  by  [adam](https://www.hexacorn.com/blog/author/adam/ "View all posts by adam")

In my recent post on [Mastodon](https://infosec.exchange/%40hexacorn/109916851629026779) I asked if there is any repo of Shadowpad side-loading combos. I asked, because long time ago I have created one for [PlugX](https://www.hexacorn.com/blog/2016/03/10/beyond-good-ol-run-key-part-36), and was hoping that maybe there is one for Shadowpad that I am not aware of.

I was aware of two existing combos at the time of posting, but [googling around](https://blog.polyswarm.io/wicked-pandas-shadowpad-rat) I found [some more](https://www.secureworks.com/research/shadowpad-malware-analysis).

Here they are:

* AppLaunch.exe (Microsoft) [[source]](https://www.secureworks.com/research/shadowpad-malware-analysis)
  + mscoree.dll
* hpqhvind.exe (Hewlett Packard) [[source]](https://www.welivesecurity.com/2020/01/31/winnti-group-targeting-universities-hong-kong/)
  + hpqhvsei.dll
* consent.exe (Microsoft) [[source]](https://www.secureworks.com/research/shadowpad-malware-analysis)
  + secur32.dll
    - secur32.dll.dat
* TosBtKbd.exe (Toshiba) [[source]](https://www.secureworks.com/research/shadowpad-malware-analysis)
  + tosbtkbd.dll
* BDReinit.exe (BitDefender) [[source]](https://www.secureworks.com/research/shadowpad-malware-analysis)
  + log.dll
    - log.dll.dat
* Oleview.exe (Microsoft) [[source]](https://www.secureworks.com/research/shadowpad-malware-analysis)
  + iviewers.dll
    - iviewers.dll.dat
* RasTls.exe [[source]](https://st.drweb.com/static/new-www/news/2020/october/Study_of_the_ShadowPad_APT_backdoor_and_its_relation_to_PlugX_en.pdf)
  + RasTls.dll (thx [@fe7ch](https://twitter.com/fe7ch))
    - RasTls.dat

This entry was posted in [Autostart (Persistence)](https://www.hexacorn.com/blog/category/autostart-persistence/) by [adam](https://www.hexacorn.com/blog/author/adam/). Bookmark the [permalink](https://www.hexacorn.com/blog/2023/02/25/beyond-good-ol-run-key-part-141/ "Permalink to Beyond good ol’ Run key, Part 141").

[Privacy Policy](https://www.hexacorn.com/blog/privacy-policy/) [Proudly powered by WordPress](https://wordpress.org/ "Semantic Personal Publishing Platform")
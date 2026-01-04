---
title: Beyond good ol’ Run key, Part 155
url: https://www.hexacorn.com/blog/2026/01/03/beyond-good-ol-run-key-part-155/
source: Hexacorn
date: 2026-01-03
fetch_date: 2026-01-04T03:37:05.970020
---

# Beyond good ol’ Run key, Part 155

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

[← Previous](https://www.hexacorn.com/blog/2026/01/02/beyond-good-ol-run-key-part-154/)
[Next →](https://www.hexacorn.com/blog/2026/01/03/beyond-good-ol-run-key-part-156/)

# Beyond good ol’ Run key, Part 155

Posted on [2026-01-03](https://www.hexacorn.com/blog/2026/01/03/beyond-good-ol-run-key-part-155/ "8:08 pm")  by  [adam](https://www.hexacorn.com/blog/author/adam/ "View all posts by adam")

Leveraging popular software for persistence is a clever way to survive in heavily monitored environments of today. The last post discussed GhostScript, and today I will cover a popular gaming platform called GOG.

Games using GOG use HKLM Registry configuration stored under keys listed below (this is a representative subset, obviously):

* SOFTWARE\GOG.com\Games\1207662533
* SOFTWARE\GOG.com\Games\1207664543
* SOFTWARE\GOG.COM\Games\1207664623
* SOFTWARE\GOG.com\Games\1207665673
* SOFTWARE\GOG.COM\GOGADVENTURESSHUGGY
* SOFTWARE\GOG.COM\GOGANODYNE
* SOFTWARE\GOG.COM\GOGDARKLANDS
* SOFTWARE\GOG.COM\GOGEARTH2140D
* SOFTWARE\GOG.COM\GOGGOBLINS1
* SOFTWARE\GOG.COM\GOGGOBLINS1FDD
* SOFTWARE\GOG.COM\GOGGOBLINS2
* SOFTWARE\GOG.COM\GOGGOBLINS2FDD
* SOFTWARE\GOG.COM\GOGGOBLINS3
* SOFTWARE\GOG.COM\GOGGOBLINS3FDD
* SOFTWARE\GOG.COM\GOGINTERSTATE82
* SOFTWARE\GOG.COM\GOGLAMULANA
* SOFTWARE\GOG.COM\GOGRETURNTOKRONDOR
* SOFTWARE\GOG.COM\GOGT7G

The thing is, that under these keys, there is a Registry ValueName called GOGGAMEDLL that points to a GOG DLL – and as you suspect, this entry can be potentially replaced by a proxy DLL.

This entry was posted in [Autostart (Persistence)](https://www.hexacorn.com/blog/category/autostart-persistence/) by [adam](https://www.hexacorn.com/blog/author/adam/). Bookmark the [permalink](https://www.hexacorn.com/blog/2026/01/03/beyond-good-ol-run-key-part-155/ "Permalink to Beyond good ol’ Run key, Part 155").

[Privacy Policy](https://www.hexacorn.com/blog/privacy-policy/) [Proudly powered by WordPress](https://wordpress.org/ "Semantic Personal Publishing Platform")
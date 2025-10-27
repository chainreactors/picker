---
title: Beyond good ol’ Run key, Part 144
url: https://www.hexacorn.com/blog/2024/11/15/beyond-good-ol-run-key-part-144/
source: Hexacorn
date: 2024-11-16
fetch_date: 2025-10-06T19:16:41.931566
---

# Beyond good ol’ Run key, Part 144

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

[← Previous](https://www.hexacorn.com/blog/2024/11/09/the-different-type-of-relocation-aka-moving-between-countries-in-practice-1-n/)
[Next →](https://www.hexacorn.com/blog/2024/11/16/adobefips-adobe-reader-lolbin/)

# Beyond good ol’ Run key, Part 144

Posted on [2024-11-15](https://www.hexacorn.com/blog/2024/11/15/beyond-good-ol-run-key-part-144/ "10:16 pm")  by  [adam](https://www.hexacorn.com/blog/author/adam/ "View all posts by adam")

The Acrobat Reader is a very popular software installed on millions of computers worldwide.

Today I noticed that anytime AcroRd32.exe program starts (tested with the latest version 24.4) it checks the following folder:

```
c:\Program Files (x86)\Adobe\Acrobat Reader DC\Reader\plug_ins\Test_Tools\
```

looking for \*.api files.

All these files are then loaded as DLLs.

The screenshot below shows what happens when the following 3 files are present in the aforementioned folder:

* aaFEAT.api
* Automation.api
* malware.api

[![](https://www.hexacorn.com/blog/wp-content/uploads/2024/11/acrobat_reader_api.png)](https://www.hexacorn.com/blog/wp-content/uploads/2024/11/acrobat_reader_api.png)

The first two are named like the two legitimate \*.api files that Acrobat Reader expects to find in the *Test\_Tools* folder. The last one is just a randomly (well, not really) named DLL to show that any \*.api file dropped there will be executed…

This entry was posted in [Autostart (Persistence)](https://www.hexacorn.com/blog/category/autostart-persistence/) by [adam](https://www.hexacorn.com/blog/author/adam/). Bookmark the [permalink](https://www.hexacorn.com/blog/2024/11/15/beyond-good-ol-run-key-part-144/ "Permalink to Beyond good ol’ Run key, Part 144").

[Privacy Policy](https://www.hexacorn.com/blog/privacy-policy/) [Proudly powered by WordPress](https://wordpress.org/ "Semantic Personal Publishing Platform")
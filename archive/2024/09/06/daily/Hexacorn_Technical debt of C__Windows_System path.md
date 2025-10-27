---
title: Technical debt of C:\Windows\System path
url: https://www.hexacorn.com/blog/2024/09/05/technical-debt-of-cwindowssystem-path/
source: Hexacorn
date: 2024-09-06
fetch_date: 2025-10-06T18:26:50.971809
---

# Technical debt of C:\Windows\System path

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

[← Previous](https://www.hexacorn.com/blog/2024/09/04/rundll32-and-phantom-dll-lolbins-32-bit-version/)
[Next →](https://www.hexacorn.com/blog/2024/09/05/the-art-of-overdlloading/)

# Technical debt of C:\Windows\System path

Posted on [2024-09-05](https://www.hexacorn.com/blog/2024/09/05/technical-debt-of-cwindowssystem-path/ "9:09 pm")  by  [adam](https://www.hexacorn.com/blog/author/adam/ "View all posts by adam")

Thanks to [@sixtyvividtails](https://x.com/sixtyvividtails) who corrected a mistake I made in the earlier version of the post

**Updated post**

One of a less known paths that is being searched when the libraries are loaded is C:\Windows\System.

Anytime the search for a library kicks off, the following system directories are being searched:

* C:\Windows\System32\
* C:\Windows\System\

We can clearly see this in Procmon when we try to test the POC from my post about *[UpdateAPI.dll](https://www.hexacorn.com/blog/2024/09/03/rundll32-and-phantom-dll-lolbins/)*:

[![](https://www.hexacorn.com/blog/wp-content/uploads/2024/09/windows_system.png)](https://www.hexacorn.com/blog/wp-content/uploads/2024/09/windows_system.png)

So, that old 16-bit legacy path is still there, even if practically no one is using it today. As such, we can use this path to drop at least some of the payloads there.

This entry was posted in [Anti-Forensics](https://www.hexacorn.com/blog/category/anti-forensics/), [Archaeology](https://www.hexacorn.com/blog/category/archaeology/), [Living off the land](https://www.hexacorn.com/blog/category/living-off-the-land/) by [adam](https://www.hexacorn.com/blog/author/adam/). Bookmark the [permalink](https://www.hexacorn.com/blog/2024/09/05/technical-debt-of-cwindowssystem-path/ "Permalink to Technical debt of C:\Windows\System path").

[Privacy Policy](https://www.hexacorn.com/blog/privacy-policy/) [Proudly powered by WordPress](https://wordpress.org/ "Semantic Personal Publishing Platform")
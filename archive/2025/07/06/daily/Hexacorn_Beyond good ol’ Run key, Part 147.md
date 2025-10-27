---
title: Beyond good ol’ Run key, Part 147
url: https://www.hexacorn.com/blog/2025/07/05/beyond-good-ol-run-key-part-147/
source: Hexacorn
date: 2025-07-06
fetch_date: 2025-10-06T23:26:08.987631
---

# Beyond good ol’ Run key, Part 147

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

[← Previous](https://www.hexacorn.com/blog/2025/06/15/vmwareresolutionset-exe-vmwareresolutionset-dll-lolbin/)
[Next →](https://www.hexacorn.com/blog/2025/07/05/beyond-good-ol-run-key-part-148/)

# Beyond good ol’ Run key, Part 147

Posted on [2025-07-05](https://www.hexacorn.com/blog/2025/07/05/beyond-good-ol-run-key-part-147/ "11:26 pm")  by  [adam](https://www.hexacorn.com/blog/author/adam/ "View all posts by adam")

I mentioned [TestHook](https://www.hexacorn.com/blog/2020/12/02/testhooks-take-2/) at least [twice](https://www.hexacorn.com/blog/2020/09/06/beyond-good-ol-run-key-part-127-testhooks-bonus/) in the past. I actually love this keyword/string, because it is associated with many undocumented internal Microsoft test frameworks that we can sometimes abuse. And many ‘TestHook’ string references are present in many binaries belonging to both Server an Desktop versions of Windows, hence a lot of research opportunities await…

And here’s one of them:

Adding an entry below:

```
HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Diagnostics\DiagTrack\TestHooks\TestAggregatorDll=<malware>
```

will result in the DLL of our choice being loaded when the system starts.

[![](https://www.hexacorn.com/blog/wp-content/uploads/2025/07/TestAggregatorDll.png)](https://www.hexacorn.com/blog/wp-content/uploads/2025/07/TestAggregatorDll.png)

This entry was posted in [Autostart (Persistence)](https://www.hexacorn.com/blog/category/autostart-persistence/) by [adam](https://www.hexacorn.com/blog/author/adam/). Bookmark the [permalink](https://www.hexacorn.com/blog/2025/07/05/beyond-good-ol-run-key-part-147/ "Permalink to Beyond good ol’ Run key, Part 147").

[Privacy Policy](https://www.hexacorn.com/blog/privacy-policy/) [Proudly powered by WordPress](https://wordpress.org/ "Semantic Personal Publishing Platform")
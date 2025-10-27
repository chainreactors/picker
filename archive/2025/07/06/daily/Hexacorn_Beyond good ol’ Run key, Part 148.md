---
title: Beyond good ol’ Run key, Part 148
url: https://www.hexacorn.com/blog/2025/07/05/beyond-good-ol-run-key-part-148/
source: Hexacorn
date: 2025-07-06
fetch_date: 2025-10-06T23:26:03.085377
---

# Beyond good ol’ Run key, Part 148

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

[← Previous](https://www.hexacorn.com/blog/2025/07/05/beyond-good-ol-run-key-part-147/)
[Next →](https://www.hexacorn.com/blog/2025/07/11/beyond-good-ol-run-key-part-149/)

# Beyond good ol’ Run key, Part 148

Posted on [2025-07-05](https://www.hexacorn.com/blog/2025/07/05/beyond-good-ol-run-key-part-148/ "11:44 pm")  by  [adam](https://www.hexacorn.com/blog/author/adam/ "View all posts by adam")

Analyzing the very same binary (*AggregatorHost.exe*) that makes the persistence trick described in my previous post work, I noticed that there is one more Registry entry we can use as a persistence mechanism:

```
HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Diagnostics\DiagTrack\TestHooks\TestUndockedAggregatorDll=<malware>
```

Same as in the previous post, it loads with a system start.

This entry was posted in [Autostart (Persistence)](https://www.hexacorn.com/blog/category/autostart-persistence/) by [adam](https://www.hexacorn.com/blog/author/adam/). Bookmark the [permalink](https://www.hexacorn.com/blog/2025/07/05/beyond-good-ol-run-key-part-148/ "Permalink to Beyond good ol’ Run key, Part 148").

[Privacy Policy](https://www.hexacorn.com/blog/privacy-policy/) [Proudly powered by WordPress](https://wordpress.org/ "Semantic Personal Publishing Platform")
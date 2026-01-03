---
title: Beyond good ol’ Run key, Part 154
url: https://www.hexacorn.com/blog/2026/01/02/beyond-good-ol-run-key-part-154/
source: Hexacorn
date: 2026-01-02
fetch_date: 2026-01-03T03:22:16.506022
---

# Beyond good ol’ Run key, Part 154

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

[← Previous](https://www.hexacorn.com/blog/2025/12/31/beyond-good-ol-run-key-part-152/)

# Beyond good ol’ Run key, Part 154

Posted on [2026-01-02](https://www.hexacorn.com/blog/2026/01/02/beyond-good-ol-run-key-part-154/ "2:07 pm")  by  [adam](https://www.hexacorn.com/blog/author/adam/ "View all posts by adam")

In this series I describe a lot of Windows persistence mechanisms. Most of them are ‘native’ to the OS, but I sometimes cover opportunities offered by popular software too. Today’s case is one of these.

[Ghostscript](https://en.wikipedia.org/wiki/Ghostscript) is a superpopular:

> suite of software based on an interpreter for Adobe Systems’ PostScript and Portable Document Format (PDF) page description languages

that can be found installed on many Windows endpoints today. It is often being installed as a dependent component supporting a lot of various applications, including PDF software, games, etc.

What we can find as particularly interesting from a persistence standpoint, is this Registry entry:

```
(HKCU|HKLM)\Software\GPL Ghostscript\<version>\GS_DLL=<DLL library>
```

Any software relying on Ghostscript will eventually refer to it, and load the DLL this entry points to. As such, it can be leveraged for persistence (proxy DLL).

This mechanism is described in detail [here](https://ghostscript.readthedocs.io/en/latest/Install.html).

If you read the linked article, you will notice that there is an alternative way to set the value of GS\_DLL by using the environmental variable. This feature can be abused for both persistence and lolbin activities.

This entry was posted in [Autostart (Persistence)](https://www.hexacorn.com/blog/category/autostart-persistence/), [LOLBins](https://www.hexacorn.com/blog/category/living-off-the-land/lolbins/) by [adam](https://www.hexacorn.com/blog/author/adam/). Bookmark the [permalink](https://www.hexacorn.com/blog/2026/01/02/beyond-good-ol-run-key-part-154/ "Permalink to Beyond good ol’ Run key, Part 154").

[Privacy Policy](https://www.hexacorn.com/blog/privacy-policy/) [Proudly powered by WordPress](https://wordpress.org/ "Semantic Personal Publishing Platform")
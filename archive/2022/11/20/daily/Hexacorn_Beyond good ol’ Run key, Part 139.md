---
title: Beyond good ol’ Run key, Part 139
url: https://www.hexacorn.com/blog/2022/11/19/beyond-good-ol-run-key-part-139/
source: Hexacorn
date: 2022-11-20
fetch_date: 2025-10-03T23:17:09.824261
---

# Beyond good ol’ Run key, Part 139

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

[← Previous](https://www.hexacorn.com/blog/2022/10/08/dealing-with-alert-fatigue-part-2/)
[Next →](https://www.hexacorn.com/blog/2022/11/19/cracking-zeppelin/)

# Beyond good ol’ Run key, Part 139

Posted on [2022-11-19](https://www.hexacorn.com/blog/2022/11/19/beyond-good-ol-run-key-part-139/ "10:53 pm")  by  [adam](https://www.hexacorn.com/blog/author/adam/ "View all posts by adam")

This one is a curious one. I actually don’t know how to trigger it!

Yet, I will document some bits and bobs, so that you may take these entry points into consideration, at least from a DFIR perspective.

So, *edgehtml.dll* and *mshtml.dll* are monsters of a library (23-25MB+). One of the things they do is they provide functions that work in so-called Diagnostic Mode. When Browser is in that mode, it checks a number of environment variables, and if they are set, it will load a COM library specified by one of these entries (JS\_DM\_CLSID).

And all these Java Script/Diagnostic Mode environment variables it checks are:

* JS\_DM\_CLSID
* JS\_DM\_FLAGS
* JS\_DM\_PATH
* JS\_DM\_ID

I know it’s not a lot, but if JS\_DM\_CLSID is set as an environmental variable, you better check it’s value as it may be loaded by the browser. If you know more about the Diagnostic Mode, please let me know.

This entry was posted in [Autostart (Persistence)](https://www.hexacorn.com/blog/category/autostart-persistence/) by [adam](https://www.hexacorn.com/blog/author/adam/). Bookmark the [permalink](https://www.hexacorn.com/blog/2022/11/19/beyond-good-ol-run-key-part-139/ "Permalink to Beyond good ol’ Run key, Part 139").

[Privacy Policy](https://www.hexacorn.com/blog/privacy-policy/) [Proudly powered by WordPress](https://wordpress.org/ "Semantic Personal Publishing Platform")
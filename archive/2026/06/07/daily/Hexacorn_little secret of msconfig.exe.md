---
title: little secret of msconfig.exe
url: https://www.hexacorn.com/blog/2026/06/07/little-secret-of-msconfig-exe/
source: Hexacorn
date: 2026-06-07
fetch_date: 2026-06-08T06:32:42.316950
---

# little secret of msconfig.exe

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

[← Previous](https://www.hexacorn.com/blog/2026/05/06/1-little-known-secret-of-forfiles-exe-part-2/)

# little secret of msconfig.exe

Posted on [2026-06-07](https://www.hexacorn.com/blog/2026/06/07/little-secret-of-msconfig-exe/ "12:41 am")  by  [adam](https://www.hexacorn.com/blog/author/adam/ "View all posts by adam")

This post doesn’t include anything ground breaking, but is just yet another attempt to describe/document less-known command line arguments of many known, often native to the platform, Windows programs.

When you launch msconfig.exe it shows a well-known configuration dialog box:

[![](https://www.hexacorn.com/blog/wp-content/uploads/2026/06/msconfig1.png)](https://www.hexacorn.com/blog/wp-content/uploads/2026/06/msconfig1.png)

It turns out the program accepts less-known command line arguments f.ex.:

* -/auto

[![](https://www.hexacorn.com/blog/wp-content/uploads/2026/06/msconfig_auto.png)](https://www.hexacorn.com/blog/wp-content/uploads/2026/06/msconfig_auto.png)

* -/basic – seems to be selecting some GUI controls on UI, but need to explore more
* -/commit <number> – where <number> is a tab on the GUI shown above
* 1 = General
  + no action is taken
* 2 = Boot

[![](https://www.hexacorn.com/blog/wp-content/uploads/2026/06/msconfig_boot.png)](https://www.hexacorn.com/blog/wp-content/uploads/2026/06/msconfig_boot.png)

* 3 = Services

[![](https://www.hexacorn.com/blog/wp-content/uploads/2026/06/msconfig_services.png)](https://www.hexacorn.com/blog/wp-content/uploads/2026/06/msconfig_services.png)

* 4 = Startup

[![](https://www.hexacorn.com/blog/wp-content/uploads/2026/06/msconfig_startup.png)](https://www.hexacorn.com/blog/wp-content/uploads/2026/06/msconfig_startup.png)

All these options make the program write some Registry settings that don’t seem to be too important per se.

For example,

```
msconfig /commit 2
```

writes

```
HKLM\SOFTWARE\Microsoft\Shared Tools\MSConfig\state\bootini = 0
```

to Registry. It’s not really that interesting.

Still, worth documenting.

This entry was posted in [little known secrets](https://www.hexacorn.com/blog/category/little-known-secrets/) by [adam](https://www.hexacorn.com/blog/author/adam/). Bookmark the [permalink](https://www.hexacorn.com/blog/2026/06/07/little-secret-of-msconfig-exe/ "Permalink to little secret of msconfig.exe").

[Privacy Policy](https://www.hexacorn.com/blog/privacy-policy/) [Proudly powered by WordPress](https://wordpress.org/ "Semantic Personal Publishing Platform")
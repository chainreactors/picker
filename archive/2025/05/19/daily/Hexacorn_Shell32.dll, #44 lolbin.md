---
title: Shell32.dll, #44 lolbin
url: https://www.hexacorn.com/blog/2025/05/18/shell32-dll-44-lolbin/
source: Hexacorn
date: 2025-05-19
fetch_date: 2025-10-06T22:26:17.189906
---

# Shell32.dll, #44 lolbin

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

[← Previous](https://www.hexacorn.com/blog/2025/05/02/minority-forensic-report-aka-defending-forward-w-o-hacking-back/)
[Next →](https://www.hexacorn.com/blog/2025/05/30/shell32-dll-61/)

# Shell32.dll, #44 lolbin

Posted on [2025-05-18](https://www.hexacorn.com/blog/2025/05/18/shell32-dll-44-lolbin/ "12:51 am")  by  [adam](https://www.hexacorn.com/blog/author/adam/ "View all posts by adam")

There is a well known shell32.dll lolbas that relies on a function called [Control\_RunDLL](https://lolbas-project.github.io/lolbas/Libraries/Shell32/). BUT, there is one more. The shell32.dll library exports a function called Control\_RunDLLNoFallback under ordinal #44.

We can use it to launch CPL files using the syntax below:

```
"C:\windows\SysWOW64\rundll32.exe" "C:\windows\SysWOW64\shell32.dll",#44 "<localpath>.cpl"
```

I didn’t discover this technique – it was observed being used by various malware families including RaspberryRobin.

This entry was posted in [Living off the land](https://www.hexacorn.com/blog/category/living-off-the-land/), [LOLBins](https://www.hexacorn.com/blog/category/living-off-the-land/lolbins/) by [adam](https://www.hexacorn.com/blog/author/adam/). Bookmark the [permalink](https://www.hexacorn.com/blog/2025/05/18/shell32-dll-44-lolbin/ "Permalink to Shell32.dll, #44 lolbin").

[Privacy Policy](https://www.hexacorn.com/blog/privacy-policy/) [Proudly powered by WordPress](https://wordpress.org/ "Semantic Personal Publishing Platform")
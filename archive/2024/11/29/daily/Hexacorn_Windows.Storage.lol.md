---
title: Windows.Storage.lol
url: https://www.hexacorn.com/blog/2024/11/28/windows-storage-lol/
source: Hexacorn
date: 2024-11-29
fetch_date: 2025-10-06T19:16:59.758035
---

# Windows.Storage.lol

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

[← Previous](https://www.hexacorn.com/blog/2024/11/28/browsing-the-browsers/)
[Next →](https://www.hexacorn.com/blog/2024/11/29/mapping-the-api-mapping-code-redundancy/)

# Windows.Storage.lol

Posted on [2024-11-28](https://www.hexacorn.com/blog/2024/11/28/windows-storage-lol/ "10:28 pm")  by  [adam](https://www.hexacorn.com/blog/author/adam/ "View all posts by adam")

This is a bit surprising, but the recent versions of *windows.storage.dll* export a number of functions identical with *shell32.dll*. In fact, *shell32.dll* imports these *windows.storage.dll* functions and is basically forwarding the execution to them, and just acting as a proxy.

Thanks to that, one can now call some of the *shell32.dll* functions directly from *windows.storage.dll*, f.ex. this well-known lolbin:

```
rundll32 c:\WINDOWS\system32\shell32.dll, ShellExec_RunDLL calc.exe
```

can be converted to:

```
rundll32 c:\WINDOWS\system32\windows.storage.dll, ShellExec_RunDLL calc.exe
```

This entry was posted in [Living off the land](https://www.hexacorn.com/blog/category/living-off-the-land/), [LOLBins](https://www.hexacorn.com/blog/category/living-off-the-land/lolbins/) by [adam](https://www.hexacorn.com/blog/author/adam/). Bookmark the [permalink](https://www.hexacorn.com/blog/2024/11/28/windows-storage-lol/ "Permalink to Windows.Storage.lol").

[Privacy Policy](https://www.hexacorn.com/blog/privacy-policy/) [Proudly powered by WordPress](https://wordpress.org/ "Semantic Personal Publishing Platform")
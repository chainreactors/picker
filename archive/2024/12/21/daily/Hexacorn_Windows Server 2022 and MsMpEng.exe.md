---
title: Windows Server 2022 and MsMpEng.exe
url: https://www.hexacorn.com/blog/2024/12/20/windows-server-2022-and-msmpeng-exe/
source: Hexacorn
date: 2024-12-21
fetch_date: 2025-10-06T19:36:57.427399
---

# Windows Server 2022 and MsMpEng.exe

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

[← Previous](https://www.hexacorn.com/blog/2024/12/15/dns-exe-and-its-quirks/)
[Next →](https://www.hexacorn.com/blog/2024/12/20/beyond-good-ol-run-key-part-145/)

# Windows Server 2022 and MsMpEng.exe

Posted on [2024-12-20](https://www.hexacorn.com/blog/2024/12/20/windows-server-2022-and-msmpeng-exe/ "12:28 am")  by  [adam](https://www.hexacorn.com/blog/author/adam/ "View all posts by adam")

Running Procmon in a boot mode is a very powerful research tool. In this short post I want to share a Procmon boot log of *MsMpEng.exe* (Windows Defender process) where we clearly see it is attempting to access a lot of (assumed bad) file names and paths.

I have not seen this documented before and I am a bit surprised, because the Windows Defender signatures are easily decompilable thanks to projects like [WDExtract](https://github.com/hfiref0x/WDExtract) and [MpLua converter](https://github.com/commial/experiments/tree/master/windows-defender/lua). Google searches for the file names presented in my boot log return nada.

So, here it is. A [list](https://hexacorn.com/d/MsMpEng.exe.txt) of paths that are most likely \_bad\_ for business.

This entry was posted in [Archaeology](https://www.hexacorn.com/blog/category/archaeology/) by [adam](https://www.hexacorn.com/blog/author/adam/). Bookmark the [permalink](https://www.hexacorn.com/blog/2024/12/20/windows-server-2022-and-msmpeng-exe/ "Permalink to Windows Server 2022 and MsMpEng.exe").

[Privacy Policy](https://www.hexacorn.com/blog/privacy-policy/) [Proudly powered by WordPress](https://wordpress.org/ "Semantic Personal Publishing Platform")
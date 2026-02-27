---
title: ShimBad the Sailor, Part 3
url: https://www.hexacorn.com/blog/2026/02/26/shimbad-the-sailor-part-3/
source: Hexacorn
date: 2026-02-26
fetch_date: 2026-02-27T04:07:03.410253
---

# ShimBad the Sailor, Part 3

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

[← Previous](https://www.hexacorn.com/blog/2026/02/21/1-little-known-secret-of-sti_ci-dll/)

# ShimBad the Sailor, Part 3

Posted on [2026-02-26](https://www.hexacorn.com/blog/2026/02/26/shimbad-the-sailor-part-3/ "1:16 am")  by  [adam](https://www.hexacorn.com/blog/author/adam/ "View all posts by adam")

Windows 11 brings us a lot of new Shim-related goodies and it makes sense to cover at least some of them.

In the [second part of this series](https://www.hexacorn.com/blog/2020/03/20/shimbad-the-sailor-part-2/) I listed a number of process names that are treated in a special way by the existing shim database entries.

It turns out that the list of these process names has been extended by at least two:

* SdbMergeTestEntry\_Added\_Exe\_Item.exe
* SdbMergeTestEntry\_Added\_Exe\_Item\_InboxApp.exe

In other words, when you run a program that is named like the two aforementioned entries, you will get these messages:

[![](https://www.hexacorn.com/blog/wp-content/uploads/2026/02/sdb1.png)](https://www.hexacorn.com/blog/wp-content/uploads/2026/02/sdb1.png)
[![](https://www.hexacorn.com/blog/wp-content/uploads/2026/02/sdb2.png)](https://www.hexacorn.com/blog/wp-content/uploads/2026/02/sdb2.png)

Additionally, Windows 11 binaries handling shims include references to a list of folders that may be of some interest:

* %windir%\apppatch\AcPluginDlls\Plugin
* %windir%\apppatch\AcPluginDlls\PluginWow
* %windir%\apppatch\AcPluginDlls\PluginWowAMD64
* %windir%\apppatch\AcPluginDlls\PluginWowARM
* %windir%\apppatch\AcPluginDlls\PluginWowARM64
* %windir%\apppatch\AcPluginDlls\PluginWowX86

The Windows 11 installations I saw so far include these test Ac plugins:

* c:\WINDOWS\apppatch\AcPluginDlls\Plugin\AcPlugin\_Test.dll
* c:\WINDOWS\apppatch\AcPluginDlls\Plugin\AcPlugin\_Test2.dll
* c:\WINDOWS\apppatch\AcPluginDlls\PluginWowX86\AcPlugin\_Test.dll
* c:\WINDOWS\apppatch\AcPluginDlls\PluginWowX86\AcPlugin\_Test2.dll

The code referencing these directories resides in a few system libraries:

* apphelp.dll
* pcasvc.dll
* appraiser.dll

but I have not explored yet how they work. As of now, I assume this is a lesser-known Shim Database enhancement mechanism that could be potentially leveraged for persistence and stealth code injection…

This entry was posted in [Anti-Forensics](https://www.hexacorn.com/blog/category/anti-forensics/) by [adam](https://www.hexacorn.com/blog/author/adam/). Bookmark the [permalink](https://www.hexacorn.com/blog/2026/02/26/shimbad-the-sailor-part-3/ "Permalink to ShimBad the Sailor, Part 3").

[Privacy Policy](https://www.hexacorn.com/blog/privacy-policy/) [Proudly powered by WordPress](https://wordpress.org/ "Semantic Personal Publishing Platform")
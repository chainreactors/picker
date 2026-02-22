---
title: 1 little known secret of sti_ci.dll
url: https://www.hexacorn.com/blog/2026/02/21/1-little-known-secret-of-sti_ci-dll/
source: Hexacorn
date: 2026-02-21
fetch_date: 2026-02-22T04:10:08.778931
---

# 1 little known secret of sti_ci.dll

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

[← Previous](https://www.hexacorn.com/blog/2026/02/14/winhttpopen-user-agents/)

# 1 little known secret of sti\_ci.dll

Posted on [2026-02-21](https://www.hexacorn.com/blog/2026/02/21/1-little-known-secret-of-sti_ci-dll/ "8:23 pm")  by  [adam](https://www.hexacorn.com/blog/author/adam/ "View all posts by adam")

In 2017 I posted about sideloading of [sti\_ci.dll](https://www.hexacorn.com/blog/2017/10/20/imagingdevices-yet-another-os-native-side-loading-program/). And it’s that DLL itself that executes the *InstallWiaDevice* installation command mentioned in that post…

How?

Via its export function called… InstallWiaDevice.

It turns out that we can launch this API directly via *rundll32.exe*:

```
rundll32.exe sti_ci.dll, InstallWiaService
```

When executed, the API runs a number of programs:

```
regsvr32.exe /s wiaservc.dll
regsvr32.exe /s sti.dll
regsvr32 /s C:\WINDOWS\syswow64\sti.dll
regsvr32.exe /s wiadefui.dll
wiaacmgr.exe /RegServer
regsvr32.exe /s wiashext.dll
regsvr32.exe /s camocx.dll
regsvr32.exe /s photowiz.dll
regsvr32.exe /s wiavusd.dll
regsvr32.exe /s wiasf.ax
```

Obviously, this creates a number of new possible lolbin opportunities. The only challenge is that since the *rundll32.exe* is executed from the system32 directory, the program will look for *regsvr32.exe*, *wiaacmgr.exe* there first, same as for the listed DLLs.

To bypass it, one could copy *rundll32.exe* to a different directory, and launch it from there — not the most elegant solution, but it works.

Bonus:

The *sti\_ci.dll* library logs executed commands in a *wiatrace.log* file. It may be located in various places on the system:

* %systemroot%\Debug\WIA\wiatrace.log
* c:\Users\<user>\AppData\Local\VirtualStore\Windows\debug\WIA\wiatrace.log

Example entries look like this:

[![](https://www.hexacorn.com/blog/wp-content/uploads/2026/02/sti_ci1.png)](https://www.hexacorn.com/blog/wp-content/uploads/2026/02/sti_ci1.png)

This entry was posted in [little known secrets](https://www.hexacorn.com/blog/category/little-known-secrets/), [Living off the land](https://www.hexacorn.com/blog/category/living-off-the-land/), [LOLBins](https://www.hexacorn.com/blog/category/living-off-the-land/lolbins/) by [adam](https://www.hexacorn.com/blog/author/adam/). Bookmark the [permalink](https://www.hexacorn.com/blog/2026/02/21/1-little-known-secret-of-sti_ci-dll/ "Permalink to 1 little known secret of sti_ci.dll").

[Privacy Policy](https://www.hexacorn.com/blog/privacy-policy/) [Proudly powered by WordPress](https://wordpress.org/ "Semantic Personal Publishing Platform")
---
title: wermgr.exe boot offdmpsvc.dll lolbin
url: https://www.hexacorn.com/blog/2025/06/14/wermgr-exe-boot-offdmpsvc-dll-lolbin/
source: Hexacorn
date: 2025-06-15
fetch_date: 2025-10-06T22:52:39.623986
---

# wermgr.exe boot offdmpsvc.dll lolbin

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

[← Previous](https://www.hexacorn.com/blog/2025/06/14/wpr-exe-boottrace-phantom-dll-axeonoffhelper-dll-lolbin/)
[Next →](https://www.hexacorn.com/blog/2025/06/15/vmwareresolutionset-exe-vmwareresolutionset-dll-lolbin/)

# wermgr.exe boot offdmpsvc.dll lolbin

Posted on [2025-06-14](https://www.hexacorn.com/blog/2025/06/14/wermgr-exe-boot-offdmpsvc-dll-lolbin/ "11:35 pm")  by  [adam](https://www.hexacorn.com/blog/author/adam/ "View all posts by adam")

Similarly as in the [previous case](https://www.hexacorn.com/blog/2025/06/14/wpr-exe-boottrace-phantom-dll-axeonoffhelper-dll-lolbin/), *wermgr.exe* accepts many command line arguments:

```
-boot
-clean
-datacollectorcreate
-nonelevated
-outproc
-purgestores
-queuereporting
-queuereporting_svc
-queuereporting_s_machine
-upload
-uploadforce
-waitforpendingreports
```

The *-boot* one is interesting as it triggers the execution of program’s path that attempts to load the following phantom DLL:

```
C:\Windows\System32\offdmpsvc.dll
```

As such, placing your payload in the aforementioned DLL will lead to its execution when you launch the following command:

```
wermgr -boot
```

This entry was posted in [Living off the land](https://www.hexacorn.com/blog/category/living-off-the-land/), [LOLBins](https://www.hexacorn.com/blog/category/living-off-the-land/lolbins/) by [adam](https://www.hexacorn.com/blog/author/adam/). Bookmark the [permalink](https://www.hexacorn.com/blog/2025/06/14/wermgr-exe-boot-offdmpsvc-dll-lolbin/ "Permalink to wermgr.exe boot offdmpsvc.dll lolbin").

[Privacy Policy](https://www.hexacorn.com/blog/privacy-policy/) [Proudly powered by WordPress](https://wordpress.org/ "Semantic Personal Publishing Platform")
---
title: VMwareResolutionSet.exe VMwareResolutionSet.dll lolbin
url: https://www.hexacorn.com/blog/2025/06/15/vmwareresolutionset-exe-vmwareresolutionset-dll-lolbin/
source: Hexacorn
date: 2025-06-16
fetch_date: 2025-10-06T22:53:33.189218
---

# VMwareResolutionSet.exe VMwareResolutionSet.dll lolbin

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

[← Previous](https://www.hexacorn.com/blog/2025/06/14/wermgr-exe-boot-offdmpsvc-dll-lolbin/)
[Next →](https://www.hexacorn.com/blog/2025/07/05/beyond-good-ol-run-key-part-147/)

# VMwareResolutionSet.exe VMwareResolutionSet.dll lolbin

Posted on [2025-06-15](https://www.hexacorn.com/blog/2025/06/15/vmwareresolutionset-exe-vmwareresolutionset-dll-lolbin/ "8:49 pm")  by  [adam](https://www.hexacorn.com/blog/author/adam/ "View all posts by adam")

If you still use VMWare, your Windows guest system will benefit from an installation of VMWare Tools.

The VMWare Tools package is usually installed into this directory:

```
c:\Program Files\VMware\VMware Tools
```

It turns out that running the executable:

```
c:\Program Files\VMware\VMware Tools\VMwareResolutionSet.exe
```

leads to it trying to lead a phantom DLL:

```
c:\Program Files\VMware\VMware Tools\VMwareResolutionSet.dll
```

So, as usual, creating your own payload DLL and placing it in that location can help us to load it via proxy.

This entry was posted in [Living off the land](https://www.hexacorn.com/blog/category/living-off-the-land/), [LOLBins](https://www.hexacorn.com/blog/category/living-off-the-land/lolbins/) by [adam](https://www.hexacorn.com/blog/author/adam/). Bookmark the [permalink](https://www.hexacorn.com/blog/2025/06/15/vmwareresolutionset-exe-vmwareresolutionset-dll-lolbin/ "Permalink to VMwareResolutionSet.exe VMwareResolutionSet.dll lolbin").

[Privacy Policy](https://www.hexacorn.com/blog/privacy-policy/) [Proudly powered by WordPress](https://wordpress.org/ "Semantic Personal Publishing Platform")
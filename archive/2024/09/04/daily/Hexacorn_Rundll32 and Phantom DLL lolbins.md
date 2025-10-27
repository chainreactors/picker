---
title: Rundll32 and Phantom DLL lolbins
url: https://www.hexacorn.com/blog/2024/09/03/rundll32-and-phantom-dll-lolbins/
source: Hexacorn
date: 2024-09-04
fetch_date: 2025-10-06T18:26:15.667151
---

# Rundll32 and Phantom DLL lolbins

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

[← Previous](https://www.hexacorn.com/blog/2024/08/13/enter-sandbox-29-the-subtle-art-of-reversing-persuasion-pushing-samples-to-run/)
[Next →](https://www.hexacorn.com/blog/2024/09/04/rundll32-and-phantom-dll-lolbins-32-bit-version/)

# Rundll32 and Phantom DLL lolbins

Posted on [2024-09-03](https://www.hexacorn.com/blog/2024/09/03/rundll32-and-phantom-dll-lolbins/ "9:23 pm")  by  [adam](https://www.hexacorn.com/blog/author/adam/ "View all posts by adam")

This may be a new, kinda ephemereal addition to the lolbin world (not sure if anyone covered it before).

Windows 11 comes with a large number of DLLs – some of which are broken.

**DuCsps.dll** on Windows 11 Pro 22H2

The *DuCsps.dll* imports 2 APIs from *UpdateAPI.dll*:

* *GetInstalledPackageInfo*, and
* *FreeInstalledPackageInfo*.

The problem is that there is no *UpdateAPI.dll.* It may be present in other versions of Windows, but it’s not present in 22H2 (note: I have not tested all the subversions, so YMMV).

**tssrvlic.dll** on Windows 11 Pro 22H2

The same goes for *tssrvlic.dll* that imports 3 APIs from a non-existing *TlsBrand.dll*:

* *RDSGetProductAccessRights*,
* *W2K3ADPUCALDetailsCreator*, and
* *RDSProductDetailsCreator*

They both create a lolbin opportunity via a missing phantom DLL, and an attacker can simply bring in their versions of malicious *UpdateAPI.dll* or *TlsBrand.dll*, and then run (from the same directory where these payloads are located) the following rundll32 commands:

```
rundll32 DuCsps.dll, foo

rundll32 tssrvlic.dll, bar
```

where *foo* and *bar* can be anything.

See below:

[![](https://www.hexacorn.com/blog/wp-content/uploads/2024/09/rundll32_phantomdll.gif)](https://www.hexacorn.com/blog/wp-content/uploads/2024/09/rundll32_phantomdll.gif)

This entry was posted in [Anti-Forensics](https://www.hexacorn.com/blog/category/anti-forensics/), [Archaeology](https://www.hexacorn.com/blog/category/archaeology/), [Living off the land](https://www.hexacorn.com/blog/category/living-off-the-land/), [LOLBins](https://www.hexacorn.com/blog/category/living-off-the-land/lolbins/), [Sideloading](https://www.hexacorn.com/blog/category/sideloading/) by [adam](https://www.hexacorn.com/blog/author/adam/). Bookmark the [permalink](https://www.hexacorn.com/blog/2024/09/03/rundll32-and-phantom-dll-lolbins/ "Permalink to Rundll32 and Phantom DLL lolbins").

[Privacy Policy](https://www.hexacorn.com/blog/privacy-policy/) [Proudly powered by WordPress](https://wordpress.org/ "Semantic Personal Publishing Platform")
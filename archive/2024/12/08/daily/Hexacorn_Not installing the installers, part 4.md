---
title: Not installing the installers, part 4
url: https://www.hexacorn.com/blog/2024/12/07/not-installing-the-installers-part-4/
source: Hexacorn
date: 2024-12-08
fetch_date: 2025-10-06T19:38:00.224938
---

# Not installing the installers, part 4

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

[← Previous](https://www.hexacorn.com/blog/2024/12/06/execcmd64-lolbin/)
[Next →](https://www.hexacorn.com/blog/2024/12/10/promoting-a-windows-2022-server-to-domain-controller-and-dns-server/)

# Not installing the installers, part 4

Posted on [2024-12-07](https://www.hexacorn.com/blog/2024/12/07/not-installing-the-installers-part-4/ "12:32 am")  by  [adam](https://www.hexacorn.com/blog/author/adam/ "View all posts by adam")

This old [series](https://www.hexacorn.com/blog/2022/06/05/not-installing-the-installers-part-3/) is not very exciting. Decompiling goodware installation scripts will never lead us to newsworthy discoveries – feel free to stop reading now.

Many installers copy files, add/change registry keys and values, install services, drivers, and do all that while their GUIs sometimes tell us what is happening, and occasionally ask us to guide them. Superboring stuff.

If you are still reading…

Recently, I noticed that some of the aforementioned ‘add/change registry keys and values’ activities affect the Process Environment block. The most popular modification is (obviously) focused on the PATH environment variable – installers just love adding new directories to it!

BUT

There is more.

The below is a list (not exhaustive) of other environment variables that are being added by installers:

* ACE\_STUDIO\_PATH
* BRAINGINES\_PATH
* CC\_PIXEL\_RATIO
* DELIGHT
* FLOW\_PATH
* FMXLINUX
* GIT\_LFS\_PATH
* GPU\_AUDIO\_PLUGIN\_INSTALLATION\_PATH
* IDF\_TOOLS\_PATH
* IFCEXPORTER
* INTELBRAS\_AMTRD\_JAVA\_HOME
* JAVA\_HOME
* JETTY\_WEB\_HOME
* JIOCLOUD\_INSTALL\_TYPE
* LANDO\_INSTALL\_PATH
* LANG
* LANG\_PSERVER
* P3DEXPORTER
* QT\_DEVICE\_PIXEL\_RATIO
* RTOOLS43\_HOME
* RTOOLS44\_AARCH64\_HOME
* RTOOLS44\_HOME
* XR\_RUNTIME\_JSON

While some of them seem to be quite unimportant, a lot of them seem to be asking for some … abuse (aka research) ?

I mean… anything that includes ‘PATH’ or ‘HOME’ in their name needs an appropriate research-driven follow-up.

Why?

All of them are under HKCU, so anyone can modify them. Secondly, these environment variables may open new ways to abuse legitimate, often signed binaries to do something they never intended to do – and as such, create new lolbin opportunities. It could be loading plug-ins from a malicious location, it could be executing framework binaries from a controlled location, there is definitely a scope for research here.

This entry was posted in [Archaeology](https://www.hexacorn.com/blog/category/archaeology/), [Batch Analysis](https://www.hexacorn.com/blog/category/batch-analysis/), [Clustering](https://www.hexacorn.com/blog/category/clustering/), [Living off the land](https://www.hexacorn.com/blog/category/living-off-the-land/), [LOLBins](https://www.hexacorn.com/blog/category/living-off-the-land/lolbins/) by [adam](https://www.hexacorn.com/blog/author/adam/). Bookmark the [permalink](https://www.hexacorn.com/blog/2024/12/07/not-installing-the-installers-part-4/ "Permalink to Not installing the installers, part 4").

[Privacy Policy](https://www.hexacorn.com/blog/privacy-policy/) [Proudly powered by WordPress](https://wordpress.org/ "Semantic Personal Publishing Platform")
---
title: Rundll32 and Phantom DLL lolbins, 32-bit version
url: https://www.hexacorn.com/blog/2024/09/04/rundll32-and-phantom-dll-lolbins-32-bit-version/
source: Hexacorn
date: 2024-09-05
fetch_date: 2025-10-06T18:25:21.518821
---

# Rundll32 and Phantom DLL lolbins, 32-bit version

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

[← Previous](https://www.hexacorn.com/blog/2024/09/03/rundll32-and-phantom-dll-lolbins/)
[Next →](https://www.hexacorn.com/blog/2024/09/05/technical-debt-of-cwindowssystem-path/)

# Rundll32 and Phantom DLL lolbins, 32-bit version

Posted on [2024-09-04](https://www.hexacorn.com/blog/2024/09/04/rundll32-and-phantom-dll-lolbins-32-bit-version/ "9:00 pm")  by  [adam](https://www.hexacorn.com/blog/author/adam/ "View all posts by adam")

As I have shown in the last [post](https://www.hexacorn.com/blog/2024/09/03/rundll32-and-phantom-dll-lolbins/), there exists a class of DLLs on Windows OS that load other libraries via import table, and sometimes these needed imported libraries do not exist. This creates an opportunity that we can leverage f.ex. by using *rundll32.exe* to load these ‘broken’ libraries, and to avoid them failing to load because of missing libraries – we provide these as a payload, saved in an appropriately named DLL files (in essence, they are phantom DLLs) .

The previous post discussed 64-bit libraries, and here I will demo a single instance of a 32-bit library like this:

**uxlib.dll** on Windows 11 Pro 22H2

It imports *IsCrossArchitectureInstall* API from *WDSUTIL.dll*, so providing our own will lead to this:

[![](https://www.hexacorn.com/blog/wp-content/uploads/2024/09/rundll32_phantomdll32.gif)](https://www.hexacorn.com/blog/wp-content/uploads/2024/09/rundll32_phantomdll32.gif)

This entry was posted in [Anti-Forensics](https://www.hexacorn.com/blog/category/anti-forensics/), [Archaeology](https://www.hexacorn.com/blog/category/archaeology/), [Living off the land](https://www.hexacorn.com/blog/category/living-off-the-land/), [LOLBins](https://www.hexacorn.com/blog/category/living-off-the-land/lolbins/) by [adam](https://www.hexacorn.com/blog/author/adam/). Bookmark the [permalink](https://www.hexacorn.com/blog/2024/09/04/rundll32-and-phantom-dll-lolbins-32-bit-version/ "Permalink to Rundll32 and Phantom DLL lolbins, 32-bit version").

[Privacy Policy](https://www.hexacorn.com/blog/privacy-policy/) [Proudly powered by WordPress](https://wordpress.org/ "Semantic Personal Publishing Platform")
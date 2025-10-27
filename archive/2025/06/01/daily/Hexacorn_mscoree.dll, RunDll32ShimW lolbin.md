---
title: mscoree.dll, RunDll32ShimW lolbin
url: https://www.hexacorn.com/blog/2025/05/31/mscoree-dll-rundll32shimw-lolbin/
source: Hexacorn
date: 2025-06-01
fetch_date: 2025-10-06T22:51:52.799251
---

# mscoree.dll, RunDll32ShimW lolbin

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

[← Previous](https://www.hexacorn.com/blog/2025/05/30/shell32-dll-61/)
[Next →](https://www.hexacorn.com/blog/2025/06/14/wpr-exe-boottrace-phantom-dll-axeonoffhelper-dll-lolbin/)

# mscoree.dll, RunDll32ShimW lolbin

Posted on [2025-05-31](https://www.hexacorn.com/blog/2025/05/31/mscoree-dll-rundll32shimw-lolbin/ "11:09 pm")  by  [adam](https://www.hexacorn.com/blog/author/adam/ "View all posts by adam")

Executing this function via rundll32.exe leads to loading of *mscoreei.dll* from one of the default .NET directories.

However…

The *RunDll32ShimW* function takes into account the value of the environmental variable *COMPlus\_InstallRoot* when it searches for the *mscoreei.dll* file.

So…

If we change the value of the *COMPlus\_InstallRoot* variable to point to a directory of our choice, place the payload in a subdirectory associated with the .NET version installed on the system, we can sideload our payload like this:

```
set COMPLUS_InstallRoot=c:\test\
rundll32.exe mscoree.dll, RunDll32ShimW
```

[![](https://www.hexacorn.com/blog/wp-content/uploads/2025/05/mscoreei.png)](https://www.hexacorn.com/blog/wp-content/uploads/2025/05/mscoreei.png)

This entry was posted in [Living off the land](https://www.hexacorn.com/blog/category/living-off-the-land/), [LOLBins](https://www.hexacorn.com/blog/category/living-off-the-land/lolbins/) by [adam](https://www.hexacorn.com/blog/author/adam/). Bookmark the [permalink](https://www.hexacorn.com/blog/2025/05/31/mscoree-dll-rundll32shimw-lolbin/ "Permalink to mscoree.dll, RunDll32ShimW lolbin").

[Privacy Policy](https://www.hexacorn.com/blog/privacy-policy/) [Proudly powered by WordPress](https://wordpress.org/ "Semantic Personal Publishing Platform")
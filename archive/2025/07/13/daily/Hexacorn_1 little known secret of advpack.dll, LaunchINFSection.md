---
title: 1 little known secret of advpack.dll, LaunchINFSection
url: https://www.hexacorn.com/blog/2025/07/12/1-little-known-secret-of-advpack-dll-launchinfsection/
source: Hexacorn
date: 2025-07-13
fetch_date: 2025-10-06T23:28:29.846885
---

# 1 little known secret of advpack.dll, LaunchINFSection

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

[← Previous](https://www.hexacorn.com/blog/2025/07/11/beyond-good-ol-run-key-part-149/)
[Next →](https://www.hexacorn.com/blog/2025/08/17/beyond-good-ol-run-key-part-150/)

# 1 little known secret of advpack.dll, LaunchINFSection

Posted on [2025-07-12](https://www.hexacorn.com/blog/2025/07/12/1-little-known-secret-of-advpack-dll-launchinfsection/ "10:42 pm")  by  [adam](https://www.hexacorn.com/blog/author/adam/ "View all posts by adam")

Yes, yet another oldie with a secret…

The .inf files are as old as Windows itself, and their internal structure has been covered by many, and over at least last two decades.

So, what’s new?

Well…

Ever heard of *LoadAdvpackExtension* ?

This simple .inf file demonstrates how to use it to load a DLL of your choice:

> [version]
> signature=”$CHICAGO$”
> AdvancedINF=2.5,”test”
>
> [DefaultInstall]
> Patching=1
> LoadAdvpackExtension=test64.dll

To launch it, you need to do the following:

```
Place the above .inf file in c:\test\test.inf
Place test64.dll in c:\test
Go to terminal: cmd.exe
Run: set path=.
Run: c:\windows\system32\rundll32.exe advpack.dll,LaunchINFSection c:\test\test.inf,,1,
```

We change the PATH to make sure our test64.dll is found in a current directory, and then loaded:

[![](https://www.hexacorn.com/blog/wp-content/uploads/2025/07/LoadAdvpackExtension-1024x161.png)](https://www.hexacorn.com/blog/wp-content/uploads/2025/07/LoadAdvpackExtension.png)

This entry was posted in [little known secrets](https://www.hexacorn.com/blog/category/little-known-secrets/), [Living off the land](https://www.hexacorn.com/blog/category/living-off-the-land/), [LOLBins](https://www.hexacorn.com/blog/category/living-off-the-land/lolbins/) by [adam](https://www.hexacorn.com/blog/author/adam/). Bookmark the [permalink](https://www.hexacorn.com/blog/2025/07/12/1-little-known-secret-of-advpack-dll-launchinfsection/ "Permalink to 1 little known secret of advpack.dll, LaunchINFSection").

[Privacy Policy](https://www.hexacorn.com/blog/privacy-policy/) [Proudly powered by WordPress](https://wordpress.org/ "Semantic Personal Publishing Platform")
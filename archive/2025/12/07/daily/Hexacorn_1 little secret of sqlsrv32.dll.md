---
title: 1 little secret of sqlsrv32.dll
url: https://www.hexacorn.com/blog/2025/12/07/1-little-secret-of-sqlsrv32-dll/
source: Hexacorn
date: 2025-12-07
fetch_date: 2025-12-08T03:20:58.544911
---

# 1 little secret of sqlsrv32.dll

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

[← Previous](https://www.hexacorn.com/blog/2025/12/06/1-little-secret-of-cliconfg-dll/)

# 1 little secret of sqlsrv32.dll

Posted on [2025-12-07](https://www.hexacorn.com/blog/2025/12/07/1-little-secret-of-sqlsrv32-dll/ "12:01 am")  by  [adam](https://www.hexacorn.com/blog/author/adam/ "View all posts by adam")

This post is not really about *sqlsrv32.dll*, but since it is poking in this library’s code that led me to rediscover the *[BidInterface](https://learn.microsoft.com/en-us/previous-versions/windows/desktop/hh829625%28v%3Dvs.85%29)* interface for the third time (I even described it [twice](https://www.hexacorn.com/blog/2019/07/13/beyond-good-ol-run-key-part-111/) [before](https://www.hexacorn.com/blog/2020/10/17/beyond-good-ol-run-key-part-129/), without anyone noticing!), it ended up in a title of this post…

Anyway, back to the rediscovery bit… I am actually quite surprised that I was able to not only rediscover it for the 3rd time, but also find a new way to abuse it. And as usual, it is the Procmon logs that did most of the work here…

When you attempt to load *sqlsrv32.dll* via *rundll32.exe* and execute any of its exported functions f.ex.:

```
rundll32 sqlsrv32.dll, TestDlgProc
```

the *sqlsrv32.dll* library will try to activate that aforementioned BidInterface libraries:

[![](https://www.hexacorn.com/blog/wp-content/uploads/2025/12/BidInterface1.png)](https://www.hexacorn.com/blog/wp-content/uploads/2025/12/BidInterface1.png)

As we can see, not only the *:Path* is being looked at, but also a few more other things:

* the full path of the executable+ its Process ID (PID)
* the full path of the executable
* the directory extracted from the path of the executable, with an asterisk

That’s a very granular control over the BidInterface tracing, and after testing these entries for *rundll32.exe*, I was able to immediately load the test DLL of my choice:

* first we create the entry for *C:\WINDOWS\system32\rundll32.exe* and pointing it to *c:\test\test64\_dll.dll*:

[![](https://www.hexacorn.com/blog/wp-content/uploads/2025/12/BidInterface2.png)](https://www.hexacorn.com/blog/wp-content/uploads/2025/12/BidInterface2.png)

* and then we launch the *rundll32.exe* command listed above:

[![](https://www.hexacorn.com/blog/wp-content/uploads/2025/12/BidInterface3-1024x190.png)](https://www.hexacorn.com/blog/wp-content/uploads/2025/12/BidInterface3.png)

Obviously, the *C:\WINDOWS\system32\\** entry pointing to the same library works as well:

[![](https://www.hexacorn.com/blog/wp-content/uploads/2025/12/BidInterface4-1024x196.png)](https://www.hexacorn.com/blog/wp-content/uploads/2025/12/BidInterface4.png)

That’s it!

This entry was posted in [little known secrets](https://www.hexacorn.com/blog/category/little-known-secrets/), [Living off the land](https://www.hexacorn.com/blog/category/living-off-the-land/), [LOLBins](https://www.hexacorn.com/blog/category/living-off-the-land/lolbins/) by [adam](https://www.hexacorn.com/blog/author/adam/). Bookmark the [permalink](https://www.hexacorn.com/blog/2025/12/07/1-little-secret-of-sqlsrv32-dll/ "Permalink to 1 little secret of sqlsrv32.dll").

[Privacy Policy](https://www.hexacorn.com/blog/privacy-policy/) [Proudly powered by WordPress](https://wordpress.org/ "Semantic Personal Publishing Platform")
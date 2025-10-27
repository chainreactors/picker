---
title: The art of underDLLoading
url: https://www.hexacorn.com/blog/2024/09/06/the-art-of-underdlloading/
source: Hexacorn
date: 2024-09-07
fetch_date: 2025-10-06T18:27:53.904113
---

# The art of underDLLoading

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

[← Previous](https://www.hexacorn.com/blog/2024/09/05/the-art-of-overdlloading/)
[Next →](https://www.hexacorn.com/blog/2024/09/07/this-post-is-totally-iconic/)

# The art of underDLLoading

Posted on [2024-09-06](https://www.hexacorn.com/blog/2024/09/06/the-art-of-underdlloading/ "10:46 pm")  by  [adam](https://www.hexacorn.com/blog/author/adam/ "View all posts by adam")

In my previous [post](https://www.hexacorn.com/blog/2024/09/05/the-art-of-overdlloading/) I created a posh artisan .exe file ornamented with a large number of intricate system32 DLL imports. The process of building that file was painful – before I even managed to run the final executable I had to troubleshoot a number issues – many of which I didn’t even expect (missing DLLs, missing manifest, random crashes, etc.).

In the process of sculpting it I decided to kick off a parallel mini project that would look at the problem from a different angle — instead of a single file, I decided to generate a lot of test executable files, where each of these files would import just ONE single DLL from the system32 directory + the kernel32 as I needed it for its *ExitProcess* API. I then ran all these compiled files one by one. The original idea was to isolate and troubleshoot problematic DLLs, but to my surprise, I got some other interesting results.

First of all, with the real-time detection on, Windows Defender started picking up on some of these executables one by one:

* [test\_aadtb.exe](https://www.virustotal.com/gui/file/160abf0a6591d638b8de8dc1844ee0a134b3e7e01858d35025ffc312824a5149?nocache=1)
* [test\_adhapi.exe](https://www.virustotal.com/gui/file/cf2ad4a99a20dd480b38d4ddfa45c1feb30accc9fb89753be6e0c53712dab66b?nocache=1)
* [test\_user32.exe](https://www.virustotal.com/gui/file/e1cb5a107d2b48b2d7a3b13ab94703ea589845747be488ffc01a02dda22d8631?nocache=1)
* and many others (I quickly disabled the real-time protection and restored the quarantined files to carry on with the test):

[![](https://www.hexacorn.com/blog/wp-content/uploads/2024/09/windefend_test_detections.png)](https://www.hexacorn.com/blog/wp-content/uploads/2024/09/windefend_test_detections.png)

Linking to *dpnaddr.dll*, *dpnathlp.dll*, *dpnet.dll*, *dpnhpast.dll*, *dpnhupnp.dll*, *dpnlobby.dll* causes an interesting side-effect. When you run an .exe that links to any of these libraries, you get a DirectPlay Windows Features install dialog box:

[![](https://www.hexacorn.com/blog/wp-content/uploads/2024/09/dplay_feature.png)](https://www.hexacorn.com/blog/wp-content/uploads/2024/09/dplay_feature.png)

This is a result of *svchost.exe* hosting *Program Compatibility Assistant Service* (*C:\Windows\system32\svchost.exe -k LocalSystemNetworkRestricted -p -s PcaSvc*) launching this dialog via *fondue.exe*:

```
Fondue.exe /enable-feature:DirectPlay /show-caller /top-most /caller-name:"test_<dllname>.exe"
```

This looks like a shim at work, but I have not verified it. And no, we cannot launch our own *fondue.exe* here as far as I can tell 🙁

Many other test files fail too, for many different reasons:

[![](https://www.hexacorn.com/blog/wp-content/uploads/2024/09/gdi32.png)](https://www.hexacorn.com/blog/wp-content/uploads/2024/09/gdi32.png)
[![](https://www.hexacorn.com/blog/wp-content/uploads/2024/09/shdocvw.png)](https://www.hexacorn.com/blog/wp-content/uploads/2024/09/shdocvw.png)
[![](https://www.hexacorn.com/blog/wp-content/uploads/2024/09/tasksched.png)](https://www.hexacorn.com/blog/wp-content/uploads/2024/09/tasksched.png)

We can extract crash details from the Windows Event Logs/Applications:

[![](https://www.hexacorn.com/blog/wp-content/uploads/2024/09/tasksched_eventlog.png)](https://www.hexacorn.com/blog/wp-content/uploads/2024/09/tasksched_eventlog.png)

When you start experimenting with a PE file format itself, there are no limits. By playing around with its frivolous structure we can create a lot of interesting and unexpected results.

This entry was posted in [Archaeology](https://www.hexacorn.com/blog/category/archaeology/), [Random ideas](https://www.hexacorn.com/blog/category/random-ideas/), [Silly](https://www.hexacorn.com/blog/category/silly/) by [adam](https://www.hexacorn.com/blog/author/adam/). Bookmark the [permalink](https://www.hexacorn.com/blog/2024/09/06/the-art-of-underdlloading/ "Permalink to The art of underDLLoading").

[Privacy Policy](https://www.hexacorn.com/blog/privacy-policy/) [Proudly powered by WordPress](https://wordpress.org/ "Semantic Personal Publishing Platform")
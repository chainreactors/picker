---
title: advpack.dll and IEAdvpack.dll logging capability
url: https://www.hexacorn.com/blog/2024/10/19/advpack-dll-and-ieadvpack-dll-logging-capability/
source: Hexacorn
date: 2024-10-20
fetch_date: 2025-10-06T18:49:44.237822
---

# advpack.dll and IEAdvpack.dll logging capability

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

[← Previous](https://www.hexacorn.com/blog/2024/10/12/the-sweet16-the-oldbin-lolbin-called-setup16-exe/)
[Next →](https://www.hexacorn.com/blog/2024/10/19/beyond-good-ol-run-key-part-143/)

# advpack.dll and IEAdvpack.dll logging capability

Posted on [2024-10-19](https://www.hexacorn.com/blog/2024/10/19/advpack-dll-and-ieadvpack-dll-logging-capability/ "9:09 pm")  by  [adam](https://www.hexacorn.com/blog/author/adam/ "View all posts by adam")

There is a very old hack out there that enables logging for the *advpack.dll* and *IEAdvpack.dll* DLLs. Many of their functions include the logging, so enabling this may help to pick up some old-school forensic logs. Of course, the value of it today is superlow, but it’s an interesting feature nevertheless, and in a way similar to [WinHTTP logging](https://www.hexacorn.com/blog/2016/12/15/supporting-dynamic-malware-analysis-with-winhttp-library-debug-logs-tracing/) I covered in the past.

To enable this feature we simply add this Registry entry:

```
HKLM\SOFTWARE\Microsoft\Advanced INF Setup
AdvpackLogFile=c:\test\log.txt
```

To test it, we can run these 2 commands:

```
rundll32.exe advpack.dll,RegisterOCX calc.exe
rundll32.exe IEAdvpack.dll,RegisterOCX calc.exe
```

The results will look as follows:

[![](https://www.hexacorn.com/blog/wp-content/uploads/2024/10/advpack_log.png)](https://www.hexacorn.com/blog/wp-content/uploads/2024/10/advpack_log.png)

This entry was posted in [Archaeology](https://www.hexacorn.com/blog/category/archaeology/), [Forensic Analysis](https://www.hexacorn.com/blog/category/forensic-analysis/) by [adam](https://www.hexacorn.com/blog/author/adam/). Bookmark the [permalink](https://www.hexacorn.com/blog/2024/10/19/advpack-dll-and-ieadvpack-dll-logging-capability/ "Permalink to advpack.dll and IEAdvpack.dll logging capability").

[Privacy Policy](https://www.hexacorn.com/blog/privacy-policy/) [Proudly powered by WordPress](https://wordpress.org/ "Semantic Personal Publishing Platform")
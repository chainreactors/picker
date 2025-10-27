---
title: wpr.exe boottrace phantom dll axeonoffhelper.dll lolbin
url: https://www.hexacorn.com/blog/2025/06/14/wpr-exe-boottrace-phantom-dll-axeonoffhelper-dll-lolbin/
source: Hexacorn
date: 2025-06-15
fetch_date: 2025-10-06T22:52:42.008525
---

# wpr.exe boottrace phantom dll axeonoffhelper.dll lolbin

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

[← Previous](https://www.hexacorn.com/blog/2025/05/31/mscoree-dll-rundll32shimw-lolbin/)
[Next →](https://www.hexacorn.com/blog/2025/06/14/wermgr-exe-boot-offdmpsvc-dll-lolbin/)

# wpr.exe boottrace phantom dll axeonoffhelper.dll lolbin

Posted on [2025-06-14](https://www.hexacorn.com/blog/2025/06/14/wpr-exe-boottrace-phantom-dll-axeonoffhelper-dll-lolbin/ "11:14 pm")  by  [adam](https://www.hexacorn.com/blog/author/adam/ "View all posts by adam")

Today I have discovered the *PipelineFilterHook* Registry entry only to find out that this [blog post](https://medium.com/%40naore32/not-just-another-dll-sideloading-blog-this-one-gets-you-localservice-privileges-27bc798c1792) has already described it in detail. Nice work!

So, I decided to take a look at my favorite phantom DLLs again, and came up with this finding…

The *wpr.exe* program accepts many command line arguments:

[![](https://www.hexacorn.com/blog/wp-content/uploads/2025/06/mpr.png)](https://www.hexacorn.com/blog/wp-content/uploads/2025/06/mpr.png)

The ‘boottrace’ command line argument is one of them, and if we provide some reasonable, even non-sensical second command line argument to the program, we can trigger the execution of *wpr.exe* program’s path that will lead to loading of *axeonoffhelper.dll* from System32 directory. As it happens, *axeonoffhelper.dll* is a phantom DLL.

So, placing your payload in:

```
C:\Windows\System32\axeonoffhelper.dll
```

and then executing f.ex.:

```
wpr -boottrace -stopboot foo
```

will lead to *C:\Windows\System32\axeonoffhelper.dll* being executed.

This entry was posted in [Living off the land](https://www.hexacorn.com/blog/category/living-off-the-land/), [LOLBins](https://www.hexacorn.com/blog/category/living-off-the-land/lolbins/) by [adam](https://www.hexacorn.com/blog/author/adam/). Bookmark the [permalink](https://www.hexacorn.com/blog/2025/06/14/wpr-exe-boottrace-phantom-dll-axeonoffhelper-dll-lolbin/ "Permalink to wpr.exe boottrace phantom dll axeonoffhelper.dll lolbin").

[Privacy Policy](https://www.hexacorn.com/blog/privacy-policy/) [Proudly powered by WordPress](https://wordpress.org/ "Semantic Personal Publishing Platform")
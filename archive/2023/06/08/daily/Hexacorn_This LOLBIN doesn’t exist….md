---
title: This LOLBIN doesn’t exist…
url: https://www.hexacorn.com/blog/2023/06/07/this-lolbin-doesnt-exist/
source: Hexacorn
date: 2023-06-08
fetch_date: 2025-10-04T11:47:36.984282
---

# This LOLBIN doesn’t exist…

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

[← Previous](https://www.hexacorn.com/blog/2023/06/03/analyzing-nested-obfuscated-php-files/)
[Next →](https://www.hexacorn.com/blog/2023/06/09/perl-and-python-scripting-templates/)

# This LOLBIN doesn’t exist…

Posted on [2023-06-07](https://www.hexacorn.com/blog/2023/06/07/this-lolbin-doesnt-exist/ "9:54 pm")  by  [adam](https://www.hexacorn.com/blog/author/adam/ "View all posts by adam")

I have written about [Nullsoft](https://www.hexacorn.com/blog/2015/06/26/enter-sandbox-part-6-the-nullsoft-hypothesis-and-other-installers-conundrums/) [installer](https://www.hexacorn.com/blog/2019/04/14/signed-nullsoft-plug-ins-potential-lolbins/) a few times before. I am a bit fascinated by it, because there is not that much research about it, in general, and even less – about its esoteric, yet omnipresent DLL plug-ins…

One of the more interesting plug-ins that I know of, and yet, one that you will never really see residing on any system, is… *ShellDispatch.dll*.

It’s a rarely used Nullsoft Plug-In DLL that is known to be used by the installer of WinAmp, yes.. THE WinAmp… and even there… it is used temporarily, as it is immediately deleted from the file system after delivering the required functionality.

What’s so special about it?

The *ShellDispatch.dll* exports a few functions:

* AddRef
* GetInterface
* Release
* RunDll\_ShellExecuteW
* ShellExecute

The *RunDll\_ShellExecuteW* is the most interesting to us as it is a callback function specifically crafted to respond to invocations via *rundll32.exe*, and since it’s a wrapper for *ShellExecute* API we can use it to launch any program of our choice, f.ex, calculator:

```
rundll32 ShellDispatch.dll, RunDll_ShellExecute open calc
```

[![](https://www.hexacorn.com/blog/wp-content/uploads/2023/06/ShellDispatch.gif)](https://www.hexacorn.com/blog/wp-content/uploads/2023/06/ShellDispatch.gif)

Again, the chances you will ever see it abused are VERY LOW.

This entry was posted in [LOLBins](https://www.hexacorn.com/blog/category/living-off-the-land/lolbins/) by [adam](https://www.hexacorn.com/blog/author/adam/). Bookmark the [permalink](https://www.hexacorn.com/blog/2023/06/07/this-lolbin-doesnt-exist/ "Permalink to This LOLBIN doesn’t exist…").

[Privacy Policy](https://www.hexacorn.com/blog/privacy-policy/) [Proudly powered by WordPress](https://wordpress.org/ "Semantic Personal Publishing Platform")
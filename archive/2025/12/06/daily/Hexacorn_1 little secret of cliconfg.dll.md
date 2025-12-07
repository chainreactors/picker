---
title: 1 little secret of cliconfg.dll
url: https://www.hexacorn.com/blog/2025/12/06/1-little-secret-of-cliconfg-dll/
source: Hexacorn
date: 2025-12-06
fetch_date: 2025-12-07T03:25:49.453473
---

# 1 little secret of cliconfg.dll

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

[← Previous](https://www.hexacorn.com/blog/2025/12/06/1-little-secret-of-mapi32-dll/)
[Next →](https://www.hexacorn.com/blog/2025/12/07/1-little-secret-of-sqlsrv32-dll/)

# 1 little secret of cliconfg.dll

Posted on [2025-12-06](https://www.hexacorn.com/blog/2025/12/06/1-little-secret-of-cliconfg-dll/ "9:46 am")  by  [adam](https://www.hexacorn.com/blog/author/adam/ "View all posts by adam")

Most of my favorite sideloading techniques rely on some old and kinda obscure localisation/test features embedded in various programming frameworks.

This post touches on yet another one of these.

When you launch this function:

```
rundll32 cliconfg.dll, OnInitDialogMain
```

the code of the DllMain of this DLL library will try to find the following localisation RLL files:

* C:\WINDOWS\system32\Resources\1024\cliconfg.RLL
* C:\WINDOWS\system32\Resources\1033\cliconfg.RLL

What is surprising though, these files are loaded via a regular *LoadLibrary* call, which obviously leads to a code execution…

So, placing your payload in any of these two RLL files, and executing any of the APIs exported by *cliconfg.dll*, will lead to loading and execution of these payloads. And if you know how *rundll32.exe* works, and paid attention to the bit mentioning DllMain being responsible for loading these localisation libraries, you know that we can specify any API name, or ordinal number, and get the payload execution anyway, As such, as long as our RLL files are in place, any of the below invocations will load the payload:

```
rundll32 cliconfg.dll, foo
rundll32 cliconfg.dll, bar
rundll32 cliconfg.dll, #1
rundll32 cliconfg.dll, #3948794357847857
```

This entry was posted in [little known secrets](https://www.hexacorn.com/blog/category/little-known-secrets/), [phantom dll](https://www.hexacorn.com/blog/category/sideloading/phantom-dll/), [Sideloading](https://www.hexacorn.com/blog/category/sideloading/) by [adam](https://www.hexacorn.com/blog/author/adam/). Bookmark the [permalink](https://www.hexacorn.com/blog/2025/12/06/1-little-secret-of-cliconfg-dll/ "Permalink to 1 little secret of cliconfg.dll").

[Privacy Policy](https://www.hexacorn.com/blog/privacy-policy/) [Proudly powered by WordPress](https://wordpress.org/ "Semantic Personal Publishing Platform")
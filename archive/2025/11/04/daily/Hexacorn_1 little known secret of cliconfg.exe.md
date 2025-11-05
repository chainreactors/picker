---
title: 1 little known secret of cliconfg.exe
url: https://www.hexacorn.com/blog/2025/11/04/1-little-known-secret-of-cliconfg-exe/
source: Hexacorn
date: 2025-11-04
fetch_date: 2025-11-05T03:11:06.903888
---

# 1 little known secret of cliconfg.exe

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

[← Previous](https://www.hexacorn.com/blog/2025/10/25/beyond-good-ol-run-key-part-153/)

# 1 little known secret of cliconfg.exe

Posted on [2025-11-04](https://www.hexacorn.com/blog/2025/11/04/1-little-known-secret-of-cliconfg-exe/ "1:33 am")  by  [adam](https://www.hexacorn.com/blog/author/adam/ "View all posts by adam")

This is a blast from the past.

Copy *c:\WINDOWS\system32\cliconfg.exe* to a folder of your choosing and execute it.

It will attempt to load a bunch of some very old-school DLLs:

* C:\Windows\System32\DBMSRPCN.DLL
* C:\Windows\System32\DBMSSPXN.DLL
* C:\Windows\System32\DBMSADSN.DLL
* C:\Windows\System32\DBMSVINN.DLL
* C:\Windows\System32\DBMSGNET.DLL
* C:\Windows\System32\DBMSSNET.DLL
* C:\Windows\System32\DBMSQLGC.DLL
* C:\Windows\System32\NTWDBLIB.DLL

The last one on the list is the one that executes code, so placing your payload inside *C:\Windows\System32\NTWDBLIB.DLL* is a guarantee that it will be executed when you run a copy of *c:\WINDOWS\system32\cliconfg.exe* from a different location.

I am lazy and am not researching the other ones, but I am sure it is most likely due to a lack of some specific export functions that my test DLLs miss to export that stop the code execution when these earlier DLLs are mapped to memory but not loaded.

This entry was posted in [little known secrets](https://www.hexacorn.com/blog/category/little-known-secrets/), [Living off the land](https://www.hexacorn.com/blog/category/living-off-the-land/), [LOLBins](https://www.hexacorn.com/blog/category/living-off-the-land/lolbins/) by [adam](https://www.hexacorn.com/blog/author/adam/). Bookmark the [permalink](https://www.hexacorn.com/blog/2025/11/04/1-little-known-secret-of-cliconfg-exe/ "Permalink to 1 little known secret of cliconfg.exe").

[Privacy Policy](https://www.hexacorn.com/blog/privacy-policy/) [Proudly powered by WordPress](https://wordpress.org/ "Semantic Personal Publishing Platform")
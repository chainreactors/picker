---
title: Mapping the API mapping/code redundancy
url: https://www.hexacorn.com/blog/2024/11/29/mapping-the-api-mapping-code-redundancy/
source: Hexacorn
date: 2024-11-30
fetch_date: 2025-10-06T19:15:16.699803
---

# Mapping the API mapping/code redundancy

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

[← Previous](https://www.hexacorn.com/blog/2024/11/28/windows-storage-lol/)
[Next →](https://www.hexacorn.com/blog/2024/11/30/1-little-known-secret-of-shellexec_rundll/)

# Mapping the API mapping/code redundancy

Posted on [2024-11-29](https://www.hexacorn.com/blog/2024/11/29/mapping-the-api-mapping-code-redundancy/ "7:23 pm")  by  [adam](https://www.hexacorn.com/blog/author/adam/ "View all posts by adam")

In my [last post](https://www.hexacorn.com/blog/2024/11/28/windows-storage-lol/) I have shown that some of the *shell32.dll* functions are now mapped to *windows.storage.dll*.

This sort of API mapping, as well as blatant code redundancy present in many Windows binaries is not new, and we have seen many instances of it over the years:

* Windows API sets
* *gdi32.dll* and *gdi32full.dll*
* *gdi32full.dll* and *win32u.dll*
* *combase.dll* and *ole32.dll*
* *kernel32.dll* and *KernelBase.dll*
* *IEAdvpack.dll* and *advpack.dll*
* *crtdll.dll*, *msvcirt.dll*, *ucrtbase.dll* and their many, many versions over the years
* *ntdll.dll* and *ntoskrnl.exe* (user mode vs. kernel mode mapping)

and so on, and so forth.

It is probably not surprising that after that latest discovery it was only natural for me to build a list of APIs (API names) that are shared between many libraries to see if I can discover more interesting bits.

Looking at the list of API names that appear to be shared between at least 2 DLL libraries on the Windows 11 24 H2 build – [win11\_24H2\_list\_64\_shared.txt](https://hexacorn.com/d/win11_24H2_list_64_shared.txt) – one can immediately see a lot of interesting findings:

* sqlite functions are exported by *SearchIndexerCore.dll*, *StateRepository.Core.dll*, *winsqlite3.dll*
* apart from *kernel32.dll* and *KernelBase.dll* there is now also *kernel.appcore.dll*
* code base of *tcblaunch.exe* and *winload.exe* seems to be overlapping a lot
* *edgehtml.dll* replaces *mshtml.dll*

Unfortunately, I have not seen anything similar to *ShellExec\_RunDLL* – a discovery that kicked off this research 🙁

This entry was posted in [Archaeology](https://www.hexacorn.com/blog/category/archaeology/) by [adam](https://www.hexacorn.com/blog/author/adam/). Bookmark the [permalink](https://www.hexacorn.com/blog/2024/11/29/mapping-the-api-mapping-code-redundancy/ "Permalink to Mapping the API mapping/code redundancy").

[Privacy Policy](https://www.hexacorn.com/blog/privacy-policy/) [Proudly powered by WordPress](https://wordpress.org/ "Semantic Personal Publishing Platform")
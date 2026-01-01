---
title: Beyond good ol’ Run key, Part 149 – update
url: https://www.hexacorn.com/blog/2025/12/31/beyond-good-ol-run-key-part-149-update/
source: Hexacorn
date: 2025-12-31
fetch_date: 2026-01-01T03:35:27.941523
---

# Beyond good ol’ Run key, Part 149 – update

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

[← Previous](https://www.hexacorn.com/blog/2025/12/07/1-little-secret-of-sqlsrv32-dll/)
[Next →](https://www.hexacorn.com/blog/2025/12/31/beyond-good-ol-run-key-part-152/)

# Beyond good ol’ Run key, Part 149 – update

Posted on [2025-12-31](https://www.hexacorn.com/blog/2025/12/31/beyond-good-ol-run-key-part-149-update/ "12:48 am")  by  [adam](https://www.hexacorn.com/blog/author/adam/ "View all posts by adam")

In my [older post](https://www.hexacorn.com/blog/2025/07/11/beyond-good-ol-run-key-part-149/), I described the persistence mechanism (*GPExtensionDLL* Registry entry) that I couldn’t make to work at that time. I eventually found a way to trigger it, using a function *LoadGPExtensionDll* exported by the *fwpolicyiomgr.dll*.

One can execute:

```
rundll32.exe fwpolicyiomgr.dll, LoadGPExtensionDll
```

to load a DLL referenced by the following Registry entry:

```
HKLM\System\CurrentControlSet\Services\mpssvc\Parameters\GPExtensionDLL=<DLL>
```

This entry was posted in [Autostart (Persistence)](https://www.hexacorn.com/blog/category/autostart-persistence/) by [adam](https://www.hexacorn.com/blog/author/adam/). Bookmark the [permalink](https://www.hexacorn.com/blog/2025/12/31/beyond-good-ol-run-key-part-149-update/ "Permalink to Beyond good ol’ Run key, Part 149 – update").

[Privacy Policy](https://www.hexacorn.com/blog/privacy-policy/) [Proudly powered by WordPress](https://wordpress.org/ "Semantic Personal Publishing Platform")
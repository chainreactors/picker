---
title: 1 little known secret of UIEOrchestratorStub.exe
url: https://www.hexacorn.com/blog/2026/09/26/1-little-known-secret-of-uieorchestratorstub-exe/
source: Hexacorn
date: 2026-09-26
fetch_date: 2026-09-27T07:24:40.378816
---

# 1 little known secret of UIEOrchestratorStub.exe

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

[← Previous](https://www.hexacorn.com/blog/2026/09/14/win11_26h2-build-xta-phantom-libraries/)
[Next →](https://www.hexacorn.com/blog/2026/09/26/1-little-known-secret-of-wincsflags-exe/)

# 1 little known secret of UIEOrchestratorStub.exe

Posted on [2026-09-26](https://www.hexacorn.com/blog/2026/09/26/1-little-known-secret-of-uieorchestratorstub-exe/ "10:28 pm")  by  [adam](https://www.hexacorn.com/blog/author/adam/ "View all posts by adam")

When you run *UIEOrchestratorStub.exe* it executes *UIEOrchestrator.exe* program located here:

```
%SystemRoot%\uus\<architecture>\UIEOrchestrator.exe
```

So, changing the *SystemRoot* environment variable to point to your chosen path will lead to execution by proxy.

On a 64-bit Windows 11 26H2, we can try this:

```
set systemroot=c:\test
UIEOrchestratorStub.exe
```

which will launch:

```
c:\test\uus\amd64\UIEOrchestrator.exe
```

This entry was posted in [Archaeology](https://www.hexacorn.com/blog/category/archaeology/), [little known secrets](https://www.hexacorn.com/blog/category/little-known-secrets/), [LOLBins](https://www.hexacorn.com/blog/category/living-off-the-land/lolbins/) by [adam](https://www.hexacorn.com/blog/author/adam/). Bookmark the [permalink](https://www.hexacorn.com/blog/2026/09/26/1-little-known-secret-of-uieorchestratorstub-exe/ "Permalink to 1 little known secret of UIEOrchestratorStub.exe").

[Privacy Policy](https://www.hexacorn.com/blog/privacy-policy/) [Proudly powered by WordPress](https://wordpress.org/ "Semantic Personal Publishing Platform")
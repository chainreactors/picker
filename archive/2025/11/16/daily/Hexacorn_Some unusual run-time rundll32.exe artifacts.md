---
title: Some unusual run-time rundll32.exe artifacts
url: https://www.hexacorn.com/blog/2025/11/16/some-unusual-run-time-rundll32-exe-artifacts/
source: Hexacorn
date: 2025-11-16
fetch_date: 2025-11-17T03:12:33.062070
---

# Some unusual run-time rundll32.exe artifacts

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

[← Previous](https://www.hexacorn.com/blog/2025/11/16/1-or-more-little-secrets-of-disksnapshot-exe/)

# Some unusual run-time rundll32.exe artifacts

Posted on [2025-11-16](https://www.hexacorn.com/blog/2025/11/16/some-unusual-run-time-rundll32-exe-artifacts/ "8:53 pm")  by  [adam](https://www.hexacorn.com/blog/author/adam/ "View all posts by adam")

If you use Process Monitor as often as I do, you probably know that loading a DLL via *rundll32.exe* produces this curious set of events:

[![](https://www.hexacorn.com/blog/wp-content/uploads/2025/11/rundll32_actctx.png)](https://www.hexacorn.com/blog/wp-content/uploads/2025/11/rundll32_actctx.png)

It turns out that the code of *rundll32.exe* includes a routine called *RunDLL\_InitActCtx* that tries to load these manifests one by one (via *CreateActCtxW* API). I was hoping this may bring some unusual sideloading opportunities, but so far, I have not found any way to abuse this feature; still, I am documenting it here – perhaps you will be more successful!

This entry was posted in [Archaeology](https://www.hexacorn.com/blog/category/archaeology/) by [adam](https://www.hexacorn.com/blog/author/adam/). Bookmark the [permalink](https://www.hexacorn.com/blog/2025/11/16/some-unusual-run-time-rundll32-exe-artifacts/ "Permalink to Some unusual run-time rundll32.exe artifacts").

[Privacy Policy](https://www.hexacorn.com/blog/privacy-policy/) [Proudly powered by WordPress](https://wordpress.org/ "Semantic Personal Publishing Platform")
---
title: shell32.dll, #61
url: https://www.hexacorn.com/blog/2025/05/30/shell32-dll-61/
source: Hexacorn
date: 2025-05-31
fetch_date: 2025-10-06T22:25:44.862130
---

# shell32.dll, #61

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

[← Previous](https://www.hexacorn.com/blog/2025/05/18/shell32-dll-44-lolbin/)
[Next →](https://www.hexacorn.com/blog/2025/05/31/mscoree-dll-rundll32shimw-lolbin/)

# shell32.dll, #61

Posted on [2025-05-30](https://www.hexacorn.com/blog/2025/05/30/shell32-dll-61/ "10:29 pm")  by  [adam](https://www.hexacorn.com/blog/author/adam/ "View all posts by adam")

The function #61 exported by the shell32.dll uses an internal name *RunFileDlg*.

So, there is no surprise that running:

```
rundll32.exe shell32.dll, #61
```

presents us the familiar *Run* Dialog Box:

[![](https://www.hexacorn.com/blog/wp-content/uploads/2025/05/shell61.png)](https://www.hexacorn.com/blog/wp-content/uploads/2025/05/shell61.png)

This entry was posted in [Archaeology](https://www.hexacorn.com/blog/category/archaeology/), [Threat Hunting](https://www.hexacorn.com/blog/category/threat-hunting/) by [adam](https://www.hexacorn.com/blog/author/adam/). Bookmark the [permalink](https://www.hexacorn.com/blog/2025/05/30/shell32-dll-61/ "Permalink to shell32.dll, #61").

[Privacy Policy](https://www.hexacorn.com/blog/privacy-policy/) [Proudly powered by WordPress](https://wordpress.org/ "Semantic Personal Publishing Platform")
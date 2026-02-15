---
title: 1 little known secret of icacls.exe
url: https://www.hexacorn.com/blog/2026/02/14/1-little-known-secret-of-icacls-exe/
source: Hexacorn
date: 2026-02-14
fetch_date: 2026-02-15T04:25:34.492240
---

# 1 little known secret of icacls.exe

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

[← Previous](https://www.hexacorn.com/blog/2026/01/03/beyond-good-ol-run-key-part-156/)
[Next →](https://www.hexacorn.com/blog/2026/02/14/1-little-known-secret-of-net-exe/)

# 1 little known secret of icacls.exe

Posted on [2026-02-14](https://www.hexacorn.com/blog/2026/02/14/1-little-known-secret-of-icacls-exe/ "12:22 am")  by  [adam](https://www.hexacorn.com/blog/author/adam/ "View all posts by adam")

Continuing the tradition of exploring lesser-known features of very well-known executables today we will look at *icacls.exe* program.

`ICACLS
(Integrity Control Access Control List) is a command-line utility in Windows (Vista and later) used to view, modify, backup, or restore Access Control Lists (ACLs) for files and folders on NTFS systems. It serves as a modern, more capable replacement for the older cacls command, allowing administrators to manage permissions, user rights, and inheritance.`

There is an undocumented */dbg* command line argument we can add to *icacls.exe* program invocations that may help us to see additional, more granular information in the output.

For instance,

```
icacls notepad.exe
vs.
icacls notepad.exe /dbg
```

[![](https://www.hexacorn.com/blog/wp-content/uploads/2026/02/icacls_dbg.png)](https://www.hexacorn.com/blog/wp-content/uploads/2026/02/icacls_dbg.png)

This entry was posted in [little known secrets](https://www.hexacorn.com/blog/category/little-known-secrets/), [Living off the land](https://www.hexacorn.com/blog/category/living-off-the-land/) by [adam](https://www.hexacorn.com/blog/author/adam/). Bookmark the [permalink](https://www.hexacorn.com/blog/2026/02/14/1-little-known-secret-of-icacls-exe/ "Permalink to 1 little known secret of icacls.exe").

[Privacy Policy](https://www.hexacorn.com/blog/privacy-policy/) [Proudly powered by WordPress](https://wordpress.org/ "Semantic Personal Publishing Platform")
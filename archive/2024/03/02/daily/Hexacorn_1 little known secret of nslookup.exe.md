---
title: 1 little known secret of nslookup.exe
url: https://www.hexacorn.com/blog/2024/03/01/1-little-known-secret-of-nslookup-exe/
source: Hexacorn
date: 2024-03-02
fetch_date: 2025-10-04T12:10:39.196012
---

# 1 little known secret of nslookup.exe

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

[← Previous](https://www.hexacorn.com/blog/2024/01/21/how-to-become-continue-to-be-a-security-researcher/)
[Next →](https://www.hexacorn.com/blog/2024/03/03/1-little-known-secret-of-explorer-exe/)

# 1 little known secret of nslookup.exe

Posted on [2024-03-01](https://www.hexacorn.com/blog/2024/03/01/1-little-known-secret-of-nslookup-exe/ "11:59 pm")  by  [adam](https://www.hexacorn.com/blog/author/adam/ "View all posts by adam")

I was recently surprised by the fact that Windows’ *nslookup.exe* accepts the local config file *.nslookuprc*. When the program starts it resolves the environment variable *HOME* and then looks for a *%HOME%\.nslookuprc* file. It then reads this config file (if it exists) line by line.

More details about syntax can be found [here](https://www.computerhope.com/nslookup.htm).

This entry was posted in [little known secrets](https://www.hexacorn.com/blog/category/little-known-secrets/), [Living off the land](https://www.hexacorn.com/blog/category/living-off-the-land/), [LOLBins](https://www.hexacorn.com/blog/category/living-off-the-land/lolbins/) by [adam](https://www.hexacorn.com/blog/author/adam/). Bookmark the [permalink](https://www.hexacorn.com/blog/2024/03/01/1-little-known-secret-of-nslookup-exe/ "Permalink to 1 little known secret of nslookup.exe").

[Privacy Policy](https://www.hexacorn.com/blog/privacy-policy/) [Proudly powered by WordPress](https://wordpress.org/ "Semantic Personal Publishing Platform")
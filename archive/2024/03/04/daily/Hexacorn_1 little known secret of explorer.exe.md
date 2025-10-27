---
title: 1 little known secret of explorer.exe
url: https://www.hexacorn.com/blog/2024/03/03/1-little-known-secret-of-explorer-exe/
source: Hexacorn
date: 2024-03-04
fetch_date: 2025-10-04T12:08:49.467178
---

# 1 little known secret of explorer.exe

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

[← Previous](https://www.hexacorn.com/blog/2024/03/01/1-little-known-secret-of-nslookup-exe/)
[Next →](https://www.hexacorn.com/blog/2024/03/16/lolbin-wow-ltd-x-2/)

# 1 little known secret of explorer.exe

Posted on [2024-03-03](https://www.hexacorn.com/blog/2024/03/03/1-little-known-secret-of-explorer-exe/ "12:33 am")  by  [adam](https://www.hexacorn.com/blog/author/adam/ "View all posts by adam")

Windows Explorer is a beast. It does so many things when it starts that it hurts…

Sometimes, literally.

One of the things it checks during its startup routine is the comparison of the Registry value HKEY\_CURRENT\_USER\Control Panel\Appearance\SchemeLangID and the result of the call to GetUserDefaultUILanguage API. If they do not match, it attempts to load a ‘desk.cpl’ library and call its UpdateCharsetChanges function.

So….

We can create a dodgy desk.cpl, copy explorer.exe to the same folder, kill all the explorer.exe instances, and then make sure the Registry value doesn’t match the result of the call to GetUserDefaultUILanguage API. Then we can run explorer.exe from that folder and the lame lolbin magic happens:

[![](https://www.hexacorn.com/blog/wp-content/uploads/2024/03/explored_desked.png)](https://www.hexacorn.com/blog/wp-content/uploads/2024/03/explored_desked.png)

This entry was posted in [little known secrets](https://www.hexacorn.com/blog/category/little-known-secrets/), [Living off the land](https://www.hexacorn.com/blog/category/living-off-the-land/), [LOLBins](https://www.hexacorn.com/blog/category/living-off-the-land/lolbins/) by [adam](https://www.hexacorn.com/blog/author/adam/). Bookmark the [permalink](https://www.hexacorn.com/blog/2024/03/03/1-little-known-secret-of-explorer-exe/ "Permalink to 1 little known secret of explorer.exe").

[Privacy Policy](https://www.hexacorn.com/blog/privacy-policy/) [Proudly powered by WordPress](https://wordpress.org/ "Semantic Personal Publishing Platform")
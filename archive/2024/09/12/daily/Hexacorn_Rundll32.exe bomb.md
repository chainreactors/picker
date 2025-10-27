---
title: Rundll32.exe bomb
url: https://www.hexacorn.com/blog/2024/09/11/rundll32-exe-bomb/
source: Hexacorn
date: 2024-09-12
fetch_date: 2025-10-06T18:25:43.913922
---

# Rundll32.exe bomb

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

[← Previous](https://www.hexacorn.com/blog/2024/09/07/this-post-is-totally-iconic/)
[Next →](https://www.hexacorn.com/blog/2024/09/14/the-delayed-import-table-phantomdll-opportunities/)

# Rundll32.exe bomb

Posted on [2024-09-11](https://www.hexacorn.com/blog/2024/09/11/rundll32-exe-bomb/ "10:08 pm")  by  [adam](https://www.hexacorn.com/blog/author/adam/ "View all posts by adam")

**Update**

Turns out [@sixtyvividtails](https://x.com/sixtyvividtails) has already [discovered](https://x.com/sixtyvividtails/status/1806114516398166477) the very same issue via a minimalist PE file back in June. Touche!

**Old Post**

This is a silly example of a basic mistake leading to a funny discovery…

When I was experimenting with the [imported](https://www.hexacorn.com/blog/2024/09/03/rundll32-and-phantom-dll-lolbins/) [phantom DLLs](https://www.hexacorn.com/blog/2024/09/04/rundll32-and-phantom-dll-lolbins-32-bit-version/) I accidentally placed a dummy 64-bit DLL in a place of a 32-bit phantom DLL called *WDSUTIL.dll* that was imported by the 32-bit *uxlib.dll*. I then attempted to enforce loading of *uxlib.dll* with a 32-bit version of rundll32.exe by referencing its full path c:\WINDOWS\SysWOW64\rundll32.exe:

```
c:\windows\syswow64\rundll32 uxlib.dll bar
```

Turns out that loading of the 32-bit library with an import that points to DLL that is actually 64-bit creates a chain of never-ending executions of the very same command line!

What happens is that when the 32-bit DLL (*uxlib.dll*) is loaded, the importing fails on the 64-bit phantomDLL (*WDSUTIL.dll*) which leads *rundll32.exe* to receive the ERROR\_BAD\_EXE\_FORMAT error from the loading attempt, which in turn leads it to follow the internal *\_TryWow64Scenario* path in its code, which… literally means creating a new SysWow64’s *rundll32.exe* process with the very same command line passed to it – aka repeating the cycle that we have started this test with!

This leads to a cascade of new *rundll32.exe* processes being spawn, and it’s similar in nature to [*regsvr32.exe* bomb](https://www.hexacorn.com/blog/2023/12/28/1-little-known-secret-of-regsvr32-exe-take-three/):

[![](https://www.hexacorn.com/blog/wp-content/uploads/2024/09/rundll32_bomb.png)](https://www.hexacorn.com/blog/wp-content/uploads/2024/09/rundll32_bomb.png)

Yes, it is a dolbin!

This entry was posted in [Archaeology](https://www.hexacorn.com/blog/category/archaeology/), [dolbin](https://www.hexacorn.com/blog/category/living-off-the-land/dolbin/), [Living off the land](https://www.hexacorn.com/blog/category/living-off-the-land/) by [adam](https://www.hexacorn.com/blog/author/adam/). Bookmark the [permalink](https://www.hexacorn.com/blog/2024/09/11/rundll32-exe-bomb/ "Permalink to Rundll32.exe bomb").

[Privacy Policy](https://www.hexacorn.com/blog/privacy-policy/) [Proudly powered by WordPress](https://wordpress.org/ "Semantic Personal Publishing Platform")
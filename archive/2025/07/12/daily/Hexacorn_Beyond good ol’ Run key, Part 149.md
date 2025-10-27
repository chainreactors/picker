---
title: Beyond good ol’ Run key, Part 149
url: https://www.hexacorn.com/blog/2025/07/11/beyond-good-ol-run-key-part-149/
source: Hexacorn
date: 2025-07-12
fetch_date: 2025-10-06T23:28:34.570872
---

# Beyond good ol’ Run key, Part 149

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

[← Previous](https://www.hexacorn.com/blog/2025/07/05/beyond-good-ol-run-key-part-148/)
[Next →](https://www.hexacorn.com/blog/2025/07/12/1-little-known-secret-of-advpack-dll-launchinfsection/)

# Beyond good ol’ Run key, Part 149

Posted on [2025-07-11](https://www.hexacorn.com/blog/2025/07/11/beyond-good-ol-run-key-part-149/ "11:10 pm")  by  [adam](https://www.hexacorn.com/blog/author/adam/ "View all posts by adam")

This post is a nothing burger. I didn’t make it work, but I still want to document it.

When I came across a ‘GPExtensionDLL’ entry expected under

```
HKLM\SYSTEM\CurrentControlSet\Services\MPSSVC\Parameters
```

I got excited, because it looked like a typical undocumented registry entry that can be abused for persistence.

After setting it up, as usual, to point to my test DLL I restarted the system only to discover the system … crashing.

After a few back and forth, it downed on me that the code that loads that DLL is surrounded by other code that relies on code pointers expected to be hard coded to point to proper function addresses, which is not always the case, hence system BSODs after calls to a null pointer-based function.

So, does this entry deserve to be even mentioned in this series?

I think so.

We cannot exclude the possibility someone will figure it out better than me, there is always an opportunity to stop the execution after the main DLL module is loaded, and in general, one of the goals of this series is to document ALL possible persistence mechanisms out there, no matter how difficult it is to actually take advantage of them…

This entry was posted in [Autostart (Persistence)](https://www.hexacorn.com/blog/category/autostart-persistence/) by [adam](https://www.hexacorn.com/blog/author/adam/). Bookmark the [permalink](https://www.hexacorn.com/blog/2025/07/11/beyond-good-ol-run-key-part-149/ "Permalink to Beyond good ol’ Run key, Part 149").

[Privacy Policy](https://www.hexacorn.com/blog/privacy-policy/) [Proudly powered by WordPress](https://wordpress.org/ "Semantic Personal Publishing Platform")
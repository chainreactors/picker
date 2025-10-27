---
title: Portability of old Windows programs…
url: https://www.hexacorn.com/blog/2024/11/23/portability-of-old-windows-programs/
source: Hexacorn
date: 2024-11-24
fetch_date: 2025-10-06T19:14:40.124943
---

# Portability of old Windows programs…

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

[← Previous](https://www.hexacorn.com/blog/2024/11/23/how-to-debug-windows-service-processes-in-the-most-old-school-possible-way/)
[Next →](https://www.hexacorn.com/blog/2024/11/28/browsing-the-browsers/)

# Portability of old Windows programs…

Posted on [2024-11-23](https://www.hexacorn.com/blog/2024/11/23/portability-of-old-windows-programs/ "7:02 pm")  by  [adam](https://www.hexacorn.com/blog/author/adam/ "View all posts by adam")

Many people believe that native Windows programs are so deeply integrated with OS that there is no way to move them between these different OS versions. And it’s fair to say that at first this belief was reinforced by that good ol’ fashioned System File Protection (SFP) service, only to be later replaced by the Trusted Installer.

The new Windows 11 Notepad app can be very annoying, plus the news about Notepad AI integration are kinda worrying, so many people revert to Registry hacks to bring the ‘[old Notepad](https://www.hexacorn.com/blog/2024/10/26/some-notes-on-windows-11-notepad/)‘ back. There are more ways than one to address this problem, and this post will focus on one of them, one that is less known…

You may not be aware, but the old Windows XP Notepad still works on Windows 11. Secondly, the same can be said about Windows 10 Notepad.

You can literally copy *c:\WINDOWS\NOTEPAD.EXE* from Windows XP or Windows 10 to Windows 11 and it will work like a charm. For later versions of Windows, the *Notepad.exe* requires language resource files to be copied as well, so you may want to copy the following files:

* *c:\Windows\notepad.exe*
* *c:\Windows\en-US\notepad.exe.mui*

Once you bring these old versions of Notepad to Windows 11 you can just store them in any directory you want. They are — believe or not — fully portable.

The very same can be said about Windows Calculator. While the Win10 Calculator was the first one pushing the Windows App agenda, the Windows XP Calculator can still run on Windows 11 w/o any issue:

[![](https://www.hexacorn.com/blog/wp-content/uploads/2024/11/calc.png)](https://www.hexacorn.com/blog/wp-content/uploads/2024/11/calc.png)
[![](https://www.hexacorn.com/blog/wp-content/uploads/2024/11/calc2.png)](https://www.hexacorn.com/blog/wp-content/uploads/2024/11/calc2.png)

Just copy the *c:\WINDOWS\System32\calc.exe* from Windows XP to Windows 11 and it will just run.

The portability of old Windows programs cannot be underestimated. With all the changes to the Windows ecosystem, with all these embedded-by-default program manifests, with all the push towards Windows Apps, ad-centric ecosystem, we still have a small window of opportunity to preserve the software that was just good at doing one thing – user-friendly programs that worked: offline, ad-, and telemetry-free.

This entry was posted in [Archaeology](https://www.hexacorn.com/blog/category/archaeology/), [Windows 11](https://www.hexacorn.com/blog/category/windows-11/) by [adam](https://www.hexacorn.com/blog/author/adam/). Bookmark the [permalink](https://www.hexacorn.com/blog/2024/11/23/portability-of-old-windows-programs/ "Permalink to Portability of old Windows programs…").

[Privacy Policy](https://www.hexacorn.com/blog/privacy-policy/) [Proudly powered by WordPress](https://wordpress.org/ "Semantic Personal Publishing Platform")
---
title: Beyond good ol’ Run key, Part 151
url: https://www.hexacorn.com/blog/2025/09/08/beyond-good-ol-run-key-part-151/
source: Hexacorn
date: 2025-09-09
fetch_date: 2025-10-02T19:50:46.107454
---

# Beyond good ol’ Run key, Part 151

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

[← Previous](https://www.hexacorn.com/blog/2025/09/03/dll-forwardsideloading-part-2/)
[Next →](https://www.hexacorn.com/blog/2025/09/19/enter-sandbox-30-static-analysis-gone-wrong/)

# Beyond good ol’ Run key, Part 151

Posted on [2025-09-08](https://www.hexacorn.com/blog/2025/09/08/beyond-good-ol-run-key-part-151/ "11:46 pm")  by  [adam](https://www.hexacorn.com/blog/author/adam/ "View all posts by adam")

Yes, they keep coming.

There are still many Windows persistence mechanisms that are not described properly and my mission is to cover it all.

Some of these mechanisms may be seen as archaic, unusual, or ‘there is no way it affects me’, but the reality is that with the gazillions of Windows installs worldwide, with the gazillion of random software installs on top of the main OS, we better do a good job in describing persistence mechanisms that are kinda niche, yet may still affect lots of people.

The old Xerox libraries include an interesting export function: XRTLLoadDebugger.

When it’s executed, it tries to load a DLL from one of these locations:

* HKEY\_LOCAL\_MACHINE\SOFTWARE\WOW6432Node\Xerox\CentreWare\Infrastructure\XDebug\ReleaseDll
* HKEY\_LOCAL\_MACHINE\SOFTWARE\WOW6432Node\Xerox\CentreWare\Infrastructure\XDebug\DebugDll

and

HKEY\_LOCAL\_MACHINE\SOFTWARE\WOW6432Node\Xerox\CentreWare\Infrastructure\XDebug\Enabled must be a REG\_DWORD equal to 1.

One can use this mechanism for persistence, other may try to use it as a lolbin.

Example samples:

* 189D385DEAC14F3FFDCE54BB492846A0D7E44B52617AFABDDC5BED023699E741\_9EAF1FF74ADDB00474E05E062DA3194BDAD92D17\_3F61204C6AF09F52BBEB52DBDA9A0CC3

This entry was posted in [Autostart (Persistence)](https://www.hexacorn.com/blog/category/autostart-persistence/) by [adam](https://www.hexacorn.com/blog/author/adam/). Bookmark the [permalink](https://www.hexacorn.com/blog/2025/09/08/beyond-good-ol-run-key-part-151/ "Permalink to Beyond good ol’ Run key, Part 151").

[Privacy Policy](https://www.hexacorn.com/blog/privacy-policy/) [Proudly powered by WordPress](https://wordpress.org/ "Semantic Personal Publishing Platform")
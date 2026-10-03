---
title: EtwCheckCoverage API
url: https://www.hexacorn.com/blog/2026/10/02/etwcheckcoverage-api/
source: Hexacorn
date: 2026-10-02
fetch_date: 2026-10-03T07:13:04.907445
---

# EtwCheckCoverage API

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

[← Previous](https://www.hexacorn.com/blog/2026/09/26/1-little-known-secret-of-aidd-dll/)

# EtwCheckCoverage API

Posted on [2026-10-02](https://www.hexacorn.com/blog/2026/10/02/etwcheckcoverage-api/ "11:32 pm")  by  [adam](https://www.hexacorn.com/blog/author/adam/ "View all posts by adam")

This is a relatively new API ([EtwCheckCoverage](https://ntdoc.m417z.com/etwcheckcoverage)) that may be of interest. It is being used by a couple of DLLs and executables in Windows 11 and here’s a list of known parameters it takes:

**comdlg32.dll**
Shell\_Picker\_Show
Shell\_Picker\_Finish
Shell\_Picker\_Cancel

**dafBth.dll**
Bluetooth\_Pairing\_Cancelled
Bluetooth\_Pairing\_Succeeded
Bluetooth\_Pairing\_Failed
Bluetooth\_Pairing\_Started
Bluetooth\_Pairing\_Deleted

**diagtrack.dll**
UTC\_OsEvents\_AbnormalShutdown

**dwmcore.dll**
Dwm\_EnergyReporter\_DataDropped\_Queuing
Dwm\_EnergyReporter\_DataDropped\_MaxEntries
Dwm\_EnergyReporter\_DataDropped\_WorkerRunning

**Faultrep.dll**
WER\_Report\_AppCrash

**localspl.dll**
Printing\_Job\_Complete\_3D
Printing\_Job\_Error\_3D
Printing\_Job\_Complete
Printing\_Job\_Error
Printing\_Job\_Start\_3D
Printing\_Job\_Start

**ncsi.dll**
NLA\_Capability\_Internet
NLA\_Capability\_Internet\_ProxyAuth
NLA\_Capability\_Internet\_BehindHotspot
NLA\_Capability\_Internet\_Proxied
NLA\_Capability\_Internet\_Corp

**rasapi32.dll**
VPN\_Connection\_Failed
VPN\_Connection\_Complete

**Taskmgr.exe**
Diag\_TaskMgr\_EndTask\_FromSmallView
Diag\_TaskMgr\_EndTask\_FromDetails
Diag\_TaskMgr\_EndTask
Diag\_Taskmgr\_Launch

**tellib.dll**
UTC\_OsEvents\_AbnormalShutdown

**wersvc.dll**
WER\_Report\_AppHang

**windows.storage.dll**
Copy\_Engine\_WCIFS\_Delete\_Attempt

wlansvc.dll
Wireless\_Connection\_Success
Wireless\_Connection\_Unsuccessful

This entry was posted in [Archaeology](https://www.hexacorn.com/blog/category/archaeology/), [Windows 11](https://www.hexacorn.com/blog/category/windows-11/) by [adam](https://www.hexacorn.com/blog/author/adam/). Bookmark the [permalink](https://www.hexacorn.com/blog/2026/10/02/etwcheckcoverage-api/ "Permalink to EtwCheckCoverage API").

[Privacy Policy](https://www.hexacorn.com/blog/privacy-policy/) [Proudly powered by WordPress](https://wordpress.org/ "Semantic Personal Publishing Platform")
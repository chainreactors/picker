---
title: Performance, Diagnostics, and WMI
url: https://posts.specterops.io/performance-diagnostics-and-wmi-21f3e01790d3?source=rss----f05f8696e3cc---4
source: Posts By SpecterOps Team Members - Medium
date: 2023-07-12
fetch_date: 2025-10-04T11:57:08.132452
---

# Performance, Diagnostics, and WMI

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F21f3e01790d3&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fposts.specterops.io%2Fperformance-diagnostics-and-wmi-21f3e01790d3&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fposts.specterops.io%2Fperformance-diagnostics-and-wmi-21f3e01790d3&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## Posts By SpecterOps Team Members](https://posts.specterops.io/?source=post_page---publication_nav-f05f8696e3cc-21f3e01790d3---------------------------------------)

·

Follow publication

[![Posts By SpecterOps Team Members](https://miro.medium.com/v2/resize:fill:76:76/1*D-FDlfkqivRBQZoESrwtqw.png)](https://posts.specterops.io/?source=post_page---post_publication_sidebar-f05f8696e3cc-21f3e01790d3---------------------------------------)

Posts from SpecterOps team members on various topics relating information security

Follow publication

# Performance, Diagnostics, and WMI

[![Steven F](https://miro.medium.com/v2/da:true/resize:fill:64:64/0*o11ibKUgsfShMjYZ)](https://medium.com/%400xthirteen?source=post_page---byline--21f3e01790d3---------------------------------------)

[Steven F](https://medium.com/%400xthirteen?source=post_page---byline--21f3e01790d3---------------------------------------)

9 min read

·

Jul 11, 2023

--

1

Listen

Share

Windows offers tons of useful tools that administrators can leverage to perform their daily jobs. A lot of times, those tools are looked at from an offensive standpoint and use cases for them are discovered. Earlier this year I read a message from a co-worker Lee Christensen ([@tifkin\_](https://twitter.com/tifkin_)) about [Service Performance DLLs](https://learn.microsoft.com/en-us/windows/win32/perfctrs/providing-counter-data-using-a-performance-dll) and upon further review, it seemed like there was potential for new opportunities to come from it.

**Quick Background**

Windows constantly collects performance data, which administrators can then use for troubleshooting and other purposes. A common tool that is leveraged is Performance Monitor, which gives information that Windows collected for services, processes or other host activity. The collected pieces of information come from libraries provided by applications, Windows’ PerfLib, or from Windows-provided DLLs. There are two versions of performance data collection specified by Windows (V1 and V2). Microsoft recommends going forward to leverage V2, but there are still V1 collectors around that will be useful for us in regards to lateral movement.

The performance collector version will determine where in the registry necessary files are referenced. For V1 providers, this is stored in *Computer\HKEY\_LOCAL\_MACHINE\SYSTEM\CurrentControlSet\Services\<Service Name\Performance* while V2 is stored in *Computer\HKEY\_LOCAL\_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Perflib\\_V2Provider*.

Performance Monitor knows what information to collect based on information located in INI files that are read into the registry. The information in the INI files includes counters and instances that are collected for the specific service. Each service that has performance monitors registered has their INI files in *C:\Windows\INF\<Service Name>.*

Press enter or click to view image in full size

![]()

DNS Service INI File

As an example is the DNS service on a Windows Server has a counter of “Total Query Received,” which (as you can guess) is a performance monitor for the total number of DNS queries the host has received. Outside of Performance Monitor, Windows offers other ways for administrators to get data from these counters. We’ll dive a little bit into this information later in the blog, but for now, I’ll just summarize and state that this information can be gathered either locally or remotely.

**Weaponization**

One thing that I try to look for from time to time is an alternative for lateral movement outside of what is public information; of that, is identifying new methods of leveraging what is already known. For example, creating a new way of executing something through WMI without leveraging common classes such as [Win32\_Process](https://learn.microsoft.com/en-us/windows/win32/cimwin32prov/win32-process), [Win32\_Service](https://learn.microsoft.com/en-us/windows/win32/cimwin32prov/win32-service), or [Win32\_ScheduledJob](https://learn.microsoft.com/en-us/windows/win32/cimwin32prov/win32-scheduledjob) (or any of the techniques laid out [here](https://www.cybereason.com/blog/wmi-lateral-movement-win32)). Taking what we know about performance data collection, we can leverage two classes for lateral movement: [Win32\_PerfFormattedData](https://learn.microsoft.com/en-us/windows/win32/cimwin32prov/win32-perfformatteddata) and [Win32\_PerfRawData](https://learn.microsoft.com/en-us/windows/win32/cimwin32prov/win32-perfrawdata). The classes provide ways of collecting and displaying performance data based on particular services or software that is installed on the host. We can use a few methods to get information about what is available to us on local or remote hosts using registry querying and WMI.

To weaponize this, we will want to identify collectors that have DLLs associated with them in the registry. There are multiple ways we can go about doing this. We can use something like this to recurse this registry path to find any services that would have a Performance registry key and values

Get-ChildItem -Path ‘HKLM:\SYSTEM\CurrentControlSet\Services’ -Recurse | Where-Object { $\_.PSPath -like “\*Performance\*” } | ForEach-Object { Write-Output $\_.PSPath }

Press enter or click to view image in full size

![]()

PowerShell Command For Querying Registry

If we want to see a list of classes and objects we can collect data from, you could also do something like:

Get-WmiObject Win32\_PerfFormattedData | Select-Object \_\_CLASS | Sort-Object -Unique -Property \_\_CLASS | format-list

Press enter or click to view image in full size

![]()

Collecting Win32\_PerfFormattedData Information

Keep in mind this will return everything that is registered with the Win32\_PerfFormattedData class and not just DLLs we can modify in the registry; ergo, not every value here should be considered as immediately abusable. These PowerShell one liners are for local enumeration, but this data can also be gathered remotely.

Returning to our Windows Server DNS service example, the Performance registry key typically has a few subkeys that we could leverage for successful execution.

Press enter or click to view image in full size

![]()

Registry Entry for DNS Service Performance

The “Library” value contains the location of the DLL that is collecting the Performance information. When WMI collects the data, that DLL is loaded and, depending on the counter, will collect that information and update values. In order for that collection to take place, the Performance Monitor needs to know which functions to run for each piece of the collection. The Open, Collect, and Close values are where this information comes from. When th...
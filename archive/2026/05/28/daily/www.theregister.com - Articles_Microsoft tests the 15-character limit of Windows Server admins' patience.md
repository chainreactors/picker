---
title: Microsoft tests the 15-character limit of Windows Server admins' patience
url: https://www.theregister.com/oses/2026/05/28/microsoft-tests-the-15-character-limit-of-windows-server-admins-patience/5247943
source: www.theregister.com - Articles
date: 2026-05-28
fetch_date: 2026-05-29T06:06:32.168059
---

# Microsoft tests the 15-character limit of Windows Server admins' patience

[Jump to main content](#main)

Search

TOPICS

* Security
  + [All Security](/security)
  + [Cyber-crime](/cyber_crime)
  + [Patches](/patches)
  + [Research](/research)
  + [CSO](/cso)
* Off-Prem
  + [All Off-Prem](/off_prem)
  + [Edge + IoT](/edge_iot)
  + [Channel](/channel)
  + [PaaS + IaaS](/tag/paas-iaas)
  + [SaaS](/saas)
* On-Prem
  + [All On-Prem](/on_prem)
  + [Systems](/systems)
  + [Storage](/storage)
  + [Networks](/networks)
  + [HPC](/hpc)
  + [Personal Tech](/personal_tech)
  + [Cx0](/cxo)
  + [Public Sector](/public-sector)
* Software
  + [All Software](/software)
  + [AI + ML](/tag/ai-ml)
  + [Applications](/applications)
  + [Databases](/databases)
  + [DevOps](/devops)
  + [OSes](/oses)
  + [Virtualization](/virtualization)
* Offbeat
  + [All Offbeat](/offbeat)
  + [Columnists](/columnists)
  + [Science](/science)
  + [BOFH](/bofh)
  + [Legal](/legal)
  + [Bootnotes](/bootnotes)
  + [Site News](/site_news)
  + [About Us](https://www.theregister.com/about_us)

* Special Features
  + [All Special Features](/special_features)
  + [HPE: AI Explainers](/explainer/ai-explainer)
  + [RSA Conference](/special_features/rsa)
  + [Agentic AI](/special_features/agentic_ai)
  + [The Future of the Datacenter](/special_features/future_of_the_datacenter)
  + [AWS:Reinvent](/special_features/aws_reinvent)
  + [Nvidia GTC](/special_features/nvidia_gtc)
  + [SC25](/special_features/2025_11_sycomp_supercomputing)
  + [Supercomputing Month](/special_features/2025_11_supercomputing_month)
  + [Computex 2026](/special_features/computex)
* Vendor Voice
  + [All Vendor Voice](https://vendorvoice.theregister.com/)
  + [Infinidat](https://vendorvoice.theregister.com/infinidat/)
  + [Everpure](https://vendorvoice.theregister.com/everpure/)
  + [Rubrik](https://vendorvoice.theregister.com/rubrik/)
  + [Make it real with Capgemini and AWS](https://vendorvoice.theregister.com/aws_capgemini/)
  + [Money Movement Hub](https://vendorvoice.theregister.com/aws_fis/)
  + [ZTE](https://vendorvoice.theregister.com/zte_news_and_stories/)
  + [Nutanix: Scale Kubernetes. Not Chaos.](https://vendorvoice.theregister.com/nutantix_cloud_native_apps/)
  + [AWS New Horizon](https://vendorvoice.theregister.com/aws_new_horizon/)
* Resources
  + [Intelligence](https://intelligence.theregister.com)
  + [Webinars & Events](https://intelligence.theregister.com/events/list/)
  + [Newsletters](https://account.theregister.com/login?r=https%3A%2F%2Faccount.theregister.com%2Fedit%2Fnewsletter%2F)

Search

[![Go to frontpage. Logo, The Register](/view-resources/dachser2/public/theregister/logo.svg)](https://www.theregister.com)

[![Go to frontpage. Logo, The Register](/view-resources/dachser2/public/theregister/logo.svg)](https://www.theregister.com)

[![Go to frontpage. Logo, The Register](/view-resources/dachser2/public/theregister/logo.svg)](https://www.theregister.com)

* [Sign in](https://account.theregister.com/login)

* [Datacenter](/tag/datacenter)
* [Security](/security)
* [Microsoft](/tag/microsoft)
* [AWS](/tag/aws)
* [Developer](/tag/developer)
* [Open Source](/tag/open%20source)
* [IT Careers](/tag/tech%20jobs)
* [Columnists](/tag/columnists)
* [Who, Me?](/tag/who%20me)
* [On Call](/tag/on%20call/)

REG AD

OSes

# Microsoft tests the 15-character limit of Windows Server admins' patience

May security update trips over hostnames of a very specific length

Richard Speed
[Richard
Speed](https://www.theregister.com/author/richard-speed)

Published
thu 28 May 2026 // 17:30 UTC

Windows Server 2016 might be long in the tooth but that isn't about to stop Microsoft breaking stuff.

The May 12 security update introduced another bug for administrators to worry about. [According](https://support.microsoft.com/en-gb/topic/may-12-2026-kb5087537-os-build-14393-9140-2ef98591-73f0-4517-9fa0-12764b51858f) to Microsoft, if the server hostname is exactly 15 characters long (like, for example, THEY-NEVER-TEST), domain controller discovery might fail.

In the notes for the glitch, Microsoft wrote: "When the hostname is 15 characters long, DCLocator calls (for example, using nltest /dsgetdc:<domain> /pdc) will return ERROR\_INVALID\_PARAMETER, preventing applications and administrative tools from locating a domain controller."

REG AD

In other words, anything that depends on a domain controller lookup might stop working. As an example, Microsoft gave Distributed File System (DFS) Namespace management, which would certainly be inconvenient. DFS Namespaces is a Windows Server role that allows admins to group shared folders across different servers into a single namespace. A single path can lead to files located on multiple servers. Unless, of course, the domain controller lookup is broken.

REG AD

Microsoft lists no workaround for affected users, though changing the server hostname to something other than 15 characters would presumably avoid the trigger. "The issue is under investigation, and additional information will be shared as soon as it becomes available," it said.

Microsoft still [officially supports](https://learn.microsoft.com/en-us/lifecycle/products/windows-server-2016) Windows Server 2016. Mainstream support ended in 2022, but extended support will continue until January 12, 2027. Microsoft is offering up to three more years of support via the Extended Security Updates (ESU) program after that.

## MORE CONTEXT

* [### Windows boot partition runs out of space for Microsoft's May security update](/oses/2026/05/18/windows-boot-partition-runs-out-of-space-for-microsofts-may-security-update/5241799)
* [### Microsoft releases Server 2016, complete with commercial Docker engine](/off-prem/2016/09/26/microsoft-releases-server-2016-complete-with-commercial-docker-engine/663065)
* [### Microsoft puts stability in the driver's seat with new initiative](/oses/2026/05/15/microsoft-puts-stability-in-the-drivers-seat-with-new-initiative/5241381)
* [### Windows 11 tops market share as 10 faces extended farewell](/software/2026/03/02/windows-11-tops-market-share-as-10-faces-extended-farewell/4577624)

Earlier this year, Esben Dochy of Lansweeper told The Register that the operating system accounted for just 2.2 percent of all Windows devices it tracks, but 20.3 percent of all servers. That figure is unlikely to have dropped dramatically in the months since, so there is a fair chance that an administrator with a 15-character hostname could be affected.

In addition to the Windows Server 2016 problems, the May 2026 security update [has failed during installation](https://www.theregister.com/oses/2026/05/18/windows-boot-partition-runs-out-of-space-for-microsofts-may-security-update/5241799) on some Windows 11 devices when the EFI System Partition is insufficient in size.

It is reassuring to know Microsoft's talent for breakage shows no bias toward any particular vintage.   ®

[active directory](/tag/active%20directory)
[security](/tag/security)
[patch](/tag/patch)
[microsoft](/tag/microsoft)
[windows server 2016](/tag/windows%20server%202016)
[oses](/tag/oses)

REG AD

[![](https://image.theregister.com/225434.jpg?imageId=225434&panox=0.00&panoy=0.00&panow=100.00&panoh=100.00&heightx=0.00&heighty=0.00&heightw=100.00&heighth=100.00&width=960&height=432&format=webp&format=jpg)

Security

## Troops’ phones gave away location data to foreign adversaries

Lawmakers push DoD to tighten smartphone controls after adversaries exploited commercial tracking data](https://www.theregister.com/security/2026/05/28/troops-phones-leaked-location-data-to-foreign-adversaries/5248108)

[Security

## Disgruntled 0-day hunter 'humiliated' by Microsoft pledges 'bone shattering drop' as Redmond calls cops

Six 0-days, three under active exploitation, more to come on July 14?](https://www.theregister.com/security/2026/05/28/microsoft-0-day-feud-escalates-as-researcher-threatens-another-windows-exploit-dump/5248085)

[THE REGISTER EXPLAINER

## Explainer: Edge AI

You can run AI at the edge, if your infrastructure supports i...
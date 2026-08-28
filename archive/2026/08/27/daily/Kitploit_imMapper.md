---
title: imMapper
url: https://kitploit.com/en/tools/github/ioallocate/immapper
source: Kitploit
date: 2026-08-27
fetch_date: 2026-08-28T13:36:41.782946
---

# imMapper

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

Kitploit is a directory of hacking, cybersecurity, and pentesting tools. Discover the latest project updates to find vulnerabilities, analyze systems, automate testing, and strengthen your security.

·Analytics preferences·[Feeds](/en/feeds)·[Contact](/en/contact)·[Privacy](/en/privacy)·© 2026 Kitploit

Tool Directory

## Categories

[View all categories](/en/categories)

Loading categories

[Tools](/en/tools)/![GitHub](/providers/github.png)GitHub/ioallocate/immapper

![](https://assets.kitploit.com/production/public/tools/53211/ed7d69a10dd604cf961995bc5f8d8aa0c046935aea8b0c6a0845875ac7f5c0a3-display-v1.webp)

[Vulnerability Analysis](/en/categories/vulnerability-analysis)[Exploitation](/en/categories/exploitation)[Hardware Security](/en/categories/hardware-security)[Learning & Education](/en/categories/education)[Binary Exploitation](/en/categories/binary-exploitation)

![GitHub](/providers/github.png)ioallocate/immapper

# imMapper

Demonstration of Abusing the Vulnerable driver AmdTools64.sys for Physical R/W.

[View Repository](https://github.com/ioallocate/immapper)

92402 days ago![Not yet reviewed](/_next/image?url=%2Fbadges%2Fkitploit_badge_not_reviewed_full.png&w=48&q=75)

### Most Popular

[View all →](/en/tools)

Discover the most used tools by our community.

Last 7 DaysLast 30 Days

Explore all tools

Browse our collection of tools

[View all tools →](/en/tools)

Share

# imMapper

* A Demonstration on how to abuse the Vulnerable Driver AmdTools64. The Driver has the ability to (only) Read/Write Kernel Space Memory, as well as to Read/Write the MSR. This requires Admin Privileges. The driver is distributed trough the tool [RGBFusion-2](https://www.gigabyte.com/microsite/512/rgb2.html).

## Exclamation-mark

* This Demonstration is only for Learning Purposes, and I Discourage the Misuse of this vulnerability, as of 8/25/2026 there is no valid CVE and is not in progress, any future CVE will not be of the original author, me.

## Question-mark

* I came upon this driver after looking through older dm's on discord, ive found an interesting dm of [sigwl](https://github.com/sigwl) showcasing me his vulnerable driver called "RGBMini", this got me researching for other possible vulnerable driver in such theme.
* At the address 0x140005380 the device object is registered with the SDDL D:P(A;;GA;;;SY)(A;;GA;;;BA), which means only the system and admins can open a handle. The Dispatch Handler at 0x1400058D8, the Vulnerability lies in it. It gives the usermode the parameters of dangerous operations, like when reading and writing physical memory instead of range and size checking, nothing is validated and everything is usermode passed.

![Asset/SDDLSnippet](https://assets.kitploit.com/production/public/readmes/53211/28ce07e7e58d2b28b838a476fcc02943972a977fa3f485c75491b1fe2a338308/45bf8bf8a78cf7cd92790f50dc0386fda37bab0e8af5fb0a2a9e448b72d4ca6e-display-v1.webp)
![Asset/DispatcherSnippet](https://assets.kitploit.com/production/public/readmes/53211/ed7d69a10dd604cf961995bc5f8d8aa0c046935aea8b0c6a0845875ac7f5c0a3/b6138a9467a753019fb5b23dc5f8dc6523ccbb12aba54bec97519af831d9e77f-display-v1.webp)

## Add

* [IDA](https://hex-rays.com/ida-pro)

## At

* I'm crediting [Leo](https://github.com/KiUserExceptionDispatcher) for helping me with the utilities of this project.

[Download Tool](https://github.com/ioallocate/immapper)
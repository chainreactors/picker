---
title: Analyzing XFS API Calls
url: https://kaimi.io/en/2024/07/analyzing-xfs-api-calls/
source: Misc
date: 2024-07-30
fetch_date: 2025-10-06T17:42:13.175160
---

# Analyzing XFS API Calls

[Skip to content](#content)

[Misc](https://kaimi.io/en/)

Misc development

Menu

* [Home](https://kaimi.io/en/)
* [About](https://kaimi.io/en/about/)
* [![](data:image/png;base64...)English](#pll_switcher)
  + [![](data:image/png;base64...)Русский](https://kaimi.io/2024/07/xfs-api-call-analysis/)
  + [![](data:image/png;base64...)English](https://kaimi.io/en/2024/07/analyzing-xfs-api-calls/)

# Analyzing XFS API Calls

Hello, my dear readers who have been missing the posts! I know you've all been waiting for brilliant posts over the past two years. But both I and d\_x have been busy with matters that, to be honest, are second only to saving the world... or maybe not. Today's topic is [CEN/XFS](https://en.wikipedia.org/wiki/CEN/XFS), a specific and extremely necessary standard for interacting with banking equipment, more specifically, the way to analyze XFS API calls on Windows. If you still don't know what CEN/XFS is (not to be confused with XFS, the file system), then you probably had a blissful life without a headache. But for those who are ready to dive into this swamp - welcome.

**What is XFS?**
The acronym stands for "Extensions for Financial Services". It allows various applications to interact with different types of banking equipment through uniform interfaces. Imagine you need to develop software that has to communicate not with one type of equipment, but with a whole zoo of various devices. That's where XFS comes to the rescue. For a very general explanation, let me refer to the following diagram:

[![](https://kaimi.io/wp-content/uploads/2024/07/1_O4efF7bFkTvykFqxj18y-A-1024x499.webp)](https://kaimi.io/wp-content/uploads/2024/07/1_O4efF7bFkTvykFqxj18y-A.webp)
*(c) Kaspersky Lab*

XFS originated from the WOSA/XFS standard. WOSA (Windows Open Service Architecture) is an older architecture from Microsoft, which... well, everything is written in Wikipedia: <https://en.wikipedia.org/wiki/Windows_Open_Services_Architecture>. Documentation on the standard is available here: <https://www.cencenelec.eu/areas-of-work/xfs_cwa16926_350_release/>.

**msxfs.dll**
Now for the main reason this post was conceived. msxfs.dll is a small library and one of the key components of XFS (available in the [SDK](https://www.cencenelec.eu/media/CEN-CENELEC/AreasOfWork/CEN%20sectors/Digital%20Society/CWA%20Download%20Area/XFS/installer_sdk340.zip)). It acts as an intermediary between the application and various financial equipment, providing a standardized API for devices like card readers, PIN pads, receipt printers, as well as dispensers. There is a lot of malware targeting ATMs that dispense money by accessing XFS (let's skip the encryption/signature and so on aside), for instance, the old [ATMii](https://securelist.com/atmii-a-small-but-effective-atm-robber/82707/) piece of malware.
When analyzing standard ATM software, malicious software, or creating signatures to detect it, it may be useful to track which functions were called from msxfs.dll, in what order, with what arguments, etc. Historically, for such analysis in the context of WinAPI, I've used [Rohitab API Monitor](http://www.rohitab.com/apimonitor): a convenient but somewhat outdated tool.

[![](https://kaimi.io/wp-content/uploads/2024/07/API-Monitor-1024x686.png)](https://kaimi.io/wp-content/uploads/2024/07/API-Monitor.png)

It allows intercepting function calls in the context of a process and displaying information about arguments, call results, and so on. The only caveat is that it requires function and argument descriptions in XML format. While such descriptions are available for most WinAPI functions, I couldn't find one for XFS, so I had to make one myself. This file I would like to share: <https://github.com/kaimi-/xfs-api-monitor>.

Place it, for example, in the following path: `API Monitor (rohitab.com)\API\XFS\XFSAPI.xml`. After that, API Monitor will pick up the specification, and you'll be able to intercept calls to msxfs.dll functions.

[![](https://kaimi.io/wp-content/uploads/2024/07/api-xfs_hook-300x224.jpg)](https://kaimi.io/wp-content/uploads/2024/07/api-xfs_hook.jpg)

That's all for now. I'll try to publish the next post within a month, not in two years.

![//kaimi.io/wp-content/uploads/2020/04/6807153.jpeg]()Author [Kaimi](https://kaimi.io/en/author/kaimi/)Posted on [July 29, 2024](https://kaimi.io/en/2024/07/analyzing-xfs-api-calls/)Categories [For newbies](https://kaimi.io/en/category/for-newbies/), [Snippets](https://kaimi.io/en/category/snippets-en/), [Windows](https://kaimi.io/en/category/windows-en/)Tags [hook](https://kaimi.io/en/tag/hook-en/), [winapi](https://kaimi.io/en/tag/winapi-en/), [windows](https://kaimi.io/en/tag/windows-2-en/), [xfs](https://kaimi.io/en/tag/xfs-en/), [xml](https://kaimi.io/en/tag/xml-en/)

## Leave a Reply [Cancel reply](/en/2024/07/analyzing-xfs-api-calls/#respond)

Your email address will not be published. Required fields are marked \*

Comment \*

Name \*

Email \*

Website

## Post navigation

[Previous Previous post: 20 years of payment processing problems](https://kaimi.io/en/2022/07/20-years-of-payment-processing-problems-en/)

Search for:

Search

[![Telegram](//kaimi.io/wp-content/uploads/2020/06/telegram.svg)](https://t.me/kaimi_io)  [t.me/kaimi\_io](https://t.me/kaimi_io)

[![Twitter](//kaimi.io/wp-content/uploads/2020/06/twitter.svg)](https://twitter.com/kaimi_io)  [twitter.com/kaimi\_io](https://twitter.com/kaimi_io)

## Categories

* [.NET](https://kaimi.io/en/category/net-en/) (1)
* [Assembler](https://kaimi.io/en/category/assembler-en/) (3)
* [C/C++](https://kaimi.io/en/category/cpp-en/) (15)
* [C#](https://kaimi.io/en/category/c-sharp-en/) (1)
* [For newbies](https://kaimi.io/en/category/for-newbies/) (17)
* [HTML/JS](https://kaimi.io/en/category/html-js-en/) (1)
* [Interesting stuff](https://kaimi.io/en/category/interesting-stuff/) (4)
* [Microcontrollers](https://kaimi.io/en/category/microcontrollers/) (1)
* [Pentest](https://kaimi.io/en/category/pentest-en/) (3)
* [Perl](https://kaimi.io/en/category/perl-en/) (4)
* [PHP](https://kaimi.io/en/category/php-en/) (2)
* [Snippets](https://kaimi.io/en/category/snippets-en/) (4)
* [Uncategorized](https://kaimi.io/en/category/uncategorized/) (4)
* [Windows](https://kaimi.io/en/category/windows-en/) (21)

## Tags

* [adminer (1)](https://kaimi.io/en/tag/adminer-en/)
* [arm (1)](https://kaimi.io/en/tag/arm-en/)
* [chkdsk (1)](https://kaimi.io/en/tag/chkdsk-en/)
* [content discovery (1)](https://kaimi.io/en/tag/content-discovery/)
* [cortex-m (1)](https://kaimi.io/en/tag/cortex-m-en/)
* [deobfuscation (1)](https://kaimi.io/en/tag/deobfuscation/)
* [Enable-MMAgent (1)](https://kaimi.io/en/tag/enable-mmagent-en/)
* [fuzzing (1)](https://kaimi.io/en/tag/fuzzing/)
* [gui (1)](https://kaimi.io/en/tag/gui-en/)
* [HAL (1)](https://kaimi.io/en/tag/hal/)
* [hook (1)](https://kaimi.io/en/tag/hook-en/)
* [integrity check (1)](https://kaimi.io/en/tag/integrity-check/)
* [LL (1)](https://kaimi.io/en/tag/ll/)
* [Macros (2)](https://kaimi.io/en/tag/macros-en/)
* [Memory combining (1)](https://kaimi.io/en/tag/memory-combining-en/)
* [Microsoft (2)](https://kaimi.io/en/tag/microsoft/)
* [MS Word (2)](https://kaimi.io/en/tag/ms-word/)
* [nasl (1)](https://kaimi.io/en/tag/nasl-en/)
* [nessus (1)](https://kaimi.io/en/tag/nessus-en/)
* [NTFS (2)](https://kaimi.io/en/tag/ntfs-en/)
* [obfuscation (1)](https://kaimi.io/en/tag/obfuscation/)
* [page combining (1)](https://kaimi.io/en/tag/page-combining-en/)
* [payment processing (1)](https://kaimi.io/en/tag/payment-processing/)
* [payments (1)](https://kaimi.io/en/tag/payments/)
* [payment systems (1)](https://kaimi.io/en/tag/payment-systems-en/)
* [paypal (1)](https://kaimi.io/en/tag/paypal-en/)
* [Perl (1)](https://kaimi.io/en/tag/perl-en/)
* [php LockIt (1)](https://kaimi.io/en/tag/php-lockit/)
* [side channel (1)](https://kaimi.io/en/tag/side-channel/)
* [SPL (1)](https://kaimi.io/en/tag/spl/)
* [task automation (1)](https://kaimi.io/en/tag/task-automation/)
* ...
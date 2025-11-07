---
title: Memory Analysis Package 0.7
url: https://blog.cerbero.io/memory-analysis-package-0-7/
source: Cerbero Blog
date: 2025-11-06
fetch_date: 2025-11-07T03:10:18.979422
---

# Memory Analysis Package 0.7

[Skip to content](#content)

[Cerbero Blog](https://blog.cerbero.io/)

Menu

* [Home](https://cerbero.io)
* Products
  + [Cerbero Suite](https://cerbero.io/suite/)
  + [Cerbero Engine](https://cerbero.io/engine/)
* [Packages](https://cerbero.io/packages/)
* [E-Zine](https://cerbero.io/e-zine/)
* [Blog](/)
* Support
  + [User Manual](https://cerbero.io/manual/)
  + [SDK Documentation](https://sdk.cerbero.io/)
  + [FAQ](https://cerbero.io/faq/)
  + [Resources](https://cerbero.io/resources/)
  + [Contact](https://cerbero.io/contact/)
* [Shop](https://cerbero.io/shop/)
  + [My account](https://cerbero.io/my-account/)
  + [Cart](https://cerbero.io/cart/)

# Memory Analysis Package 0.7

We are excited to announce the release of the [Memory Analysis 0.7 package](https://cerbero.io/packages/memoryanalysis/), which is currently in beta. This version introduces significant improvements that partly stem from testing our solution against various CTF challenges.

These new features, together with the recent release of Cerbero Suite 8.6, make this update particularly noteworthy. Thanks to the sophisticated caching mechanism implemented in the latest release of Cerbero Suite, memory analysis is now faster than ever. If you thought it was already fast, you are in for a surprise!

* [File Scan](#file_scan)
* [Pool Scan](#pool_scan)
* [Multi-Format Input](#multi_format)
* [VMEM and VMSS Format Support](#vmem)
* [NT/LM Password Hash Decryption](#hash_dump)
* [User-Mode Memory Region Exclusion](#reg_excl)
* [Unlinked Processes Detection](#unlinked)

### File Scan

The package now includes an action that lets you scan and extract files directly from memory.

[](/wp-content/uploads/2025/11/ma07/file_scan.mp4)

All cache types are supported, so if a file was cached in memory, it can be extracted.

![](/wp-content/uploads/2025/11/ma07/file_scan.png)

### Pool Scan

You can now scan memory pools for specific items of your choice.

[](/wp-content/uploads/2025/11/ma07/pool_scan.mp4)

For each pool item found, you can inspect its associated structures and data in detail.

### Multi-Format Input

Previously, while the Windows Crash Dump format was supported through its [dedicated package](https://cerbero.io/packages/windowscrashdumpformat/), analyzing its memory snapshot required opening it as a standard file. That is no longer the case.

The memory analysis logic provider now accepts multiple input formats and automatically detects the correct one. When opening a memory dump, a dialog prompts you to select the intended format.

![](/wp-content/uploads/2025/11/ma07/multi_format.png)

### VMEM and VMSS Format Support

The VMWare VMEM format is now fully supported. Although VMEM files can sometimes represent raw memory, they sometimes rely on an accompanying VMSS (VMWare Suspended Status) file to properly reconstruct memory mappings.

Support has been added not only for the VMEM format but also for inspecting VMSS files directly, which can contain valuable state information and other useful data.

![](/wp-content/uploads/2025/11/ma07/vmss.png)

### NT/LM Password Hash Decryption

NT/LM password hashes are now decrypted automatically, allowing them to be exported and cracked using tools such as [hashcat](https://github.com/hashcat/hashcat) or [John the Ripper Jumbo](https://github.com/openwall/john).

![](/wp-content/uploads/2025/11/ma07/hash_dump.png)

This capability is especially valuable in digital forensics, where recovered credentials can help identify attacker behavior, detect privilege escalation, or uncover unauthorized access.

### User-Mode Memory Region Exclusion

There are times when it is necessary to operate only on selected user-mode memory while excluding specific regions, for instance large reserved areas that slow down analysis. [In one](https://blog.cerbero.io/memory-challenge-4-remember-me/) of the CTF challenges, we had to copy part of a process’s memory to skip such a region to improve performance.

Now, you can exclude any user-mode memory region simply by unchecking it, and the exclusion is reflected immediately in the hex view. This allows for faster mining of files, string searches, and other operations.

[](/wp-content/uploads/2025/11/ma07/reg_excl.mp4)

### Unlinked Processes Detection

It is now possible to detect unlinked processes directly by specifying it in the options.

![](/wp-content/uploads/2025/11/ma07/unlink_options.png)

Unlinked processes may appear as artifacts of dumping a live system or as a deliberate technique used by malware to hide from process listings. In the image below, you can see a malicious process that unlinked itself from the list of active processes.

![](/wp-content/uploads/2025/11/ma07/unlinked_proc.png)

We are very enthusiastic about the progress of the Memory Analysis package and look forward to demonstrating these features in action, particularly through real-world CTF challenges.

![](https://secure.gravatar.com/avatar/7a86aa69922858b8d41989621fc1ea364aae1e027546f88a54d94ab1ec2187fc?s=49&d=mm&r=g)Author [Erik Pistelli](https://blog.cerbero.io/author/cerbero/)Posted on [November 6, 2025November 6, 2025](https://blog.cerbero.io/memory-analysis-package-0-7/)Categories [Package](https://blog.cerbero.io/category/package/)Tags [Memory Forensics](https://blog.cerbero.io/tag/memory-forensics/), [VMWare](https://blog.cerbero.io/tag/vmware/), [windows](https://blog.cerbero.io/tag/windows/)

## Leave a Reply [Cancel reply](/memory-analysis-package-0-7/#respond)

Your email address will not be published. Required fields are marked \*

Comment \*

Name \*

Email \*

Website

[ ]  Save my name, email, and website in this browser for the next time I comment.

## Post navigation

[Previous Previous post: Cerbero Suite 8.6](https://blog.cerbero.io/cerbero-suite-8-6/)

Search for:

Search

## Recent Posts

* [Memory Analysis Package 0.7](https://blog.cerbero.io/memory-analysis-package-0-7/)
* [Cerbero Suite 8.6](https://blog.cerbero.io/cerbero-suite-8-6/)
* [Memory Challenge 6: Injector](https://blog.cerbero.io/memory-challenge-6-injector/)
* [Memory Challenge 5: DumpMe](https://blog.cerbero.io/memory-challenge-5-dumpme/)
* [Memory Challenge 4: Remember Me](https://blog.cerbero.io/memory-challenge-4-remember-me/)
* [AI Assistant Package (Beta)](https://blog.cerbero.io/ai-assistant-package-beta/)
* [Memory Challenge 3: Invisible](https://blog.cerbero.io/memory-challenge-3-invisible/)
* [MSI Format Package](https://blog.cerbero.io/msi-format-package/)
* [Memory Challenge 2: MEM Challenge](https://blog.cerbero.io/memory-challenge-2-mem-challenge/)
* [Memory Analysis Package 0.6](https://blog.cerbero.io/memory-analysis-package-0-6/)

## Archives

Archives

Select Month
 November 2025  (2)
 October 2025  (9)
 September 2025  (2)
 August 2025  (2)
 July 2025  (2)
 June 2025  (3)
 May 2025  (7)
 April 2025  (4)
 March 2025  (2)
 October 2024  (3)
 September 2024  (1)
 August 2024  (3)
 July 2024  (5)
 June 2024  (2)
 April 2024  (4)
 March 2024  (1)
 February 2024  (1)
 January 2024  (4)
 December 2023  (3)
 November 2023  (7)
 October 2023  (3)
 September 2023  (1)
 July 2023  (1)
 May 2023  (11)
 March 2023  (9)
 February 2023  (3)
 January 2023  (1)
 November 2022  (1)
 September 2022  (2)
 August 2022  (2)
 July 2022  (3)
 June 2022  (2)
 May 2022  (5)
 April 2022  (3)
 March 2022  (4)
 February 2022  (6)
 January 2022  (1)
 November 2021  (4)
 October 2021  (5)
 September 2021  (7)
 June 2021  (1)
 April 2021  (1)
 March 2021  (4)
 February 2021  (1)
 December 2020  (1)
 November 2020  (1)
 October 2020  (1)
 September 2020  (2)
 July 2020  (2)
 January 2020  (1)
 September 2019  (1)
 August 2019  (2)
 July 2019  (1)
 June 2019  (1)
 May 2019  (3)
 April 2019  (2)
 June 2018  (1)
 April 2018  (1)
 March 2018  (1)
 January 2018  (1)
 November 2017  (2)
 March 2017  (5)
 July 2016  (2)
 May 2016  (2)
 April 2016  (1)
 October 2015  (2)
 September 2015  (2)
 June 2015  (2)
 December 2014  (2)
 October 2014  (1)
 September 2014  (3)
 Augu...
---
title: Memory Analysis Package 0.7.6
url: https://blog.cerbero.io/memory-analysis-package-0-7-6/
source: Cerbero Blog
date: 2025-12-04
fetch_date: 2025-12-05T03:17:05.685222
---

# Memory Analysis Package 0.7.6

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
  + [Contact](https://cerbero.io/contact/)
* [Shop](https://cerbero.io/shop/)
  + [My account](https://cerbero.io/my-account/)
  + [Cart](https://cerbero.io/cart/)

# Memory Analysis Package 0.7.6

We are excited to announce the release of the [Memory Analysis 0.7.6 package](https://cerbero.io/packages/memoryanalysis/). This version introduces several improvements, some of which stem from testing our solution against various CTF challenges and didn’t make it into version 0.7.

* [Code Injection](#code_injection)
* [Unlinked Modules](#unlinked_mods)
* [Process Pool Scan](#pool_scan)
* [File Object Data Extraction](#file_obj)
* [Mapped Executable Analysis](#pe)

### Code Injection

In this release we’ve added two new options. The first is code injection detection.

![](/wp-content/uploads/2025/11/ma075/options.png)

If you didn’t select the option in the initialization dialog, you can still run the scan using the dedicated action. When code injection is detected, the following view is displayed.

![](/wp-content/uploads/2025/11/ma075/injection.png)

Each entry shows the initial bytes of the region, its disassembly, and the file format if identified. In this example, we can see an injected executable.

### Unlinked Modules

To scan for unlinked user-mode modules, use the dedicated action.

![](/wp-content/uploads/2025/11/ma075/modules.png)

Each module entry displays the lists that reference it. The selected module, for instance, does not appear in any of the linked lists.

### Process Pool Scan

You can now perform a pool scan for processes to avoid relying on system lists to retrieve them.

![](/wp-content/uploads/2025/11/ma075/pool_option.png)

While this option is slow, it is especially useful when working with corrupted memory dumps.

![](/wp-content/uploads/2025/11/ma075/broken.png)

The image above shows a memory dump that cannot be parsed correctly. The pool scan for processes allows us to at least partially explore the processes.

### File Object Data Extraction

Although the file scan introduced in version 0.7 already allowed dumping cached file data from memory, it wasn’t possible to extract the same data from object lists. This capability has now been added.

![](/wp-content/uploads/2025/11/ma075/file.png)

### Mapped Executable Analysis

It is often necessary to analyze a Portable Executable (PE) mapped in memory but not referenced anywhere. To address this, we’ve added an action that rebuilds the mapped executable so it can also be examined with external tools.

![](/wp-content/uploads/2025/11/ma075/pe.png)

Alongside these features, this release includes several minor improvements and bug fixes.

![](https://secure.gravatar.com/avatar/7a86aa69922858b8d41989621fc1ea364aae1e027546f88a54d94ab1ec2187fc?s=49&d=mm&r=g)Author [Erik Pistelli](https://blog.cerbero.io/author/cerbero/)Posted on [December 4, 2025](https://blog.cerbero.io/memory-analysis-package-0-7-6/)Categories [Package](https://blog.cerbero.io/category/package/)Tags [Code Injection](https://blog.cerbero.io/tag/code-injection/), [Memory Forensics](https://blog.cerbero.io/tag/memory-forensics/), [windows](https://blog.cerbero.io/tag/windows/)

## Leave a Reply [Cancel reply](/memory-analysis-package-0-7-6/#respond)

Your email address will not be published. Required fields are marked \*

Comment \*

Name \*

Email \*

Website

[ ]  Save my name, email, and website in this browser for the next time I comment.

## Post navigation

[Previous Previous post: Memory Challenge 10: Mellitus](https://blog.cerbero.io/memory-challenge-10-mellitus/)

Search for:

Search

## Recent Posts

* [Memory Analysis Package 0.7.6](https://blog.cerbero.io/memory-analysis-package-0-7-6/)
* [Memory Challenge 10: Mellitus](https://blog.cerbero.io/memory-challenge-10-mellitus/)
* [XST Format Package](https://blog.cerbero.io/xst-format-package/)
* [Memory Challenge 9: BankingTroubles](https://blog.cerbero.io/memory-challenge-9-bankingtroubles/)
* [InnoSetup Format Package 3.0](https://blog.cerbero.io/innosetup-format-package-3-0/)
* [Memory Challenge 8: MemLabs Lab 4 – Obsession](https://blog.cerbero.io/memory-challenge-8-memlabs-lab-4-obsession/)
* [AD1 Format Package](https://blog.cerbero.io/ad1-format-package/)
* [Memory Challenge 7: DeepDive](https://blog.cerbero.io/memory-challenge-7-deepdive/)
* [Memory Analysis Package 0.7](https://blog.cerbero.io/memory-analysis-package-0-7/)
* [Cerbero Suite 8.6](https://blog.cerbero.io/cerbero-suite-8-6/)

## Archives

Archives

Select Month
 December 2025  (2)
 November 2025  (8)
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
 August 2014  (1)
 July 2014  (1)
 December 2013  (2)
 November 2013  (5)
 October 2013  (5)
 September 2013  (6)
 August 2013  (6)
 July 2013  (1)
 June 2013  (4)
 May 2013  (7)
 April 2013  (5)
 March 2013  (3)
 February 2013  (4)
 January 2013  (3)
 December 2012  (3)
 November 2012  (5)
 October 2012  (3)
 September 2012  (1)
 August 2012  (2)
 July 2012  (2)
 June 2012  (2)
 May 2012  (2)
 April 2012  (1)
 March 2012  (6)
 February 2012  (5)
 January 2012  (8)
 November 2011  (1)
 August 2011  (1)

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
  + [Contact](https://cerbero.io/contact/)
* [Shop](https://cerbero.io/shop/)
  + [My account](https://cerbero.io/my-account/)
  + [Cart](https://cerbero.io/cart/)

[Cerbero Blog](https://blog.cerbero.io/)  [Proudly powered by WordPress](https://wordpress.org/)
---
title: Memory Challenge 11: BOughT
url: https://blog.cerbero.io/memory-challenge-11-bought/
source: Cerbero Blog
date: 2025-12-08
fetch_date: 2025-12-09T03:16:56.633521
---

# Memory Challenge 11: BOughT

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

# Memory Challenge 11: BOughT

We’re testing our [Memory Analysis package](https://cerbero.io/packages/memoryanalysis/) (currently in beta) against various challenges available online.

[](/wp-content/uploads/2025/11/bought_challenge.mp4)

We found this challenge on [Hack The Box](https://app.hackthebox.com/sherlocks/BOughT), so credit goes to them for creating it.

The scenario is as follows:

*“A non-technical client recently purchased a used computer for personal use from a stranger they encountered online. Since acquiring the computer, the client has been using it without making any changes, specifically not installing or uninstalling any software. However, they have begun experiencing issues related to internet connectivity. This includes receiving error messages such as “Server Not Found” and encountering difficulties with video streaming. Despite these problems, checks with the Windows Network Troubleshooter indicate no issues with the internet connection itself. The client has provided a memory image and disk artifacts for investigation to determine if there are any underlying issues causing these problems.”*

The challenge includes several questions. We begin by identifying the suspicious process and examining the mutex it creates. To confirm that the mutex is associated with the malware, we decompile the application directly within the memory dump, analyze its anti-debugging technique, and observe one of the files it opens on disk. Using the [AD1 Format package](https://cerbero.io/packages/ad1format/), we can access the disk artifacts to inspect the config.ini file accessed by the malware and extract the FQDN of the target website.

![](https://secure.gravatar.com/avatar/7a86aa69922858b8d41989621fc1ea364aae1e027546f88a54d94ab1ec2187fc?s=49&d=mm&r=g)Author [Erik Pistelli](https://blog.cerbero.io/author/cerbero/)Posted on [December 8, 2025](https://blog.cerbero.io/memory-challenge-11-bought/)Categories [Video](https://blog.cerbero.io/category/video/)Tags [Challenge](https://blog.cerbero.io/tag/challenge/), [Memory Forensics](https://blog.cerbero.io/tag/memory-forensics/), [windows](https://blog.cerbero.io/tag/windows/)

## Leave a Reply [Cancel reply](/memory-challenge-11-bought/#respond)

Your email address will not be published. Required fields are marked \*

Comment \*

Name \*

Email \*

Website

[ ]  Save my name, email, and website in this browser for the next time I comment.

## Post navigation

[Previous Previous post: Memory Analysis Package 0.7.6](https://blog.cerbero.io/memory-analysis-package-0-7-6/)

Search for:

Search

## Recent Posts

* [Memory Challenge 11: BOughT](https://blog.cerbero.io/memory-challenge-11-bought/)
* [Memory Analysis Package 0.7.6](https://blog.cerbero.io/memory-analysis-package-0-7-6/)
* [Memory Challenge 10: Mellitus](https://blog.cerbero.io/memory-challenge-10-mellitus/)
* [XST Format Package](https://blog.cerbero.io/xst-format-package/)
* [Memory Challenge 9: BankingTroubles](https://blog.cerbero.io/memory-challenge-9-bankingtroubles/)
* [InnoSetup Format Package 3.0](https://blog.cerbero.io/innosetup-format-package-3-0/)
* [Memory Challenge 8: MemLabs Lab 4 – Obsession](https://blog.cerbero.io/memory-challenge-8-memlabs-lab-4-obsession/)
* [AD1 Format Package](https://blog.cerbero.io/ad1-format-package/)
* [Memory Challenge 7: DeepDive](https://blog.cerbero.io/memory-challenge-7-deepdive/)
* [Memory Analysis Package 0.7](https://blog.cerbero.io/memory-analysis-package-0-7/)

## Archives

Archives

Select Month
 December 2025  (3)
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
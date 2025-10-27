---
title: Promoting a Windows 2022 server to Domain Controller and DNS Server
url: https://www.hexacorn.com/blog/2024/12/10/promoting-a-windows-2022-server-to-domain-controller-and-dns-server/
source: Hexacorn
date: 2024-12-11
fetch_date: 2025-10-06T19:40:50.094675
---

# Promoting a Windows 2022 server to Domain Controller and DNS Server

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

[← Previous](https://www.hexacorn.com/blog/2024/12/07/not-installing-the-installers-part-4/)
[Next →](https://www.hexacorn.com/blog/2024/12/15/dns-exe-and-its-quirks/)

# Promoting a Windows 2022 server to Domain Controller and DNS Server

Posted on [2024-12-10](https://www.hexacorn.com/blog/2024/12/10/promoting-a-windows-2022-server-to-domain-controller-and-dns-server/ "11:44 pm")  by  [adam](https://www.hexacorn.com/blog/author/adam/ "View all posts by adam")

I asked myself what tangible artifacts present on a file system can immediately tell us that the server system in place is a Domain Controller and/or DNS server.

I decided to run a simple experiment.

I installed a test version of Windows Server 2022, took a snapshot of the file system, then added DC and DNS capabilities, then took a snapshot of a file system again.

The (slightly edited) diff of these 2 can be found [here](http://hexacorn.com/d/win_srv_2022_dc_dns_diff.txt).

This entry was posted in [Archaeology](https://www.hexacorn.com/blog/category/archaeology/) by [adam](https://www.hexacorn.com/blog/author/adam/). Bookmark the [permalink](https://www.hexacorn.com/blog/2024/12/10/promoting-a-windows-2022-server-to-domain-controller-and-dns-server/ "Permalink to Promoting a Windows 2022 server to Domain Controller and DNS Server").

[Privacy Policy](https://www.hexacorn.com/blog/privacy-policy/) [Proudly powered by WordPress](https://wordpress.org/ "Semantic Personal Publishing Platform")
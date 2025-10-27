---
title: dns.exe and its quirks
url: https://www.hexacorn.com/blog/2024/12/15/dns-exe-and-its-quirks/
source: Hexacorn
date: 2024-12-16
fetch_date: 2025-10-06T19:35:50.140626
---

# dns.exe and its quirks

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

[← Previous](https://www.hexacorn.com/blog/2024/12/10/promoting-a-windows-2022-server-to-domain-controller-and-dns-server/)
[Next →](https://www.hexacorn.com/blog/2024/12/20/windows-server-2022-and-msmpeng-exe/)

# dns.exe and its quirks

Posted on [2024-12-15](https://www.hexacorn.com/blog/2024/12/15/dns-exe-and-its-quirks/ "12:21 am")  by  [adam](https://www.hexacorn.com/blog/author/adam/ "View all posts by adam")

This is not a proper research yet. I just happened to stumble upon an interesting artifact which is a file:

```
C:\Windows\System32\dns\RFC5011.csv
```

that *dns.exe* service process tries to read.

This csv file appears to be related to DNSSEC, but I don’t know enough about it, plus have not spent enough time analyzing the actual *dns.exe* binary to determine the csv file’s purpose and layout yet.

BUT

The code reading this CSV file refers to *TrustAnchor* and *TrustPoint* strings so it’s possible the program is using the content of the file to import a set of trusted public keys utilized by DNSSEC. Which of course could be abused.

After poking around a bit more, I have created a list of file system-based artifacts that the DNS-related executables and libraries (c:\Windows\System32\dns.exe, c:\Windows\System32\dnscmd.exe, c:\Windows\System32\dnsmgr.dll) touch:

* C:\Windows\System32\dns\backup\boot
* C:\Windows\System32\dns\backup\boot.first
* C:\Windows\System32\dns\backup\dns.log
* C:\Windows\System32\dns\boot
* C:\Windows\System32\dns\boot.txt
* C:\Windows\System32\dns\boot.write.error
* C:\Windows\System32\dns\dns.log
* C:\Windows\System32\dns\RFC5011.csv
* C:\Windows\System32\dns\TrustAnchors.dns

This is really not very useful yet, but it is a good starting point to dig deeper.

This entry was posted in [Archaeology](https://www.hexacorn.com/blog/category/archaeology/) by [adam](https://www.hexacorn.com/blog/author/adam/). Bookmark the [permalink](https://www.hexacorn.com/blog/2024/12/15/dns-exe-and-its-quirks/ "Permalink to dns.exe and its quirks").

[Privacy Policy](https://www.hexacorn.com/blog/privacy-policy/) [Proudly powered by WordPress](https://wordpress.org/ "Semantic Personal Publishing Platform")
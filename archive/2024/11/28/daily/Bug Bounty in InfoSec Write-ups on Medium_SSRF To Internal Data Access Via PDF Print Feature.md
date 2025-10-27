---
title: SSRF To Internal Data Access Via PDF Print Feature
url: https://infosecwriteups.com/ssrf-to-internal-data-access-via-pdf-print-feature-b8e6a912844a?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2024-11-28
fetch_date: 2025-10-06T19:17:15.944279
---

# SSRF To Internal Data Access Via PDF Print Feature

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fb8e6a912844a&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fssrf-to-internal-data-access-via-pdf-print-feature-b8e6a912844a&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fssrf-to-internal-data-access-via-pdf-print-feature-b8e6a912844a&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-b8e6a912844a---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-b8e6a912844a---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# SSRF To Internal Data Access Via PDF Print Feature

[![Bishal Shrestha](https://miro.medium.com/v2/resize:fill:64:64/1*69Ov1zWMeaoJYT9wGOKT_w.jpeg)](https://bishal0x01.medium.com/?source=post_page---byline--b8e6a912844a---------------------------------------)

[Bishal Shrestha](https://bishal0x01.medium.com/?source=post_page---byline--b8e6a912844a---------------------------------------)

3 min read

·

Nov 25, 2024

--

2

Listen

Share

**Introduction:** Server-Side Request Forgery (SSRF) is a web security vulnerability that occurs when an attacker manipulates a server into making unauthorized HTTP or other protocol-based requests to unintended destinations. This exploit typically arises when an application fetches remote resources based on user-supplied input without adequately validating or sanitizing the input.

### **Hunting SSRF in a Financial Application**

Most of the time, I focus on a single program when hunting for vulnerabilities. Sticking to one program allows me to understand its core functionalities and business logic more thoroughly. In this case, I was working on a private program related to finance. This application used different internal domains for handling financial data, fetching the data via iframes.

Initially, I overlooked testing for CSRF or other bugs because I assumed the requests were encrypted. However, after digging deeper, I realized that the “encrypted” requests were merely Base64-encoded! That discovery led to the reporting of a few CSRF vulnerabilities and XSS bugs, even though some of them were on out-of-scope domains. These domains, however, directly impacted the main scope host and were used in the web application.

## The SSRF Discovery

While exploring the application further, I found a **Print** functionality. This feature converts the page into HTML, encodes it in Base64, and sends it for printing. This reminded me of SSRF techniques from **NahamSec’s and other security researcher write-ups and videos**, especially around PDF conversion features, which often have SSRF potential.

Press enter or click to view image in full size

![]()

I started experimenting with payloads to check for SSRF. Initially, I used commands aimed at AWS metadata endpoints and Linux file paths, such as:

```
"><iframe src="http://169.254.169.254/latest/meta-data" height=2500 width=500>
"><iframe src="cat /etc/passwd" height=2500 width=500>
```

However, I faced issues with the height and width parameters in the iframe, which distorted the output. After some trial and error, I figured out the correct structure for these parameters.

Later, I identified that the backend server was running **Windows OS**. This discovery shifted my focus to testing Windows-specific directories. I used payloads like:

```
"><iframe src="C:\Windows\debug\NetSetup.LOG" height=2500 width=500>
 "><iframe/src="C:/Windows/win.ini">
```

I then encoded this payload into Base64:

```
Ij48aWZyYW1lL3NyYz0iQzpcV2luZG93c1xkZWJ1Z1xOZXRTZXR1cC5MT0ciIGhlaWdodD0yNTAwIHdpZHRoPTUwMD4=
Ij48aWZyYW1lL3NyYz0iQzpcV2luZG93c1xkZWJ1Z1xOZXRTZXR1cC5MT0ciIGhlaWdodD01MDAgd2lkdGg9NzAwPg==
```

This payload was successfully executed at the following endpoint:

```
https://aa.REDACTED.com/REDACTED/Print/PrintToPDF
```

Press enter or click to view image in full size

![]()

HTTP Request with encoded payload

Press enter or click to view image in full size

![]()

Press enter or click to view image in full size

![]()

## Hit-and-Trial for Exploitation:

With this breakthrough, I tested various other payloads to explore the backend further. Each time, I adjusted the parameters and encoded the payload in Base64 to ensure it executed properly. Eventually, I successfully retrieved sensitive data and confirmed the SSRF vulnerability.

This experience underscored the importance of persistence and creative thinking in bug hunting, as even initially overlooked features can lead to significant discoveries when explored thoroughly.

Press enter or click to view image in full size

![]()

Response from Program owner behind reducing the priority.

Initially, the issue was triaged as a **P1** by one of Bugcrowd’s Application Security Engineers (ASE) under the `server_side_injection.file_inclusion.local` category in the VRT. However, the program owner later reclassified it as a **P2**, providing additional explanation for the downgrade.

Press enter or click to view image in full size

![]()

I always feel that until we discover these bugs ourselves, it doesn’t feel real. :D This was my first SSRF bug ever! Thank you for taking the time to read this write-up. Keep learning and happy hacking!

## Timeline:

*Reported →*(22 Mar 2024 15:55:11 UTC)

*Triaged →*(27 Mar 2024 06:10:41 UTC)

*Resolved →(*17 May 2024 17:58:02 UTC)

[Information Security](https://medium.com/tag/information-security?source=post_page-----b8e6a912844a---------------------------------------)

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----b8e6a912844a---------------------------------------)

[Ssrf](https://medium.com/tag/ssrf?source=post_page-----b8e6a912844a---------------------------------------)

--

--

2

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--b8e6a912844a---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--b8e6a912844a---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--b8e6a912844a---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--b8e6a912844a---------------------------------------)

·[Last published 4 hours ago](/baby-dfc2547dc387?source=post_page---post_...
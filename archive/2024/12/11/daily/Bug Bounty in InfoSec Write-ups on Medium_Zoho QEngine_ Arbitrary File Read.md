---
title: Zoho QEngine: Arbitrary File Read
url: https://infosecwriteups.com/zoho-qengine-arbitrary-file-read-08df3d1e167e?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2024-12-11
fetch_date: 2025-10-06T19:39:21.591815
---

# Zoho QEngine: Arbitrary File Read

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F08df3d1e167e&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fzoho-qengine-arbitrary-file-read-08df3d1e167e&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fzoho-qengine-arbitrary-file-read-08df3d1e167e&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-08df3d1e167e---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-08df3d1e167e---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# **Zoho QEngine: Arbitrary File Read**

[![Jayateertha Guruprasad](https://miro.medium.com/v2/resize:fill:64:64/1*bmKMCGbQfIUNeymH5M7Pow.jpeg)](https://jayateerthag.medium.com/?source=post_page---byline--08df3d1e167e---------------------------------------)

[Jayateertha Guruprasad](https://jayateerthag.medium.com/?source=post_page---byline--08df3d1e167e---------------------------------------)

2 min read

·

Dec 10, 2024

--

Listen

Share

[**Zoho QEngine**](https://www.zoho.com/qengine/) is a test automation software to test your code on various devices & browsers before they get released.

🚀 One of its handy functions is **openURL()**, which lets you load a test URL in a supported browser like Chrome. Sounds neat, right? But as a security researcher, I couldn’t resist digging a bit deeper. 😏

## 🛠️ First Stop: Common SSRF Attack Vectors

Initially like all security researchers, My initial intinct was to test for good ol’ **SSRF** test cases & check if, I am able to access their internal services or cloud metadata urls [169.254.169.254](https://book.hacktricks.xyz/pentesting-web/ssrf-server-side-request-forgery/cloud-ssrf).

💡 **Fun fact**: **Zoho runs most of its services on its own cloud, no surprise — these URLs didn’t fetch anything interesting.**

## 🔄 Switching Gears: Testing Non-HTTP Protocols

What if we try something besides http://? 🤔 Like… file:// protocol?

*💻 Enter:* ***openURL(“file:///etc/passwd”, “new tab”)***

Press enter or click to view image in full size

![]()

QEngine Vulnerable Test Case Code

🎆 **BOOM!** we now get to see the content of /etc/passwd from Zoho QEngine’s test environment. 🕵️‍♂️

Press enter or click to view image in full size

![]()

/etc/passwd screenshot of test case

## 🔒 Why It’s Low Risk (But Still Cool)

Zoho QEngine runs each test case in an isolated Docker environment. So, there’s no sensitive data here to steal-phew! 😌

Imagine if this was run on a real system without Docker. The impact could be HUGE! 🚨

I made a detailed report of my findings and submitted it to **Zoho’s** [**BugBounty**](https://bugbounty.zohocorp.com/bb/#/submitbug) platform. They confirmed the issue and rewarded me with 💸.

## 💡 Key Takeaways

1. Always validate user inputs by enforcing strict whitelisting of protocols, domains, and paths for URLs. This includes checking for internal service URLs and metadata endpoints to prevent unintended access.
2. While Dockerized environments enhance security, don’t rely solely on them for isolation. They might still expose environment secrets, configuration files, or other sensitive data. In some cases, vulnerabilities could even lead to Docker escapes.

*Originally published at* [*https://blog.jayateerthag.in*](https://blog.jayateerthag.in/post/zoho_qengine_arbitrary_local_file_read_using_file_protocol/) *on December 10, 2024.*

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----08df3d1e167e---------------------------------------)

[Cybersecurity](https://medium.com/tag/cybersecurity?source=post_page-----08df3d1e167e---------------------------------------)

[Hacking](https://medium.com/tag/hacking?source=post_page-----08df3d1e167e---------------------------------------)

[Bug Bounty Writeup](https://medium.com/tag/bug-bounty-writeup?source=post_page-----08df3d1e167e---------------------------------------)

[Bug Bounty Tips](https://medium.com/tag/bug-bounty-tips?source=post_page-----08df3d1e167e---------------------------------------)

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--08df3d1e167e---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--08df3d1e167e---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--08df3d1e167e---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--08df3d1e167e---------------------------------------)

·[Last published 4 hours ago](/baby-dfc2547dc387?source=post_page---post_publication_info--08df3d1e167e---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Jayateertha Guruprasad](https://miro.medium.com/v2/resize:fill:96:96/1*bmKMCGbQfIUNeymH5M7Pow.jpeg)](https://jayateerthag.medium.com/?source=post_page---post_author_info--08df3d1e167e---------------------------------------)

[![Jayateertha Guruprasad](https://miro.medium.com/v2/resize:fill:128:128/1*bmKMCGbQfIUNeymH5M7Pow.jpeg)](https://jayateerthag.medium.com/?source=post_page---post_author_info--08df3d1e167e---------------------------------------)

[## Written by Jayateertha Guruprasad](https://jayateerthag.medium.com/?source=post_page---post_author_info--08df3d1e167e---------------------------------------)

[386 followers](https://jayateerthag.medium.com/followers?source=post_page---post_author_info--08df3d1e167e---------------------------------------)

·[39 following](https://medium.com/%40jayateerthag/following?source=post_page---post_author_info--08df3d1e167e---------------------------------------)

I get paid for breaking things !

## No responses yet

[Help](https://help.medium.com/hc/en-us?source=post_page-----08df3d1e167e---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----08df3d1e167e---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----08df3d1e167e---------------------------------------)

[Careers](https://m...
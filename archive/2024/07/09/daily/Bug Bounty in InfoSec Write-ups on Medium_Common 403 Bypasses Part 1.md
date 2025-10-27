---
title: Common 403 Bypasses Part 1
url: https://infosecwriteups.com/common-403-bypasses-part-1-a455f2a1410b?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2024-07-09
fetch_date: 2025-10-06T17:43:14.505536
---

# Common 403 Bypasses Part 1

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fa455f2a1410b&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fcommon-403-bypasses-part-1-a455f2a1410b&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fcommon-403-bypasses-part-1-a455f2a1410b&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-a455f2a1410b---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-a455f2a1410b---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# Common 403 Bypasses Part 1

[![Ott3rly](https://miro.medium.com/v2/resize:fill:64:64/1*3wMPJmhJUNOpqobsPBkS8g.jpeg)](https://ott3rly.medium.com/?source=post_page---byline--a455f2a1410b---------------------------------------)

[Ott3rly](https://ott3rly.medium.com/?source=post_page---byline--a455f2a1410b---------------------------------------)

4 min read

·

Jul 1, 2024

--

Listen

Share

Are you tired of seeing those 403 Forbidden errors that block you while testing? Don’t worry, some effective techniques could help to avoid this hassle! Let’s explore some 403 Bypasses that work!

## What is the 403 Status Code?

This [status code](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/403) limits users’ access to specific hosts, endpoints, etc. It could be implemented either in the web application code, or there could be certain Web Application Firewall rules. There might be different cases for bypasses because of different sets of technologies. So it does mean that there won’t be an all-in-one solution for most cases, but we will still explore the most common ways!

There are multiple techniques that we will try to cover in this writeup:

* Applying special characters to the URL
* Switching HTTP Methods
* Headers manipulation
* Switching IP or using a VPN provider

## Fuzzing HTTP Methods

Let’s start with the method which is pretty easy to check. If you get 403 status just by trying to access a certain endpoint, while on other endpoints you are getting 200, this could be one of the first things to try. The idea is to check the web application’s handling of different HTTP methods (like GET, POST, PUT, DELETE, etc.), to see if changing them can lead to other status codes like 200. It is just as simple as that, to quickly check this, you could use an HTTP proxy like burp:

Press enter or click to view image in full size

![]()

or you could send the request with CLI tools like curl:

Press enter or click to view image in full size

![]()

## Headers Manipulation

Another technique could be used when you get a 403 code when trying to access a website for the first time. I do recommend trying to play around with those headers:

Press enter or click to view image in full size

![]()

Together with them, you could use 127.0.0.1, localhost or even some cloud internal IPs could work as well:

Press enter or click to view image in full size

![]()

Some Burp Suite plugins do that, or you could inject just another header like this inside the request. I also use this with CLI tools as an extra header, for example, when using httpx at the mass scale:

Press enter or click to view image in full size

![]()

## Changing IP Address or Using a VPN

You could also get blocked by a Web Application Firewall by doing malicious actions. For example, if you send too many requests containing known malicious payloads, using too many requests per second, trying to access known sensitive files, your IP might get blacklisted. Your IP could get blacklisted for a certain amount of time, or even indefinitely! For this reason, I do recommend having either an IP proxy, which could take more effort, or just using a VPN provider. I do use [NordVPN](https://ott3rly.com/NordVPN), not for those reasons to access certain content, but mainly when I get blocked while testing! I do save a lot of time and nerves when using this product since others could be slow or not really reliable.

## Fuzzing the URL Path

And the last one — is using some tricks to the URL path. I have had the most success with this one. Either if you having issues accessing the website for the first time, or a certain endpoint is not reachable, it is worth trying to send these payloads:

Press enter or click to view image in full size

![]()

I have discovered some swagger documentation sites using this method, which eventually led me to discover a more severe bug — SQL injection.

## Summary

As the introduction of 403 bypasses, we’ve covered some ways to tackle 403 Forbidden errors, from simple URL changes to sophisticated header manipulations. In the second part, we will dive into more techniques and I will also show you some of my favorite command line utilities to automate detection! It was my pleasure sharing this knowledge, wish you a nice hunt!

If you find this information useful, please share this article on your social media, I will greatly appreciate it! I am active on [Twitter](https://ott3rly.com/twitter), check out some content I post there daily! If you are interested in video content, check my [YouTube](https://ott3rly.com/youtube). Also, if you want to reach me personally, you can visit my [Discord](https://ott3rly.com/discord) server. Cheers!

*Originally published at* [*https://ott3rly.com*](https://ott3rly.com/common-403-bypasses-part-1/) *on July 1, 2024.*

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----a455f2a1410b---------------------------------------)

[Bug Bounty Tips](https://medium.com/tag/bug-bounty-tips?source=post_page-----a455f2a1410b---------------------------------------)

[Information Security](https://medium.com/tag/information-security?source=post_page-----a455f2a1410b---------------------------------------)

[Infosec](https://medium.com/tag/infosec?source=post_page-----a455f2a1410b---------------------------------------)

[Cybersecurity](https://medium.com/tag/cybersecurity?source=post_page-----a455f2a1410b---------------------------------------)

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--a455f2a1410b---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--a455f2a1410b---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publicatio...
---
title: Discovering vulnerabilities quickly with targeted scanning — Portswigger
url: https://infosecwriteups.com/discovering-vulnerabilities-quickly-with-targeted-scanning-portswigger-b8c102f5c3ba?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2023-01-15
fetch_date: 2025-10-04T03:56:48.097323
---

# Discovering vulnerabilities quickly with targeted scanning — Portswigger

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fb8c102f5c3ba&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fdiscovering-vulnerabilities-quickly-with-targeted-scanning-portswigger-b8c102f5c3ba&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fdiscovering-vulnerabilities-quickly-with-targeted-scanning-portswigger-b8c102f5c3ba&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[Mastodon](https://me.dm/%40cyberw1ng)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-b8c102f5c3ba---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-b8c102f5c3ba---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# Discovering vulnerabilities quickly with targeted scanning — Portswigger

## This lab contains a vulnerability that enables you to read arbitrary files from the server. To solve the lab, retrieve the contents of /etc/passwd within 10 minutes | Approach

[![Karthikeyan Nagaraj](https://miro.medium.com/v2/da:true/resize:fill:64:64/1*MQN6JztXVcWsGNXCfJGlgw.gif)](https://cyberw1ng.medium.com/?source=post_page---byline--b8c102f5c3ba---------------------------------------)

[Karthikeyan Nagaraj](https://cyberw1ng.medium.com/?source=post_page---byline--b8c102f5c3ba---------------------------------------)

3 min read

·

Dec 31, 2022

--

1

Listen

Share

Press enter or click to view image in full size

![]()

[## Lab: Discovering vulnerabilities quickly with targeted scanning | Web Security Academy

### Practice exploiting vulnerabilities on realistic targets. Record your progression from Apprentice to Expert. See where…

portswigger.net](https://portswigger.net/web-security/essential-skills/using-burp-scanner-during-manual-testing/lab-discovering-vulnerabilities-quickly-with-targeted-scanning?source=post_page-----b8c102f5c3ba---------------------------------------)

### Let’s Start — You have to solve the lab in 10 Minutes

Access the Lab, Turn on the Proxy, and Turn off your Intercept in Burpsuite

Now notice the Content list of HTTP history in the Proxy tab, you can see that there is a request `/product/stock`from that the Parameter `ProductID` is an endpoint to test.

![]()

Right-click on `/product/stock`→ Do Active Scan
Try to Change the Parameters to various values

Press enter or click to view image in full size

![]()

Press enter or click to view image in full size

![]()

The scanner found an Out-of-band resource load on `/product/stock`

![]()

![]()

It is possible to induce the application to retrieve the contents of an arbitrary external URL and return those contents in its own response.

* Send the Request to the Repeater
* Add the below Payload in `ProductID` Parameter

```
<foo xmlns:xi="http://www.w3.org/2001/XInclude"><xi:include parse="text" href="file:///etc/passwd"/></foo>
```

![]()

Send the Request, Now you can able to view the `/etc/passwd`

![]()

Feel Free to Ask Queries via [LinkedIn](https://www.linkedin.com/in/karthikeyan-nagaraj) and to Buy me a Cofee : )

[![]()](https://buymeacoffee.com/cyberw1ng)

Thank you for Reading!!

Happy Hunting ~

```
Author: Karthikeyan Nagaraj ~ Cyberw1ng
```

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----b8c102f5c3ba---------------------------------------)

[Portswigger](https://medium.com/tag/portswigger?source=post_page-----b8c102f5c3ba---------------------------------------)

[Burpsuite](https://medium.com/tag/burpsuite?source=post_page-----b8c102f5c3ba---------------------------------------)

[Writeup](https://medium.com/tag/writeup?source=post_page-----b8c102f5c3ba---------------------------------------)

[Penetration Testing](https://medium.com/tag/penetration-testing?source=post_page-----b8c102f5c3ba---------------------------------------)

--

--

1

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--b8c102f5c3ba---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--b8c102f5c3ba---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--b8c102f5c3ba---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--b8c102f5c3ba---------------------------------------)

·[Last published 5 days ago](/how-to-find-p1-bugs-using-google-in-your-target-part-1-e37455324dc1?source=post_page---post_publication_info--b8c102f5c3ba---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Karthikeyan Nagaraj](https://miro.medium.com/v2/resize:fill:96:96/1*MQN6JztXVcWsGNXCfJGlgw.gif)](https://cyberw1ng.medium.com/?source=post_page---post_author_info--b8c102f5c3ba---------------------------------------)

[![Karthikeyan Nagaraj](https://miro.medium.com/v2/resize:fill:128:128/1*MQN6JztXVcWsGNXCfJGlgw.gif)](https://cyberw1ng.medium.com/?source=post_page---post_author_info--b8c102f5c3ba---------------------------------------)

[## Written by Karthikeyan Nagaraj](https://cyberw1ng.medium.com/?source=post_page---post_author_info--b8c102f5c3ba---------------------------------------)

[12.8K followers](https://cyberw1ng.medium.com/followers?source=post_page---post_author_info--b8c102f5c3ba---------------------------------------)

·[1 following](https://medium.com/%40cyberw1ng/following?source=post_page---post_author_info--b8c102f5c3ba---------------------------------------)

Entrepreneur | Writer | Cyber Security Consultant | AI Researcher TopMate - <https://topmate.io/cyberw1ng>

## Responses (1)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----b8c102f5c3ba---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----b8c102f5c3ba---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----b8c102f5c3ba---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----b8c102f5c3ba---------------------------------------)

Press

[Blog](https://blog.medi...
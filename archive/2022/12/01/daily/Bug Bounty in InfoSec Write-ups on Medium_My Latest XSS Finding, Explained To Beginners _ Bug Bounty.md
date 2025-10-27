---
title: My Latest XSS Finding, Explained To Beginners | Bug Bounty
url: https://infosecwriteups.com/my-latest-xss-finding-explained-to-beginners-bug-bounty-8674fa3626e7?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2022-12-01
fetch_date: 2025-10-04T00:11:32.642455
---

# My Latest XSS Finding, Explained To Beginners | Bug Bounty

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F8674fa3626e7&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fmy-latest-xss-finding-explained-to-beginners-bug-bounty-8674fa3626e7&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fmy-latest-xss-finding-explained-to-beginners-bug-bounty-8674fa3626e7&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-8674fa3626e7---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-8674fa3626e7---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# My Latest XSS Finding, Explained To Beginners | Bug Bounty

[![Fırat](https://miro.medium.com/v2/resize:fill:64:64/1*SCkq2tULGFnERCJPAP-LXQ.jpeg)](https://medium.com/%40fiirat?source=post_page---byline--8674fa3626e7---------------------------------------)

[Fırat](https://medium.com/%40fiirat?source=post_page---byline--8674fa3626e7---------------------------------------)

2 min read

·

Nov 30, 2022

--

1

Listen

Share

It’s been a while since i posted a writeup so i thought it would be wise to make one for beginners.

So to begin i want to answer some questions, what is **Cross-site** **Scripting(XSS)?**

Press enter or click to view image in full size

![]()

imperva.com

**Cross-site Scripting(XSS)** is a really well-known vulnerability that occurs because applications take user inputs in an unsecured way. There is other types of XSS vulnerabilities too but today i am going to talk about **Reflected** **Cross-site Scripting.**

Lots of wannabe bug bounty hunters thinks that xss just copying and pasting *<img src=x onerror=alert(1)>* everywhere and expecting to see a pop up on the screen. What xss really about is actually the context. So let’s say the XSS context is into an HTML tag attribute value, you might be able to terminate the attribute value, close the tag and create a second tag which will store your payload. Unfortunately in most cases, angle brackets will be blocked or encoded.

**But** if you know about XSS contexts, you may still be able to terminate the attribute value and create a new attribute that will store your payload. I.E

```
" autofocus onfocus=alert(document.domain) x="
```

To close up, i am going to talk about **my finding.**

I found an error page on webarchive, there was a parameter called result in the url but site wasn’t showing anything. So i thought it’d be wise to look at the source code of the site and to my luck the parameter was reflecting inside of a script tag. If you were to just paste*“><img src=x onerror=alert(1)>* into the parameter, you wouldn’t see any pop up. You need to close the script tag first and create a new tag that will store your payload. The final payload i used as a PoC in my report was

```
</script>"><img src=x onerror=alert(1)>
```

**Reported On: 11/10/2022**

**Triaged On: 11/11/2022**

**$$$ Bounty Paid On: 11/15/2022**

Triaged in 1 day and i got paid $$$ bounty in a week. It was one of the fastest paid report.

### From Infosec Writeups: A lot is coming up in the Infosec every day that it’s hard to keep up with. [Join our weekly newsletter](https://weekly.infosecwriteups.com/) to get all the latest Infosec trends in the form of 5 articles, 4 Threads, 3 videos, 2 GitHub Repos and tools, and 1 job alert for FREE!

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----8674fa3626e7---------------------------------------)

[Infosec](https://medium.com/tag/infosec?source=post_page-----8674fa3626e7---------------------------------------)

[Web App Security](https://medium.com/tag/web-app-security?source=post_page-----8674fa3626e7---------------------------------------)

--

--

1

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--8674fa3626e7---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--8674fa3626e7---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--8674fa3626e7---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--8674fa3626e7---------------------------------------)

·[Last published 5 days ago](/how-to-find-p1-bugs-using-google-in-your-target-part-1-e37455324dc1?source=post_page---post_publication_info--8674fa3626e7---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Fırat](https://miro.medium.com/v2/resize:fill:96:96/1*SCkq2tULGFnERCJPAP-LXQ.jpeg)](https://medium.com/%40fiirat?source=post_page---post_author_info--8674fa3626e7---------------------------------------)

[![Fırat](https://miro.medium.com/v2/resize:fill:128:128/1*SCkq2tULGFnERCJPAP-LXQ.jpeg)](https://medium.com/%40fiirat?source=post_page---post_author_info--8674fa3626e7---------------------------------------)

[## Written by Fırat](https://medium.com/%40fiirat?source=post_page---post_author_info--8674fa3626e7---------------------------------------)

[105 followers](https://medium.com/%40fiirat/followers?source=post_page---post_author_info--8674fa3626e7---------------------------------------)

·[5 following](https://medium.com/%40fiirat/following?source=post_page---post_author_info--8674fa3626e7---------------------------------------)

web application security researcher

## Responses (1)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----8674fa3626e7---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----8674fa3626e7---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----8674fa3626e7---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----8674fa3626e7---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----8674fa3626e7---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-...
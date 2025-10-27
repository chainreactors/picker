---
title: Finding subdomains that are hidden in the cloud.
url: https://infosecwriteups.com/finding-subdomains-that-are-hidden-in-the-cloud-ec54412802bf?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-02-12
fetch_date: 2025-10-06T20:34:41.390065
---

# Finding subdomains that are hidden in the cloud.

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fec54412802bf&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Ffinding-subdomains-that-are-hidden-in-the-cloud-ec54412802bf&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Ffinding-subdomains-that-are-hidden-in-the-cloud-ec54412802bf&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-ec54412802bf---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-ec54412802bf---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# Finding subdomains that are hidden in the cloud.

[![loyalonlytoday](https://miro.medium.com/v2/resize:fill:64:64/1*J5mQT2d2tdE3ZSlbk8dzyg.jpeg)](https://medium.com/%40loyalonlytoday?source=post_page---byline--ec54412802bf---------------------------------------)

[loyalonlytoday](https://medium.com/%40loyalonlytoday?source=post_page---byline--ec54412802bf---------------------------------------)

3 min read

·

Feb 11, 2025

--

1

Share

> **Free link in the comments**
>
> 👋 Hello all👋

**In this blog, we will see how to find subdomains with the help of cloud providers like Amazon, Digital Ocean, Google, Microsoft, and Oracle.**

**So let’s see how to find them.**

**Click on the below link**⬇️**.**

[## Home \* Directory Lister

### Yet another directory listing, powered by Directory Lister.

kaeferjaeger.gay](https://kaeferjaeger.gay/?source=post_page-----ec54412802bf---------------------------------------)

**Scroll down a little bit. you will find sni-ip-ranges. like shown in the image below.**

Press enter or click to view image in full size

![]()

Screenshot by author

**in that sni-ip-ranges folder.**

Press enter or click to view image in full size

![]()

Screenshot by author

**open that folder one by one and open that file one by one.**

![]()

Screenshot by author

**Copy that file URL.**

**run all the below-given commands on your Kali Linux one by one.**

```
wget…
```

--

--

1

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--ec54412802bf---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--ec54412802bf---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--ec54412802bf---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--ec54412802bf---------------------------------------)

·[Last published just now](/actuator-unleashed-a-guide-to-finding-and-exploiting-spring-boot-actuator-endpoints-29252dcd9d79?source=post_page---post_publication_info--ec54412802bf---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![loyalonlytoday](https://miro.medium.com/v2/resize:fill:96:96/1*J5mQT2d2tdE3ZSlbk8dzyg.jpeg)](https://medium.com/%40loyalonlytoday?source=post_page---post_author_info--ec54412802bf---------------------------------------)

[![loyalonlytoday](https://miro.medium.com/v2/resize:fill:128:128/1*J5mQT2d2tdE3ZSlbk8dzyg.jpeg)](https://medium.com/%40loyalonlytoday?source=post_page---post_author_info--ec54412802bf---------------------------------------)

[## Written by loyalonlytoday](https://medium.com/%40loyalonlytoday?source=post_page---post_author_info--ec54412802bf---------------------------------------)

[1.7K followers](https://medium.com/%40loyalonlytoday/followers?source=post_page---post_author_info--ec54412802bf---------------------------------------)

·[230 following](https://medium.com/%40loyalonlytoday/following?source=post_page---post_author_info--ec54412802bf---------------------------------------)

TELEGRAM CHANNEL: [https://t.me/+PsN9eskK4p1jYzA1](https://t.me/%2BPsN9eskK4p1jYzA1) | OSINT & BUG BOUNTY HUNTING

## Responses (1)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----ec54412802bf---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----ec54412802bf---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----ec54412802bf---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----ec54412802bf---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----ec54412802bf---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----ec54412802bf---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----ec54412802bf---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----ec54412802bf---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----ec54412802bf---------------------------------------)
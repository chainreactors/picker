---
title: Accessing Admin Directory
url: https://infosecwriteups.com/accessing-admin-directory-eec04145a0fc?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-07-14
fetch_date: 2025-10-06T23:22:58.919015
---

# Accessing Admin Directory

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Feec04145a0fc&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Faccessing-admin-directory-eec04145a0fc&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Faccessing-admin-directory-eec04145a0fc&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-eec04145a0fc---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-eec04145a0fc---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# Accessing Admin Directory

[![SIDDHANT SHUKLA](https://miro.medium.com/v2/resize:fill:64:64/1*8ZQ4ust4pThkatOZK2KniQ.jpeg)](https://ghostman01.medium.com/?source=post_page---byline--eec04145a0fc---------------------------------------)

[SIDDHANT SHUKLA](https://ghostman01.medium.com/?source=post_page---byline--eec04145a0fc---------------------------------------)

3 min read

·

Jul 12, 2025

--

2

Share

*Bug hunting through sleep, subdomains, and surprises*

![]()

Mr. Prince

### [**Read for Free..👈**](https://ghostman01.medium.com/eec04145a0fc?sk=ea797934d2921c7e12935998157d4a4e)

## 🐞 Back on the Hunt

Hey folks!
 After spending a few hours hunting and reporting a `.git` exposure via CloudFront, I got back to my primary target to continue digging. If you missed that earlier write-up, you can check it out here:

[## The Hidden .git

### How I found an exposed .git/config file on a CloudFront-backed subdomain after a string of dead ends and persistence.

infosecwriteups.com](/the-hidden-git-b30afef0b462?source=post_page-----eec04145a0fc---------------------------------------)

How I found an exposed `.git/config` on a CloudFront-backed subdomain by staying persistent through dead ends.

## 🚀 Starting Fresh

I began with a basic recon routine — checking which subdomains were alive:

```
subfinder -d target.com --all --recursive | httpx
```

One subdomain stood out. I opened it in the browser and saw a plain message:

```
Cannot GET /
```

A boring 404 to most people — but to me, that’s a signal to dig deeper. I launched `dirsearch` to check for any hidden files or directories:

```
dirsearch -u https://sub.target.com -f -F -x 403 -t 3
```

--

--

2

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--eec04145a0fc---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--eec04145a0fc---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--eec04145a0fc---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--eec04145a0fc---------------------------------------)

·[Last published 2 hours ago](/actuator-unleashed-a-guide-to-finding-and-exploiting-spring-boot-actuator-endpoints-29252dcd9d79?source=post_page---post_publication_info--eec04145a0fc---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![SIDDHANT SHUKLA](https://miro.medium.com/v2/resize:fill:96:96/1*8ZQ4ust4pThkatOZK2KniQ.jpeg)](https://ghostman01.medium.com/?source=post_page---post_author_info--eec04145a0fc---------------------------------------)

[![SIDDHANT SHUKLA](https://miro.medium.com/v2/resize:fill:128:128/1*8ZQ4ust4pThkatOZK2KniQ.jpeg)](https://ghostman01.medium.com/?source=post_page---post_author_info--eec04145a0fc---------------------------------------)

[## Written by SIDDHANT SHUKLA](https://ghostman01.medium.com/?source=post_page---post_author_info--eec04145a0fc---------------------------------------)

[855 followers](https://ghostman01.medium.com/followers?source=post_page---post_author_info--eec04145a0fc---------------------------------------)

·[424 following](https://medium.com/%40ghostman01/following?source=post_page---post_author_info--eec04145a0fc---------------------------------------)

just a lazy hunter.

## Responses (2)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----eec04145a0fc---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----eec04145a0fc---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----eec04145a0fc---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----eec04145a0fc---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----eec04145a0fc---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----eec04145a0fc---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----eec04145a0fc---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----eec04145a0fc---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----eec04145a0fc---------------------------------------)
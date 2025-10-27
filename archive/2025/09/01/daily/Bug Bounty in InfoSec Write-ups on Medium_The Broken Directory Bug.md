---
title: The Broken Directory Bug
url: https://infosecwriteups.com/the-broken-directory-bug-184f37087479?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-09-01
fetch_date: 2025-10-02T19:29:12.931761
---

# The Broken Directory Bug

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F184f37087479&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fthe-broken-directory-bug-184f37087479&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fthe-broken-directory-bug-184f37087479&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-184f37087479---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-184f37087479---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# The Broken Directory Bug

## Hidden Directories in Chaos of Waybackurls

[![SIDDHANT SHUKLA](https://miro.medium.com/v2/resize:fill:64:64/1*8ZQ4ust4pThkatOZK2KniQ.jpeg)](https://ghostman01.medium.com/?source=post_page---byline--184f37087479---------------------------------------)

[SIDDHANT SHUKLA](https://ghostman01.medium.com/?source=post_page---byline--184f37087479---------------------------------------)

3 min read

·

Aug 31, 2025

--

3

Share

### [Read for Freee..ee.e](https://ghostman01.medium.com/184f37087479?sk=1dddfd81611ea8ee0546ae3ef7c4fa28)

Press enter or click to view image in full size

![]()

Anbu Black Ops

### 🐺Hunters,

I was hunting on my primary payment app back in January 2025 and at that time I don’t know have much knowledge of recon, so I started with very basic thing. As you read this blogs you’ll know how this discovery leads to a big discovery.

### Basic Recon

I started with selecting a subdomain of my target and I started with very simple recon tool waybackurls to get the history of my targeted subdomain:

```
waybackurls subdomain.com | anew waybacksubs.txt
```

From waybackurls data I got a lot of .png, .jpeg, .js files and broken directories.

I started clicking those image files and broken links to get sensitive directories and any unauthorized page.

After sometime, I realized this subdomain is only used for storing static files.

### Sensitive Directories

I started with general sensitive directories which includes:

```
admin,documents,logs,private
```

Now I started with target specific sensitive directories which includes:

```
report,payment,transaction,merchant
```

--

--

3

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--184f37087479---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--184f37087479---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--184f37087479---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--184f37087479---------------------------------------)

·[Last published 4 days ago](/how-to-find-p1-bugs-using-google-in-your-target-part-1-e37455324dc1?source=post_page---post_publication_info--184f37087479---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![SIDDHANT SHUKLA](https://miro.medium.com/v2/resize:fill:96:96/1*8ZQ4ust4pThkatOZK2KniQ.jpeg)](https://ghostman01.medium.com/?source=post_page---post_author_info--184f37087479---------------------------------------)

[![SIDDHANT SHUKLA](https://miro.medium.com/v2/resize:fill:128:128/1*8ZQ4ust4pThkatOZK2KniQ.jpeg)](https://ghostman01.medium.com/?source=post_page---post_author_info--184f37087479---------------------------------------)

[## Written by SIDDHANT SHUKLA](https://ghostman01.medium.com/?source=post_page---post_author_info--184f37087479---------------------------------------)

[825 followers](https://ghostman01.medium.com/followers?source=post_page---post_author_info--184f37087479---------------------------------------)

·[423 following](https://medium.com/%40ghostman01/following?source=post_page---post_author_info--184f37087479---------------------------------------)

just a lazy hunter.

## Responses (3)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----184f37087479---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----184f37087479---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----184f37087479---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----184f37087479---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----184f37087479---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----184f37087479---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----184f37087479---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----184f37087479---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----184f37087479---------------------------------------)
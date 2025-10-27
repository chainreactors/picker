---
title: Revisiting a Simple SQL Injection Methodology
url: https://infosecwriteups.com/revisiting-a-simple-sql-injection-methodology-ecd42634a21e?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-01-12
fetch_date: 2025-10-06T20:08:14.362855
---

# Revisiting a Simple SQL Injection Methodology

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fecd42634a21e&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Frevisiting-a-simple-sql-injection-methodology-ecd42634a21e&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Frevisiting-a-simple-sql-injection-methodology-ecd42634a21e&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-ecd42634a21e---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-ecd42634a21e---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# Simple SQL Injection Methodology with The Photon Crawler

[![Jason Jacobs, MSc.](https://miro.medium.com/v2/resize:fill:64:64/1*rIRjyNeezYPCoeQNAEyhpA.jpeg)](https://medium.com/%40jasonjayjacobs?source=post_page---byline--ecd42634a21e---------------------------------------)

[Jason Jacobs, MSc.](https://medium.com/%40jasonjayjacobs?source=post_page---byline--ecd42634a21e---------------------------------------)

4 min read

·

Jan 10, 2025

--

Share

Press enter or click to view image in full size

![]()

Image Credits: UK Cybersecurity Blog, 2023

### The Mantra

> As boring and repetitive as it seems, every professional must be able to revisit the cyber bootcamp to sharpen their skills and methodology for every engagement.

If you take a closer look at a vast number of “Bug Bounty Tips” that are majorly trending on Twitter and LinkedIn, they can be classified as repackaged “Web Penetration Testing” methodology.

Its not always a matter of

1. What tools do I use?
2. How many [Seclists](https://github.com/danielmiessler/SecLists) wordlists can I brute-force with?
3. How many [PayloadAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings) files have I added to my inventory?

Sometimes its simply a matter of “*Where have you looked*” and “*What features have you tested*”. I believe that the key to adding more findings to your report is to stay invested enough in the aspect of all points where the Web Application performs **CRUD** *(Create, Read, Update, Delete)* actions on data and secondly, paying attention to the parameters and HTTP headers of various **GET** and **POST** requests.

There is much to discover and add to your inventory from simple searches such as “sqli methodology” on Twitter like the example seen in the Tweet…

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--ecd42634a21e---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--ecd42634a21e---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--ecd42634a21e---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--ecd42634a21e---------------------------------------)

·[Last published 5 hours ago](/baby-dfc2547dc387?source=post_page---post_publication_info--ecd42634a21e---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Jason Jacobs, MSc.](https://miro.medium.com/v2/resize:fill:96:96/1*rIRjyNeezYPCoeQNAEyhpA.jpeg)](https://medium.com/%40jasonjayjacobs?source=post_page---post_author_info--ecd42634a21e---------------------------------------)

[![Jason Jacobs, MSc.](https://miro.medium.com/v2/resize:fill:128:128/1*rIRjyNeezYPCoeQNAEyhpA.jpeg)](https://medium.com/%40jasonjayjacobs?source=post_page---post_author_info--ecd42634a21e---------------------------------------)

[## Written by Jason Jacobs, MSc.](https://medium.com/%40jasonjayjacobs?source=post_page---post_author_info--ecd42634a21e---------------------------------------)

[255 followers](https://medium.com/%40jasonjayjacobs/followers?source=post_page---post_author_info--ecd42634a21e---------------------------------------)

·[53 following](https://medium.com/%40jasonjayjacobs/following?source=post_page---post_author_info--ecd42634a21e---------------------------------------)

I write research-based CyberSecurity content for the beginners and enthusiasts • MSc. Cybersecurity • eCPPT • eWPT • eJPT • Security+ 🧑‍💻

## No responses yet

[Help](https://help.medium.com/hc/en-us?source=post_page-----ecd42634a21e---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----ecd42634a21e---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----ecd42634a21e---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----ecd42634a21e---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----ecd42634a21e---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----ecd42634a21e---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----ecd42634a21e---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----ecd42634a21e---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----ecd42634a21e---------------------------------------)
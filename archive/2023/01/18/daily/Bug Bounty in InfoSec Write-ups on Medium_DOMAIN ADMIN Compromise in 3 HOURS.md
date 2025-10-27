---
title: DOMAIN ADMIN Compromise in 3 HOURS
url: https://infosecwriteups.com/domain-admin-compromise-in-3-hours-5778902604c9?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2023-01-18
fetch_date: 2025-10-04T04:08:12.313675
---

# DOMAIN ADMIN Compromise in 3 HOURS

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F5778902604c9&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fdomain-admin-compromise-in-3-hours-5778902604c9&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fdomain-admin-compromise-in-3-hours-5778902604c9&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-5778902604c9---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-5778902604c9---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# DOMAIN ADMIN Compromise in 3 HOURS

[![popalltheshells](https://miro.medium.com/v2/resize:fill:64:64/1*-b6WuCfmjt3_kUbryMzqvw.jpeg)](https://popalltheshells.medium.com/?source=post_page---byline--5778902604c9---------------------------------------)

[popalltheshells](https://popalltheshells.medium.com/?source=post_page---byline--5778902604c9---------------------------------------)

4 min read

·

May 29, 2022

--

2

Share

Hi everyone; I hope you enjoyed my previous blog post on “[How I obtained Admin access in 30 seconds](https://popalltheshells.medium.com/i-obtained-admin-access-via-account-activation-link-in-30-seconds-dd7f115ae1d2)” — so today I am bringing you another ***CRITICAL*** finding I discovered recently; which sheds some lights on the importance of **changing default credentials** and **password reuse**.

— THREE HOURS OF ENUMERATION and EXPLOITATION —

First we all love some enumeration. With a simple nmap scan on the target(s), I identified one interesting application server called **Sun GlassFish Enterprise Server**. After some investigation and research, I found out that this application is responsible for deploying web applications within the enterprise environment. WOW. Alright, so with this information we know that this server is responsible for deploying at least some of the company’s web applications. By using our trustee Google, we can find out that the default credential for Sun GlassFish is **admin** with a password of **adminadmin.** With this newly found information; I was able to gain admin access to the application responsible for deploying web applications within the client’s environment.

One thing that stands out to me the most is the fact that this application takes **.war** file; which is responsible for distributing a collection of JAR-files, JavaServer Pages, Java Servlets, Java classes, and other files that constitute a web application (Wikipedia).

Press enter or click to view image in full size

![]()

--

--

2

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--5778902604c9---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--5778902604c9---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--5778902604c9---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--5778902604c9---------------------------------------)

·[Last published 5 days ago](/how-to-find-p1-bugs-using-google-in-your-target-part-1-e37455324dc1?source=post_page---post_publication_info--5778902604c9---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![popalltheshells](https://miro.medium.com/v2/resize:fill:96:96/1*-b6WuCfmjt3_kUbryMzqvw.jpeg)](https://popalltheshells.medium.com/?source=post_page---post_author_info--5778902604c9---------------------------------------)

[![popalltheshells](https://miro.medium.com/v2/resize:fill:128:128/1*-b6WuCfmjt3_kUbryMzqvw.jpeg)](https://popalltheshells.medium.com/?source=post_page---post_author_info--5778902604c9---------------------------------------)

[## Written by popalltheshells](https://popalltheshells.medium.com/?source=post_page---post_author_info--5778902604c9---------------------------------------)

[470 followers](https://popalltheshells.medium.com/followers?source=post_page---post_author_info--5778902604c9---------------------------------------)

·[6 following](https://medium.com/%40popalltheshells/following?source=post_page---post_author_info--5778902604c9---------------------------------------)

I write for fun about interesting things that I learn throughout my journey. Also, legit question, at what point can I identify as a security researcher?

## Responses (2)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----5778902604c9---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----5778902604c9---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----5778902604c9---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----5778902604c9---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----5778902604c9---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----5778902604c9---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----5778902604c9---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----5778902604c9---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----5778902604c9---------------------------------------)
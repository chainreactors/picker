---
title: What is /etc/passwd group shadow file in Linux
url: https://infosecwriteups.com/what-is-etc-passwd-group-shadow-file-in-linux-bd7b28f353f3?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2024-09-02
fetch_date: 2025-10-06T18:24:52.044440
---

# What is /etc/passwd group shadow file in Linux

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fbd7b28f353f3&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fwhat-is-etc-passwd-group-shadow-file-in-linux-bd7b28f353f3&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fwhat-is-etc-passwd-group-shadow-file-in-linux-bd7b28f353f3&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-bd7b28f353f3---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-bd7b28f353f3---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# What is /etc/passwd group shadow file in Linux

[![Sujal Meghwal](https://miro.medium.com/v2/resize:fill:64:64/1*FImaBGNqx8gmum8n7OPshw.jpeg)](https://sujalmeghwal.medium.com/?source=post_page---byline--bd7b28f353f3---------------------------------------)

[Sujal Meghwal](https://sujalmeghwal.medium.com/?source=post_page---byline--bd7b28f353f3---------------------------------------)

2 min read

·

May 22, 2023

--

Share

Press enter or click to view image in full size

![]()

**Passwd** is a file where information related to the user is stored such as name, user id, group id,gecos field, home directory, and command shell it is in human-readable format

**group** is the file in a human-readable file where information related to which user account belongs to which group is stored

**shadow** is a file where encrypted passwords of the user account are stored

Formate of `passwd` is unique to another file

Press enter or click to view image in full size

![]()

**Username:** Is the name of the account

**Password:** In the `/etc/passwd` file, the password field usually contains an encrypted password or a special value such as "x" or "\*" indicating that the password is stored in the `/etc/shadow` file. The `/etc/shadow` file, accessible only to the system administrator (root), contains the actual encrypted passwords.

**User id (UID):** Unix-like operating systems identify a user by a value called a user identifier. and it is in a number

**0** UID belongs to the Root account which has full control over the system

**1–99: these** UID are predefined accounts

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--bd7b28f353f3---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--bd7b28f353f3---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--bd7b28f353f3---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--bd7b28f353f3---------------------------------------)

·[Last published 3 hours ago](/baby-dfc2547dc387?source=post_page---post_publication_info--bd7b28f353f3---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Sujal Meghwal](https://miro.medium.com/v2/resize:fill:96:96/1*FImaBGNqx8gmum8n7OPshw.jpeg)](https://sujalmeghwal.medium.com/?source=post_page---post_author_info--bd7b28f353f3---------------------------------------)

[![Sujal Meghwal](https://miro.medium.com/v2/resize:fill:128:128/1*FImaBGNqx8gmum8n7OPshw.jpeg)](https://sujalmeghwal.medium.com/?source=post_page---post_author_info--bd7b28f353f3---------------------------------------)

[## Written by Sujal Meghwal](https://sujalmeghwal.medium.com/?source=post_page---post_author_info--bd7b28f353f3---------------------------------------)

[924 followers](https://sujalmeghwal.medium.com/followers?source=post_page---post_author_info--bd7b28f353f3---------------------------------------)

·[26 following](https://medium.com/%40sujalmeghwal/following?source=post_page---post_author_info--bd7b28f353f3---------------------------------------)

Penetration Tester and Bug Bounty Hunter passionate about cybersecurity. Skilled in C, and Python3 Linkden <https://www.linkedin.com/in/sujal-meghwal-724a62323/>

## No responses yet

[Help](https://help.medium.com/hc/en-us?source=post_page-----bd7b28f353f3---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----bd7b28f353f3---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----bd7b28f353f3---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----bd7b28f353f3---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----bd7b28f353f3---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----bd7b28f353f3---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----bd7b28f353f3---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----bd7b28f353f3---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----bd7b28f353f3---------------------------------------)
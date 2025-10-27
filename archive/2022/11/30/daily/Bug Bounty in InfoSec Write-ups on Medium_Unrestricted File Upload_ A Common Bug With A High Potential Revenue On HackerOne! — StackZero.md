---
title: Unrestricted File Upload: A Common Bug With A High Potential Revenue On HackerOne! — StackZero
url: https://infosecwriteups.com/unrestricted-file-upload-a-common-bug-with-a-high-potential-revenue-on-hackerone-stackzero-dcf71e56e48b?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2022-11-30
fetch_date: 2025-10-04T00:04:20.957587
---

# Unrestricted File Upload: A Common Bug With A High Potential Revenue On HackerOne! — StackZero

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fdcf71e56e48b&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Funrestricted-file-upload-a-common-bug-with-a-high-potential-revenue-on-hackerone-stackzero-dcf71e56e48b&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Funrestricted-file-upload-a-common-bug-with-a-high-potential-revenue-on-hackerone-stackzero-dcf71e56e48b&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-dcf71e56e48b---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-dcf71e56e48b---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# Unrestricted File Upload: A Common Bug With A High Potential Revenue On HackerOne! — StackZero

[![StackZero](https://miro.medium.com/v2/resize:fill:64:64/1*NfCOWe2r5LeicNQD3t8xMA.png)](https://medium.com/%40stackzero?source=post_page---byline--dcf71e56e48b---------------------------------------)

[StackZero](https://medium.com/%40stackzero?source=post_page---byline--dcf71e56e48b---------------------------------------)

9 min read

·

Nov 29, 2022

--

Share

Press enter or click to view image in full size

![]()

> This article was originally published at <https://www.stackzero.net/unrestricted-file-upload-vulnerability/>

A file upload vulnerability also called unrestricted file upload or arbitrary file upload is a potential security risk that allows an attacker to upload malicious files to a web server.
It occurs when an application does not properly validate the file type or its content. In this way an attacker may be able to upload a file that could compromise the security of the server.
Frequently the uploaded file is a backdoor that some Kali Linux tools like msfvenom can easily generate once the attacker knows the server’s technology.

## What is file-upload XSS?

A frequently asked question is “what is file-upload xss”, and the answer is that it’s not so much different from what we’ve said!

In the case of file-upload XSS the target is the client that runs the uploaded script.

But just to add a bit more details:

File-upload [Cross-Site Scripting](https://www.stackzero.net/xss/) (XSS) attack is a type of web application attack that occurs when an attacker uploads a malicious file to a website that in some way reflects a script.
The script…

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--dcf71e56e48b---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--dcf71e56e48b---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--dcf71e56e48b---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--dcf71e56e48b---------------------------------------)

·[Last published 5 days ago](/how-to-find-p1-bugs-using-google-in-your-target-part-1-e37455324dc1?source=post_page---post_publication_info--dcf71e56e48b---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![StackZero](https://miro.medium.com/v2/resize:fill:96:96/1*NfCOWe2r5LeicNQD3t8xMA.png)](https://medium.com/%40stackzero?source=post_page---post_author_info--dcf71e56e48b---------------------------------------)

[![StackZero](https://miro.medium.com/v2/resize:fill:128:128/1*NfCOWe2r5LeicNQD3t8xMA.png)](https://medium.com/%40stackzero?source=post_page---post_author_info--dcf71e56e48b---------------------------------------)

[## Written by StackZero](https://medium.com/%40stackzero?source=post_page---post_author_info--dcf71e56e48b---------------------------------------)

[362 followers](https://medium.com/%40stackzero/followers?source=post_page---post_author_info--dcf71e56e48b---------------------------------------)

·[61 following](https://medium.com/%40stackzero/following?source=post_page---post_author_info--dcf71e56e48b---------------------------------------)

I have a passion for sharing my knowledge and helping others stay safe online. I just want to share tips and advice useful for me.

## No responses yet

[Help](https://help.medium.com/hc/en-us?source=post_page-----dcf71e56e48b---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----dcf71e56e48b---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----dcf71e56e48b---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----dcf71e56e48b---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----dcf71e56e48b---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----dcf71e56e48b---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----dcf71e56e48b---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----dcf71e56e48b---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----dcf71e56e48b---------------------------------------)
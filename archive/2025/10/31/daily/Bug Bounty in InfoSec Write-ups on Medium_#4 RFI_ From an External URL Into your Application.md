---
title: #4 RFI: From an External URL Into your Application
url: https://infosecwriteups.com/4-rfi-from-an-external-url-into-your-application-a5aeb1c5958c?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-10-31
fetch_date: 2025-11-01T03:11:12.887283
---

# #4 RFI: From an External URL Into your Application

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fa5aeb1c5958c&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2F4-rfi-from-an-external-url-into-your-application-a5aeb1c5958c&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2F4-rfi-from-an-external-url-into-your-application-a5aeb1c5958c&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-a5aeb1c5958c---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-a5aeb1c5958c---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# #4 RFI: From an External URL Into your Application

[![Imvkale](https://miro.medium.com/v2/da:true/resize:fill:64:64/0*SQ78jVXi-gQuwHYw)](https://imvkale.medium.com/?source=post_page---byline--a5aeb1c5958c---------------------------------------)

[Imvkale](https://imvkale.medium.com/?source=post_page---byline--a5aeb1c5958c---------------------------------------)

4 min read

·

4 days ago

--

Share

Press enter or click to view image in full size

![]()

Understanding RFI isn’t just about finding a bug; it’s about recognizing a critical design flaw that, if exploited, hands an attacker the keys to your server. Let’s explore what RFI is, how to confirm its presence, and the devastating impact it can have.

## What is Remote File Inclusion (RFI)?

**Remote File Inclusion (RFI)** occurs when a web application allows a user to specify a remote URL as input, and the application’s underlying code (like PHP’s `include()` or `require()`) then fetches and executes the content of that URL.

Imagine your application is supposed to load a template file. With RFI, instead of loading `header.php` from its own server, it's tricked into loading `http://attacker.com/malicious_shell.php`. If the server is configured to execute included files, your attacker's code runs with the privileges of your web server.

[FriendLink](https://medium.com/%40imvkale/4-rfi-from-an-external-url-into-your-application-a5aeb1c5958c?sk=b11849ed220ae47a7a57671610befecc)🔗

### RFI vs. LFI: The Key Differences

* **LFI:** Allows including files that are already on the server’s local file system. This often requires directory traversal (`../../`) and relies on finding or uploading malicious content locally (e.g., log poisoning, file upload).
* **RFI:** Allows including files from any remote URL(e.g., `http://`, `ftp://`)…

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--a5aeb1c5958c---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--a5aeb1c5958c---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--a5aeb1c5958c---------------------------------------)

[73K followers](/followers?source=post_page---post_publication_info--a5aeb1c5958c---------------------------------------)

·[Last published 19 hours ago](/everyone-wants-to-hack-no-one-wants-to-think-a6bb8a313501?source=post_page---post_publication_info--a5aeb1c5958c---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Imvkale](https://miro.medium.com/v2/resize:fill:96:96/0*SQ78jVXi-gQuwHYw)](https://imvkale.medium.com/?source=post_page---post_author_info--a5aeb1c5958c---------------------------------------)

[![Imvkale](https://miro.medium.com/v2/resize:fill:128:128/0*SQ78jVXi-gQuwHYw)](https://imvkale.medium.com/?source=post_page---post_author_info--a5aeb1c5958c---------------------------------------)

[## Written by Imvkale](https://imvkale.medium.com/?source=post_page---post_author_info--a5aeb1c5958c---------------------------------------)

[16 followers](https://imvkale.medium.com/followers?source=post_page---post_author_info--a5aeb1c5958c---------------------------------------)

·[30 following](https://medium.com/%40imvkale/following?source=post_page---post_author_info--a5aeb1c5958c---------------------------------------)

hey guys how are you, i am a security researcher eager to write walkthroughs. Follow me on: <https://www.linkedin.com/in/iamvikramkale/>

## No responses yet

[Help](https://help.medium.com/hc/en-us?source=post_page-----a5aeb1c5958c---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----a5aeb1c5958c---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----a5aeb1c5958c---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----a5aeb1c5958c---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----a5aeb1c5958c---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----a5aeb1c5958c---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----a5aeb1c5958c---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----a5aeb1c5958c---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----a5aeb1c5958c---------------------------------------)
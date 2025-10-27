---
title: Hard-Coded credentials in Android app
url: https://infosecwriteups.com/what-is-in-the-strings-xml-b204b2e9bd67?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2023-03-12
fetch_date: 2025-10-04T09:21:45.254394
---

# Hard-Coded credentials in Android app

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fb204b2e9bd67&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fwhat-is-in-the-strings-xml-b204b2e9bd67&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fwhat-is-in-the-strings-xml-b204b2e9bd67&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-b204b2e9bd67---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-b204b2e9bd67---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# Hard-Coded credentials in Android app

[![Barath Stalin](https://miro.medium.com/v2/da:true/resize:fill:64:64/0*QSoMFmFJzk2KtF7d)](https://medium.com/%40severustalin?source=post_page---byline--b204b2e9bd67---------------------------------------)

[Barath Stalin](https://medium.com/%40severustalin?source=post_page---byline--b204b2e9bd67---------------------------------------)

2 min read

·

Feb 1, 2023

--

3

Listen

Share

In the Android, application it is a package called apk(android package kit), it is similar to a zip-like format to extract the data from apk, we use [apktool](https://ibotpeaches.github.io/Apktool/) and JADX-GUI.

> [JADX-GUI](https://github.com/skylot/jadx) is a very awesome tool to extract the data from apk and view the decompiled code. If we normally extract the data file, we couldn’t able to read. It is a hard thing to read. Using JADX we can able to easily understand code.

Press enter or click to view image in full size

![]()

Photo by [Denny Müller](https://unsplash.com/%40redaquamedia?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com/?utm_source=medium&utm_medium=referral)

Every app had the strings.xml, which is a file used to store the strings in the application package.

**How I found the API Key disclosure issue!**

1. Download the apk file from the internet(which app you want to test)

2. Open JADX -> File ->Add File -> Click the test.apk It takes some time to decompile it (depending on your system environment)

3. Scroll Down the left side can able to see Resources -> resources.arsc -> res -> values -> strings.xml

4. Sometimes it may have API Keys, AWS Keys, Default passwords, admin creds, etc

Press enter or click to view image in full size

![]()

**Note:-**

If you find any API Key please refer [to this](https://github.com/streaak/keyhacks) git repository to explain the impact

Linkedin : [Barath Stalin](https://www.linkedin.com/in/barathstalin/)

[Android](https://medium.com/tag/android?source=post_page-----b204b2e9bd67---------------------------------------)

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----b204b2e9bd67---------------------------------------)

[Pentesting](https://medium.com/tag/pentesting?source=post_page-----b204b2e9bd67---------------------------------------)

[Cybersecurity](https://medium.com/tag/cybersecurity?source=post_page-----b204b2e9bd67---------------------------------------)

[Hacking](https://medium.com/tag/hacking?source=post_page-----b204b2e9bd67---------------------------------------)

--

--

3

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--b204b2e9bd67---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--b204b2e9bd67---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--b204b2e9bd67---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--b204b2e9bd67---------------------------------------)

·[Last published 5 days ago](/how-to-find-p1-bugs-using-google-in-your-target-part-1-e37455324dc1?source=post_page---post_publication_info--b204b2e9bd67---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Barath Stalin](https://miro.medium.com/v2/resize:fill:96:96/0*QSoMFmFJzk2KtF7d)](https://medium.com/%40severustalin?source=post_page---post_author_info--b204b2e9bd67---------------------------------------)

[![Barath Stalin](https://miro.medium.com/v2/resize:fill:128:128/0*QSoMFmFJzk2KtF7d)](https://medium.com/%40severustalin?source=post_page---post_author_info--b204b2e9bd67---------------------------------------)

[## Written by Barath Stalin](https://medium.com/%40severustalin?source=post_page---post_author_info--b204b2e9bd67---------------------------------------)

[61 followers](https://medium.com/%40severustalin/followers?source=post_page---post_author_info--b204b2e9bd67---------------------------------------)

·[3 following](https://medium.com/%40severustalin/following?source=post_page---post_author_info--b204b2e9bd67---------------------------------------)

Security Researcher | Pentester | CTF Player | Blogger

## Responses (3)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----b204b2e9bd67---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----b204b2e9bd67---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----b204b2e9bd67---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----b204b2e9bd67---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----b204b2e9bd67---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----b204b2e9bd67---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----b204b2e9bd67---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----b204b2e9bd67---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----b204b2e9bd67---------------------------------------)
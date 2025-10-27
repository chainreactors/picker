---
title: Tricky & Simple EXIF protection Bypass
url: https://infosecwriteups.com/tricky-simple-exif-protection-bypass-5d0babd908f3?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2024-12-05
fetch_date: 2025-10-06T19:37:31.694816
---

# Tricky & Simple EXIF protection Bypass

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F5d0babd908f3&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Ftricky-simple-exif-protection-bypass-5d0babd908f3&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Ftricky-simple-exif-protection-bypass-5d0babd908f3&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-5d0babd908f3---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-5d0babd908f3---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# Tricky & Simple EXIF protection Bypass

[![Saurabh sanmane](https://miro.medium.com/v2/resize:fill:64:64/1*Qiw_r-boFS8aPIHkAKrPww@2x.jpeg)](https://saurabhsanmane.medium.com/?source=post_page---byline--5d0babd908f3---------------------------------------)

[Saurabh sanmane](https://saurabhsanmane.medium.com/?source=post_page---byline--5d0babd908f3---------------------------------------)

2 min read

·

Dec 3, 2024

--

Listen

Share

Press enter or click to view image in full size

![]()

Hello Hackers! 👋

It’s been a year and a half since my last write-up, so I thought lets share something simple yet interesting. I recently came across an intriguing vulnerability and thought I’d share it with you all. Let’s dive in!

For beginners or those unfamiliar with EXIF vulnerabilities, I recommend reviewing this [**article**](https://shahjerry33.medium.com/exif-data-exposure-9bdd6c2c4f2a) first before returning to the current one.

As always there is an web-application, this platform allows users to upload an image as their profile picture. However, I noticed that the image wasn’t being replicated anywhere within the application’s dashboard or services, so I moved on to explore other functionalities such as login and password reset..

During the login process, after entering an email address, the application displayed the user’s profile picture.

Press enter or click to view image in full size

![]()

I opened the image in a new tab, and the URL appeared as follows:

https://pic.abc.com/eyJ----------------------JWT\_token--------------------

If I paste this URL on [**jimpl.com**](https://jimpl.com/) to retrieve EXIF data it did not show any location specific data.

However, I decided to investigate further.

(Again if you don’t know about JWT token go through this [**article**](https://medium.com/%40dmosyan/json-web-tokens-explained-1ca3bd7dc7a0).)

I extracted the JWT token from the URL, navigated to JWT.io, and pasted the token there. In the token’s header section, I discovered a different URL.

![]()

I copied this new URL and pasted it into Jimpl.com, where I was able to successfully retrieve the EXIF data associated with the image, effectively bypassing the EXIF protection mechanism.

Press enter or click to view image in full size

![]()

Isn’t it interesting and simple?

If you liked it do follow me on [Twitter](https://x.com/saurabhsanmane2/) & [Linkedin](https://in.linkedin.com/in/saurabhssanmane) .

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----5d0babd908f3---------------------------------------)

[Cybersecurity](https://medium.com/tag/cybersecurity?source=post_page-----5d0babd908f3---------------------------------------)

[Ethical Hacking](https://medium.com/tag/ethical-hacking?source=post_page-----5d0babd908f3---------------------------------------)

[Vulnerability](https://medium.com/tag/vulnerability?source=post_page-----5d0babd908f3---------------------------------------)

[Information Disclosure](https://medium.com/tag/information-disclosure?source=post_page-----5d0babd908f3---------------------------------------)

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--5d0babd908f3---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--5d0babd908f3---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--5d0babd908f3---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--5d0babd908f3---------------------------------------)

·[Last published 4 hours ago](/baby-dfc2547dc387?source=post_page---post_publication_info--5d0babd908f3---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Saurabh sanmane](https://miro.medium.com/v2/resize:fill:96:96/1*Qiw_r-boFS8aPIHkAKrPww@2x.jpeg)](https://saurabhsanmane.medium.com/?source=post_page---post_author_info--5d0babd908f3---------------------------------------)

[![Saurabh sanmane](https://miro.medium.com/v2/resize:fill:128:128/1*Qiw_r-boFS8aPIHkAKrPww@2x.jpeg)](https://saurabhsanmane.medium.com/?source=post_page---post_author_info--5d0babd908f3---------------------------------------)

[## Written by Saurabh sanmane](https://saurabhsanmane.medium.com/?source=post_page---post_author_info--5d0babd908f3---------------------------------------)

[79 followers](https://saurabhsanmane.medium.com/followers?source=post_page---post_author_info--5d0babd908f3---------------------------------------)

·[7 following](https://medium.com/%40saurabhsanmane/following?source=post_page---post_author_info--5d0babd908f3---------------------------------------)

Indian | Ethical Hacker | Information Security Analyst

## No responses yet

[Help](https://help.medium.com/hc/en-us?source=post_page-----5d0babd908f3---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----5d0babd908f3---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----5d0babd908f3---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----5d0babd908f3---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----5d0babd908f3---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----5d0babd908f3----...
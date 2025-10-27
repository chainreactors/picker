---
title: Bug on ParrotCTF
url: https://infosecwriteups.com/bug-on-parrotctf-e64424b0d043?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2024-10-28
fetch_date: 2025-10-06T18:47:57.578297
---

# Bug on ParrotCTF

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fe64424b0d043&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fbug-on-parrotctf-e64424b0d043&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fbug-on-parrotctf-e64424b0d043&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-e64424b0d043---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-e64424b0d043---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# Bug on ParrotCTF

[![Sidharth Panda](https://miro.medium.com/v2/resize:fill:64:64/1*VBLzbLyWXsq_wCrLHqpnlg.jpeg)](https://sidharthpanda1.medium.com/?source=post_page---byline--e64424b0d043---------------------------------------)

[Sidharth Panda](https://sidharthpanda1.medium.com/?source=post_page---byline--e64424b0d043---------------------------------------)

2 min read

·

Oct 14, 2024

--

Listen

Share

![]()

ParrotCTF

Hello fellas, how are you guys doing!! Well, I am here with another bug write-up.

A little background details about me. I am a new bug bounty hunter still learning about the bugs and trying up new things. For which I am solving THM rooms, HTB rooms, and newly came across a website named, [parrotctf](https://parrot-ctfs.com) which is a great room for intermediate hackers.

Now coming back to how I got the bug on their website.

## **DotGit**

This is a Firefox extension used by hackers/hunters to get the hidden .git directory of the website if it is present.

Link to download: <https://addons.mozilla.org/en-US/firefox/addon/dotgit/>

Once downloaded just pin it to your extension bar, and the next time you will visit any site it will directly show if any is .git directory is present.

## Bug Details

Exposed .git directory is considered as a security misconfiguration. It is significant because it can reveal sensitive information and lead to potential security vulnerabilities such as:-

* Source Code Access.
* Commit History and Sensitive Information.
* Usernames and internal information.
* Information on dependencies and deployment details.

## How I found it

So, when I was reading on Active Directory (AD), I got a notification on dotgit extension mentioning about 2.git directories.

![]()

I decided to look it up over web, and got the following response.

Press enter or click to view image in full size

![]()

and

![]()

Once I found it, I submitted it on discord server and the founder looked an confirmed that it was exposed. within 2–3 hours he updated me that it is mitigated and the site has patched.

Press enter or click to view image in full size

![]()

So yup that is it. This is how I found a security information exposure on parrotctf.

Bug Found: 13–10–2024

Bug Reported: 13–10–2024

Bug Patched: 13–10–2024

I would like to end this write-up here I hope this write-up may come into some help of yours.

Keep learning, keep hacking.

0xkalki signing out.

Radhe Radhe

[Bugbounty](https://medium.com/tag/bugbounty?source=post_page-----e64424b0d043---------------------------------------)

[Hacking](https://medium.com/tag/hacking?source=post_page-----e64424b0d043---------------------------------------)

[Extention](https://medium.com/tag/extention?source=post_page-----e64424b0d043---------------------------------------)

[Parrotctf](https://medium.com/tag/parrotctf?source=post_page-----e64424b0d043---------------------------------------)

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--e64424b0d043---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--e64424b0d043---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--e64424b0d043---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--e64424b0d043---------------------------------------)

·[Last published 3 hours ago](/baby-dfc2547dc387?source=post_page---post_publication_info--e64424b0d043---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Sidharth Panda](https://miro.medium.com/v2/resize:fill:96:96/1*VBLzbLyWXsq_wCrLHqpnlg.jpeg)](https://sidharthpanda1.medium.com/?source=post_page---post_author_info--e64424b0d043---------------------------------------)

[![Sidharth Panda](https://miro.medium.com/v2/resize:fill:128:128/1*VBLzbLyWXsq_wCrLHqpnlg.jpeg)](https://sidharthpanda1.medium.com/?source=post_page---post_author_info--e64424b0d043---------------------------------------)

[## Written by Sidharth Panda](https://sidharthpanda1.medium.com/?source=post_page---post_author_info--e64424b0d043---------------------------------------)

[64 followers](https://sidharthpanda1.medium.com/followers?source=post_page---post_author_info--e64424b0d043---------------------------------------)

·[23 following](https://medium.com/%40sidharthpanda1/following?source=post_page---post_author_info--e64424b0d043---------------------------------------)

CTF player, coder, and trying not to be a script kiddie. Connect with me over: Instagram: @sidharth\_11151926 LinkedIn: [linkedin.com/in/sidharthpanda1126](http://linkedin.com/in/sidharthpanda1126)

## No responses yet

[Help](https://help.medium.com/hc/en-us?source=post_page-----e64424b0d043---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----e64424b0d043---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----e64424b0d043---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----e64424b0d043---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----e64424b0d043---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----e64424b0d043---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502...
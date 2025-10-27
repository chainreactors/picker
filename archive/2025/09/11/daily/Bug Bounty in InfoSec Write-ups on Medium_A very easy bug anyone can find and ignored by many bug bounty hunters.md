---
title: A very easy bug anyone can find and ignored by many bug bounty hunters
url: https://infosecwriteups.com/a-very-easy-bug-anyone-can-find-8d2b11a768c7?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-09-11
fetch_date: 2025-10-02T19:57:50.798090
---

# A very easy bug anyone can find and ignored by many bug bounty hunters

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F8d2b11a768c7&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fa-very-easy-bug-anyone-can-find-8d2b11a768c7&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fa-very-easy-bug-anyone-can-find-8d2b11a768c7&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-8d2b11a768c7---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-8d2b11a768c7---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# A very easy bug anyone can find

[![Be nice insabat](https://miro.medium.com/v2/da:true/resize:fill:64:64/0*4PbEBGv0pYv2HfgQ)](https://medium.com/%40InsbatArshad?source=post_page---byline--8d2b11a768c7---------------------------------------)

[Be nice insabat](https://medium.com/%40InsbatArshad?source=post_page---byline--8d2b11a768c7---------------------------------------)

2 min read

·

Sep 15, 2024

--

1

Share

Hello readers how are you, i hope all of you are doing great.

I am back with another writeup for the community:

I was just searching for private programs for hyperlink injection on google after choosing a random program i was just click on blog then will reached at <https://target.com/blog>

scroll down and see that there was a submit form having name and email field with the help of that we can subscribe to the platform for new blog posts notifications, then i immidiately injected html and ssti payload

{{8\*8}}/”><A HREF=bing.com>HELLO</A”>

in name field and my email in email field then “click keep me updated button” yes i received an email but some malicious characters removed from the payload and some were cached as it is

Press enter or click to view image in full size

![]()

then i again went to submit form and injected simple hyper link payload like “ sign in here evil.com and get 100$ bonus” in name field and click the submit button and went to my inbox and my hyper link was successfully injected

Press enter or click to view image in full size

![]()

I was surprised, but not 100% sure about bounty or acceptance of bug, because some programs dont take serious this bug, i was…

--

--

1

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--8d2b11a768c7---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--8d2b11a768c7---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--8d2b11a768c7---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--8d2b11a768c7---------------------------------------)

·[Last published 4 days ago](/how-to-find-p1-bugs-using-google-in-your-target-part-1-e37455324dc1?source=post_page---post_publication_info--8d2b11a768c7---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Be nice insabat](https://miro.medium.com/v2/resize:fill:96:96/0*4PbEBGv0pYv2HfgQ)](https://medium.com/%40InsbatArshad?source=post_page---post_author_info--8d2b11a768c7---------------------------------------)

[![Be nice insabat](https://miro.medium.com/v2/resize:fill:128:128/0*4PbEBGv0pYv2HfgQ)](https://medium.com/%40InsbatArshad?source=post_page---post_author_info--8d2b11a768c7---------------------------------------)

[## Written by Be nice insabat](https://medium.com/%40InsbatArshad?source=post_page---post_author_info--8d2b11a768c7---------------------------------------)

[297 followers](https://medium.com/%40InsbatArshad/followers?source=post_page---post_author_info--8d2b11a768c7---------------------------------------)

·[106 following](https://medium.com/%40InsbatArshad/following?source=post_page---post_author_info--8d2b11a768c7---------------------------------------)

penetration tester, ethical hacker, bug bounty hunter...

## Responses (1)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----8d2b11a768c7---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----8d2b11a768c7---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----8d2b11a768c7---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----8d2b11a768c7---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----8d2b11a768c7---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----8d2b11a768c7---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----8d2b11a768c7---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----8d2b11a768c7---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----8d2b11a768c7---------------------------------------)
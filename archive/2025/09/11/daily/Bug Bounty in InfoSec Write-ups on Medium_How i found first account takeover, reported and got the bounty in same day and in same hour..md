---
title: How i found first account takeover, reported and got the bounty in same day and in same hour.
url: https://infosecwriteups.com/bismillah-hir-rahman-nir-raheem-9adef82e9718?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-09-11
fetch_date: 2025-10-02T19:57:47.156661
---

# How i found first account takeover, reported and got the bounty in same day and in same hour.

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F9adef82e9718&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fbismillah-hir-rahman-nir-raheem-9adef82e9718&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fbismillah-hir-rahman-nir-raheem-9adef82e9718&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-9adef82e9718---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-9adef82e9718---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

[![Be nice insabat](https://miro.medium.com/v2/da:true/resize:fill:64:64/0*4PbEBGv0pYv2HfgQ)](https://medium.com/%40InsbatArshad?source=post_page---byline--9adef82e9718---------------------------------------)

[Be nice insabat](https://medium.com/%40InsbatArshad?source=post_page---byline--9adef82e9718---------------------------------------)

3 min read

·

Sep 9, 2024

--

3

Share

How i found, reported and got the bounty of my first easy account take over on the reset password functionality

Assalam o alaikum wa rakh ma tullah

Advance apologise for any mistake

Nice to see you here i am writing my third article which is also very interesting because i found a bug three days ago at 11:30 to 11:40 approximately, reported it at 11:50 and the bounty was rewarded at 12:37 you can see

Press enter or click to view image in full size

![]()

Lets start the story, it was my first account takeover i am very excited and must have to share it with all the community

So lets assume the target as target.com and its signup page is on app.target.com i have reported an info disclosure on same program a couple of week ago also but that was not applicable, so after 5 to 7 days i decided to test it again and open the target and was testing for account takeover via host header on forgot password option, forgot password email was looked like “any.app.target.com/reset-password/token?email=myemail.com”

i tried to change the host header from any.app.target.com to any.app.target.com.evil.pk and sent the password reset request, then go to gmail, there is no message then i also change the origin header to any.app.target.com.evil.pk there was also not any response in email, then i changed the origin header to its original form and go to referer header and change it to any.app.taget.com.evil.pk and…

--

--

3

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--9adef82e9718---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--9adef82e9718---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--9adef82e9718---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--9adef82e9718---------------------------------------)

·[Last published 4 days ago](/how-to-find-p1-bugs-using-google-in-your-target-part-1-e37455324dc1?source=post_page---post_publication_info--9adef82e9718---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Be nice insabat](https://miro.medium.com/v2/resize:fill:96:96/0*4PbEBGv0pYv2HfgQ)](https://medium.com/%40InsbatArshad?source=post_page---post_author_info--9adef82e9718---------------------------------------)

[![Be nice insabat](https://miro.medium.com/v2/resize:fill:128:128/0*4PbEBGv0pYv2HfgQ)](https://medium.com/%40InsbatArshad?source=post_page---post_author_info--9adef82e9718---------------------------------------)

[## Written by Be nice insabat](https://medium.com/%40InsbatArshad?source=post_page---post_author_info--9adef82e9718---------------------------------------)

[297 followers](https://medium.com/%40InsbatArshad/followers?source=post_page---post_author_info--9adef82e9718---------------------------------------)

·[106 following](https://medium.com/%40InsbatArshad/following?source=post_page---post_author_info--9adef82e9718---------------------------------------)

penetration tester, ethical hacker, bug bounty hunter...

## Responses (3)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----9adef82e9718---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----9adef82e9718---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----9adef82e9718---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----9adef82e9718---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----9adef82e9718---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----9adef82e9718---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----9adef82e9718---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----9adef82e9718---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----9adef82e9718---------------------------------------)
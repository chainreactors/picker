---
title: Portswigger Lab: JWT authentication bypass via algorithm confusion with no exposed key, a slightly…
url: https://infosecwriteups.com/portswigger-lab-jwt-authentication-bypass-via-algorithm-confusion-with-no-exposed-key-a-slightly-e28602b6ef70?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2022-12-13
fetch_date: 2025-10-04T01:18:14.083075
---

# Portswigger Lab: JWT authentication bypass via algorithm confusion with no exposed key, a slightly…

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fe28602b6ef70&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fportswigger-lab-jwt-authentication-bypass-via-algorithm-confusion-with-no-exposed-key-a-slightly-e28602b6ef70&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fportswigger-lab-jwt-authentication-bypass-via-algorithm-confusion-with-no-exposed-key-a-slightly-e28602b6ef70&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-e28602b6ef70---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-e28602b6ef70---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# Portswigger Lab: JWT authentication bypass via algorithm confusion with no exposed key, a slightly different walkthrough

## , or how I learned the importance of RTFM yet again

[![Vuk Ivanovic](https://miro.medium.com/v2/resize:fill:64:64/1*6QX8KKh6p2FhUxOAq1QQ8Q.png)](https://medium.com/%40vuk.ivanovic9000?source=post_page---byline--e28602b6ef70---------------------------------------)

[Vuk Ivanovic](https://medium.com/%40vuk.ivanovic9000?source=post_page---byline--e28602b6ef70---------------------------------------)

5 min read

·

Dec 12, 2022

--

Share

I mean, to be perfectly honest, this article started as a huge complaint in my head while I was working on solving [the lab in question](https://portswigger.net/web-security/jwt/algorithm-confusion/lab-jwt-authentication-bypass-via-algorithm-confusion-with-no-exposed-key), but in the end it turned out I was in the wrong. So, here’s a different walkthrough compared to the community walkthroughs under the solutions of this lab. And, if you consider yourself not as smart at times when it seems that you ought to be which then leads into frustration/anger, just keep in mind to take some deep breaths to calm down and think things through. You’ll be surprised at how far you can get when taking things slowly, even when you’re sure that you have done it all correctly and you think that the solution is just this one little thing that you missed so you try and speed through looking for it. But, of course you can’t find it because it’s not just one little thing. What you do find is that you are even more angry because you’ve been mentally running through this maze, and you can’t find the cheese, but you can smell it, and that drives you crazy. Instead, just start slowly from the get go, and the smell of cheese won’t be spread evenly all over the maze confusing you in which direction to go. Which means, you’ll actually get to the cheese sooner while not losing your cool. I don't know why the maze and cheese metaphor, but there you go :)

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--e28602b6ef70---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--e28602b6ef70---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--e28602b6ef70---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--e28602b6ef70---------------------------------------)

·[Last published 5 days ago](/how-to-find-p1-bugs-using-google-in-your-target-part-1-e37455324dc1?source=post_page---post_publication_info--e28602b6ef70---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Vuk Ivanovic](https://miro.medium.com/v2/resize:fill:96:96/1*6QX8KKh6p2FhUxOAq1QQ8Q.png)](https://medium.com/%40vuk.ivanovic9000?source=post_page---post_author_info--e28602b6ef70---------------------------------------)

[![Vuk Ivanovic](https://miro.medium.com/v2/resize:fill:128:128/1*6QX8KKh6p2FhUxOAq1QQ8Q.png)](https://medium.com/%40vuk.ivanovic9000?source=post_page---post_author_info--e28602b6ef70---------------------------------------)

[## Written by Vuk Ivanovic](https://medium.com/%40vuk.ivanovic9000?source=post_page---post_author_info--e28602b6ef70---------------------------------------)

[808 followers](https://medium.com/%40vuk.ivanovic9000/followers?source=post_page---post_author_info--e28602b6ef70---------------------------------------)

·[40 following](https://medium.com/%40vuk.ivanovic9000/following?source=post_page---post_author_info--e28602b6ef70---------------------------------------)

IT Security and bug bounty hunting, knowledge collector especially anything with word quantum, and sometimes writer of fiction.

## No responses yet

[Help](https://help.medium.com/hc/en-us?source=post_page-----e28602b6ef70---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----e28602b6ef70---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----e28602b6ef70---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----e28602b6ef70---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----e28602b6ef70---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----e28602b6ef70---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----e28602b6ef70---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----e28602b6ef70---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----e28602b6ef70---------------------------------------)
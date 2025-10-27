---
title: “That One Time I Found a Golden Ticket in a Desktop App”
url: https://infosecwriteups.com/that-one-time-i-found-a-golden-ticket-in-a-desktop-app-8db725c10338?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-09-13
fetch_date: 2025-10-02T20:05:39.762029
---

# “That One Time I Found a Golden Ticket in a Desktop App”

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F8db725c10338&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fthat-one-time-i-found-a-golden-ticket-in-a-desktop-app-8db725c10338&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fthat-one-time-i-found-a-golden-ticket-in-a-desktop-app-8db725c10338&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-8db725c10338---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-8db725c10338---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# “That One Time I Found a Golden Ticket in a Desktop App”

[![Aman Sharma](https://miro.medium.com/v2/da:true/resize:fill:64:64/0*gTsmBWudIxLcZoel)](https://amannsharmaa.medium.com/?source=post_page---byline--8db725c10338---------------------------------------)

[Aman Sharma](https://amannsharmaa.medium.com/?source=post_page---byline--8db725c10338---------------------------------------)

6 min read

·

Sep 9, 2025

--

Share

Let’s be real. We’ve all seen those mind-blowing bug bounty write-ups on Twitter. The ones that make you wonder, “How did they even think of that?” I used to feel the same way. Then I found a vulnerability that changed my perspective entirely. It wasn’t a complex, chain-exploitation zero-day. It was something much simpler, and because of that, much more common.

[free link](https://amannsharmaa.medium.com/that-one-time-i-found-a-golden-ticket-in-a-desktop-app-8db725c10338?sk=d6371e6792846a825bc134614f4f3b2d)

Press enter or click to view image in full size

![]()

I want to pull back the curtain and show you the exact, practical steps behind a find that involved a desktop app and a secret it was never supposed to have. This is a hands-on guide, the kind I wish I had when I started.

### The “Aha!” Moment: It’s All in the Box

The target was a desktop application built with Electron. If you’ve ever used Slack, Discord, or VS Code, you’ve used an Electron app. Developers love it because they can build desktop software using web tech — HTML, CSS, and JavaScript.

But here’s the thing every hacker needs to know: that beautiful, packaged app you download is basically a box holding all its source code. And sometimes, the developers accidentally leave the key to the kingdom inside that box.

My journey started with a simple question: “What’s actually in this thing?”

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--8db725c10338---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--8db725c10338---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--8db725c10338---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--8db725c10338---------------------------------------)

·[Last published 4 days ago](/how-to-find-p1-bugs-using-google-in-your-target-part-1-e37455324dc1?source=post_page---post_publication_info--8db725c10338---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Aman Sharma](https://miro.medium.com/v2/resize:fill:96:96/0*gTsmBWudIxLcZoel)](https://amannsharmaa.medium.com/?source=post_page---post_author_info--8db725c10338---------------------------------------)

[![Aman Sharma](https://miro.medium.com/v2/resize:fill:128:128/0*gTsmBWudIxLcZoel)](https://amannsharmaa.medium.com/?source=post_page---post_author_info--8db725c10338---------------------------------------)

[## Written by Aman Sharma](https://amannsharmaa.medium.com/?source=post_page---post_author_info--8db725c10338---------------------------------------)

[739 followers](https://amannsharmaa.medium.com/followers?source=post_page---post_author_info--8db725c10338---------------------------------------)

·[14 following](https://medium.com/%40amannsharmaa/following?source=post_page---post_author_info--8db725c10338---------------------------------------)

| Data Enthusiast | SQL | Python | Power BI | ML | Exploring Cybersecurity & Bug Bounty | Sharing real-world analytics, dashboards & security insights.

## No responses yet

[Help](https://help.medium.com/hc/en-us?source=post_page-----8db725c10338---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----8db725c10338---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----8db725c10338---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----8db725c10338---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----8db725c10338---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----8db725c10338---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----8db725c10338---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----8db725c10338---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----8db725c10338---------------------------------------)
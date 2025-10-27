---
title: How a Simple Bug Could Have Taken Down Your Instagram Tags
url: https://infosecwriteups.com/how-a-simple-bug-could-have-taken-down-your-instagram-tags-d3247e931c9d?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2024-11-24
fetch_date: 2025-10-06T19:14:58.245632
---

# How a Simple Bug Could Have Taken Down Your Instagram Tags

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fd3247e931c9d&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-a-simple-bug-could-have-taken-down-your-instagram-tags-d3247e931c9d&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-a-simple-bug-could-have-taken-down-your-instagram-tags-d3247e931c9d&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-d3247e931c9d---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-d3247e931c9d---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# **How a Simple Bug Could Have Taken Down Your Instagram Tags**

[![Kiril Krivoguz](https://miro.medium.com/v2/da:true/resize:fill:64:64/0*aqpPtHR387_KME7t)](https://medium.com/%40kiril.krivogyz?source=post_page---byline--d3247e931c9d---------------------------------------)

[Kiril Krivoguz](https://medium.com/%40kiril.krivogyz?source=post_page---byline--d3247e931c9d---------------------------------------)

3 min read

·

Oct 7, 2024

--

1

Listen

Share

Hey everyone! I wanted to share a recent finding of mine — a vulnerability in Instagram’s tagging functionality that could have led to a denial of service (DoS) condition for users. I’ve already reported this to Meta, and they’ve implemented a fix. Let’s dive into the technical details and see what we can learn from it.

What are Tags on Instagram?

Just a quick refresher: Instagram allows users to tag each other in posts, which creates a link to their profile and sends them a notification. It’s a core feature for giving credit, acknowledging presence, and connecting with others on the platform.

Press enter or click to view image in full size

![]()

Uncovering the Vulnerability.

I was testing the Instagram Android app, focusing on the tagging feature, and using Burp Suite to intercept and modify requests. I noticed a parameter called “categories” within the tagging request (POST /API/v1/media/your\_id/edit\_media/). This parameter seemed to be related to the profile category of the tagged account (e.g., “Business,” “Public Figure”).

Curious, I started manipulating this parameter. Initially, I simply changed its value to a random string, and to my surprise, I was able to tag someone with a fabricated category. This unexpected behavior hinted at a potential issue.

To explore further, I sent an extremely large string (around 8MB) as the value for the “categories” parameter. And it worked! There was no input validation or character limit in place.

Press enter or click to view image in full size

![]()

Press enter or click to view image in full size

![]()

The consequence? When I logged in as the tagged account, their “Tags” section failed to load. This meant an attacker could effectively prevent users from accessing and managing their tags — a classic DoS scenario.

![]()

Further testing revealed that if the victim had enabled the option to manually approve tags, the “Pending Tags” section would also crash. This prevented the victim from reviewing and approving legitimate tags, and since they couldn’t reject the malicious tag either, there was no way for them to self-mitigate the issue.

![]()

**Impact**

This vulnerability could have been exploited to disrupt the user experience for any Instagram user, hindering their ability to engage with a core feature of the platform.

**Tools and Techniques**

For those interested in Instagram Android app testing, this tool was helpful for bypassing SSL pinning: <https://github.com/Eltion/Instagram-SSL-Pinning-Bypass>

**Key Takeaway**

This vulnerability highlights how even seemingly minor features, like tagging, can have hidden complexities that lead to security flaws. It underscores the importance of thorough testing, especially focusing on edge cases and unexpected inputs.

A key takeaway for fellow bug hunters is to always consider character limits and input validation, even for parameters that aren’t immediately visible. Don’t assume any limitations are in place!

Finally, this finding is a reminder that vulnerabilities can exist anywhere, even in widely used applications like Instagram. It encourages us to keep exploring, learning, and pushing the boundaries of security testing. You never know what you might find!

**Timeline**

* Reported: April 24, 2024
* Triaged: May 3, 2024
* $500 awarded: May 8, 2024
* Fixed: May 16, 2024

Press enter or click to view image in full size

![]()

Thanks for reading!

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----d3247e931c9d---------------------------------------)

[Bug Bounty Writeup](https://medium.com/tag/bug-bounty-writeup?source=post_page-----d3247e931c9d---------------------------------------)

[Bug Bounty Tips](https://medium.com/tag/bug-bounty-tips?source=post_page-----d3247e931c9d---------------------------------------)

[Hacking](https://medium.com/tag/hacking?source=post_page-----d3247e931c9d---------------------------------------)

[Instagram](https://medium.com/tag/instagram?source=post_page-----d3247e931c9d---------------------------------------)

--

--

1

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--d3247e931c9d---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--d3247e931c9d---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--d3247e931c9d---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--d3247e931c9d---------------------------------------)

·[Last published 4 hours ago](/baby-dfc2547dc387?source=post_page---post_publication_info--d3247e931c9d---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Kiril Krivoguz](https://miro.medium.com/v2/resize:fill:96:96/0*aqpPtHR387_KME7t)](https://medium.com/%40kiril.krivogyz?source=post_page---post_author_info--d3247e931c9d---------------------------------------)

[![Kiril Krivoguz](https://miro.medium.co...
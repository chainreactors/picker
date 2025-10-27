---
title: This Clickjacking Bug Was Worth $140 – Here’s How
url: https://infosecwriteups.com/this-clickjacking-bug-was-worth-140-heres-how-8da607927f62?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-09-14
fetch_date: 2025-10-02T20:08:59.726644
---

# This Clickjacking Bug Was Worth $140 – Here’s How

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F8da607927f62&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fthis-clickjacking-bug-was-worth-140-heres-how-8da607927f62&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fthis-clickjacking-bug-was-worth-140-heres-how-8da607927f62&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-8da607927f62---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-8da607927f62---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# **💰 This Clickjacking Bug Was Worth $140 – Here’s How**

[![Manav](https://miro.medium.com/v2/resize:fill:64:64/1*1bxZBHgXieZgmlxhRcd9Jw.jpeg)](https://medium.com/%40manav_24?source=post_page---byline--8da607927f62---------------------------------------)

[Manav](https://medium.com/%40manav_24?source=post_page---byline--8da607927f62---------------------------------------)

3 min read

·

Jul 28, 2025

--

Listen

Share

*Hello friends, welcome back!*
Today, I’ll be sharing how I discovered a Clickjacking vulnerability and successfully chained it with an open redirect to earn a **$140** bounty 💰. It’s a great example of how chaining simple bugs can lead to real impact. Whether you’re new to bug hunting or experienced hunter you’re more than welcome here. Let’s dive in! 🔍

![]()

### **What is Clickjacking?**

Clickjacking is something many of us in the security space have come across before, but just to keep things clear, let’s quickly revisit what it actually is.

Clickjacking is a trick where users are made to click on something without realizing it, usually by showing a real page inside a hidden or fake frame, so the user thinks they’re clicking one thing, but they’re actually clicking something else.

> “Let’s see how I chained Clickjacking with an Open Redirect.”

### **STEPS TO REPRODUCE :**

1 -> Let’s consider the target as **redacted.com**. I found the vulnerability on the “**Login**” page, As I was Doing Login process I thought, “*Why not test for Clickjacking real quick?*” It’s simple, but you never know what might turn up.

2 -> I visited to [clickjacker.io](https://clickjacker.io/) to test the url and confirming the Clickjacking issue, I realized it might not be enough on its own to qualify for a bounty. So, I thought to chain it with something more impactful.

Press enter or click to view image in full size

![]()

3 -> I decided to chain it with Open redirect which can be classified as a low or medium severity.. I wrote a HTML code in a notepad file. Which allowed me to combine both vulnerabilities and demonstrate how they could be exploited together.

Press enter or click to view image in full size

![]()

4 -> Replace the affected URL with: <https://example.com> .

5 -> Save this as a HTML File and opened it in a web browser | Click on Click here to win the Prize..

6 -> BOOM !!!! I was redirected to [evil.com](https://evil.com/)

Press enter or click to view image in full size

![]()

> **📬 Disclosure & Reward**

When I reported the bug, the expectation was not so high for a reward.But the team confirmed it and sent a **$140 bounty**. Not bad for something I discovered just by stumbling around.

Press enter or click to view image in full size

![]()

That’s a wrap on this little adventure ,hope you found it insightful!
Feel free to reach out on [LinkedIn](https://www.linkedin.com/in/manav2829/) if you’ve got questions or just want to connect.
Always happy to chat, share, and learn together.
**Happy Hunting!!** 🔍🐞

![]()

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----8da607927f62---------------------------------------)

[Red Team](https://medium.com/tag/red-team?source=post_page-----8da607927f62---------------------------------------)

[Bug Bounty Writeup](https://medium.com/tag/bug-bounty-writeup?source=post_page-----8da607927f62---------------------------------------)

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--8da607927f62---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--8da607927f62---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--8da607927f62---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--8da607927f62---------------------------------------)

·[Last published 4 days ago](/how-to-find-p1-bugs-using-google-in-your-target-part-1-e37455324dc1?source=post_page---post_publication_info--8da607927f62---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Manav](https://miro.medium.com/v2/resize:fill:96:96/1*1bxZBHgXieZgmlxhRcd9Jw.jpeg)](https://medium.com/%40manav_24?source=post_page---post_author_info--8da607927f62---------------------------------------)

[![Manav](https://miro.medium.com/v2/resize:fill:128:128/1*1bxZBHgXieZgmlxhRcd9Jw.jpeg)](https://medium.com/%40manav_24?source=post_page---post_author_info--8da607927f62---------------------------------------)

[## Written by Manav](https://medium.com/%40manav_24?source=post_page---post_author_info--8da607927f62---------------------------------------)

[45 followers](https://medium.com/%40manav_24/followers?source=post_page---post_author_info--8da607927f62---------------------------------------)

·[8 following](https://medium.com/%40manav_24/following?source=post_page---post_author_info--8da607927f62---------------------------------------)

Cyber security Researcher || Bug Bounty Hunter || Red Teamer || Pentester || VAPT

## No responses yet

[Help](https://help.medium.com/hc/en-us?source=post_page-----8da607927f62---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----8da607927f62---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----8da607927f62---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d...
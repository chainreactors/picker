---
title: “The Registration Flaw That Almost Got Missed: Hunting Weak Authentication Links”
url: https://infosecwriteups.com/the-registration-flaw-that-almost-got-missed-hunting-weak-authentication-links-75337daa6bf9?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-09-27
fetch_date: 2025-10-02T20:46:41.001048
---

# “The Registration Flaw That Almost Got Missed: Hunting Weak Authentication Links”

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F75337daa6bf9&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fthe-registration-flaw-that-almost-got-missed-hunting-weak-authentication-links-75337daa6bf9&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fthe-registration-flaw-that-almost-got-missed-hunting-weak-authentication-links-75337daa6bf9&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-75337daa6bf9---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-75337daa6bf9---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# “The Registration Flaw That Almost Got Missed: Hunting Weak Authentication Links”

[![Aman Sharma](https://miro.medium.com/v2/da:true/resize:fill:64:64/0*gTsmBWudIxLcZoel)](https://amannsharmaa.medium.com/?source=post_page---byline--75337daa6bf9---------------------------------------)

[Aman Sharma](https://amannsharmaa.medium.com/?source=post_page---byline--75337daa6bf9---------------------------------------)

5 min read

·

6 days ago

--

Share

I was about to close the tab when I noticed it. The password reset email from the fintech startup used `http://` instead of `https://`. At first glance, it seemed minor—until I realized the reset token in that insecure link was all an attacker needed to take over any account. This "low-severity" find turned into a critical demonstration of how authentication systems fail at the most basic level.

[free link](https://amannsharmaa.medium.com/the-registration-flaw-that-almost-got-missed-hunting-weak-authentication-links-75337daa6bf9?sk=a11b65a61c2d02dae9895fc1fc97f9a3)

Press enter or click to view image in full size

![]()

### When HTTPS Becomes Optional: The Verification Link Problem

Many developers assume that because the login page uses HTTPS, their entire application is secure. But the emails they send tell a different story.

The Real-World Impact:
On a popular productivity app, I found that account verification links were sent over HTTP. The sequence went like this:

1. User registers at `<https://app.com/signup>`
2. App sends verification email with link: `<http://app.com/verify?token=abc123>`
3. User clicks link and gets automatically logged in

The vulnerability? Anyone intercepting that email (on public Wi-Fi, compromised email account, or malicious ISP) could capture the token and hijack the account…

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--75337daa6bf9---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--75337daa6bf9---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--75337daa6bf9---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--75337daa6bf9---------------------------------------)

·[Last published 4 days ago](/how-to-find-p1-bugs-using-google-in-your-target-part-1-e37455324dc1?source=post_page---post_publication_info--75337daa6bf9---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Aman Sharma](https://miro.medium.com/v2/resize:fill:96:96/0*gTsmBWudIxLcZoel)](https://amannsharmaa.medium.com/?source=post_page---post_author_info--75337daa6bf9---------------------------------------)

[![Aman Sharma](https://miro.medium.com/v2/resize:fill:128:128/0*gTsmBWudIxLcZoel)](https://amannsharmaa.medium.com/?source=post_page---post_author_info--75337daa6bf9---------------------------------------)

[## Written by Aman Sharma](https://amannsharmaa.medium.com/?source=post_page---post_author_info--75337daa6bf9---------------------------------------)

[739 followers](https://amannsharmaa.medium.com/followers?source=post_page---post_author_info--75337daa6bf9---------------------------------------)

·[14 following](https://medium.com/%40amannsharmaa/following?source=post_page---post_author_info--75337daa6bf9---------------------------------------)

| Data Enthusiast | SQL | Python | Power BI | ML | Exploring Cybersecurity & Bug Bounty | Sharing real-world analytics, dashboards & security insights.

## No responses yet

[Help](https://help.medium.com/hc/en-us?source=post_page-----75337daa6bf9---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----75337daa6bf9---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----75337daa6bf9---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----75337daa6bf9---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----75337daa6bf9---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----75337daa6bf9---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----75337daa6bf9---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----75337daa6bf9---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----75337daa6bf9---------------------------------------)
---
title: I Found a Bug in Internal Testing: Stored XSS in KYC Form Address Field
url: https://infosecwriteups.com/i-found-a-bug-in-internal-testing-stored-xss-in-kyc-form-address-field-4ede43cf99a2?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-07-08
fetch_date: 2025-10-06T23:24:01.122677
---

# I Found a Bug in Internal Testing: Stored XSS in KYC Form Address Field

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F4ede43cf99a2&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fi-found-a-bug-in-internal-testing-stored-xss-in-kyc-form-address-field-4ede43cf99a2&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fi-found-a-bug-in-internal-testing-stored-xss-in-kyc-form-address-field-4ede43cf99a2&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[Mastodon](https://me.dm/%40yaminiy369)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-4ede43cf99a2---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-4ede43cf99a2---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# I Found a Bug in Internal Testing: Stored XSS in KYC Form Address Field

[![Yamini Yadav_369](https://miro.medium.com/v2/resize:fill:64:64/1*p_XKCX_UY71fc1nF8ueZJw.png)](https://yamini369.medium.com/?source=post_page---byline--4ede43cf99a2---------------------------------------)

[Yamini Yadav\_369](https://yamini369.medium.com/?source=post_page---byline--4ede43cf99a2---------------------------------------)

9 min read

·

Jul 7, 2025

--

Share

![]()

Image by Pixabay

### When an Address Field Became an XSS Bug Bounty

It was just another Tuesday of internal testing on our trading platform when I stumbled on something unexpected. I was filling out the KYC form for a test user — you know, the usual Name, Address, ID number — and I thought, **“What if I try putting some HTML or script into the *Address* field?”** To my surprise, the app accepted it! Later, when I viewed that user’s profile, the hidden test script I entered popped up an alert. I had discovered a **Stored Cross-Site Scripting (XSS)** vulnerability in the address field.

This hit me as a reminder of why **input validation** is so important. Simply put, input validation means checking user-provided data before using it in the application. It’s often called the “first line of defense” in secure development. By validating input (for example, ensuring an address field contains only normal characters and not HTML tags), we prevent *malicious* code from being injected into our system.

The OWASP Secure Coding guide even advises using a whitelist approach (an *allow-list*) to define what good input looks like, rather than trying to block bad input, which attackers can often bypass. In short, when we *don’t* validate inputs properly, we leave openings for all sorts of attacks —…

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--4ede43cf99a2---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--4ede43cf99a2---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--4ede43cf99a2---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--4ede43cf99a2---------------------------------------)

·[Last published 2 hours ago](/actuator-unleashed-a-guide-to-finding-and-exploiting-spring-boot-actuator-endpoints-29252dcd9d79?source=post_page---post_publication_info--4ede43cf99a2---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Yamini Yadav_369](https://miro.medium.com/v2/resize:fill:96:96/1*p_XKCX_UY71fc1nF8ueZJw.png)](https://yamini369.medium.com/?source=post_page---post_author_info--4ede43cf99a2---------------------------------------)

[![Yamini Yadav_369](https://miro.medium.com/v2/resize:fill:128:128/1*p_XKCX_UY71fc1nF8ueZJw.png)](https://yamini369.medium.com/?source=post_page---post_author_info--4ede43cf99a2---------------------------------------)

[## Written by Yamini Yadav\_369](https://yamini369.medium.com/?source=post_page---post_author_info--4ede43cf99a2---------------------------------------)

[140 followers](https://yamini369.medium.com/followers?source=post_page---post_author_info--4ede43cf99a2---------------------------------------)

·[29 following](https://medium.com/%40yamini369/following?source=post_page---post_author_info--4ede43cf99a2---------------------------------------)

| Bug Hunter | Finding and securing web vulnerabilities. It's not about competing with others; it's about self-improvement. ✨️🧿🦢🦋📚📸

## No responses yet

[Help](https://help.medium.com/hc/en-us?source=post_page-----4ede43cf99a2---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----4ede43cf99a2---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----4ede43cf99a2---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----4ede43cf99a2---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----4ede43cf99a2---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----4ede43cf99a2---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----4ede43cf99a2---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----4ede43cf99a2---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----4ede43cf99a2---------------------------------------)
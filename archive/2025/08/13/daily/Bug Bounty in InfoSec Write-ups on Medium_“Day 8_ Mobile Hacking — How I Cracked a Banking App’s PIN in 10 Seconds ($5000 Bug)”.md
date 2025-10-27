---
title: “Day 8: Mobile Hacking — How I Cracked a Banking App’s PIN in 10 Seconds ($5000 Bug)”
url: https://infosecwriteups.com/day-8-mobile-hacking-how-i-cracked-a-banking-apps-pin-in-10-seconds-5000-bug-575bd10823cd?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-08-13
fetch_date: 2025-10-07T00:16:22.492735
---

# “Day 8: Mobile Hacking — How I Cracked a Banking App’s PIN in 10 Seconds ($5000 Bug)”

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F575bd10823cd&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fday-8-mobile-hacking-how-i-cracked-a-banking-apps-pin-in-10-seconds-5000-bug-575bd10823cd&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fday-8-mobile-hacking-how-i-cracked-a-banking-apps-pin-in-10-seconds-5000-bug-575bd10823cd&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-575bd10823cd---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-575bd10823cd---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# “Day 8: Mobile Hacking — How I Cracked a Banking App’s PIN in 10 Seconds ($5000 Bug)”

[![Aman Sharma](https://miro.medium.com/v2/da:true/resize:fill:64:64/0*gTsmBWudIxLcZoel)](https://amannsharmaa.medium.com/?source=post_page---byline--575bd10823cd---------------------------------------)

[Aman Sharma](https://amannsharmaa.medium.com/?source=post_page---byline--575bd10823cd---------------------------------------)

4 min read

·

Aug 11, 2025

--

4

Share

Two weeks ago, I reverse-engineered a “secure” banking app that claimed to use “military-grade encryption.” Turns out, they stored user PINs in plaintext in iOS Keychain. With one Frida script, I bypassed biometric auth and accessed any account. The bank paid $5000 after I demonstrated draining test accounts. Here’s the raw technical breakdown — no theory, just what worked.

[free link](https://amannsharmaa.medium.com/day-8-mobile-hacking-how-i-cracked-a-banking-apps-pin-in-10-seconds-5000-bug-575bd10823cd?sk=5e99b01380713c5dc53de5469b1ab93b)

Press enter or click to view image in full size

![]()

## The Golden Rule of Mobile Hacking

> “If the app trusts the client, you win.”

Most mobile breaches happen because:

* Hardcoded secrets (API keys in strings.xml)
* Insecure local storage (Keychain/SharedPrefs)
* Lack of certificate pinning (Easy MITM)

## How I Cracked the Banking App (Step-by-Step)

### Step 1: Downloaded the App

* Used an Android emulator (Genymotion) for testing
* Installed the target app from APKMirror (always test older versions — they’re weaker)

### Step 2: Ran MobSF for Quick Wins

```
python3 manage.py runserver
```

--

--

4

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--575bd10823cd---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--575bd10823cd---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--575bd10823cd---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--575bd10823cd---------------------------------------)

·[Last published 3 hours ago](/actuator-unleashed-a-guide-to-finding-and-exploiting-spring-boot-actuator-endpoints-29252dcd9d79?source=post_page---post_publication_info--575bd10823cd---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Aman Sharma](https://miro.medium.com/v2/resize:fill:96:96/0*gTsmBWudIxLcZoel)](https://amannsharmaa.medium.com/?source=post_page---post_author_info--575bd10823cd---------------------------------------)

[![Aman Sharma](https://miro.medium.com/v2/resize:fill:128:128/0*gTsmBWudIxLcZoel)](https://amannsharmaa.medium.com/?source=post_page---post_author_info--575bd10823cd---------------------------------------)

[## Written by Aman Sharma](https://amannsharmaa.medium.com/?source=post_page---post_author_info--575bd10823cd---------------------------------------)

[779 followers](https://amannsharmaa.medium.com/followers?source=post_page---post_author_info--575bd10823cd---------------------------------------)

·[14 following](https://medium.com/%40amannsharmaa/following?source=post_page---post_author_info--575bd10823cd---------------------------------------)

| Data Enthusiast | SQL | Python | Power BI | ML | Exploring Cybersecurity & Bug Bounty | Sharing real-world analytics, dashboards & security insights.

## Responses (4)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----575bd10823cd---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----575bd10823cd---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----575bd10823cd---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----575bd10823cd---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----575bd10823cd---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----575bd10823cd---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----575bd10823cd---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----575bd10823cd---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----575bd10823cd---------------------------------------)
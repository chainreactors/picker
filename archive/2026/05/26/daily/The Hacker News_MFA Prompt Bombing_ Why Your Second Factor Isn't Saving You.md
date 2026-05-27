---
title: MFA Prompt Bombing: Why Your Second Factor Isn't Saving You
url: https://thehackernews.com/2026/05/mfa-prompt-bombing-why-your-second.html
source: The Hacker News
date: 2026-05-26
fetch_date: 2026-05-27T06:12:49.222228
---

# MFA Prompt Bombing: Why Your Second Factor Isn't Saving You

#1 Trusted Cybersecurity News Platform

Followed by 5.70+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Get the Latest News](#email-outer)

* [Home](/)
* [Newsletter](#email-outer)
* [Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Threat Intelligence](/search/label/Threat%20Intelligence)
* [Vulnerabilities](/search/label/Vulnerability)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Awards](https://awards.thehackernews.com/)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Awards](https://awards.thehackernews.com/)
* [Free eBooks](https://thehackernews.tradepub.com)

About Site

* [About THN](/p/about-us.html)
* [Jobs](/p/careers-technical-writer-designer-and.html)
* [Advertise with us](/p/advertising-with-hacker-news.html)

Contact/Tip Us

[**

Reach out to get featured—contact us to send your exclusive story idea, research, hacks, or ask us a question or leave a comment/feedback!](/p/submit-news.html)

Follow Us On Social Media

[**](https://www.facebook.com/thehackernews)
[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.youtube.com/c/thehackernews?sub_confirmation=1)
[**](https://www.instagram.com/thehackernews/)

[** RSS Feeds](https://feeds.feedburner.com/TheHackersNews)
[** Email Alerts](#email-outer)

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhyqUz0-ifa8jE9rCzud3wzxmhcuzTp1VOWFEvGMoZXDYfaB_4459fPyvyQw7wvAnzjzDL09PkyJM83QGheO69fC3esg1WA7WnJ89i_t_q3K8DxYmgV__QujU8RWRnCK4MpbKqu8nwuMFfLaiRVHy_ov7IZ16hoKI3rIu-5BcISmqXPjlQU7N0sa4lWI-n-/s728-e100/wiz-d.png)](https://thehackernews.uk/wiz-ai-state-d)

# [MFA Prompt Bombing: Why Your Second Factor Isn't Saving You](https://thehackernews.com/2026/05/mfa-prompt-bombing-why-your-second.html)

**The Hacker News**May 26, 2026Password Security / Social Engineering

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgtums9LZoPXx5AzbNIYmdrNPI6vAAWAnYGfW6NzZ4DkICva0wX2GjMPvmYoq4EVuhvWUc6FyLrgJJ0Hvh8w0TBJ4MLkQplbffUwg89oiQxoJhV-93mboD0D2rdkrrhsblZ2tLJv-auc2GBNjIMsg8wGUCYOkZHNDHaQoqhDbLXrFC3-rD3cz0pI12U7rR2/s1700-e365/prompt-1.jpg)

Multi-factor authentication (MFA) was supposed to close a critical gap in identity security. It meant that, even if an attacker possessed the account credentials, they couldn't log in without the second factor. While that logic was sound, attackers have now figured out that they don't need to steal the second factor: they just need the user to hand it over.

If your workforce authenticates with push-based MFA, this attack is a live threat to your organization today. Tools like [Specops Secure Access](https://specopssoft.com/product/specops-secure-access/?utm_source=thehackernews&utm_medium=referral&utm_campaign=thehackernews_referral_na&utm_content=article) are built specifically to close that gap, but before getting into the fix, it's worth understanding how this technique works.

## How MFA prompt bombing works

The attack requires three key elements to work:

* Valid account credentials, usually sourced from breached password dumps on the dark web
* A login portal that uses push-based MFA (such as a VPN, Microsoft 365, Okta, or Duo)
* A victim who is alerted every time the attacker tries the login

Attackers repeatedly trigger the prompt, attempting to trick the target or wear them down to approve the request. Sometimes, attackers will pair prompt bombing with a [vishing call](https://specopssoft.com/blog/ai-vishing-voice-deception/?utm_source=thehackernews&utm_medium=referral&utm_campaign=thehackernews_referral_na&utm_content=article) pretending to be from IT, where they will try to socially engineer the target. The danger is that these methods only need to work once.

If the prompt is approved, the attacker is logged in as that user. Security systems typically won't be alerted, as the login looks entirely legitimate.

## The Cisco breach

The 2022 Cisco breach is a key example of how effective this technique is against even mature security programs. An attacker linked to the Yanluowang ransomware group compromised a Cisco employee's personal Google account, which was syncing browser-stored credentials, including the employee's Cisco VPN password.

From there, the attacker pushed MFA prompts to the employee's phone. That initially didn't work, so they began using vishing calls posing as trusted support organizations, speaking in various accents, and eventually convincing the employee to accept a push notification.

Once accepted, the attacker had VPN access as the employee. They then enrolled their own devices for MFA to maintain persistence, escalated to administrative privileges, reached Citrix servers and domain controllers, and exfiltrated around 2.8GB of data before being evicted. The fact that prompt bombing worked against a company like Cisco, which is far from having a weak security posture, highlights just how dangerous and effective the attack has become.

## Why push MFA doesn't eliminate risk

The issue with push-based MFA is that users are asked to approve or deny a login with very little to go on. There's no clear indication of where the request originated, what device is being used, or whether the login attempt was initiated by the user at all. In isolation, that might be manageable. But when prompts start arriving repeatedly, it's easy to assume something's misfiring rather than recognizing it as a potential attack.

If that's paired with a well-timed phone call from someone posing as IT support, the situation becomes even harder to assess. At that point, the user isn't acting carelessly, but responding to a scenario designed to feel routine and legitimate, using credentials the attacker already has.

## 3 ways organizations can prevent prompt bombing

### **1. Use fatigue and phishing-resistant MFA factors**

Push notifications are the weakest common form of MFA. [Phishing-resistant](https://specopssoft.com/blog/mfa-phishing-fatigue-resistant/?utm_source=thehackernews&utm_medium=referral&utm_campaign=thehackernews_referral_na&utm_content=article) factors such as FIDO2 security keys, hardware tokens like YubiKey, or number-matching codes from authenticator apps are harder to abuse.

[Specops Secure Access](https://specopssoft.com/product/specops-secure-access/?utm_source=thehackernews&utm_medium=referral&utm_campaign=thehackernews_referral_na&utm_content=article) supports more than 15 identity providers and includes these fatigue-resistant options for Windows logon, RDP, and VPN connections, so organizations can retire push-only MFA for high-risk access points.

|  |
| --- |
| [![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiN_IZn-B10sbxf4iQ8qZWfUp8JBNzJl0yWOLzBLl5umlvlT6ZX_CPma_0aoJgTJxEG_A4861eiB0jvgN15ARESEBOR3oL4Fm0dUODoWrfdAVCoY3otMlMERxwOrc9JQZ4cNEntpm2qIwXAbZ1jk8-3f9OwqVEBI9T09WSfqX7VOgrHNhjPFco51xCTKAd0/s1700-e365/1.gif) |
| Specops Secure Access |

### **2. Block compromised passwords at the source**

Prompt bombing is only made possible when the attacker already has a valid password. Scanning Active Directory (AD) continuously against a live database of breached passwords, and forcing a reset when a match appears, removes the fuel for the attack. Relying on default AD password policies won't catch reused, incremental, or breached passwords. If you don't know where you stand today, [Specops Password Auditor](https://specopssoft.com/product/specops-password-auditor/?utm_source=thehackernews&utm_medium=referral&utm_campaign=thehackernews_referral_na&utm_content=article) is a free, read-only scan of your AD that flags vulnerabiliti...
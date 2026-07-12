---
title: Critical Zimbra Flaw Could Let Crafted Emails Run Malicious Code in User Sessions
url: https://thehackernews.com/2026/07/critical-zimbra-flaw-could-let-crafted_0483473395.html
source: The Hacker News
date: 2026-07-11
fetch_date: 2026-07-12T05:12:05.271036
---

# Critical Zimbra Flaw Could Let Crafted Emails Run Malicious Code in User Sessions

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgrKWHErc__Wn0forfQ5eJ5sIR1hVKCHCTeNQOaAX4lbygJ8S1Xpemx6JXl78dpwiT65DDBGURp48A3EemKzmli-jXPI3v1928MnJm-1j2ZPUaFXCvuySFhyphenhyphenKR-Li6fAinFT2bhLgsqUSNUR_ggMAnOHi3jD1qYWHXvueX8WdtxAd6GYety9cBGYABo18hX/s728-e100/tt-d.jpg)](https://thehackernews.uk/ai-zero-trust-h-d)

# [Critical Zimbra Flaw Could Let Crafted Emails Run Malicious Code in User Sessions](https://thehackernews.com/2026/07/critical-zimbra-flaw-could-let-crafted_0483473395.html)

**Ravie Lakshmanan**Jul 11, 2026Vulnerability / Email Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEirVz95zYTg61VRro9unfJCWWwwUrv3pQdtyNT7rPL8iCg6n0S6bky4dqPiluQHfSvQMIO9cyYgrz-07ZCx8yG_qND_J9XJ_0BoUON9p3zj0etafNvjg45txAeu4uCDEMxGDNv2tIxNuqrC0OsKG_sWZp5QIlEkbqZ_g_EEcAdXUQbuo_EgsXwT3mERTTk/s1700-e365/zimbra-email-hack.jpg)

Zimbra is urging customers to apply updates to address a critical security vulnerability impacting the Classic Web Client that could result in arbitrary code execution.

The vulnerability has been [described](https://wiki.zimbra.com/wiki/Zimbra_Releases/10.1.19) as a case of stored cross-site scripting (XSS) that could allow specially crafted emails to execute malicious scripts in a user's session. It has yet to be assigned a CVE identifier.

"The update fixes a security issue in the Classic Web Client where a specially crafted email could run malicious code when the email is opened," Zimbra [said](https://blog.zimbra.com/2026/07/patch-release-update-zimbra-10-1-19/). "If exploited, it could allow access to mailbox information, session data, or account settings."

XSS vulnerabilities occur when an application includes untrusted data in a web page without proper validation or escaping. This allows attackers to inject and execute malicious JavaScript in victims' browsers, which can result in session hijacking, credential theft, and account compromise.

[![Cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiBxLQDy7VdLze43eMmpRllTXaPKPfB_veNUxQlqIu3-68GBJtegkhDGCqtaiSymOQviROdxln1FSd4zdMp5Jv9jeF1xQxLPc9uo9H7zW2nWHNax0wT0Y8JRj-zyUfbaCLqhxSfQT2sCfhWMBPL6UVgsh5RYVNVxwus_mW_BY9Ptwz3z7iF0_LWOnte-gqg/s1600/sy-d-1.jpg)](https://thehackernews.uk/sygnia-cyber-response-d-1)

Stored XSS, or persistent XSS, is a type of XSS flaw where the injected script is permanently stored on the target servers in a database in the form of a seemingly harmless comment or a forum post, causing any site visitor to be compromised as soon as the page containing the JavaScript is loaded on their web browser.

Although Zimbra makes no mention of the vulnerability being exploited in the wild, XSS flaws in Zimbra have been an attack magnet for years, with bad actors attempting to [weaponize](https://thehackernews.com/2022/02/hackers-exploited-0-day-vulnerability.html) such vulnerabilities as far back as December 2021.

Last October, a stored XSS flaw in the Classic Web Client ([CVE-2025-27915](https://thehackernews.com/2025/10/zimbra-zero-day-exploited-to-target.html), CVSS Score: 5.4) was alleged to have been exploited as a zero-day in attacks targeting the Brazilian military, although Zimbra told The Hacker News at the time that it found no evidence to back it up.

Other XSS flaws that have been exploited by threat actors include [CVE-2023-37580](https://thehackernews.com/2023/11/zero-day-flaw-in-zimbra-email-software.html) and [CVE-2024-27443](https://thehackernews.com/2025/05/russia-linked-apt28-exploited-mdaemon.html). Given its high potential for abuse, users are recommended to update to Zimbra Collaboration Suite version 10.1.19 for optimal protection.

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/) to read more exclusive content we post.

SHARE
[**](#link_share)
[**](#link_share)
[**](#link_share)
**

[**Tweet](#link_share)

[**Share](#link_share)

[**Share](#link_share)

**Share

**
[**Share on Facebook](#link_share)
[**Share on Twitter](#link_share)
[**Share on Linkedin](#link_share)
[**Share on Reddit](#link_share)
[**Share on Hacker News](#link_share)
[**Share on Email](#link_share)
[**Share on WhatsApp](#link_share)
[![Facebook Messenger](data:image/png;base64...)Share on Facebook Messenger](#link_share)
[**Share on Telegram](#link_share)

SHARE **

[Application Security](https://thehackernews.com/search/label/Application%20Security), [browser security](https://thehackernews.com/search/label/browser%20security), [Code Execution](https://thehackernews.com/search/label/Code%20Execution), [Cross-site Scripting](https://thehackernews.com/search/label/Cross-site%20Scripting), [email security](https://thehackernews.com/search/label/email%20security), [enterprise security](https://thehackernews.com/search/label/enterprise%20security), [Vulnerability](https://thehackernews.com/search/label/Vulnerability), [Web Security](https://thehackernews.com/search/label/Web%20Security)

⚡ Top Stories This Week

[![16-Year-Old Linux KVM Flaw Lets Guest VMs Escape to Host on Intel and AMD x86 Systems](data:image/svg+xml;base64... "16-Year-Old Linux KVM Flaw Lets Guest VMs Escape to Host on Intel and AMD x86 Systems")

16-Year-Old Linux KVM Flaw Lets Guest VMs Escape to Host on Intel and AMD x86 Systems](https://thehackernews.com/2026/07/16-year-old-linux-kvm-flaw-lets-guest.html)

[![BeyondTrust Patches Critical Auth Bypass Flaws in Remote Support and PRA](data:image/svg+xml;base64... "BeyondTrust Patches Critical Auth Bypass Flaws in Remote Support and PRA")

BeyondTrust Patches Critical Auth Bypass Flaws in Remote Support and PRA](https://thehackernews.com/2026/07/beyondtrust-patches-critical-auth.html)

[![Court Filing Reveals Windows Device ID Helped FBI Trace Alleged Scattered Spider Hacker](data:image/svg+xml;base64... "Court Filing Reveals Windows Device ID Helped FBI Trace Alleged Scattered Spider Hacker")

Court Filing Reveals Windows Device ID Helped FBI Trace Alleged Scattered Spider Hacker](https://thehackernews.com/2026/07/court-filing-reveals-windows-device-id.html)

[![Rogue Agent Flaw Could Have Let Attackers Hijack ...
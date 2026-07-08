---
title: BeyondTrust Patches Critical Auth Bypass Flaws in Remote Support and PRA
url: https://thehackernews.com/2026/07/beyondtrust-patches-critical-auth.html
source: The Hacker News
date: 2026-07-07
fetch_date: 2026-07-08T05:05:53.638273
---

# BeyondTrust Patches Critical Auth Bypass Flaws in Remote Support and PRA

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

# [BeyondTrust Patches Critical Auth Bypass Flaws in Remote Support and PRA](https://thehackernews.com/2026/07/beyondtrust-patches-critical-auth.html)

**Ravie Lakshmanan**Jul 07, 2026Vulnerability / Enterprise Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEim5I3ndx1DHNKSznD7AT_CM4ApiaXDfZcQAwsCSDnHq7u8dkGcOzway-IBZJ44bFJintaRMSry4yHbaacESRFOJsRC_UBV6N9l_K4ICcqWsZ2E4zQ5BGibAkxjxm0qPYiiLEvAvDizmPZVYwXC6jN9pgB5G-3xZ9ifiEWisKsZoi9rBjJN1mepJjPl61s9/s1700-e365/bt.jpg)

BeyondTrust has released updates to address two critical security flaws affecting Remote Support (RS) and Privileged Remote Access (PRA) products that, if successfully exploited, could allow unauthenticated attackers to take control of susceptible devices.

The [vulnerabilities](https://www.beyondtrust.com/trust-center/security-advisories/bt26-03) are listed below -

* **CVE-2026-40138** (CVSS score: 9.2) - A pre-authentication vulnerability exists in the authentication subsystem of BeyondTrust Remote Support and Privileged Remote Access stemming from improper validation of authentication data that could allow a network-positioned attacker to bypass access controls and gain unauthorized access to the appliance, including accounts with elevated privileges.
* **CVE-2026-40139** (CVSS score: 9.2) - A pre-authentication vulnerability exists in the authentication subsystem of BeyondTrust Remote Support stemming from improper processing of authentication requests that could allow an unauthenticated remote attacker to bypass access controls and gain unauthorized access to the appliance, including accounts with elevated privileges.
* **CVE-2026-40140** (CVSS score: 8.7) - A pre-authentication vulnerability in the network communication subsystem stemming from insufficient validation of client-supplied input that could allow an unauthenticated remote attacker to trigger a denial-of-service condition, affecting appliance availability.
* **CVE-2026-40141** (CVSS score: 8.5) - A vulnerability exists in a web application component of BeyondTrust Remote Support and Privileged Remote Access stemming from insufficient validation of user-supplied input that could allow an authenticated attacker with limited privileges to access unintended resources or data beyond their authorization scope.

It's worth noting that the successful exploitation of CVE-2026-40138 and CVE-2026-40139 hinges on a specific authentication configuration being enabled. In the case of CVE-2026-40141, exploitation, should it occur, is restricted to accounts with specific permissions.

[![Cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiqmM4NpfZsx4cw-HrXQlCjZQmrF8bYnmB23AmpOPi16kPNB9lvICjpdYEclxJwyQ9OE8GgzQ8aOEI68tRuxNqov0MHz2Sq8xEPiYWM3Js6FM5t2nm2JHWodmR7qVSot14ZtWVqQRQ6B88OnMaVxCPwRG7xGPoIIZxF6QAhWVhMkQfs11NjyNtHsGEUH4_q/s728-e100/sygnia-d-1.jpg)](https://thehackernews.uk/sygnia-cyber-response-d-1)

BeyondTrust said all the identified internally as part of ongoing security assessments, with assistance using publicly available artificial intelligence (AI) models like Anthropic Claude Opus 4.8 and its own proprietary research tooling.

"The most severe vulnerabilities may allow an unauthenticated remote attacker to bypass access controls and gain unauthorized access to the appliance under specific configurations," it said. "Additional vulnerabilities may allow service disruption, unintended data access, and, under distinct configurations, elevated access by an authenticated user that may impact system integrity."

The issues have been addressed in the following versions -

* Remote Support RS 25.3.2 or lower (Fixed in RS 25.3.3 and above)
* Privileged Remote Access PRA 25.3.2 or lower (Fixed in PRA 25.3.3 and above)

BeyondTrust makes no mention of the vulnerabilities being exploited in the wild. However, security flaws in RS and PRA products ([CVE-2024-12356](https://thehackernews.com/2026/02/beyondtrust-flaw-used-for-web-shells.html) and [CVE-2026-1731](https://thehackernews.com/2026/02/beyondtrust-flaw-used-for-web-shells.html)) have come under repeated exploitation in the past to deploy web shells and backdoors, making it essential that users move quickly to apply the fixes.

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

[AI Security](https://thehackernews.com/search/label/AI%20Security), [Authentication Security](https://thehackernews.com/search/label/Authentication%20Security), [denial of service](https://thehackernews.com/search/label/denial%20of%20service), [enterprise security](https://thehackernews.com/search/label/enterprise%20security), [Patch Management](https://thehackernews.com/search/label/Patch%20Management), [Vulnerability](https://thehackernews.com/search/label/Vulnerability), [Web Security](https://thehackernews.com/search/label/Web%20Security)

⚡ Top Stories This Week

[![ThreatsDay: AI Compute Hijacking, Apple Email Flaw, BlueHammer Ransomware + 14 Stories](data:image/svg+xml;base64... "ThreatsDay: AI Compute Hijacking, Apple Email Flaw, BlueHammer Ransomware + 14 Stories")

ThreatsDay: AI Compute Hijacking, Apple Email Flaw, BlueHammer Ransomware + 14 Stories](https://thehackernews.com/...
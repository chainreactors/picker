---
title: Google Rolls Out DBSC in Chrome 146 to Block Session Theft on Windows
url: https://thehackernews.com/2026/04/google-rolls-out-dbsc-in-chrome-146-to.html
source: The Hacker News
date: 2026-04-10
fetch_date: 2026-04-11T04:22:56.998599
---

# Google Rolls Out DBSC in Chrome 146 to Block Session Theft on Windows

#1 Trusted Cybersecurity News Platform

Followed by 5.40+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Subscribe – Get Latest News](#email-outer)

* [** Home](/)
* [** Newsletter](#email-outer)
* [** Webinars](/p/upcoming-hacker-news-webinars.html)

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

# [Google Rolls Out DBSC in Chrome 146 to Block Session Theft on Windows](https://thehackernews.com/2026/04/google-rolls-out-dbsc-in-chrome-146-to.html)

**Ravie Lakshmanan**Apr 10, 2026Malware / Browser Security

[![Device Bound Session Credentials](data:image/png;base64... "Device Bound Session Credentials")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiC-kFnk6uDzN76983rxMJBgJzi5ByxqZ0SM5RAfG1171e3I_lRUCBHIZ0kmMRkxERMiWEO9WRX3D6mkadUuRhw69KYHi4VzPrIa4s4IVilNmFANa2EMbuk1blKF_4ChwqIBuTb4FLj_dqhTDUDsivEnw8OmDL85giaaJTiqATwZArXUq6_3_X7tfd_RLbV/s1700-e365/chrome-cookies.jpg)

Google has made **Device Bound Session Credentials** ([DBSC](https://thehackernews.com/2025/07/google-launches-dbsc-open-beta-in.html)) generally available to all Windows users of its Chrome web browser, months after it [began testing](https://thehackernews.com/2025/07/google-launches-dbsc-open-beta-in.html) the security feature in open beta.

The public availability is currently limited to Windows users on Chrome 146, with macOS expansion planned in an upcoming Chrome release.

"This project represents a significant step forward in our ongoing efforts to combat session theft, which remains a prevalent threat in the modern security landscape," Google's Chrome and Account Security teams [said](https://security.googleblog.com/2026/04/protecting-cookies-with-device-bound.html) in a Thursday post.

Session theft involves the covert exfiltration of session cookies from the web browser, either by gathering existing ones or waiting for a victim to log in to an account, to an attacker-controlled server.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/vpn-risk-report-inside-d)

Typically, this happens when users inadvertently download information-stealing malware into their systems. These stealer malware families – of which there are many, such as Atomic, Lumma, and Vidar Stealer – come with capabilities to harvest a wide range of information from compromised systems, including cookies.

Because session cookies often have extended lifespans, attackers can leverage them to gain unauthorized access to victims' online accounts without having to know their passwords. Once collected, these tokens are packaged and sold to other threat actors for financial gain. Cybercriminals who acquire them can follow up with their attacks of their own.

DBSC, first [announced](https://thehackernews.com/2024/04/google-chrome-beta-tests-new-dbsc.html) by Google in April 2024, aims to counter this abuse by cryptographically tying the authentication session to a specific device. In doing so, the idea is to render cookies worthless even if they get stolen by malware.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhxT7sVyKGgXDSeg-GcHvKWbpHvrvgjS8DhwcRhvZgtRD1s2dlh-40Q09IIcm7a0OkglGBZ0LVTsuWchqlL81h-rsLnyuEZHrqgx0LLa-ML1GD1P9-bjH17I6qqVddpw7X5CClHgglbcqtOP59HdaUkwOfBqJqhM0xjwlkwizGrFoG_tUUlvClxGnOK-Bbw/s1700-e365/cookie.png)

"It does this using hardware-backed security modules, such as the Trusted Platform Module (TPM) on Windows and the Secure Enclave on macOS, to generate a unique public/private key pair that cannot be exported from the machine," Google explained.

"The issuance of new short-lived session cookies is contingent upon Chrome proving possession of the corresponding private key to the server. Because attackers cannot steal this key, any exfiltrated cookies quickly expire and become useless to those attackers."

In the event a user's device does not support secure key storage, DBSC gracefully falls back to standard behavior without breaking the authentication flow, Google [said](https://developer.chrome.com/docs/web-platform/device-bound-session-credentials) in its developer documentation.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/fast-response-not-fast-d)

The tech giant said it has observed a significant reduction in session theft since its launch, an early indication of the success of the countermeasure. The official launch is just the start, as the company plans to bring DBSC to a broader range of devices and introduce advanced capabilities to better integrate with enterprise environments.

Google, which worked with Microsoft to design the standard with an aim to make it an open web standard, also emphasized that the DBSC architecture is private by design and that the distinct key approach ensures that websites cannot use the session credentials to correlate a user's activity across different sessions or sites on the same device.

"Furthermore, the protocol is designed to be lean: it does not leak device identifiers or attestation data to the server beyond the per-session public key required to certify proof of possession," it added. "This minimal information exchange ensures DBSC helps secure sessions without enabling cross-site tracking or acting as a device fingerprinting mechanism."

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

[browser security](https://thehackernews.com/search/label/browser%20security), [Chrome](https://thehackernews.com/search/label/Chrome), [cybersecurity](https://thehackernews.com/search/label/cybersecurity), [Google](https://thehackernews.com/search/label/Google), [Infostealer](https://thehackernews.com/search/label/Infostealer), [Malware](https://thehackernews.com/search/label/Malware), [Privacy](https://thehackernews.com/search/label/Privacy), [Windows](https://thehackernews.com/search/label/Windows)

Trending News

[![Micros...
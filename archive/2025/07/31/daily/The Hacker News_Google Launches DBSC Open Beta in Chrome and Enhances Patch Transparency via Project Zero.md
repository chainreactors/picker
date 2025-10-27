---
title: Google Launches DBSC Open Beta in Chrome and Enhances Patch Transparency via Project Zero
url: https://thehackernews.com/2025/07/google-launches-dbsc-open-beta-in.html
source: The Hacker News
date: 2025-07-31
fetch_date: 2025-10-06T23:55:58.303616
---

# Google Launches DBSC Open Beta in Chrome and Enhances Patch Transparency via Project Zero

#1 Trusted Cybersecurity News Platform

Followed by 5.20+ million[**](https://twitter.com/thehackersnews)
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
* [Data Breaches](/search/label/data%20breach)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Vulnerabilities](/search/label/Vulnerability)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Contact](/p/submit-news.html)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
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

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjWa8tsMNqlevi1HGF1ALQRGIq7hROPFAbHd3R1RTEOe73T8_Q2xW_-91t2jSGjU5peiPb8QYblGp4igNW-u2Qmlxbp2BKzTVMSvyXDZJmC-BYpiiJHrcnG5drmSP97iZ9PVIf1DeEr7U-7vWpe4HXwfMjt8FGNgq5mOycOJluYr9wF7YOKrQY9MfArwgjt/s728-e100/ai-agent-security-d.png)](https://thehackernews.uk/ai-agent-security-d)

# [Google Launches DBSC Open Beta in Chrome and Enhances Patch Transparency via Project Zero](https://thehackernews.com/2025/07/google-launches-dbsc-open-beta-in.html)

**Jul 30, 2025**Ravie LakshmananDevice Security / AI Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgb_X0qYyIcH-M0bDL7Y1LgpA0Cq6g8lp0UtxlOUhPGUdehXwtL7q4FwjNSSm-oo_28z4_umFDm1bKwuAofAlWAcp8XScsGw9pl-ZOVglgSANm8SZF2IiOfHXCiSHXxfnUqLG0267X6LObs2NPJnUNA3gUvJRTIIbefFLhRCEcgkObL8b0HRPz9_EHVrIoC/s790-rw-e365/google-chrome.jpg)

Google has announced that it's making available a security feature called **Device Bound Session Credentials (DBSC)** in open beta to ensure that users are safeguarded against session cookie theft attacks.

DBSC, first [introduced](https://thehackernews.com/2024/04/google-chrome-beta-tests-new-dbsc.html) as a prototype in April 2024, is designed to bind authentication sessions to a device so as to prevent threat actors from using stolen cookies to sign-in to victims' accounts and gain unauthorized access from a separate device under their control.

"Available in the Chrome browser on Windows, DBSC strengthens security after you are logged in and helps bind a session cookie – small files used by websites to remember user information – to the device a user authenticated from," Andy Wen, senior director of product management at Google Workspace, [said](https://workspace.google.com/blog/identity-and-security/defending-against-account-takeovers-top-threats-passkeys-and-dbsc).

DBSC is not only meant to secure user accounts post-authentication. It makes it a lot more difficult for bad actors to reuse session cookies and improves session integrity.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The company also noted that [passkey support](https://thehackernews.com/2024/07/google-adds-passkeys-to-advanced.html) is now generally available to more than 11 million Google Workspace customers, along with expanded admin controls to audit enrollment and restrict passkeys to physical security keys.

Lastly, Google intends to roll out a shared signals framework ([SSF](https://openid.net/specs/openid-sharedsignals-framework-1_0-ID3.html)) receiver in closed beta for select customers in order to enable the exchange of crucial security signals in near real-time using the OpenID standard.

"This framework acts as a robust system for 'transmitters' to promptly inform 'receivers' about significant events, facilitating a coordinated response to security threats," Wen said.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg-rkL6ap2Vq8leRuIUoQaY_5YeFP6ZnSzZ4ql2vvatdfIs31lPXs8VUcHoR91ZYIkIJ3zS_8Gzphgzk3e0rQdYpd6WJX1WS4t7pu9uvJXvG6GPlpgCjCTwUJCKkfFBiSFv74bORQy6yn3N2Wc9MOfyHyGxi9vUuejwCnf3hncq3QiRyzDPk7zjB5MyuOgC/s790-rw-e365/dbsc.png)

"Beyond threat detection and response, signal sharing also allows for the general sharing of different properties, such as device or user information, further enhancing the overall security posture and collaborative defense mechanisms."

### Google Project Zero Unveils Reporting Transparency

The development comes as Google Project Zero, a security team within the company that's tasked with hunting zero-day vulnerabilities, announced a new trial policy called Reporting Transparency to address what has been described as an upstream patch gap.

While patch gap typically refers to the time period between when a fix is released for a vulnerability and a user installs the appropriate update, upstream patch gap denotes the timespan where an upstream vendor has a fix available but downstream customers are yet to integrate the patch and ship it to end users.

To close this upstream patch app, Google said it's adding a new step where it intends to publicly share the discovery of a vulnerability within a week of reporting it to the relevant vendor.

This information is expected to include the vendor or open-source project that received the report, the affected product, the date the report was filed, and when the 90-day disclosure deadline expires. The [current list](https://googleprojectzero.blogspot.com/p/reporting-transparency.html) includes two Microsoft Windows bugs, one flaw in Dolby Unified Decoder, and three issues in Google BigWave.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"The primary goal of this trial is to shrink the upstream patch gap by increasing transparency," Project Zero's Tim Willis [said](https://googleprojectzero.blogspot.com/2025/07/reporting-transparency.html). "By providing an early signal that a vulnerability has been reported upstream, we can better inform downstream dependents. For our small set of issues, they will have an additional source of information to monitor for issues that may affect their users."

Google further said it plans to apply this principle to [Big Sleep](https://thehackernews.com/2025/07/google-ai-big-sleep-stops-exploitation.html), an artificial intelligence (AI) agent that was launched last year as part of a collaboration between DeepMind and Google Project Zero to augment vulnerability discovery.

The search behemoth also stressed that no technical details, proof-of-concept code, or any other information that could "materially assist" bad actors will be released until the deadline.

With the latest approach, Google Project Zero said it hopes to move the needle on releasing patches to the devices, systems, and services relied on by end users in a timely fashion and bolster the overall security ecosystem.

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/) to read more exclusive content we post.

SHARE
[**](#link_share)
[**](#link_share)
[**](#link_share)
**

[**Tweet](#link_share...
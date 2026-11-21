---
title: WhatsApp Patches 3 Security Flaws, Including Android Bug Suspected of Use in Scams
url: https://thehackernews.com/2026/11/whatsapp-patches-3-security-flaws.html
source: The Hacker News
date: 2026-11-20
fetch_date: 2026-11-21T09:02:34.943151
---

# WhatsApp Patches 3 Security Flaws, Including Android Bug Suspected of Use in Scams

#1 Trusted Cybersecurity News Platform

Followed by 5.80+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[Get Updates](#email-outer)

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi1FgbfB9gCsTYnkXg_UHMHoWinmHvbkdAdbnpnrFQzzIG00gtoQsaz3DVhUgvHic2vd-yM_5XIb9H5N6i7stc2WQFHqPn9bN7B_IIFDtEJbNnNcvNZ3IbmHi-kKM8V_3VaZj1zzoHwCVjkzUQwFzzTMhaTH7W2jlKhsI9m3HEBAVjHyuBiJBdX0l8jX9Ll/s727-nu-rw-lo-l85-e365/wiz-d.png)](https://thehackernews.uk/claude-security-tips-d)

# [WhatsApp Patches 3 Security Flaws, Including Android Bug Suspected of Use in Scams](https://thehackernews.com/2026/11/whatsapp-patches-3-security-flaws.html)

**Ravie Lakshmanan**Nov 20, 2026Vulnerability / Mobile Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhUSbYUJJkBlZsaH90SXIaxYAv5iJN7ZEus7Q24A_Z9fDNNlnOjFnNZ3SnA6er-iuMgQnE6k73nwVwAEPPk1AjRT12N9o8cJft3_dPqMZKeJbpq6QIcGbN1z1UbE_Q3fXTyp1c0XmqynQu2lJPeIYoraqXFcgM-wQH4b1rIBrOKF221CIKLldJIZVJ4g7cr/s1700-nu-rw-lo-l85-e365/whatsapp.jpg)

Meta-owned WhatsApp has [addressed](https://www.whatsapp.com/security/advisories/2026/) security vulnerabilities, including one impacting its Android app that it suspects may have been exploited in connection with scam messages.

The vulnerability, tracked as [CVE-2026-23871](https://www.cve.org/CVERecord?id=CVE-2026-23871) (CVSS score: 3.5), has been described as a case of incomplete validation of external ad-reply URLs in WhatsApp for Android and WhatsApp Business for Android before 2.26.17.4.

The issue could have "caused a target's device to reveal its IP information to an attacker if an attacker sent media from an attacker-controlled URL when a crafted [Click to WhatsApp](https://whatsappbusiness.com/products/ads-that-click-to-whatsapp/) ad-reply message was rendered and displayed in a message thread," WhatsApp said.

The messaging platform said it may have been "abused in conjunction with specific spam messages." Internal researchers on the WhatsApp Security Team have been credited with discovering and reporting the issue.

When reached for comment, a WhatsApp spokesperson told The Hacker News that the vulnerability was discovered while disrupting a scam campaign. "We believe a scammer was using it to make their scam message seem more credible," the spokesperson added.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/threat-protection-d)

WhatsApp did not disclose the scale of the activity, and if those efforts were successful.

Also addressed by the company are two other flaws -

* **[CVE-2026-102769](https://www.cve.org/CVERecord?id=CVE-2026-102769)** (CVSS score: 6.8) - An SQL injection vulnerability in WhatsApp for Android prior to version 2.26.35.74 that occurred when a recipient tapped on a specially crafted "order details" message sent from an unofficial client, causing locally-stored WhatsApp files to be deleted.
* **[CVE-2026-44908](https://www.cve.org/CVERecord?id=CVE-2026-44908)** (CVSS score: 4.8) - A trust-validation vulnerability in WhatsApp's certificate verification mechanism for Meta AI's confidential computing infrastructure that affects WhatsApp for iOS before 2.26.24.72, WhatsApp Business for iOS and WhatsApp for Mac Desktop before v2.26.23.72, WhatsApp for Android before v2.26.23.74, and WhatsApp Business for Android before v2.26.23.70.

Interestingly, CVE-2026-102769 is also capable of leaking one bit of information through a timing-based side channel if the user is online at the time of receipt of the malicious message.

It "leaked one bit of information asked by the attacker about the user's chat database via an induced-crash delivery receipt timing side channel," WhatsApp added. There is no evidence the vulnerability has been exploited in the wild.

Successful exploitation of CVE-2026-44908, on the other hand, could have allowed a bad actor positioned within Meta infrastructure to bypass the hardware root of trust using a Versioned Chip Endorsement Key ([VCEK](https://docs.amd.com/api/khub/documents/U5H~LHvkigTowyppBkpyrA/content)) certificate not signed by the hardware manufacturer's key.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/network-defense-dd)

"Any such VCEK Cert would first have to be published to the third-party binary transparency ledger used by WhatsApp Private Processing," WhatsApp noted. "The ledger shows that every published VCEK certificate chains to the hardware root of trust, confirming no exploitation."

WhatsApp is advising users to keep their apps and devices up to date to ensure optimal protection. The company also said that it continuously works to strengthen its systems and acknowledged the bug bounty community's contributions towards keeping the platform secure.

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

[Android](https://thehackernews.com/search/label/Android), [mobile security](https://thehackernews.com/search/label/mobile%20security), [Privacy](https://thehackernews.com/search/label/Privacy), [SQL Injection](https://thehackernews.com/search/label/SQL%20Injection), [Vulnerability](https://thehackernews.com/search/label/Vulnerability), [WhatsApp](https://thehackernews.com/search/label/WhatsApp)

⚡ Top Stories This Week

[![The Hacker News](data:image/svg+xml;base64...)

Default 'admin:admin' Server Password Helps Researchers Hack Two Automakers, Unlock and Start Cars](https://thehackernews.com/2026/11/default-adminadmin-server-password.html)

[![The Hacker News](data:image/svg+xml;base64...)

PostgreSQL Patches 52 Flaws, Including 22-Year-Old Bug Enabling Authenticated RCE](https://thehackernews.com/2026/11/postgresql-patches-52-flaws-including.html)

[!...
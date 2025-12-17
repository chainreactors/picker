---
title: Fortinet FortiGate Under Active Attack Through SAML SSO Authentication Bypass
url: https://thehackernews.com/2025/12/fortinet-fortigate-under-active-attack.html
source: The Hacker News
date: 2025-12-16
fetch_date: 2025-12-17T03:20:28.431202
---

# Fortinet FortiGate Under Active Attack Through SAML SSO Authentication Bypass

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

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi4PKjL50qMNKKq6z8Ofu7tXpz51soFtMEKzX6_qMTj-_Exp3EctK0Z7KiOlubgst1DxPrrk8TgthgjViGZmg4FlcOYG8L63G_dX8731tRGkOc42mbtdMv6KDyjdNKRdCPHkhUQJmcoxcFKLcQjeILTu-wEtAOXsTp7JyWMIuP0k1RJo9sZjTo5dYL8CyFQ/s728-e100/z-dd.png)](https://thehackernews.uk/zz--header-d)

# [Fortinet FortiGate Under Active Attack Through SAML SSO Authentication Bypass](https://thehackernews.com/2025/12/fortinet-fortigate-under-active-attack.html)

**Dec 16, 2025**Ravie LakshmananNetwork Security / Vulnerability

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgQJ_qq1hYIZDr0BJrkSi2LLidWTwFd6Hulhty9DbaKd-4PuGyZcmRDQDMyMfHj0dsS87KDoQba3ZEo7ohgSpjNCziDz5NasZQ-qleWrf5lZduSbw8Ptjx_uX_V8SgFrp4k8fUFR5mQCtFhFBeu8ykYU_dUhuW6R27KQQQk_tpDOB-DZ-XIK9gWEW2TJLdT/s790-rw-e365/fortinet.jpg)

Threat actors have begun to exploit two newly disclosed security flaws in Fortinet FortiGate devices, less than a week after public disclosure.

Cybersecurity company Arctic Wolf said it observed active intrusions involving malicious single sign-on (SSO) logins on FortiGate appliances on December 12, 2025. The attacks exploit [two critical authentication bypasses](https://thehackernews.com/2025/12/fortinet-ivanti-and-sap-issue-urgent.html) (CVE-2025-59718 and CVE-2025-59719, CVSS scores: 9.8). Patches for the flaws were released by Fortinet last week for FortiOS, FortiWeb, FortiProxy, and FortiSwitchManager.

"These vulnerabilities allow unauthenticated bypass of SSO login authentication via crafted SAML messages, if the FortiCloud SSO feature is enabled on affected devices," Arctic Wolf Labs [said](https://arcticwolf.com/resources/blog/arctic-wolf-observes-malicious-sso-logins-following-disclosure-cve-2025-59718-cve-2025-59719/) in a new bulletin.

It's worth noting that while FortiCloud SSO is disabled by default, it is automatically enabled during FortiCare registration unless administrators explicitly turn it off using the "Allow administrative login using FortiCloud SSO" setting in the registration page.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/zscaler-ai-event-d)

In the malicious activity observed by Arctic Wolf, IP addresses associated with a limited set of hosting providers, such as The Constant Company llc, Bl Networks, and Kaopu Cloud Hk Limited, were used to carry out malicious SSO logins against the "admin" account.

Following the logins, the attackers have been found to export device configurations via the GUI to the same IP addresses.

In light of ongoing exploitation activity, organizations are advised to apply the patches as soon as possible. As mitigations, it's essential to disable FortiCloud SSO until the instances are updated to the latest version and limit access to management interfaces of firewalls and VPNs to trusted internal users.

"Although credentials are typically hashed in network appliance configurations, threat actors are known to crack hashes offline, especially if credentials are weak and susceptible to dictionary attacks," Arctic Wolf said.

Fortinet customers who find indicators of compromise (IoCs) consistent with the campaign are recommended to assume compromise and reset hashed firewall credentials stored in the exfiltrated configurations.

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

[Authentication](https://thehackernews.com/search/label/Authentication)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[Firewall](https://thehackernews.com/search/label/Firewall)[Fortinet](https://thehackernews.com/search/label/Fortinet)[network security](https://thehackernews.com/search/label/network%20security)[Threat Intelligence](https://thehackernews.com/search/label/Threat%20Intelligence)[Vulnerability](https://thehackernews.com/search/label/Vulnerability)

Trending News

[![Android Malware FvncBot, SeedSnatcher, and ClayRat Gain Stronger Data Theft Features](data:image/svg+xml;base64... "Android Malware FvncBot, SeedSnatcher, and ClayRat Gain Stronger Data Theft Features")

Android Malware FvncBot, SeedSnatcher, and ClayRat Gain Stronger Data Theft Features](https://thehackernews.com/2025/12/android-malware-fvncbot-seedsnatcher.html)

[![New Advanced Phishing Kits Use AI and MFA Bypass Tactics to Steal Credentials at Scale](data:image/svg+xml;base64... "New Advanced Phishing Kits Use AI and MFA Bypass Tactics to Steal Credentials at Scale")

New Advanced Phishing Kits Use AI and MFA Bypass Tactics to Steal Credentials at Scale](https://thehackernews.com/2025/12/new-advanced-phishing-kits-use-ai-and.html)

[![Apple Issues Security Updates After Two WebKit Flaws Found Exploited in the Wild](data:image/svg+xml;base64... "Apple Issues Security Updates After Two WebKit Flaws Found Exploited in the Wild")

Apple Issues Security Updates After Two WebKit Flaws Found Exploited in the Wild](https://thehackernews.com/2025/12/apple-issues-security-updates-after-two.html)

[![New React RSC Vulnerabilities Enable DoS and Source Code Exposure](data:image/svg+xml;base64... "New React RSC Vulnerabilities Enable DoS and Source Code Exposure")

New React RSC Vulnerabilities Enable DoS and Source Code Exposure](https://thehackernews.com/2025/12/new-react-rsc-vulnerabilities-enable.html)

[![React2Shell Exploitation Escalates into Large-Scale Global Attacks, Forcing Emergency Mitigation](data:image/svg+xml;base64... "React2Shell Exploitation Escalates into Large-Scale Global Attacks, Forcing Emergency Mitigation")

React2Shell Exploitation Escalates into Large-Scale...
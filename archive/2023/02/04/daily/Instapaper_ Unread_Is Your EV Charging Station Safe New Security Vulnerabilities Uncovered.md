---
title: Is Your EV Charging Station Safe New Security Vulnerabilities Uncovered
url: https://thehackernews.com/2023/02/is-your-ev-charging-station-safe-new.html
source: Instapaper: Unread
date: 2023-02-04
fetch_date: 2025-10-04T05:43:30.492554
---

# Is Your EV Charging Station Safe New Security Vulnerabilities Uncovered

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

# [Is Your EV Charging Station Safe? New Security Vulnerabilities Uncovered](https://thehackernews.com/2023/02/is-your-ev-charging-station-safe-new.html)

**Feb 03, 2023**Ravie LakshmananAutomotive Security / Vulnerability

[![EV Charging Station](data:image/png;base64... "EV Charging Station")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjfOTNvViA-FJHb9291B6NVQb0NQO5-DstXVIiU4xcMunVEepqlJWT2EozNR0PYZWNQEf3t2kjN9c2t62k6aHSTG0y6yOuZYGBFOXkQQvJr3-OY70N0k_cZYlLzdVfHZRnnF_puQmL3UIadzfkhks2vX9tz9WV41tgrJkqaHmCjRhR-AOaqzspqBP0M/s790-rw-e365/car-hacking.png)

Two new security weaknesses discovered in several electric vehicle (EV) charging systems could be exploited to remotely shut down charging stations and even expose them to data and energy theft.

The findings, which come from Israel-based SaiFlow, once again demonstrate the [potential risks](https://thehackernews.com/2022/12/siriusxm-vulnerability-lets-hackers.html) facing the EV charging infrastructure.

The issues have been identified in version 1.6J of the Open Charge Point Protocol ([OCPP](https://www.openchargealliance.org/protocols/ocpp-201/)) standard that uses WebSockets for communication between EV charging stations and the Charging Station Management System (CSMS) providers. The current version of OCPP is 2.0.1.

"The OCPP standard doesn't define how a CSMS should accept new connections from a charge point when there is already an active connection," SaiFlow researchers Lionel Richard Saposnik and Doron Porat [said](https://www.saiflow.com/hijacking-chargers-identifier-to-cause-dos/).

"The lack of a clear guideline for multiple active connections can be exploited by attackers to disrupt and hijack the connection between the charge point and the CSMS."

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

This also means that a cyber attacker could spoof a connection from a valid charger to its CSMS provider when it's already connected, effectively leading to either of the two scenarios:

* A denial-of-service (DoS) condition that arises when the CSMS provider closes the original WebSocket connection when a new connection is established

* Information theft that stems from keeping the two connections alive but returning responses to the "new" rogue connection, permitting the adversary to access the driver's personal data, credit card details, and CSMS credentials.

The forging is made possible owing to the fact that CSMS providers are configured to solely rely on the charging point identity for authentication.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"Combining the mishandling of new connections with the weak OCPP authentication and chargers identities policy could lead to a vast Distributed DoS (DDoS) attack on the [Electric Vehicle Supply Equipment] network," the researchers said.

[![EV Charging Station](data:image/png;base64... "EV Charging Station")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhX2cE6c7b3MiAYs9T2Koe8mv7fngKUtjw5IkYLgmpH6AmXx-_Id73JgIy0RFe9uUEbdtn3kr9ChjOJ1DwOszmni1p6w_Go3My6FTmhonv--Tf4Xv15TDi1tHVprkq5v6i98oC6v3UMljHcLiKBMBHHy9pGJlMkFLFSN7EZZa-iEVDat3xGPmBRW1kn/s790-rw-e365/exploit.png)

OCPP 2.0.1 remediates the weak authentication policy by requiring charging point credentials, thereby closing out the loophole. That said, mitigations for when there are more than one connection from a single charging point should necessitate validating the connections by sending a ping or a heartbeat request, SaiFlow noted.

"If one of the connections is not responsive, the CSMS should eliminate it," the researchers explained. "If both connections are responsive, the operator should be able to eliminate the malicious connection directly or via a CSMS-integrated cybersecurity module."

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

[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[ddos](https://thehackernews.com/search/label/ddos)[hacking news](https://thehackernews.com/search/label/hacking%20news)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw")

SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](https://thehackernews.com/2025/09/solarwinds-releases-hotfix-for-critical.html)

[![Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](data:image/svg+xml;base64... "Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants")

Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](https://thehackernews.com/2025/09/microsoft-patches-critical-entra-id.html)

[![Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials](data:image/svg+xml;base64... "Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials")

Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials](...
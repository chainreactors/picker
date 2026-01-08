---
title: Microsoft Warns Misconfigured Email Routing Can Enable Internal Domain Phishing
url: https://thehackernews.com/2026/01/microsoft-warns-misconfigured-email.html
source: The Hacker News
date: 2026-01-07
fetch_date: 2026-01-08T03:30:50.962918
---

# Microsoft Warns Misconfigured Email Routing Can Enable Internal Domain Phishing

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

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhlCcy_j509wX0FKMRQX-zVzeBNtSIDsH6oDFlljaAeQRz65xSx8g9jicghxtpvDC8yI10jCv1TPEcyPvfoCKOby_0ZjsnNc-3wZG5YeA8sZQBCbZxhzd00jR2ZG8rZr-vp3WLrbXaMVbsVrDwBEeBWBbNSSwFjeuNzhrVOigDqTM7VWfSUJqBwEoYALS58/s728-e100/z-header-d.png)](https://thehackernews.uk/modern-security-shift-d)

# [Microsoft Warns Misconfigured Email Routing Can Enable Internal Domain Phishing](https://thehackernews.com/2026/01/microsoft-warns-misconfigured-email.html)

**Jan 07, 2026**Ravie LakshmananEmail Security / Financial Fraud

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgHZJ_x-tDf2JaX7jVZDlS1KTcw7PnwLR03qRgpIHRBtIvLNIybJd8Gw058LyQyjV73UUJy39rcTziPgH9B1cqkTeOMF5zn7GstRSXG-MV1kWEfbnsACIM7VDbodevFXrvnYQjZjQMmicjj16dM6nb1tUEhsoDSQ5UOFAGpaG3P0XCpR5s5nazAf9npmgge/s790-rw-e365/email-phishing.jpg)

Threat actors engaging in phishing attacks are exploiting routing scenarios and misconfigured spoof protections to impersonate organizations' domains and distribute emails that appear as if they have been sent internally.

"Threat actors have leveraged this vector to deliver a wide variety of phishing messages related to various phishing-as-a-service (PhaaS) platforms such as [Tycoon 2FA](https://thehackernews.com/2025/12/new-advanced-phishing-kits-use-ai-and.html)," the Microsoft Threat Intelligence team [said](https://www.microsoft.com/en-us/security/blog/2026/01/06/phishing-actors-exploit-complex-routing-and-misconfigurations-to-spoof-domains/) in a Tuesday report. "These include messages with lures themed around voicemails, shared documents, communications from human resources (HR) departments, password resets or expirations, and others, leading to credential phishing."

While the attack vector is [not necessarily new](https://thehackernews.com/2025/09/axios-abuse-and-salty-2fa-kits-fuel.html), the tech giant said it has witnessed a surge in the use of the tactic since May 2025 as part of opportunistic campaigns targeting a wide variety of organizations across multiple industries and verticals. This includes a campaign that has employed spoofed emails to conduct financial scams against organizations.

A successful attack could allow threat actors to siphon credentials and leverage them for follow-on activities, ranging from data theft to business email compromise (BEC).

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/zero-trust-summit-d)

The problem manifests primarily in scenarios where a tenant has configured a complex routing scenario and spoof protections are not strictly enforced. An example of complex routing involves pointing the mail exchanger record (MX record) to either an on-premises Exchange environment or a third-party service before reaching Microsoft 365

This creates a security gap that attackers can exploit to send spoofed phishing messages that seem to originate from the tenant's own domain. The vast majority of phishing campaigns that leverage this approach have been found to make use of the [Tycoon 2FA](https://www.cybereason.com/blog/tycoon-phishing-kit-analysis) [PhaaS kit](https://socradar.io/blog/tycoon-2fa-an-evolving-phishing-kit-phaas-threats/). Microsoft said it blocked more than 13 million malicious emails linked to the kit in October 2025.

[PhaaS toolkits](https://www.trellix.com/blogs/research/phaas-phishing-as-a-service-on-the-rise/) are plug-and-play platforms that allow fraudsters to create and manage phishing campaigns easily, making it accessible even for those with limited technical skills. They [provide](https://www.huntress.com/cybersecurity-101/topic/phishing-as-a-service) features like customizable phishing templates, infrastructure, and other tools to facilitate credential theft and circumvent multi-factor authentication using adversary-in-the-middle (AiTM) phishing.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiNSqfWicxUKN1cyMZNNRtYIjOhXrB-LJgz8UsGS2D8h1_DSZzLNxo2WUbz5nNL3dAvbNnPu-LdU16tOKTQY1j-AzGS2TA9P4Z9Yh-EZfU9sbIYrDuGg-MFDH61OdqD2rQlMSbZ44y5Wp8M8N541970jyaWNjTnkD3m3GeQpgpQ74ReibDYPgsRJjjSRv8W/s790-rw-e365/phishing.png)

The Windows maker said it has also spotted emails intended to trick organizations into paying bogus invoices, potentially leading to financial losses. The spoofed messages also impersonate legitimate services like DocuSign or claim to be from HR regarding salary or benefits changes.

Phishing emails propagating financial scams often resemble a conversation between the CEO of the targeted organization, an individual requesting payment for services provided, or the firm's accounting department. They also contain three attached files to lend the scheme a false sense of trust -

* A fake invoice for thousands of dollars to be wired to a bank account
* An IRS W-9 form listing the name and social security number of the individual used to set up the bank account
* A fake bank letter was allegedly provided by an employee at the online bank used to set up the fraudulent account

"They may employ clickable links in the email body or QR codes in attachments or other means of getting the recipient to navigate to a phishing landing page," it added. "The appearance of having been sent from an internal email address is the most visible distinction to an end user, often with the same email address used in the 'To' and 'From' fields."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/attack-surface-insight-d)

To counter this risk, organizations are advised to set strict Domain-based Message Authentication, Reporting, and Conformance (DMARC) [reject](https://learn.microsoft.com/en-us/defender-office-365/email-authentication-dmarc-configure) and Sender Policy Framework (SPF) [hard fail policies](https://www.valimail.com/resources/guides/email-security-best-practices/spf-softfail-vs-hardfail/) and [properly configure](https://learn.microsoft.com/en-in/exchange/mail-flow-best-practices/manage-mail-flow-using-third-party-cloud) third-party connectors, such as spam filtering services or archiving tools.

It's worth noting that tenants with MX records pointed directly to Office 365 are not vulnerable to the attack vector. Additionally, it's recommended to [turn off Direct Send](https://techcommunity.microsoft.com/blog/exchange/introducing-more-control-over-direct-...
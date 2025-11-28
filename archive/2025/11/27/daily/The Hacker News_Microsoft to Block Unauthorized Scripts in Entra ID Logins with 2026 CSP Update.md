---
title: Microsoft to Block Unauthorized Scripts in Entra ID Logins with 2026 CSP Update
url: https://thehackernews.com/2025/11/microsoft-to-block-unauthorized-scripts.html
source: The Hacker News
date: 2025-11-27
fetch_date: 2025-11-28T03:13:19.017584
---

# Microsoft to Block Unauthorized Scripts in Entra ID Logins with 2026 CSP Update

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

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhjMQkm7Ao3yQkNVeqy3au4G4E34VWzSsT55GDPjHHGjbHksJqrJCyM1ChO1hB9WzaFzZcwNTn8fOLN8b3U599XinIlPZBBqNnwZYJFQD0i2dLVdAjszjU-a3Y0iLd5UHOg0H9-IFtS0nGf4MeOGk4NsNNAq-pMpFpi_aZrXHGV7UgoEEOlkFGBW5HOsJFC/s728-e100/zz--header-d.png)](https://thehackernews.uk/zz--header-d)

# [Microsoft to Block Unauthorized Scripts in Entra ID Logins with 2026 CSP Update](https://thehackernews.com/2025/11/microsoft-to-block-unauthorized-scripts.html)

**Nov 27, 2025**Ravie LakshmananWeb Security / Zero Trust

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEggbH_BZ4IWtK9XUQJlVK_lYU-KRFB6bMqJMGZUr640ws6tiDaAcew4Pf9SC_Mc3aUrTo52vkVQ2OGUXwZ1y9M0jRb0mywWeYspEWQ2QyjaRfWz1Z8jTDn1HzsNL87aEZRvaEvsuEzCx0DG4CAGMUbazLVxKSLjPpNh255KfuycID8w7BgOm445sOl4cZt0/s790-rw-e365/entra-id.jpg)

Microsoft has announced plans to improve the security of Entra ID authentication by blocking unauthorized script injection attacks starting a year from now.

The update to its Content Security Policy (CSP) aims to enhance the Entra ID sign-in experience at "login.microsoftonline[.]com" by only letting scripts from trusted Microsoft domains run.

"This update strengthens security and adds an extra layer of protection by allowing only scripts from trusted Microsoft domains to run during authentication, blocking unauthorized or injected code from executing during the sign-in experience," the Windows maker [said](https://techcommunity.microsoft.com/blog/microsoft-entra-blog/enhance-protection-of-microsoft-entra-id-authentication-by-blocking-external-scr/4435200).

Specifically, it only allows script downloads from Microsoft trusted CDN domains and inline script execution from a Microsoft trusted source. The updated policy is limited to browser-based sign-in experiences for URLs beginning with login.microsoftonline.com. Microsoft Entra External ID will not be affected.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/zz--inside-d)

The change, which has been described as a proactive measure, is part of Microsoft's Secure Future Initiative ([SFI](https://www.microsoft.com/en-us/trust-center/security/secure-future-initiative)) and is designed to safeguard users against cross-site scripting (XSS) attacks that make it possible to inject malicious code into websites. It's expected to be rolled out globally starting mid-to-late October 2026.

Microsoft is urging organizations to test their sign-in flows thoroughly ahead of time to ensure that there are no issues and the sign-in experience has no friction.

It's also advising customers to refrain from using browser extensions or tools that inject code or script into the Microsoft Entra sign-in experience. Those who follow this approach are recommended to switch to other tools that don't inject code.

To identify any CSP violations, users can go through a sign-in flow with the dev console open and access the browser's Console tool within the developer tools to check for errors that say "Refused to load the script" for going against the "[script-src](https://content-security-policy.com/script-src/)" and "[nonce](https://content-security-policy.com/nonce/)" directives.

Microsoft's SFI is a multi-year effort that seeks to put security above all else when designing new products and better prepare for the growing sophistication of cyber threats.

It was first launched in November 2023 and expanded in May 2024 following a report from the U.S. Cyber Safety Review Board (CSRB), which [concluded](https://thehackernews.com/2024/04/us-cyber-safety-board-slams-microsoft.html) that the company's "security culture was inadequate and requires an overhaul."

In its [third progress report](https://www.microsoft.com/en-us/trust-center/security/secure-future-initiative/sfi-progress-report-november-2025) published this month, the tech giant said it has deployed over 50 new detections in its infrastructure to target high-priority tactics, techniques, and procedures, and that the adoption of phishing-resistant multi-factor authentication (MFA) for users and devices has hit 99.6%.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/endpoint-protect-d)

Other notable changes enacted by Microsoft are as follows -

* Enforced Mandatory MFA across all services, including for all Azure service users
* Introduced Automatic recovery capabilities via Quick Machine Recovery, expanded passkey and Windows Hello support, and improved memory safety in UEFI firmware and drivers by using Rust
* Migrated 95% of Microsoft Entra ID signing VMs to Azure Confidential Compute and moved 94.3% of Microsoft Entra ID security token validation to its standard identity Software Development Kit (SDK)
* Discontinued the use of Active Directory Federation Services (ADFS) in our productivity environment
* Decommissioned 560,000 additional unused and aged tenants and 83,000 unused Microsoft Entra ID apps across Microsoft production and productivity environments
* Advanced threat hunting by centrally tracking 98% of production infrastructure
* Achieved complete network device inventory and mature asset lifecycle management
* Almost entirely locked code signing to production identities
* Published 1,096 CVEs, including 53 no-action cloud CVEs, and paid out $17 million in bounties

"To align with Zero Trust principles, organizations should automate vulnerability detection, response, and remediation using integrated security tools and threat intelligence," Microsoft said. "Maintaining real-time visibility into security incidents across hybrid and cloud environments enables faster containment and recovery."

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
[**Sh...
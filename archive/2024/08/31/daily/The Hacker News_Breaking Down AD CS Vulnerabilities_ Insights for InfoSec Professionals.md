---
title: Breaking Down AD CS Vulnerabilities: Insights for InfoSec Professionals
url: https://thehackernews.com/2024/08/breaking-down-ad-cs-vulnerabilities.html
source: The Hacker News
date: 2024-08-31
fetch_date: 2025-10-06T18:12:53.040259
---

# Breaking Down AD CS Vulnerabilities: Insights for InfoSec Professionals

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

# [Breaking Down AD CS Vulnerabilities: Insights for InfoSec Professionals](https://thehackernews.com/2024/08/breaking-down-ad-cs-vulnerabilities.html)

**Aug 30, 2024**The Hacker NewsVulnerability / Network Security

[![AD CS Vulnerabilities](data:image/png;base64... "AD CS Vulnerabilities")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj5YTUlWPmUtsZzTzgJa4oOCvHRip6kcEvUB4wDHPdngVxIba5xBGopEcGhTyTI0vrUUu_XYWaUrFfUsfhcLlXdldRMRR7137eLwURg03bh1ISSCvQ_HyPVZAvCVMvroBRgGbQVE6LpKdzkJx-YwJ8bz9lt_BJqxGUNU1P0SzatRhZSMWMhuw9gnysJCzQ/s790-rw-e365/main.png)

***The most dangerous vulnerability you've never heard of.***

In the world of cybersecurity, vulnerabilities are discovered so often, and at such a high rate, that it can be very difficult to keep up with. Some vulnerabilities will start ringing alarm bells within your security tooling, while others are far more nuanced, but still pose an equally dangerous threat. Today, we want to discuss one of these more nuanced vulnerabilities as it is likely lurking in your environment waiting to be exploited: Active Directory Certificate Services vulnerabilities.

[vPenTest by Vonahi Security](https://www.vonahi.io/services/network-penetration-testing) recently implemented an attack vector specifically designed to identify and mitigate these hidden AD CS threats. But first, let's explore why AD CS vulnerabilities are so dangerous and how they work.

## **What is Active Directory Certificate Services?**

Active Directory Certificate Services ("AD CS"), as defined by Microsoft is, "a Windows Server role for issuing and managing public key infrastructure (PKI) certificates used in secure communication and authentication protocols." Some common features and services that rely on AD CS are:

* The Windows Logon Process
* Enterprise VPN and Wireless Networks
* Email Encryption and Digital Signatures
* Smart Card Authentication

As companies continue to increase the variety of technologies available within their organizations, AD CS will become more common and more necessary, especially as companies continue to host their services in the cloud. Many AWS, Azure and GCP services require certificate-based authentication to function, so it is expected that AD CS will become an increasingly prominent and required service in modern multi-cloud networks.

[![AD CS Vulnerabilities](data:image/png;base64... "AD CS Vulnerabilities")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiSqcwjSHpYyPPxK2f0b2Jb1qYozUMNbVirUdFCX2q9BK6h7DYh-V6bIxGi-JjKdL6KdOXBz8RyGJkrU1nnm7ZmL9V6H4k3eLEj_E06aCLDmww9hfYwfqT2O0Jyc26_rXHTH-UTULakmLu7B8tyCx2tKBph5DhVQU9Pk7V3kLU6k82Xtaj6ygnO9yZ13lk/s790-rw-e365/1.png)

## **Hidden hazards.**

As with all powerful tools, there is a responsibility to maintain these tools properly, as they can very often be misused without the proper safeguards. This is indeed the case with AD CS. Since AD CS is a core component of the modern Windows and Active Directory authentication and authorization framework, any vulnerabilities that exist pose a great risk to those environments. As we saw 6-7 years ago with Kerberos, and continue to see today, if key authentication infrastructure is compromised, it can be abused to great lengths. The same is the case with AD CS, if not to a greater extent.

[![AD CS Vulnerabilities](data:image/png;base64... "AD CS Vulnerabilities")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgvVCAhe55jr3RYfJp8nzS_wy6TiEbzbZ2Bpez8G5rq9ZL1rqtLoslq2V73pl6XuOj0LaSy9tiTPaAuItz-s8yMEePaFp1W7Y2RN7rEquBtcV9LKV0NmtTxG8xpcGjDV6y4yX_dQSKMxH-xAHHQRDHqky1H-UFl5HVv2nWQgtRXxH178XNWegaKGiyUAL4/s790-rw-e365/2.png)

## **AD CS Attack Basics**

AD CS attacks rely on the fact that the domain trusts the Certificate Authority ("CA") server as much as it trusts its Kerberos servers and other identity servers. Think of the CA server as a gatekeeper. Just as a gatekeeper controls access to a secure area, the CA server controls the distribution and validation of certificates, ensuring that only trusted entities can gain access.

However, AD CS attacks leverage this fact in order to circumvent the need for things like passwords or encryption keys. There are four major classes of AD CS vulnerabilities:

* ESC – This class of vulnerabilities results in some level of privilege escalation within the victim network / domain. Attackers can abuse these vulnerabilities to convert their access from a low- privileged user, to the domain administrator, with little to no effort.
* THEFT – These vulnerabilities are present when there are not significant security controls around the client endpoint, which allow for the authentication certificates to be stolen, resulting in either privilege escalation or persistence in the environment.
* PERSIST – As the name states, these vulnerabilities result in a situation in the network environment in which the attacker can abuse their access to a certificate in order to persist their access in an environment, without the need for a password.
* CVE – Separate from the first three classes, these vulnerabilities are based on abusing certain known vulnerabilities within AD CS that have patches.

Critically worth noting is that, while Microsoft does track and have patches released for the AD CS vulnerabilities that have been assigned CVEs, for the majority of these vulnerabilities, Microsoft puts the onus of repair and security on the consumer, which leads to the presence of these vulnerabilities much more often.

The most dangerous of the AD CS vulnerability categories is the ESC category (ESC as in privilege escalation). These pose the greatest threat to the user's environment as they require little to no privileges, depending on the specific misconfiguration. One such misconfiguration is the ESC2 vulnerability, which occurs from a server's need to impersonate certain users under particular circumstances.

This attack allows a standard user to enroll for a certificate by impersonating them via the request's on-behalf-of field. By doing this, a standard ...
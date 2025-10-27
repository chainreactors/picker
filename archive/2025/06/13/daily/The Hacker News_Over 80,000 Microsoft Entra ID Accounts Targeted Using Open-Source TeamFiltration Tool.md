---
title: Over 80,000 Microsoft Entra ID Accounts Targeted Using Open-Source TeamFiltration Tool
url: https://thehackernews.com/2025/06/over-80000-microsoft-entra-id-accounts.html
source: The Hacker News
date: 2025-06-13
fetch_date: 2025-10-06T23:00:48.717431
---

# Over 80,000 Microsoft Entra ID Accounts Targeted Using Open-Source TeamFiltration Tool

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

# [Over 80,000 Microsoft Entra ID Accounts Targeted Using Open-Source TeamFiltration Tool](https://thehackernews.com/2025/06/over-80000-microsoft-entra-id-accounts.html)

**Jun 12, 2025**Ravie LakshmananEnterprise Security / Active Directory

[![Open-Source TeamFiltration Tool](data:image/png;base64... "Open-Source TeamFiltration Tool")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjvR5NY7GSRQbAIPYuPNuD-LfkXzm4RThbBs3ZP19HH3toBuwloVhX_4ZzbFVmpRwXaZ5kwRR4UkK79Kw3j5FIsd2QTCRrjIfizRYsZJziNqhoi6NIIZUASde5dlOfzU07WALkHrvF1jmcKzbU-iXiyr7G6OHqG2QXDv45li52xIx5x9ypCIgidR0_Zc3g2/s790-rw-e365/Microsoft-Entra-ID.jpg)

Cybersecurity researchers have uncovered a new account takeover (ATO) campaign that leverages an open-source penetration testing framework called TeamFiltration to breach Microsoft Entra ID (formerly Azure Active Directory) user accounts.

The activity, codenamed **UNK\_SneakyStrike** by Proofpoint, has targeted over 80,000 user accounts across hundreds of organizations' cloud tenants since a surge in login attempts was observed in December 2024, leading to successful account takeovers.

"Attackers leverage Microsoft Teams API and Amazon Web Services (AWS) servers located in various geographical regions to launch user-enumeration and password-spraying attempts," the enterprise security company [said](https://www.proofpoint.com/us/blog/threat-insight/attackers-unleash-teamfiltration-account-takeover-campaign). "Attackers exploited access to specific resources and native applications, such as Microsoft Teams, OneDrive, Outlook, and others."

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

TeamFiltration, [publicly released](https://github.com/Flangvik/TeamFiltration) by researcher Melvin "Flangvik" Langvik in August 2022 at the [DEF CON security conference](https://media.defcon.org/DEF%20CON%2030/DEF%20CON%2030%20presentations/Melvin%20Flangvik%20Langvik%20-%20Taking%20a%20Dump%20In%20The%20Cloud.pdf), is described as a [cross-platform framework](https://www.splunk.com/en_us/blog/security/hunting-m365-invaders-blue-team-s-guide-to-initial-access-vectors.html) for "enumerating, spraying, exfiltrating, and backdooring" Entra ID accounts.

The tool offers extensive capabilities to facilitate account takeover using password spraying attacks, data exfiltration, and persistent access by uploading malicious files to the target's Microsoft OneDrive account.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgwacVK9e75Iezv9pbluQJcOyo8nhChpMR0BTE7d3BzhixK-lon-P7ESfoJnPSgwtZzbybbO72Q-Ppix0Ua4aglOrU42TrEOawcCOjRMIwlXoBzUyqgwknbFT71cB_BFIgz-GGUor9umAdxrGMWXKx1Iko3MowjDU_af57cnwOv3RmP5U8H5GUZflIVipQx/s790-rw-e365/ms.png)

While the tool requires an Amazon Web Services (AWS) account and a disposable Microsoft 365 account to facilitate password spraying and account enumeration functions, Proofpoint said it observed evidence of malicious activity leveraging TeamFiltration to conduct these activities such that each password spraying wave originates from a different server in a new geographic location.

At its peak, the campaign targeted 16,500 accounts in a single day in early January 2025. The three primary source geographies linked to malicious activity based on the number of IP addresses include the United States (42%), Ireland (11%), and Great Britain (8%).

When reached for comment, an AWS spokesperson told The Hacker News that customers are required to abide by its terms and that it takes steps to block prohibited content.

"AWS has clear terms that require our customers to use our services in compliance with applicable law," the spokesperson said. "When we receive reports of potential violations of our terms, we act quickly to review and take steps to disable prohibited content. We value collaboration with the security research community and encourage researchers to report suspected abuse to AWS Trust & Safety through our dedicated [abuse reporting process](https://support.aws.amazon.com/#/contacts/report-abuse)."

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The UNK\_SneakyStrike activity has been described as "large-scale user enumeration and password spraying attempts," with the unauthorized access efforts occurring in "highly concentrated bursts" targeting several users within a single cloud environment. This is followed by a lull that lasts for four to five days.

The findings once again highlight how tools designed to assist cybersecurity professionals can be misused by threat actors to carry out a wide range of nefarious actions that allow them to breach user accounts, harvest sensitive data, and establish persistent footholds.

"UNK\_SneakyStrike's targeting strategy suggests they attempt to access all user accounts within smaller cloud tenants while focusing only on a subset of users in larger tenants," Proofpoint said. "This behaviour matches the tool's advanced target acquisition features, designed to filter out less desirable accounts."

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

[Active Directory](https://thehackernews.com/search/label/Active%20Directory)[Amazon Web Services](...
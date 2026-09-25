---
title: TeamFiltration Campaign Compromises Seven Microsoft 365 Accounts Using Default Passwords
url: https://thehackernews.com/2026/09/teamfiltration-compromises-seven.html
source: The Hacker News
date: 2026-09-24
fetch_date: 2026-09-25T06:53:34.568685
---

# TeamFiltration Campaign Compromises Seven Microsoft 365 Accounts Using Default Passwords

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiHP9KRFkaxKFUKQNRU3CkfxCyJLEuIfmo6ov7iWHHRBE1ShJKfXdPvozMZMVuvOJipQ8Qbap3UBmtjKvZh-xBqLeUartPWmRuQj2W8nqdCk2_XlYLXpj15R4Du2oJ1nNVPqIuR-TwbMyPQe4gxxCcMYvUMbFO_Nin2OdhyzkJvX8Sn83aEbM1C5sgaaCqI/s728-nu-rw-lo-l85-e365/wiz-sep-d.png)](https://thehackernews.uk/claude-security-guide-d)

# [TeamFiltration Campaign Compromises Seven Microsoft 365 Accounts Using Default Passwords](https://thehackernews.com/2026/09/teamfiltration-compromises-seven.html)

**Ravie Lakshmanan**Sep 24, 2026Cloud Security / Identity Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgQgKN3zS7GtEpakDcL7zk0tL-zcz3GJMkVf9vMLCVXf33XZ1Yad77dg3Zen_EEB58BltCG_pj0c-yVDm6VbV9cw5Baxtf26vVtRwW4qwDDy1s8HYMFKfTyl382lwJIRfSWBSA-WK6RAZ8lmy9zf5IZb_Ilqol0AcVdEaMp599tZ4NxqUc-KY4-fyFNYYFg/s1700-nu-rw-lo-l85-e365/ms-365.jpg)

Cybersecurity researchers have disclosed details of an active TeamFiltration campaign codenamed **[UNK\_CondorFiltration](https://www.proofpoint.com/us/blog/threat-insight/Spraying-in-the-Andes-TeamFiltration-Returns)** that has targeted over 5,700 accounts across 28 Microsoft 365 tenants.

According to Proofpoint, the activity has primarily focused on Chilean retail and financial institutions. It originated from 1,487 unique AWS EC2 source IP addresses.

"The campaign compromised 7 accounts – all of which were unmanaged functional or service accounts rather than individual employee accounts – highlighting a critical exposure gap around forgotten, non-human identities carrying default or unrotated passwords and no MFA [multi-factor authentication]," the enterprise security company said in a statement.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/trust-world-update-d)

The Microsoft 365 brute-force campaign is said to have unfolded across three different waves from late July to August 2026, with an unnamed Chilean retailer facing the brunt of 78.3% of all observed authentication events -

* July 21-24, targeting approximately 100–120 unique accounts per day and directed against two major Chilean banking institutions
* July 26-28, targeting a peak of about 1,520 accounts on July 27 before dropping sharply and directed against another major Chilean financial institution
* August 13-16, targeting a peak of about 1,560 accounts on August 15 and directed against a major Chilean retailer, leading to seven account compromises

Evidence indicates that the threat actor likely sprayed accounts with default passwords, including credentials provisioned by IT teams and never rotated. The activity mainly targeted dormant service accounts as opposed to personal employee accounts, since users are mandated to change passwords from time to time.

These service accounts, per Proofpoint, were provisioned to run business operations and then left unmonitored, while still carrying their original credentials. Every successful compromise has been linked to unmonitored service accounts with a default password.

Six of the seven compromised accounts were broken into within 7 minutes, likely indicating a shared or default password set rather than individually targeted credential stuffing.

The activity is characterized by the use of TeamFiltration, a legitimate cross-platform offensive framework designed for "enumerating, spraying, exfiltrating, and backdooring" Entra ID accounts. It allows an operator to validate email accounts, test common or targeted passwords across enumerated accounts, harvest sensitive data, and gain covert, interactive access to OneDrive.

Across most of the compromised accounts, the threat actor leveraged the foothold to access Microsoft Office, OneDrive, and Teams, potentially indicative of data harvesting and exfiltration. That said, sign-in events alone cannot be taken as evidence of exfiltration.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-security-guide-b)

Less than 2 minutes after successful compromise, the operator has been observed pivoting to a German VPN node to probe the corporate VPN ("vpn.[redacted].cl/SAML20/SP"), access Azure Portal, browse SharePoint Online, and initiate Microsoft Graph API token requests.

This is not the first time TeamFiltration has been put to use in malicious attacks. In June 2025, Proofpoint detailed another threat cluster dubbed [UNK\_SneakyStrike](https://thehackernews.com/2025/06/over-80000-microsoft-entra-id-accounts.html) that targeted over 80,000 user accounts across hundreds of organizations' cloud tenants using the open-source penetration testing framework.

"The UNK\_CondorFiltration campaign is a reminder that one of the weakest links in an enterprise identity perimeter is often not a phished employee or a zero-day exploit," Proofpoint said. "It is the forgotten account. Service accounts provisioned for convenience and never revisited are a structurally unprotected attack surface."

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

[Cloud security](https://thehackernews.com/search/label/Cloud%20security), [Identity Security](https://thehackernews.com/search/label/Identity%20Security), [Microsoft](https://thehackernews.com/search/label/Microsoft)

⚡ Top Stories This Week

[![The Hacker News](data:image/svg+xml;base64...)

Claude Opus 5 Helped Researchers Take Over OpenAI Staff Accounts via Chained Flaws](https://thehackernews.com/2026/09/claude-opus-5-helped-researchers-take.html)

[![The Hacker News](data:image/svg+xml;base64...)

Google Gemini ...
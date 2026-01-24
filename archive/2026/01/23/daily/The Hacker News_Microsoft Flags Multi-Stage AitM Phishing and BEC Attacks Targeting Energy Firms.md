---
title: Microsoft Flags Multi-Stage AitM Phishing and BEC Attacks Targeting Energy Firms
url: https://thehackernews.com/2026/01/microsoft-flags-multi-stage-aitm.html
source: The Hacker News
date: 2026-01-23
fetch_date: 2026-01-24T03:32:39.861264
---

# Microsoft Flags Multi-Stage AitM Phishing and BEC Attacks Targeting Energy Firms

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

# [Microsoft Flags Multi-Stage AitM Phishing and BEC Attacks Targeting Energy Firms](https://thehackernews.com/2026/01/microsoft-flags-multi-stage-aitm.html)

**Ravie Lakshmanan**Jan 23, 2026Identity Security / Cloud Securit

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgBbSlIXcDChwJf0Cmq4j01QoZOUqnaRGaciqD9J0XKMk-2_Fnzge5_qv44fs_4xzO3OORbk0kiYFOHlocsuJBdVDxC86k-GMG-21LAJ-62F15I6XyUVobMKwVVh6h8PxP6rsJSPaSFUh50yCflaAxLI-UpGwbCLAaCtKqoti67rT6jChpeTei6TUjjYCE4/s1600-e365/1000049930.png)

Microsoft has warned of a multi‑stage adversary‑in‑the‑middle ([AitM](https://thehackernews.com/2023/06/microsoft-uncovers-banking-aitm.html)) phishing and business email compromise (BEC) campaign targeting multiple organizations in the energy sector.

"The campaign abused SharePoint file‑sharing services to deliver phishing payloads and relied on inbox rule creation to maintain persistence and evade user awareness," the Microsoft Defender Security Research Team [said](https://www.microsoft.com/en-us/security/blog/2026/01/21/multistage-aitm-phishing-bec-campaign-abusing-sharepoint/). "The attack transitioned into a series of AitM attacks and follow-on BEC activity spanning multiple organizations."

As part of post-exploitation activity following initial compromise, the unknown attackers have been found to leverage trusted internal identities from the victim to carry out large‑scale intra‑organizational and external phishing in an effort to cast a wide net and widen the scope of the campaign.

The starting point of the attack is a phishing email likely sent from an email address belonging to a trusted organization, which was compromised beforehand. Abusing this legitimate channel, the threat actors sent out messages masquerading as SharePoint document‑sharing workflows to give it a veneer of credibility and trick recipients into clicking on phishing URLs.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/zero-trust-summit-d)

Because services like SharePoint and OneDrive are widely used in enterprise environments and the emails originate from a legitimate address, they are unlikely to raise suspicion, allowing adversaries to deliver phishing links or stage malicious payloads. This approach is also called living-off-trusted-sites ([LOTS](https://www.microsoft.com/en-us/security/blog/2026/01/21/multistage-aitm-phishing-bec-campaign-abusing-sharepoint/)), as it weaponizes the familiarity and ubiquity of such platforms to subvert email‑centric detection mechanisms.

The URL, for its part, redirects users to a fake credential prompt to view the purported document. Armed with access to the account using the stolen credentials and the session cookie, the attackers create inbox rules to delete all incoming emails and mark all emails as read. With this foundation in place, the compromised inbox is used to send phishing messages containing a fake URL designed to conduct credential theft using an AitM attack.

In one case, Microsoft said the attacker initiated a large-scale phishing campaign involving more than 600 emails that were sent to the compromised user's contacts, both within and outside of the organization. The threat actors have also been observed taking steps to delete undelivered and out of office emails, and assure message recipients of the email's authenticity if they raised any concerns. The correspondence is then deleted from the mailbox.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgu-w1ax9sBSlN39BeyX3ckS_Gw_03rQS8aqd_IIRjn501it7Iy6LFUZ_OO3VdoTOd1pytsdQJ5l89QuqzhOt4kR3DNjtZEsryU2r2-nHEmmHHhS7BuFYrENRHBYJBE_1mvbHsMGsG9i-tPYzIkThO1NTOK00EqUXBYxKElUca4wvlVWvhyWhu4JcMF6ANE/s1600-e365/1000049928.jpg)

"These techniques are common in any BEC attacks and are intended to keep the victim unaware of the attacker's operations, thus helping in persistence," the Windows maker noted.

Microsoft said the attack highlights the "operational complexity" of AitM, stating password resets alone cannot remediate the threat, as impacted organizations must ensure that they have revoked active session cookies and removed attacker-created inbox rules used to evade detection.

To that end, the company noted that it worked with customers to revoke multi-factor authentication (MFA) changes made by the attacker on the compromised user's accounts and delete suspicious rules created on those accounts. It's currently not known how many organizations were compromised and if it's the work of any known cybercrime group.

Organizations are advised to work with their identity provider to make sure security controls like phishing-resistant MFA are in place, enable [conditional access policies](https://learn.microsoft.com/azure/active-directory/fundamentals/concept-fundamentals-security-defaults), implement [continuous access evaluation](https://learn.microsoft.com/azure/active-directory/conditional-access/concept-continuous-access-evaluation), and use anti-phishing solutions that monitor and scan incoming emails and visited websites.

The attack outlined by Microsoft highlights the [ongoing trend](https://www.netcraft.com/blog/shared-document-spam-delivers-remote-access-tool) among threat actors to [abuse trusted services](https://www.netcraft.com/blog/confluence-svg-rfp-phishing-scam) such as Google Drive, Amazon Web Services (AWS), and Atlassian's Confluence wiki to redirect to credential harvesting sites and stage malware. This eliminates the need for attackers to build out their own infrastructure as well as makes malicious activity appear legitimate.

The disclosure comes as identity services provider Okta said it detected custom phishing kits that are designed specifically for use in voice phishing (aka vishing) campaigns targeting Google, Microsoft, Okta, and a wide range of cryptocurrency platforms. In these campaigns, the adversary, posing as tech support personnel, calls prospective targets using a spoofed support hotline or company phone number.

The attacks aim to trick users into visiting a malicious URL and hand over their credentials, which are subsequently relayed to the threat actors in real-time via a Telegram channel, granting them unauthorized access to their accounts. The social engineering efforts are well planned, with the attackers conducting reconnaissance on the targets and crafting customized phishin...
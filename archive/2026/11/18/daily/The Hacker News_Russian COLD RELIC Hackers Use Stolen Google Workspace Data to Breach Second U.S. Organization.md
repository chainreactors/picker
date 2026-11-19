---
title: Russian COLD RELIC Hackers Use Stolen Google Workspace Data to Breach Second U.S. Organization
url: https://thehackernews.com/2026/11/russian-cold-relic-hackers-use-stolen.html
source: The Hacker News
date: 2026-11-18
fetch_date: 2026-11-19T09:47:37.083506
---

# Russian COLD RELIC Hackers Use Stolen Google Workspace Data to Breach Second U.S. Organization

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

# [Russian COLD RELIC Hackers Use Stolen Google Workspace Data to Breach Second U.S. Organization](https://thehackernews.com/2026/11/russian-cold-relic-hackers-use-stolen.html)

**Ravie Lakshmanan**Nov 18, 2026Cyber Espionage / Cloud Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjLbxlzqi-uBPlDXGecxrfXQ8kZLpAKsDO5c7KmTTyYyNQQE6bdI0TqT7Rk_JrKRie2pMB_xrLRKy1Cksp1GYHfUGHXz7UGg5nWOAQmPmiRKoUJkMCHrMvW7A72W9x7_I7KESMQmJLQVrJth_Ozj7i1nF7IPB4W_WV-NQyy0afEMgGVbGdaSNfIjolqtC4-/s1700-nu-rw-lo-l85-e365/cloud.jpg)

The Russia-linked cyber espionage group known as **Cold Relic** (formerly COLDRIVER and UNC4057) has been observed weaponizing a single cloud compromise into a launchpad for a series of linked intrusions resulting in third-party compromise.

Google's Mandiant and Threat Intelligence Group (GTIG) said it investigated a 2026 compromise at a U.S.-based organization in which the adversary leveraged data, the corporate staff directory, and identities harvested from an earlier attack on another U.S.-based entity in late 2025.

Cold Relic, also tracked as Callisto, Gossamer Bear, and Star Blizzard, has a [track record](https://thehackernews.com/2026/03/ta446-deploys-leaked-darksword-ios.html) of orchestrating sophisticated phishing and malware campaigns to gain access information that may be of strategic importance to the Russian government.

The access is abused to register rogue multi-factor authentication (MFA) devices, passkeys, and MFA backup codes to establish long-term persistence and then conduct aggressive data collection and exfiltration operations targeting email, chat, and cloud storage repositories. In addition, the compromised access is used to target the victim's social and professional networks.

Attacks mounted by the threat actor have successfully compromised high-value targets, including government officials, defense contractors, and non-governmental organizations (NGOs) across Europe and North America.

"Once Cold Relic compromises a target, it uses stolen emails and data to establish authentic pretexts and impersonate contacts when reaching out to subsequent targets," Google [said](https://cloud.google.com/blog/topics/threat-intelligence/cold-relic-a-case-study-in-impersonation-and-compromise).

According to the tech giant's cybersecurity and incident response teams, Cold Relic compromised the cloud productivity environment of an unspecified U.S.-based organization in late 2025. Initial access to the network was achieved by means of a residential proxy network located in close geographical proximity to the victim.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/threat-protection-d)

Using the stolen credentials of a Super Admin account and combining it with an MFA push notification fatigue attack, the threat actor is said to have gained access to the account after the victim accepted an MFA request. This was followed by the attacker registering their own device within the tenant to retain access. The threat actor was also observed using passkeys and MFA backup codes as alternate access mechanisms.

"Cold Relic used the privileges of the compromised Super Admin account to download the contents of the entire organization's cloud storage drive by both mass sharing files to a Cold Relic-operated email account and downloading files directly," Google explained.

"While operating inside the tenant of the victim organization, Cold Relic accessed the Admin Console, queried Admin security investigation and email audit logs to check defensive visibility, and viewed, modified, and deleted Alert Center notifications to remove forensic evidence of the initial intrusion."

These actions ultimately enabled the threat actor to export full employee lists and domain-wide data via the [Google Takeout service](https://knowledge.workspace.google.com/admin/users/advanced/allow-or-block-google-takeout) using the Super Admin privileges. Following mass data theft, the attackers continued to maintain access over several months and perform additional activities -

* Sync email inbox via OAuth to external email clients.
* Re-authenticate using unrevoked attacker-enrolled passkeys that persisted across password and session resets and bypassed device registration controls.
* Target cloud drive document access related to credentials, email archives, personnel information, and other documents of interest.

Even after the attackers were ousted from the victim organization, Google said it observed Cold Relic using email accounts impersonating employees of the victim organization to target both internal employees and associates within the same professional circles as part of a renewed social engineering campaign.

The attack then moved to the next phase when the threat actor compromised a Microsoft Entra ID user account of a second U.S.-based organization that used Entra ID as its federated single sign-on (SSO) identity provider for Google Workspace.

By impersonating an employee at the first organization, the threat actor established communications with the target over a secure messaging app and then shared phishing links designed to harvest credentials and authentication tokens for Entra ID under the pretext of sharing a document containing details about a technical issue.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/network-defense-dd)

"Upon successful authentication using the stolen credentials, Cold Relic registered and used a new MFA device in the SSO solution to retain access to the user account throughout the intrusion," Google said.

"By impersonating someone known in the same professional circles as the new target, Cold Relic increased their chance of phishing success. Ultimately, in this case, Cold Relic was able to obtain credentials to the organization and perform bulk download of files accessible in the compromised user's cloud drive."

Upon successfully compromising the second organization, the messaging a...
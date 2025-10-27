---
title: Axios Abuse and Salty 2FA Kits Fuel Advanced Microsoft 365 Phishing Attacks
url: https://thehackernews.com/2025/09/axios-abuse-and-salty-2fa-kits-fuel.html
source: The Hacker News
date: 2025-09-10
fetch_date: 2025-10-02T19:56:09.543348
---

# Axios Abuse and Salty 2FA Kits Fuel Advanced Microsoft 365 Phishing Attacks

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

# [Axios Abuse and Salty 2FA Kits Fuel Advanced Microsoft 365 Phishing Attacks](https://thehackernews.com/2025/09/axios-abuse-and-salty-2fa-kits-fuel.html)

**Sep 09, 2025**Ravie LakshmananPhishing / Email Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEihdRbIp3q2q7MpV9hjqNW0Ngask5kqyovpxQFae7nJiGapCmRMCHnLtmNNdlUNzc5lPBzb_cvCmpnTU5xtoqqzJD7uJUC7J4ip0IVVbJd6bmXvC4NG9Ro0Pp49vkiu61uX-p5cz9wvSk_4tJNzR19XZGXLt9zTm5zeq4mZxsEvrwDl_xVNaF5MG_E-qSO5/s790-rw-e365/ms-phish.jpg)

Threat actors are abusing HTTP client tools like [Axios](https://github.com/axios/axios) in conjunction with Microsoft's Direct Send feature to form a "highly efficient attack pipeline" in recent phishing campaigns, according to new findings from ReliaQuest.

"Axios user agent activity surged 241% from June to August 2025, dwarfing the 85% growth of all other flagged user agents combined," the cybersecurity company [said](https://reliaquest.com/blog/threat-spotlight-attackers-exploit-axios-for-automated-phishing/) in a report shared with The Hacker News. "Out of 32 flagged user agents observed in this timeframe, Axios accounted for 24.44% of all activity."

The abuse of Axios was [previously flagged](https://thehackernews.com/2025/02/cybercriminals-use-axios-and-node-fetch.html) by Proofpoint in January 2025, detailing campaigns utilizing HTTP clients to send HTTP requests and receive HTTP responses from web servers to conduct account takeover (ATO) attacks on Microsoft 365 environments.

ReliaQuest told The Hacker News that there is no evidence to suggest these activities are related, adding that the tool is regularly exploited alongside popular phishing kits. "The usefulness of Axios means it is almost certainly being adopted by all types of threat actors regardless of sophistication levels or motivation," the company stated.

Similarly, phishing campaigns have also been observed increasingly using a legitimate feature in Microsoft 365 (M365) called [Direct Send](https://thehackernews.com/2025/07/hackers-using-pdfs-to-impersonate.html) to [spoof trusted users](https://thehackernews.com/2025/08/phishing-campaign-uses-upcrypter-in.html) and distribute email messages.

In amplifying Axios abuse through Microsoft Direct Send, the attack aims to weaponize a trusted delivery method to ensure that their messages slip past secure gateways and land in users' inboxes. Indeed, attacks that paired Axios with Direct Send have been found to achieve a 70% success rate in recent campaigns, surging past non-Axios campaigns with "unparalleled efficiency."

The campaign observed by ReliaQuest is said to have commenced in July 2025, initially singling out executives and managers in finance, health care, and manufacturing sectors, before expanding its focus to target all users.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Calling the approach a game changer for attackers, the company pointed out that the campaign not only is successful at bypassing traditional security defenses with improved precision, but also enables them to mount phishing operations at an unprecedented scale.

In these attacks, Axios is used to intercept, modify, and replay HTTP requests, thereby making it possible to capture session tokens or multi-factor authentication (MFA) codes in real-time or exploit SAS tokens in Azure authentication workflows to gain access to sensitive resources.

"Attackers use this blind spot to bypass MFA, hijack session tokens, and automate phishing workflows," ReliaQuest said. "The customizability offered by Axios lets attackers tailor their activity to further mimic legitimate workflows."

The email messages involve using compensation-themed lures to trick recipients into opening PDF documents containing malicious QR codes, which, when scanned, direct users to fake login pages mimicking Microsoft Outlook to facilitate credential theft. As an extra layer of defense evasion, some of these pages are hosted on Google Firebase infrastructure to capitalize on the reputation of the app development platform.

Besides lowering the technical barrier for sophisticated attacks, Axios's prevalence in enterprise and developer setups also means that it offers attackers a way to blend in with regular traffic and fly under the radar.

To mitigate the risk posed by this threat, organizations are advised to secure Direct Send and disable it if not required, configure appropriate anti-spoofing policies on email gateways, train employees to recognize phishing emails, and block suspicious domains.

"Axios amplifies the impact of phishing campaigns by bridging the gap between initial access and full-scale exploitation. Its ability to manipulate authentication workflows and replay HTTP requests allows attackers to weaponize stolen credentials in ways that are both scalable and precise."

"This makes Axios integral to the rising success of Direct Send phishing campaigns, showing how attackers are evolving beyond traditional phishing tactics to exploit authentication systems and APIs at a level that traditional defenses are ill-equipped to handle."

The development comes as Mimecast detailed a large-scale credential harvesting campaign targeting hospitality industry professionals by impersonating trusted hotel management platforms Expedia Partner Central and Cloudbeds in emails that claim to be guest booking confirmations and partner central notifications.

"This credential harvesting operation leverages the routine nature of hotel booking communications," the company [said](https://www.mimecast.com/threat-intelligence-hub/hospitality-focused-phishing-campaign-impersonates-expedia-and-cloudbeds/). "The campaign employs urgent, business-critical subject lines designed to prompt immediate action from hotel managers and staff."

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The findings also follow the discovery of an ongoing campaign that has employed a nascen...
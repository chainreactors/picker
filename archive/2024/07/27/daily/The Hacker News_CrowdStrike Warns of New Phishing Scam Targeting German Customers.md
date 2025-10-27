---
title: CrowdStrike Warns of New Phishing Scam Targeting German Customers
url: https://thehackernews.com/2024/07/crowdstrike-warns-of-new-phishing-scam.html
source: The Hacker News
date: 2024-07-27
fetch_date: 2025-10-06T17:46:34.613032
---

# CrowdStrike Warns of New Phishing Scam Targeting German Customers

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

# [CrowdStrike Warns of New Phishing Scam Targeting German Customers](https://thehackernews.com/2024/07/crowdstrike-warns-of-new-phishing-scam.html)

**Jul 26, 2024**The Hacker NewsEnterprise Security / Network Security

[![CrowdStrike](data:image/png;base64... "CrowdStrike")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj0wzC4c52os5T_IzuUdmFgH5XQmKfurpTsHKK_WwxFh7QRF2fTj4Ew8USVmUYPuauNoLwNKYINrUMszxFj9VWNSAe4kQcakeHeqv6cpshxs4BOP5duWbYhsAWYS_JgZpdKkEC-aoCop3qa6Gfc768MqdB4e86tfTH0aAUmoGo9nOgiGnk3nhesF0NKMakE/s790-rw-e365/malware.png)

CrowdStrike is alerting about an unfamiliar threat actor attempting to capitalize on the [Falcon Sensor update fiasco](https://thehackernews.com/2024/07/crowdstrike-explains-friday-windows.html) to distribute dubious installers targeting German customers as part of a highly targeted campaign.

The cybersecurity company said it identified what it described as an unattributed spear-phishing attempt on July 24, 2024, distributing an inauthentic CrowdStrike Crash Reporter installer via a website impersonating an unnamed German entity.

The imposter website is said to have been created on July 20, a day after the [botched update](https://thehackernews.com/2024/07/cybercriminals-exploit-crowdstrike.html) crashed nearly 9 million Windows devices, causing extensive IT disruptions across the world.

"After the user clicks the Download button, the website leverages JavaScript (JS) that masquerades as JQuery v3.7.1 to download and deobfuscate the installer," CrowdStrike's Counter Adversary Operations team [said](https://www.crowdstrike.com/blog/malicious-inauthentic-falcon-crash-reporter-installer-spearphishing/).

"The installer contains CrowdStrike branding, German localization, and a password [is] required to continue installing the malware."

Specifically, the spear-phishing page featured a download link to a ZIP archive file containing a malicious InnoSetup installer, with the malicious code serving the executable injected into a JavaScript file named "jquery-3.7.1.min.js" in an apparent effort to evade detection.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Users who end up launching the bogus installer are then prompted to enter a "Backend-Server" to proceed further. CrowdStrike said it was unable to recover the final payload deployed via the installer.

The campaign is assessed to be highly targeted owing to the fact that the installer is password-protected and requires input that's likely only known to the targeted entities. Furthermore, the presence of the German language suggests that the activity is geared towards German-speaking CrowdStrike customers.

"The threat actor appears to be highly aware of operations security (OPSEC) practices, as they have focused on anti-forensic techniques during this campaign," CrowdStrike said.

"For example, the actor registered a subdomain under the it[.]com domain, preventing historical analysis of the domain-registration details. Additionally, encrypting the installer contents and preventing further activity from occurring without a password precludes further analysis and attribution."

[![CrowdStrike](data:image/png;base64... "CrowdStrike")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhjr7nFAOfmux3dKmBE4MXxA1UI095eueQlSxdjWItTiNrigbOl-GYnbev5cYRbHlp3uZJCsUIA5AEqeyMkjJCJhPrz4izXYnsxwFazsV5fuUeWTy2_nhfpbbA0jfjFzoQ_ZMo35MWNcLyIEt-xp94HF5-IqFM3Bm1_zd-fh9YQIAXZNb7JacNbQy3LuRGd/s790-rw-e365/code.png)

The development comes amid a wave of phishing attacks taking advantage of the CrowdStrike update issue to propagate stealer and wiper malware malware -

* A phishing domain crowdstrike-office365[.]com that [hosts](https://www.crowdstrike.com/blog/lumma-stealer-with-cypherit-phishing-lure/) rogue archive files containing a Microsoft Installer (MSI) loader that ultimately executes a commodity information stealer called [Lumma](https://thehackernews.com/2024/07/microsoft-defender-flaw-exploited-to.html).

* A ZIP file ("CrowdStrike Falcon.zip") that contains a Python-based information stealer tracked as [Connecio](https://www.crowdstrike.com/blog/threat-actor-distributes-python-based-information-stealer/) that collects system information, external IP address, and data from various web browsers, and exfiltrates them to SMTP accounts listed on a Pastebin dead-drop URL.
* An email phishing campaign [orchestrated](https://www.trellix.com/blogs/research/handalas-wiper-targets-israel/) by the [Handala Hacking Team](https://cyberint.com/blog/threat-intelligence/handala-hack-what-we-know-about-the-rising-threat-actor/) targeting Israeli entities that tricks recipients into downloading an "outage fix," which launches an installer responsible for unpacking and executing an AutoIt script to launch a data wiper and exfiltrate system information via Telegram's API.

Web infrastructure and security company Akamai [said](https://www.akamai.com/blog/security-research/2024-july-crowdstrike-bsod-domains-what-could-come-next) it uncovered no less than 180 newly created counterfeit typosquat domains purporting to assist with navigating the incident, whether it be technical support, quick fixes, or legal support, in an attempt to introduce malware or steal sensitive information.

On Thursday, CrowdStrike's CEO George Kurtz said 97% of the Windows devices that went offline during the global IT outage are now operational.

"At CrowdStrike, our mission is to earn your trust by safeguarding your operations. I am deeply sorry for the disruption this outage has caused and personally apologize to everyone impacted," Kurtz [said](https://www.linkedin.com/posts/georgekurtz_falcon-content-update-remediation-and-guidance-activity-7222323091652108289-19Xv). "While I can't promise perfection, I can promise a response that is focused, effective, and with a sense of urgency."

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Previously, the company's chief security officer Shawn Henr...
---
title: Iran-Linked MuddyWater Hackers Target U.S. Networks With New Dindoor Backdoor
url: https://thehackernews.com/2026/03/iran-linked-muddywater-hackers-target.html
source: The Hacker News
date: 2026-03-06
fetch_date: 2026-03-07T03:57:09.082518
---

# Iran-Linked MuddyWater Hackers Target U.S. Networks With New Dindoor Backdoor

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

[![Security Service Edge](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEguiZ85S7494GyqhFt9uP48C8ggEnb3bp9Qmsdv4LOYjNWfa98MKx17Dk7o1nJrEV3ai3edIGIgwt6oO5iJMmYLcyu6PojcvJnO4IfLhVK2dzGKFyEroFjKQhnp2hd5Cc6G4CynJRfb55aclnGwj7rse9jMncn_vu_tFqQZtHZH3Sb5dMXwRKN-kSVYUMzD/s1700-e365/ai-d.png)](https://thehackernews.uk/wiz-ai-security-d)

# [Iran-Linked MuddyWater Hackers Target U.S. Networks With New Dindoor Backdoor](https://thehackernews.com/2026/03/iran-linked-muddywater-hackers-target.html)

**Ravie Lakshmanan**Mar 06, 2026Cyber Warfare / Cloud Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiGoo0ChP6Wq4Hd0U_DeehQmIN-4DHpRX8YdIY6vSO3kEUeTeILUvJMbAZO2gplvYIYCG_q13wfn_So9SkmjHIFZdwyQZKf0uSyyUMpCV-0uUuptOsPsdAvQQbzBdTAG7zoeX2Zf5L2zrHoY0z-qd5RnNvHsm_R4qaVGKzY440Tkdv2zUJ7y9iUE-UP8Ddl/s1700-e365/iran-hackers.jpg)

New research from Broadcom's Symantec and Carbon Black Threat Hunter Team has [discovered](https://www.security.com/threat-intelligence/iran-cyber-threat-activity-us) evidence of an Iranian hacking group embedding itself in several U.S. companies' networks, including banks, airports, non-profit, and the Israeli arm of a software company.

The activity has been attributed to a state-sponsored hacking group called **[MuddyWater](https://thehackernews.com/2026/02/muddywater-targets-mena-organizations.html)** (aka Seedworm). It's affiliated with the Iranian Ministry of Intelligence and Security (MOIS). The campaign is assessed to have begun in early February, with recent activity detected following [U.S. and Israeli military strikes on Iran](https://thehackernews.com/2026/03/149-hacktivist-ddos-attacks-hit-110.html).

"The software company is a supplier to the defense and aerospace industries, among others, and has a presence in Israel, with the company's Israel operation seeming to be the target in this activity," the security vendor said in a report shared with The Hacker News.

The attacks targeting the software company, as well as a U.S. bank and a Canadian non-profit, have been found to pave the way for a previously unknown backdoor dubbed Dindoor, which leverages the [Deno](https://deno.com/) JavaScript runtime for execution. Broadcom said it also identified an attempt to exfiltrate data from the software company using the Rclone utility to a Wasabi cloud storage bucket. However, it's currently not known if the effort paid off.

Also found in the networks of a U.S. airport and a non-profit was a separate Python backdoor called Fakeset, which was downloaded from servers belonging to Backblaze, an American cloud storage and data backup company. The digital certificate used to sign Fakeset has also been used to sign Stagecomp and Darkcomp malware, both previously linked to MuddyWater.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/not-fast-enough-d)

"While this malware wasn't seen on the targeted networks, the use of the same certificates suggests the same actor -- namely Seedworm -- was behind the activity on the networks of the U.S. companies," Symantec and Carbon Black said.

"Iranian threat actors have become increasingly proficient in recent years. Not only has their tooling and malware improved, but they've also demonstrated strong social engineering capabilities, including spear-phishing campaigns and 'honeytrap' operations used to build relationships with targets of interest to gain access to accounts or sensitive information."

The findings come against the backdrop of an escalating military conflict in Iran, triggering a barrage of cyber attacks in the digital sphere. Recent research from Check Point has uncovered the pro-Palestinian hacktivist group known as Handala Hack (aka Void Manticore) routing its operations through Starlink IP ranges to probe externally facing applications for misconfigurations and weak credentials.

In recent months, multiple [Iran-nexus adversaries](https://www.tenable.com/blog/operation-epic-fury-potential-iranian-cyber-counteroffensive-operations), such as [Agrius](https://thehackernews.com/2023/11/iranian-hackers-launches-destructive.html) (aka Agonizing Serpens, Marshtreader, and Pink Sandstorm), have also [observed](https://blog.checkpoint.com/research/what-defenders-need-to-know-about-irans-cyber-capabilities/) scanning for vulnerable Hikvision cameras and video intercom solutions using known security flaws such as [CVE-2017-7921](https://thehackernews.com/2026/03/hikvision-and-rockwell-automation-cvss.html) and [CVE-2023-6895](https://nvd.nist.gov/vuln/detail/CVE-2023-6895).

The targeting, per Check Point, has intensified in the wake of the current Middle East conflict. The exploitation attempts against IP cameras have witnessed a surge in Israel and Gulf countries, including the U.A.E., Qatar, Bahrain, and Kuwait, along with Lebanon and Cyprus. The activity has singled out cameras from Dahua and Hikvision, weaponizing the two aforementioned vulnerabilities, as well as [CVE-2021-36260](https://nvd.nist.gov/vuln/detail/CVE-2021-36260), [CVE-2025-34067](https://nvd.nist.gov/vuln/detail/CVE-2025-34067), and [CVE-2021-33044](https://nvd.nist.gov/vuln/detail/cve-2021-33044).

"Taken together, these findings are consistent with the assessment that Iran, as part of its doctrine, leverages camera compromise for operational support and ongoing battle damage assessment (BDA) for missile operations, potentially in some cases prior to missile launches," the company [said](https://research.checkpoint.com/2026/interplay-between-iranian-targeting-of-ip-cameras-and-physical-warfare-in-the-middle-east/).

"As a result, tracking camera-targeting activity from specific, attributed infrastructures may serve as an early indicator of potential follow-on kinetic activity."

The U.S. and Israel's war with Iran has also prompted an advisory from the Canadian Centre for Cyber Security (CCCS), which [cautioned](https://www.cyber.gc.ca/en/guidance/cyber-threat-bulletin-iranian-cyber-threat-response-usisrael-strikes-february-2026) that Iran will likely use its cyber apparatus to stage retaliatory attacks against critical infrastructure and information operations to further the regime's interests.

Some other key developments that have unfolded in recent days are listed below -

* Israeli intelligence agencies [h...
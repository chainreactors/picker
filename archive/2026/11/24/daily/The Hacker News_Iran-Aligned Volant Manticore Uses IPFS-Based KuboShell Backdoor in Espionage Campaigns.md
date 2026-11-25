---
title: Iran-Aligned Volant Manticore Uses IPFS-Based KuboShell Backdoor in Espionage Campaigns
url: https://thehackernews.com/2026/11/iran-aligned-volant-manticore-uses-ipfs.html
source: The Hacker News
date: 2026-11-24
fetch_date: 2026-11-25T10:48:29.315380
---

# Iran-Aligned Volant Manticore Uses IPFS-Based KuboShell Backdoor in Espionage Campaigns

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

# [Iran-Aligned Volant Manticore Uses IPFS-Based KuboShell Backdoor in Espionage Campaigns](https://thehackernews.com/2026/11/iran-aligned-volant-manticore-uses-ipfs.html)

**Ravie Lakshmanan**Nov 24, 2026Cyber Espionage / Malware

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhqukTcR2pkDWiTqMzORa4j7zZRB0MDUGfBly50X7gPwPHqSeBmfReQWpMR9IdPOP_NbeuQSBdYPknSgxvutDll4VAZNSoGqcwmXzhZNEez-UoE-MwTnM9i9XxjoLYRdhY0iY6tD9BK9IDB0o8RUU7sNsOex5tVNtoNwRHCCAxM9ri66c4G2wPa9AqW9saA/s1700-nu-rw-lo-l85-e365/iran-hackers.jpg)

A previously undocumented Iran-aligned cyber espionage group called **Volant Manticore** has targeted telecommunications companies, airlines, and critical infrastructure in Cyprus.

Central to the [group's operations](https://research.checkpoint.com/2026/volant-manticore-flying-under-the-radar/) is a backdoor called KuboShell that uses the InterPlanetary File System ([IPFS](https://thehackernews.com/2022/07/researchers-warns-of-increase-in.html)) for command-and-control (C2) and deploys Homa, a post-compromise framework that's a reimplementation of MuddyWater's [MuddyC2Go](https://thehackernews.com/2023/11/muddyc2go-new-c2-framework-iranian.html). Evidence indicates that the threat actor has been operational since late August 2025.

Also delivered alongside these tools are Remote Monitoring and Management (RMM) programs like MeshCentral and NetLock RMM. In tandem, the group has been observed orchestrating credential harvesting campaigns to collect email and corporate credentials of some of the impersonated organizations.

The use of legitimate RMM tools for persistent access has been a hallmark of the [MuddyWater group](https://thehackernews.com/2023/06/from-muddyc3-to-phonyc2-irans.html), although the adversary has since also [increasingly](https://thehackernews.com/2024/07/iranian-hackers-deploy-new-bugsleep.html) deployed its [own malware](https://thehackernews.com/2025/10/iran-linked-muddywater-targets-100.html) in attacks. Both MuddyWater and Volant Manticore are assessed to be affiliated with Iran's Ministry of Intelligence and Security (MOIS).

"While we identified multiple links to MuddyWater, we assess that Volant Manticore likely consists of former MuddyWater operators who branched off from the group and currently operate as a separate threat cluster," Check Point said in an analysis published today. "Volant Manticore's targeting priorities appear responsive to regional geopolitical developments."

This assessment is based on the use of an older MuddyWater framework and its playbook, while diverging from established modus operandi over time to incorporate its own attack methods like credential-harvesting campaigns. The targeting of Cyprus, a country that does not align with MuddyWater's targeting patterns, and the use of separate infrastructure points to a group that pursues its own strategic objectives.

Attack chains have been found to leverage artificial intelligence (AI)-generated personas in bogus CVs to trick targets into clicking on a link to download the complete resume, resulting in the deployment of KuboShell on the victim's system. The activity is said to have been aimed at a Cyprus-based airline that operates flights between Cyprus and Israel.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/threat-protection-d)

This includes a shift toward Saudi Arabian healthcare entities, coinciding with [escalating](https://www.cfr.org/global-conflict-tracker/conflict/war-yemen) [hostilities](https://www.cnbc.com/2026/11/23/trump-iran-war-hormuz-saudi-.html) between Saudi Arabia and the Iranian-backed Houthis.

"This fits the MOIS's track record of targeting hospitals and healthcare providers through cyber operations during military conflicts, in some cases attempting to disrupt their operations," the cybersecurity company said.

As recently as September 2026, the group has been found to launch a phishing campaign against Saudi targets, distributing the backdoor and N-able RMM through two different healthcare-themed ZIP archives named "AI\_Healthcare\_Seminar.zip" and "Ai\_Healthcare\_Seminar\_Online.zip," respectively. Some of the emails have been sent from a compromised account belonging to a private hospital in Saudi Arabia.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhZl7HpKW83zTEaPtcaPYyUhWvdizf_Dl35jyImBwDQdsc08inmKDn9Zp2ClZvIt9De8d_7avT69FZpntZ9QWKvoZBdQHhpLNusc6A3KvTdLTTFo155ZpSjfrfUhBBr3h91FDOFCVDpduN9cql-M7NhnArOjq5pBstTcFkXVtgIlhTESNvGkkWYN83b18vn/s1700-nu-rw-lo-l85-e365/iran-malware.png)

A Windows backdoor, KuboShell uses IPFS for C2 and relies on [Pinata](https://pinata.cloud/) to facilitate file transfer over the peer-to-peer (P2P) file-sharing network.

"On startup, KuboShell checks whether it has administrator privileges. If not, it tries to relaunch itself with higher privileges, which triggers a User Account Control (UAC) prompt," Check Point explained.

"KuboShell retrieves the MAC address of the machine's first network adapter and uses it as a unique identifier for each victim. It then registers the host by uploading a file containing hi, saved to C:\Users\Public\<MAC>.log, using a hard-coded Pinata access token."

Once registered, KuboShell checks Pinata for a command file named <MAC>.txt, and if the file exists, looks up the file’s IPFS identifier and downloads its contents through Pinata's public gateway. The downloaded content is executed via PowerShell in a hidden window. The results of the execution are saved in a file named "C:\Users\Public\<MAC>re.txt" and uploaded back to the server.

It's worth noting that the backdoor is not responsible for capturing the output. Rather, the results are returned only if the received command writes them to the text file. KuboShell then checks for a new command every 60 seconds.

Analysis indicates that KuboShell is primarily used to run basic reconnaissance commands and assess the compromised environment before ...
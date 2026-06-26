---
title: New Mistic Backdoor Linked to KongTuke in ClickFix and ModeloRAT Campaigns
url: https://thehackernews.com/2026/06/new-mistic-backdoor-linked-to-kongtuke.html
source: The Hacker News
date: 2026-06-25
fetch_date: 2026-06-26T06:09:44.232774
---

# New Mistic Backdoor Linked to KongTuke in ClickFix and ModeloRAT Campaigns

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjQl2axNwsfhbXOFynrg_uAZsvHi3OvNGSA8KJO-BKR8Xm3x7yjKV3EvfY4v5mwXx6LF0uWFb9h9d9iAV_Pi-YYhqimX9wx4OaLdDJEdR215Xrxq_PAtXkaLfQso4pTSjbj6fvh_ZTliLpzWZSZfcoZgyXtKwhN-SSDDlmbtUqGLshc0KqYQGWYHMN52Sl1/s728-e100/zz-d.jpg)](https://thehackernews.uk/ai-vuln-protection-d)

# [New Mistic Backdoor Linked to KongTuke in ClickFix and ModeloRAT Campaigns](https://thehackernews.com/2026/06/new-mistic-backdoor-linked-to-kongtuke.html)

**Ravie Lakshmanan**Jun 25, 2026Initial Access Broker / Ransomware

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhC1-4l_iOC19z96Q7C7O_dZSKwEvMnMLhHyb7kpt2rpOzQmn3gKpz6_BaZmSpzgvyhTJf8BBQmBTx0Nvymxk1vfO5O5bE0nNGbYPHAcb5F8ZF_WjTyQe4AXSK71q6fESS9i5Rdpcfzt6ULab7eo21OZKRCYlqwU7G97mF4-AeVVANlT4YIbigdYxUJkwfy/s1700-e365/clickattack.jpg)

A new, stealthy backdoor named **Mistic** has been deployed as part of suspected financially motivated attacks aimed at multiple organizations spanning insurance, education, IT, and professional services sectors since April 2026.

According to Symantec and Carbon Black's Threat Hunter Team, the backdoor, also tracked as MLTBackdoor, is said to be linked to an initial access broker (IAB) named KongTuke (aka 404 TDS, Chaya\_002, LandUpdate808, TAG-124, and Woodgnat), and dropped along with ModeloRAT, a Python remote access trojan (RAT) previously attributed to the group.

"The backdoor runs payloads in memory with no file written to disk and includes a kill switch that lets it delete itself, which are features consistent with an operator seeking long-term, low-visibility access," Broadcom's cybersecurity teams [said](https://www.security.com/threat-intelligence/new-mistic-backdoor-modeloRAT) in a report shared with The Hacker News.

ModeloRAT was [first flagged](https://thehackernews.com/2026/01/crashfix-chrome-extension-delivers.html) by Huntress in January 2026 in connection with a variant of a ClickFix campaign dubbed CrashFix, in which the KongTuke actors used a malicious Google Chrome extension masquerading as an ad blocker to intentionally crash a victim's web browser and trick them into running arbitrary commands under the pretext of running a security scan.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-cant-stop-d)

The malware was also distributed in a different ClickFix campaign that involved running commands carrying out a Domain Name System (DNS) lookup to retrieve the next-stage payload, with Microsoft [noting](https://thehackernews.com/2026/02/microsoft-discloses-dns-based-clickfix.html) that the attack chain uses DNS as a "lightweight staging or signaling channel."

Mistic's use of ClickFix as a delivery vector was [highlighted](https://thehackernews.com/2026/06/threatsday-bulletin-worm-code-leaked-ai.html#clickfix-backdoor-expands) by Zscaler ThreatLabz earlier this month, attributing the activity to a ransomware-related threat actor to establish a foothold for lateral movement.

The latest findings from Broadcom show that the malware relies on DLL side-loading techniques, using trusted Microsoft endpoint security tooling ("MpExtMs.exe") to blend in and avoid raising red flags. The backdoor runs directly in memory, enabling a wide range of capabilities typically associated with a malware family of this kind -

* Upload or download a file
* Move, rename, or delete a file
* Create a folder
* Modify the time interval after which it polls a remote server for commands
* Execute code received from C2 in memory without leaving any artifacts on disk
* Load Beacon Object Files (BOFs) to dynamically expand its capabilities
* Terminate and delete itself

"The targeting appears to be opportunistic, with the attackers casting a wide net and then assessing which organizations they could sell access to rather than focusing on a single sector," Symantec and Carbon Black said, adding that ModeloRAT has been observed in attacks that deployed Qilin ransomware.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/vpn-threat-report-m)

KongTuke is known to operate a traffic distribution system (TDS) built on compromised WordPress sites, using it to serve an ever-evolving set of lures that lead unsuspecting site visitors to malware. As recently as last month, Rapid7 and ReliaQuest [revealed](https://thehackernews.com/2026/05/threatsday-bulletin-pan-os-rce-mythos.html#teams-helpdesk-lure) that the threat actor has pivoted to sending Microsoft Teams messages from a fake IT Support account to trigger an attack chain that leads to the deployment of ModeloRAT.

"The stealth of the backdoor is also notable, as is the fact that Woodgnat is also possibly behind the development of ModeloRAT, indicating a group that is quite highly skilled at the development of stealthy remote access tools," Broadcom said.

"The use of custom tools in ransomware attacks is becoming a more common phenomenon, with multiple examples of ransomware groups using custom exfiltration and other tools in recent times. Backdoor.Mistic appears to be a continuation of this trend, though it appears to be likely developed by access brokers working with ransomware affiliates rather than a ransomware group itself."

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

[ClickFix](https://thehackernews.com/search/label/ClickFix), [DLL side-loading](https://thehackernews.com/search/label/DLL%20side-loading), [Initial Access Broker](https://thehackernews.com/search/label/Initial%20Access%20Brok...
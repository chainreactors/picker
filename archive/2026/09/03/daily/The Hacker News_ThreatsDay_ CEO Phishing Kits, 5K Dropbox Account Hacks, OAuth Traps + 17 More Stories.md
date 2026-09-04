---
title: ThreatsDay: CEO Phishing Kits, 5K Dropbox Account Hacks, OAuth Traps + 17 More Stories
url: https://thehackernews.com/2026/09/threatsday-ceo-phishing-kits-5k-dropbox.html
source: The Hacker News
date: 2026-09-03
fetch_date: 2026-09-04T06:44:13.865350
---

# ThreatsDay: CEO Phishing Kits, 5K Dropbox Account Hacks, OAuth Traps + 17 More Stories

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

# [ThreatsDay: CEO Phishing Kits, 5K Dropbox Account Hacks, OAuth Traps + 17 More Stories](https://thehackernews.com/2026/09/threatsday-ceo-phishing-kits-5k-dropbox.html)

**Ravie Lakshmanan**Sep 03, 2026Hacking News / Cybersecurity News

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhUcEnh-e0_L2Oz7JQcSCFBd90F29Z7_wHbJYiWOxWeZTeLLHbRZYK6vt1PrcUOgSFei7fxLMnP2lp0QyEOW2rzfcsnBFhayNHtKLPtHJFsu55w_GxuA3XLkZf-kleynMxXjc8zELZt7FBZFdqCAtesj3Fj148fwlGitAxZxu6t1wZDb7wgZQ1MR-Vmc4FL/s1700-nu-rw-lo-l85-e365/threats-main.jpg)

The worst part is how normal these attacks look. A call from IT. A shared file. A trusted app. A simple request to click “Allow.” Why break in when someone might open the door?

That idea runs through this edition. Attackers use real tools, fake login pages, old account links, and software guides that point to unsafe downloads. One wrong letter in a web address can be enough.

There is also ransomware, stolen ID data, hidden attack servers, and weak settings that should have been fixed long ago. Here’s the full list.

**The threats change every week. Subscribe, and we’ll alert you when each new ThreatsDay Bulletin is out.**

1. Fake IT, Real Access

   [Threat Actors Impersonate IT Support](https://www.microsoft.com/en-us/security/blog/2026/09/02/impersonating-it-support-threat-actors-turn-remote-session-into-enterprise-wide-access/)

   Microsoft has warned of a human-operated intrusion campaign that leverages Microsoft Teams external collaboration to impersonate IT or help desk personnel and socially engineer users into granting an interactive remote session. "Once remote control is established via RMM tools, the threat actor uses PowerShell to download and silently install a malicious MSI package, which in turn stages a portable Node.js runtime and an obfuscated JavaScript implant that provides persistent command execution and command and control (C2)," the tech giant [said](https://www.microsoft.com/en-us/security/blog/2026/09/02/impersonating-it-support-threat-actors-turn-remote-session-into-enterprise-wide-access/). "After the implant is deployed, the threat actor performs extensive host and Active Directory reconnaissance, periodically captures screenshots of the victim's desktop, executes follow-on payloads through trusted Windows binaries, and pivots across the enterprise over Windows Remote Management (WinRM) toward high-value assets such as domain controllers." Microsoft has described the "intrusion pattern" as high-impact as it grants an external operator interactive access to internal infrastructure.
2. Teams Vishing at Scale

   [Spring Ring Abuses Microsoft Teams in Vishing Campaign](https://unit42.paloaltonetworks.com/spring-ring-voice-phishing-campaigns/)

   In more Teams-related abuse, a coordinated social engineering operation dubbed Spring Ring has been observed leveraging external Microsoft Teams accounts to masquerade as IT help desk personnel to target more than 150 employees across at least 10 companies in various industries between January and April 2026. "What seems like a benign chat is in fact a voice phishing (vishing) call, during which adversaries try to coerce victims into executing remote monitoring and management (RMM) tools or custom malware," Palo Alto Networks Unit 42 [said](https://unit42.paloaltonetworks.com/spring-ring-voice-phishing-campaigns/). "In a more advanced variant, attackers transitioned from a vishing call to a full-blown Microsoft NT LAN Manager (NTLM) relay attack aimed at an organization's domain controller (DC)." As many as 26 distinct attacker identities have been identified behind the chat and call attempts.

   [![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhLO4gyzDPIqQ6rAWdAvEqMms8pokCDarKt7RTui-viWghAeWD8rqNTHl_5vCxblSAM-WIKEQ_X-CbFyhqE5DEzKRMqL260E9GIVL6ySQmx0GbQiFa_u-9XhlJFhGJe0nuqot6PC3xQfSfNFizL7ImgfKhlXsRL0XIbs22PNaDbwWdVbggAKzQszPmMR2tu/s1700-nu-rw-lo-l85-e365/unit.png)
3. Ransomware Affiliate Playbook

   [The Gentlemen Ransomware Operation Analyzed](https://www.sophos.com/en-gb/blog/ungentlemanly-behavior-insights-into-a-ransomware-operation)

   In a new report, Sophos revealed that [The Gentlemen](https://thehackernews.com/2026/06/the-gentlemen-raas-uses-gentlekiller.html) ransomware operation, which it tracks as Gold Sherwood, has claimed a total of 683 victims by the end of July 2026. In July alone, the group is said to have added 169 victims. "The Gentlemen ransomware intrusions [...] demonstrate a repeatable affiliate playbook that combines opportunistic initial access, rapid privilege escalation, legitimate remote access mechanisms, tool staging in trusted system paths, targeted data exfiltration, aggressive defense evasion, backup disruption, and ransomware deployment," Sophos [said](https://www.sophos.com/en-gb/blog/ungentlemanly-behavior-insights-into-a-ransomware-operation). "Affiliates are operationally flexible: they use native Windows utilities, commercial and open-source tools, BYOVD-based EDR killers, and backup service tampering to adapt to victims’ environments and maximize impact before encryption."
4. PhaaS Survives Takedown

   [Outsider Resurfaces Despite Law Enforcement Action](https://www.group-ib.com/blog/chenlun-outsider-phaas-kit/)

   The [Outsider](https://thehackernews.com/2026/06/google-sues-chinese-smishing-network.html) phishing-as-a-service (PaaS) platform has continued to be a resilient threat in the face of law enforcement action that took down a number of domains related to the service. The kit is operated by a threat actor known as "ChenLun." Group-IB [said](https://www.group-ib.com/blog/chenlun-outsider-phaas-kit/) it has identified over 700 new phishing pages created using the kit within a month after Google filed a civil lawsuit against its operators, indicating that affiliates are continuing to use the service. The campaigns are delivered via SMS. "What was once a technically d...
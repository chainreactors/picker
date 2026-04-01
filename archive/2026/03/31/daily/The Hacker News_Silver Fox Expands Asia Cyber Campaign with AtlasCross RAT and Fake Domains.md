---
title: Silver Fox Expands Asia Cyber Campaign with AtlasCross RAT and Fake Domains
url: https://thehackernews.com/2026/03/silver-fox-expands-asia-cyber-campaign.html
source: The Hacker News
date: 2026-03-31
fetch_date: 2026-04-01T04:47:53.359465
---

# Silver Fox Expands Asia Cyber Campaign with AtlasCross RAT and Fake Domains

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

# [Silver Fox Expands Asia Cyber Campaign with AtlasCross RAT and Fake Domains](https://thehackernews.com/2026/03/silver-fox-expands-asia-cyber-campaign.html)

**Ravie Lakshmanan**Mar 31, 2026Malware / Encryption

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhgQmoJ2iwUTLR-DicdD0xa7_oYXgpGalL3L_-4LyX9YMApiotQC-omFlhdcQByUQat1YJdd7ElMqhp8FDYpoaljcvVmCFPXS4yRRh0_KnKa6FgqoEpiaKHJhoecKKap1MgoPWw1a6H7LfJrYo9m_YXqh3BaoES1tPEmuCbgO3snV34jtkrK7j8t4Qk30jj/s1700-e365/cyberattacks-asia.jpg)

Chinese-speaking users are the target of an active campaign that uses typosquatted domains impersonating trusted software brands to deliver a previously undocumented remote access trojan named **AtlasCross RAT**.

"The operation covers VPN clients, encrypted messengers, video conferencing tools, cryptocurrency trackers, and e-commerce applications, with eleven confirmed delivery domains impersonating brands including Surfshark VPN, Signal, Telegram, Zoom, Microsoft Teams, and others," Germany-based cybersecurity company Hexastrike [said](https://hexastrike.com/resources/blog/threat-intelligence/trust-the-tunnel-get-the-trojan-silver-fox-delivers-atlascross-rat-via-weaponized-vpn-installers/) in a report published last week.

The activity has been attributed to a Chinese cybercrime group called [Silver Fox](https://thehackernews.com/2025/12/silver-fox-targets-indian-users-with.html), which is also tracked as SwimSnake, The Great Thief of Valley (or Valley Thief), UTG-Q-1000, and Void Arachne.

The discovery of AtlasCross RAT represents an evolution of the threat actor's arsenal from Gh0st RAT derivatives like ValleyRAT (aka Winos 4.0), Gh0stCringe, and HoldingHands RAT (aka Gh0stBins).

The attack chains involve using bogus websites as lures to trick users into downloading ZIP archives containing an installer that drops a trojanized Autodesk binary along with the legitimate decoy application.

The trojanized AutoDesk installer, in turn, launches a shellcode loader that decrypts an embedded Gh0st RAT configuration to extract the command-and-control (C2) details and then downloads a second-stage shellcode payload from "bifa668[.]com" over TCP on port 9899, ultimately leading to the execution of AtlasCross RAT in memory.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/not-fast-enough-d)

The majority of fake websites were registered in a single day on October 27, 2025, indicating a deliberate approach behind the campaign. The list of confirmed malware delivery domains is listed below -

* app-zoom.com (Zoom)
* eyy-eyy.com (unknown)
* kefubao-pc.com (KeFuBao, a Chinese customer service software for e-commerce)
* quickq-quickq.com (QuickQ VPN)
* signal-signal.com (Signal)
* telegrtam.com.cn (Telegram)
* trezor-trezor.com (Trezor)
* ultraviewer-cn.com (UltraViewer)
* wwtalk-app.com (WangWang)
* www-surfshark.com (Surfshark VPN)
* www-teams.com (Microsoft Teams)

All identified installer packages have been found to carry the same stolen Extended Validation code-signing certificate issued to DUC FABULOUS CO.,LTD, a Vietnamese entity registered in Hanoi. The fact that the same certificate has been [used](https://www.elastic.co/guide/en/security/8.19/prebuilt-rule-8-19-1-first-time-seen-commonly-abused-remote-access-tool-execution.html) in other unrelated malware campaigns has raised the possibility of widespread reuse within the cybercriminal ecosystem to lend malicious payloads a veneer of legitimacy and bypass security checks.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjALoDsXqj6_iytDdB9q6calZ7q0LogXTXeQqQtj4LViMHBIsezGtPmEkadT2Dn4NNKkFZ86VZ4k9QYcMktvXkWcBJ7iJ1XpSGBIxBx5wSwJ13g_4DCsXQChOfrqOx_WY2Gwao0erjafU3sZxTMqgD_2VZMwdrQ_oUeSMhcHbri0BLwaaxGQIjaKWLV1Gkq/s1700-e365/victim.png)

"The RAT embeds the PowerChell framework, a native C/C++ PowerShell execution engine that hosts the .NET CLR directly within the malware process and disables AMSI, ETW, Constrained Language Mode, and ScriptBlock logging before executing any commands," Hexastrike said. "C2 traffic is encrypted with ChaCha20 using per-packet random keys generated via hardware RNG."

AtlasCross RAT comes with capabilities to facilitate targeted DLL injection into WeChat, RDP session hijacking, active TCP-level termination of connections from Chinese security products (e.g., 360 Safe, Huorong, Kingsoft, and QQ PC Manager) instead of using the Bring Your Own Vulnerable Driver ([BYOVD](https://thehackernews.com/2025/09/silver-fox-exploits-microsoft-signed.html)) technique, file and shell operations, and persistent scheduled task creation.

"The AtlasAgent/AtlasCross RAT represents the current evolution of the group’s tooling, building on Gh0st RAT protocol foundations consistent with the ValleyRAT and Winos 4.0 lineage," the company added. "The addition of the PowerChell framework and a comprehensive security bypass chain marks a significant capability upgrade."

In a report published earlier this month, Chinese security vendor Knownsec 404 characterized Silver Fox as one of the "most active cyber threats" in recent years, targeting managerial and finance staff in organizations via WeChat, QQ, phishing emails, and fake tool sites to infect them with malware to enable remote control, data theft, and financial fraud.

"Silver Fox's domain strategy hinges on highly mimicking official domains combined with regional labeling to suppress user suspicion," the company [said](https://medium.com/%40knownsec404team/unmasking-silverfoxs-new-trends-decoding-evasion-tactics-domain-impersonation-and-8a7f03571186). "Operators use a multi-pronged approach – typo-squatting, domain hijacking, and DNS manipulation – to create a façade of legitimacy."

Recent attack campaigns have also been observed transitioning from ValleyRAT delivered via malicious PDF attachments in phishing emails targeting Taiwanese organizations to abusing a legitimate but misconfigured C...
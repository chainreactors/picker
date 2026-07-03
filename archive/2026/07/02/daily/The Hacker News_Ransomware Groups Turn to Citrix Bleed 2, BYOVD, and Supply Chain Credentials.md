---
title: Ransomware Groups Turn to Citrix Bleed 2, BYOVD, and Supply Chain Credentials
url: https://thehackernews.com/2026/07/ransomware-groups-turn-to-citrix-bleed.html
source: The Hacker News
date: 2026-07-02
fetch_date: 2026-07-03T05:48:49.218466
---

# Ransomware Groups Turn to Citrix Bleed 2, BYOVD, and Supply Chain Credentials

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgrKWHErc__Wn0forfQ5eJ5sIR1hVKCHCTeNQOaAX4lbygJ8S1Xpemx6JXl78dpwiT65DDBGURp48A3EemKzmli-jXPI3v1928MnJm-1j2ZPUaFXCvuySFhyphenhyphenKR-Li6fAinFT2bhLgsqUSNUR_ggMAnOHi3jD1qYWHXvueX8WdtxAd6GYety9cBGYABo18hX/s728-e100/tt-d.jpg)](https://thehackernews.uk/ai-zero-trust-h-d)

# [Ransomware Groups Turn to Citrix Bleed 2, BYOVD, and Supply Chain Credentials](https://thehackernews.com/2026/07/ransomware-groups-turn-to-citrix-bleed.html)

**Ravie Lakshmanan**Jul 02, 2026Malware / Cyber Attack

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh5gkjf1FwB4__nC6-pLZYnDv2rJA29UAL9mxfCv4BNSl1FxNpat9jD-OiMRLewjXJXyiSGvqiLYcewN_b1lLFHh0FhzKkrHFzu82jziSuOodYX87FkwjuCcXaqwzWRsiFdsBcd9mzDnak1rJpDu46F8TV206IEcD1pE7njojB8TcQEZ4Wa70KnK2vyeVKI/s1700-e365/ransomwares.jpg)

Threat actors associated with the **Anubis** ransomware operation have been observed exploiting the [Citrix Bleed 2](https://thehackernews.com/2025/07/cisa-adds-citrix-netscaler-cve-2025.html) (CVE-2025-5777) vulnerability to obtain initial access.

"Although tactics differ between affiliates, common patterns emerged in tradecraft through use of legitimate Remote Management and Monitoring (RMM) tooling, credential access, and hands-on-keyboard procedures used for lateral movement," Arctic Wolf [said](https://arcticwolf.com/resources/blog/citrixbleed-2-to-cloudflared-the-tools-and-techniques-behind-anubis-ransomware-attacks/) in a report published this week.

"Anubis affiliates repeatedly abused legitimate remote access and administration tools, including ScreenConnect, Zoho Assist, MeshAgent, Remotely, UltraVNC, and Total Software Deployment, to blend in with normal IT activity while maintaining control of victim systems."

Anubis is a ransomware-as-a-service (RaaS) group that first emerged in late 2024 as a rebrand of Sphinx ransomware. The ransomware operation was formally announced on the Ransomware and Advanced Malware Protection (RAMP) underground forum in February 2025. According to [data](https://ransomware.live/group/anubis) from Ransomware.Live, the cybercrime crew has claimed 91 victims on its data leak site, with 11 victims reported in June 2026 alone.

Some of the prominent sectors targeted include healthcare, business services, manufacturing, technology, and financial services. More than 50% of the victims are located in the U.S., followed by the U.K., Australia, France, and Canada.

In a report published in July 2025, Rubrik Zero Labs said Anubis advertises attractive profit splits, offering affiliates 80% of the ransom amounts paid, and pairs it with an irreversible data-wiping feature that ups the pressure on victims to pay up.

"When Anubis's /WIPEMODE module is activated, files remain in directories but are reduced to a 0 KB size regardless of ransom payment," Rubrik [noted](https://zerolabs.rubrik.com/blog/anubis-ransomware-stresses-need-advanced-data-backup) at the time. "Knowing threat actors can revert victims' environments to this scorched-earth state with a single command significantly increases pressure on victims to pay before the wiper is fully activated."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-vuln-protection-d)

The ransomware intrusions, observed this year, involve both valid VPN credential use and the exploitation of CVE-2025-5777 (CVSS score: 9.3), a critical flaw impacting Citrix NetScaler ADC and Gateway that could be abused by an attacker to bypass authentication when the appliance is configured as a Gateway or AAA virtual server.

The exact source of VPN credentials used in these intrusions is unknown. However, it's possible they were procured following prior compromise, or through initial access brokers (IABs), credential stuffing, or information stealer activity.

"In addition to CitrixBleed 2 exploitation, valid Cisco AnyConnect VPN logins were observed from several hosting ASNs, including AS20473 — The Constant Company and AS55286 — ServerMania," Arctic Wolf explained. "Malicious VPN authentication was then followed by login activity involving RDP and SMB, leading to credential access, PsExec service creation, RMM deployment, and ultimately invoking cloud-transfer tooling for exfiltration."

Lateral movement is facilitated via RDP and PsExec, which then leads to the deployment of various legitimate RMM tools for persistent access, granting the attackers the ability to transfer files and remotely execute code, while staying under the radar. Select intrusions also configure a Cloudflare Tunnel (aka cloudflared) to establish tunnels to victim environments.

The next phase of the attacks involves gathering credentials to facilitate deeper access to the compromised environment, after which tools like S3 Browser, rclone, s5cmd, WinSCP, and PuTTY are installed for data transfer or exfiltration prior to ransomware deployment. In parallel, steps are taken to impair system defenses and complicate post-incident analysis.

"These techniques included Windows Defender real-time protection disablement, SophosUninstall activity, PCHunter-related artifacts, and log clearing or manipulation across multiple systems," the cybersecurity company explained. "In at least one intrusion, an Anubis encryptor was deleted after execution, reducing the availability of on-disk payload artifacts for later analysis."

### The Gentlemen's Go Backdoor and BYOVD 0-Day Exploit

The disclosure comes as Kaspersky detailed **[The Gentlemen](https://zerolabs.rubrik.com/blog/under-hood-deconstructing-gentlemen-esxi-ransomware)** RaaS group's exploitation of known vulnerabilities and stolen or weak login credentials to breach targets and its use of a Go-based backdoor to enable remote command execution after reconnaissance, lateral movement through Group Policy or PsExec, and defense evasion using the bring your own vulnerable driver (BYOVD) technique.

The implant is designed to collect system information, exfiltrate it to an external server ("81.177.215[.]15:9443") over a bidirectional TCP connection, and await operator responses that are then executed on the host using "cmd.exe" if the response byte is "c." If the byte is "s," a SOCKS proxy connection is established.

"This functionality likely enables The Gentlemen's red team to pivot within ...
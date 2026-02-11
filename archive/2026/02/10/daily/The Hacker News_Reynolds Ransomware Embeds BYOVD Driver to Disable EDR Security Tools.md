---
title: Reynolds Ransomware Embeds BYOVD Driver to Disable EDR Security Tools
url: https://thehackernews.com/2026/02/reynolds-ransomware-embeds-byovd-driver.html
source: The Hacker News
date: 2026-02-10
fetch_date: 2026-02-11T04:24:30.867975
---

# Reynolds Ransomware Embeds BYOVD Driver to Disable EDR Security Tools

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

[![Security Service Edge](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg5Ij_-TeqFMEsRFzgRRFzSRlVK6oHCncN_eJ2fkOdsA_1tN9HQbAlEEife2Z2JUt1lPv4st5n9KZP84jGEYY9Up6BQ7QE-N5rs6OhzL5thxGzVxnMx3JH9cGRLi9S5Kl-iV5PgjBeTdkBLnv_inF8UUAo88iqdmgJuPIc_6qiPyUMXwFyZWbZvkZkcRXSw/s728-e100/gartner-d.jpg)](https://thehackernews.uk/sse-awards-insight-d)

# [Reynolds Ransomware Embeds BYOVD Driver to Disable EDR Security Tools](https://thehackernews.com/2026/02/reynolds-ransomware-embeds-byovd-driver.html)

**Ravie Lakshmanan**Feb 10, 2026Malware / Endpoint Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjqTeSYoXhnTy-zKDDdC_mNC4M0z32QT7sAvTipDACRrlUcGRFE2rWJ3wGacGPtT8n9evbDa7H2cL0GRj8ABmUgdMvaS9UBi8fhZMkvoXV8BhfCGYeCMvmReDOgrTzB6hVf0dEZ6V_cA9wDhkwzDFdqhBtMOtibNJsge2YkohfspG3Z-y45_ysTjatb2M6F/s1700-e365/edr.jpg)

Cybersecurity researchers have disclosed details of an emergent ransomware family dubbed **Reynolds** that comes embedded with a built-in bring your own vulnerable driver (BYOVD) component for defense evasion purposes within the ransomware payload itself.

BYOVD refers to an [adversarial technique](https://www.halcyon.ai/blog/understanding-byovd-attacks-and-mitigation-strategies) that abuses legitimate but flawed driver software to escalate privileges and disable Endpoint Detection and Response (EDR) solutions so that malicious activities go unnoticed. The strategy has been [adopted](https://thehackernews.com/2024/01/kasseika-ransomware-using-byovd-trick.html) by [many ransomware groups](https://thehackernews.com/2026/01/new-osiris-ransomware-emerges-as-new.html) over the years.

"Normally, the BYOVD defense evasion component of an attack would involve a distinct tool that would be deployed on the system prior to the ransomware payload in order to disable security software," the Symantec and Carbon Black Threat Hunter Team [said](https://www.security.com/threat-intelligence/black-basta-ransomware-byovd) in a report shared with The Hacker News. "However, in this attack, the vulnerable driver (an NsecSoft NSecKrnl driver) was bundled with the ransomware itself."

Broadcom's cybersecurity teams noted that this tactic of bundling a defense evasion component within the ransomware payload is not novel, and that it has been observed in a [Ryuk ransomware attack in 2020](https://www.fortinet.com/blog/threat-research/ryuk-revisited-analysis-of-recent-ryuk-attack) and in an incident involving a lesser-known ransomware family called [Obscura](https://thehackernews.com/2025/09/weekly-recap-drift-breach-chaos-zero.html#:~:text=New%20Ransomware%20Strains%20Detailed) in late August 2025.

In the Reynolds campaign, the ransomware is designed to drop a vulnerable NsecSoft NSecKrnl driver and terminate processes associated with various security programs from Avast, CrowdStrike Falcon, Palo Alto Networks Cortex XDR, Sophos (along with HitmanPro.Alert), and Symantec Endpoint Protection, among others.

It's worth noting that the NSecKrnl driver is susceptible to a known security flaw ([CVE-2025-68947](https://nvd.nist.gov/vuln/detail/CVE-2025-68947), CVSS score: 5.7) that could be exploited to terminate arbitrary processes. Notably, the driver has been [put to use](https://hexastrike.com/resources/blog/threat-intelligence/valleyrat-exploiting-byovd-to-kill-endpoint-security/) by a threat actor known as Silver Fox in attacks designed to kill endpoint security tools prior to delivering [ValleyRAT](https://www.cybereason.com/blog/fake-installer-valleyrat).

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/sse-customer-awards-d)

Over the past year, the hacking group has previously wielded multiple legitimate but flawed drivers – including [truesight.sys](https://thehackernews.com/2025/02/2500-truesightsys-driver-variants.html) and [amsdk.sys](https://thehackernews.com/2025/09/silver-fox-exploits-microsoft-signed.html) – as part of BYOVD attacks to disarm security programs.

By bringing together defense evasion and ransomware capabilities into one component, it makes it harder for defenders to stop the attack, not to mention obviating the need for an affiliate to separately incorporate this step into their modus operandi.

"Also of note in this attack campaign was the presence of a suspicious side-loaded loader on the target's network several weeks prior to the ransomware being deployed," Symantec and Carbon Black said. "Also of note in this attack campaign was the presence of a suspicious side-loaded loader on the target's network several weeks prior to the ransomware being deployed."

Another tool deployed on the target network a day after the ransomware deployment was the GotoHTTP remote access program, indicating that the attackers may be looking to maintain persistent access to the compromised hosts.

"BYOVD is popular with attackers due to its effectiveness and reliance on legitimate, signed files, which are less likely to raise red flags," the company said.

"The advantages of wrapping the defense evasion capability in with the ransomware payload, and the reason ransomware actors might do this, may include the fact that packaging the defense evasion binary and the ransomware payload together is “quieter”, with no separate external file dropped on the victim network."

The finding coincides with various ransomware-related developments in recent weeks -

* A [high-volume phishing campaign](https://www.forcepoint.com/blog/x-labs/phorpiex-global-group-ransomware-lnk-phishing) has used emails with Windows shortcut (LNK) attachments to run PowerShell code that fetches a [Phorpiex](https://thehackernews.com/2024/05/ongoing-campaign-bombarded-enterprises.html) dropper, which is then used to deliver the [GLOBAL GROUP](https://thehackernews.com/2025/07/newly-emerged-global-group-raas-expands.html) ransomware. The ransomware is notable for carrying out all activity locally on the compromised system, making it compatible with air‑gapped environments. It also conducts no data exfiltration.
* Attacks mounted by [WantToCry](https://www.seqrite.com/blog/wanttocry-ransomware-smb-vulnerability/) have [abused](https://www.sophos.com/en-us/blog/malicious-use-of-virtual-machine-infrastructure) virtual machines (VMs) provisioned by ISPsystem, a legitimate virtual infrastructure management provider, to host and deliver malicious payloads at scale. Some ...
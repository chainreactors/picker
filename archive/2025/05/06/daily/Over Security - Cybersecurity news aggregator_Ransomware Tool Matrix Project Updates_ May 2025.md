---
title: Ransomware Tool Matrix Project Updates: May 2025
url: https://blog.bushidotoken.net/2025/05/ransomware-tool-matrix-project-updates.html
source: Over Security - Cybersecurity news aggregator
date: 2025-05-06
fetch_date: 2025-10-06T22:29:40.115973
---

# Ransomware Tool Matrix Project Updates: May 2025

[Skip to main content](#main)

### Search This Blog

# [@BushidoToken Threat Intel](https://blog.bushidotoken.net/)

### Ransomware Tool Matrix Project Updates: May 2025

* Get link
* Facebook
* X
* Pinterest
* Email
* Other Apps

-
[May 05, 2025](https://blog.bushidotoken.net/2025/05/ransomware-tool-matrix-project-updates.html "permanent link")

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi_BpTZksj9aZ67Y0MoiVTbyhuF2ZNK6mjoCeIlkF5MIjc7DlouoqPLYd-7XXsHgxT6Vytvvo-gY5b8JO3Ujab_8XLnSo1LbYrBUW78GrP2U8wx3ZT-B2ZwMGLO2aVCovVuIX3qZWYIN3X-GCw470E7tr2aiI0CPIgi9bkXbvDldhDL1hNZEc48rVTPyvxY/s320/OIG2.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi_BpTZksj9aZ67Y0MoiVTbyhuF2ZNK6mjoCeIlkF5MIjc7DlouoqPLYd-7XXsHgxT6Vytvvo-gY5b8JO3Ujab_8XLnSo1LbYrBUW78GrP2U8wx3ZT-B2ZwMGLO2aVCovVuIX3qZWYIN3X-GCw470E7tr2aiI0CPIgi9bkXbvDldhDL1hNZEc48rVTPyvxY/s1024/OIG2.jpg)

**Introduction**

This blog is a summary and analysis of recent additions to
the [Ransomware
Tool Matrix (RTM)](https://github.com/BushidoUK/Ransomware-Tool-Matrix) as well as the [Ransomware
Vulnerability Matrix (RVM)](https://github.com/BushidoUK/Ransomware-Vulnerability-Matrix). Feedback from the infosec community about these projects has
been overwhelmingly positive and many researchers have contacted me to tell me
how helpful they have found these to be. It makes me happy to hear how doing something in my spare
time can help stop ransomware attacks and cybercriminals from exploiting our
society’s systems. And it is for that reason, I shall continue to maintain
these projects as long as ransomware is still around. For anyone new to these projects, please read the
descriptions on GitHub or feel free to watch my talk explaining the project at [BSides London](https://www.youtube.com/watch?v=hyoOhAoaX1g).

**Background on the current ransomware ecosystem as of May
2025**

Following the impact of Operation Cronos against LockBit and
the exit scam by ALPHV/BlackCat, the ransomware ecosystem has been even more unstable
than usual. The exit scams and law enforcement infiltration operations
have created a zero trust environment for the cybercriminals participating in
the ransomware economy. The days of affiliates putting their faith in one RaaS
platform seem to be long gone and many are experimenting and going from one
RaaS to the next.

## Sources of Threat Intelligence for the RTM

The RTM was updated with OSINT reports shared by
cybersecurity researchers at various private service providers or vendors. The
thing to remember about these reports is that the tool usage is going to be
slightly outdated due to the time it takes incident response teams to wrap up
an investigation, compile findings, and publish a report.

From the reports, threat groups such as Qilin, BlackSuit,
RansomEXX, Medusa, BianLian, Hunters International and PLAY have been active
for over one year or for multiple years. These are established groups. Since
RansomHub and LockBit have shut down, it is more likely than not that the
affiliates have already shifted to one of the other RaaS platforms, like Qilin,
among others.

There has also been a number of ransomware operations suspected
to be linked to Chinese cyber-espionage groups, such as RA World (for using PlugX),
NailaoLocker (for using ShadowPad and PlugX), and CrazyHunter (for its focus on
Taiwan).

Threat groups such as IMN Crew, QWCrypt (linked to RedCurl),
NightSpire, SuperBlack, and Helldown are all rising threat groups that have
more recently begun their ransomware campaigns.

These factors have led to seeing a large variety of tool
usage in ransomware operations being observed across the landscape. The
reliance on tools from sites like GitHub and other free software sites, however,
continues to remain a constant theme among all of these ransomware operations.

List of sources used for the May 2025 major update to the
RTM:

|  |  |  |
| --- | --- | --- |
| **Group Name** | **Report Publish Date** | **URL** |
| Qilin | 25 April 2025  10 March 2025 | [redpiranha.net](https://redpiranha.net/news/qilin-ransomware-all-you-need-know)  [picussecurity.com](https://www.picussecurity.com/resource/blog/qilin-ransomware) |
| IMN Crew | 24 April 2025 | [s-rminform.com](https://www.s-rminform.com/latest-thinking/ransomware-in-focus-meet-imn-crew) |
| CrazyHunter | 16 April 2025 | [trendmicro.com](https://www.trendmicro.com/en_us/research/25/d/crazyhunter-campaign.html) |
| RansomEXX | 8 April 2025 | [microsoft.com](https://www.microsoft.com/en-us/security/blog/2025/04/08/exploitation-of-clfs-zero-day-leads-to-ransomware-activity/) |
| BlackSuit | 31 March 2025 | [thedfirreport.com](https://thedfirreport.com/2025/03/31/fake-zoom-ends-in-blacksuit-ransomware/) |
| QWCrypt | 26 March 2025 | [bitdefender.com](https://www.bitdefender.com/en-us/blog/businessinsights/redcurl-qwcrypt-ransomware-technical-deep-dive) |
| RansomHub | 26 March 2025  20 March 2025 | [welivesecurity.com](https://www.welivesecurity.com/en/eset-research/shifting-sands-ransomhub-edrkillshifter/)  [security.com](https://www.security.com/threat-intelligence/ransomhub-betruger-backdoor) |
| Medusa | 26 March 2025  6 March 2025 | [welivesecurity.com](https://www.welivesecurity.com/en/eset-research/shifting-sands-ransomhub-edrkillshifter/)  [security.com](https://www.security.com/threat-intelligence/medusa-ransomware-attacks) |
| BianLian | 26 March 2025 | [welivesecurity.com](https://www.welivesecurity.com/en/eset-research/shifting-sands-ransomhub-edrkillshifter/) |
| PLAY | 26 March 2025 | [welivesecurity.com](https://www.welivesecurity.com/en/eset-research/shifting-sands-ransomhub-edrkillshifter/) |
| NightSpire | 25 March 2025 | [s-rminform.com](https://www.s-rminform.com/latest-thinking/ransomware-in-focus-meet-nightspire) |
| Hunters International | 19 March 2025 | [esentire.com](https://www.esentire.com/blog/from-access-to-encryption-dissecting-hunters-internationals-latest-ransomware-attack) |
| SuperBlack | 13 March 2025 | [forescout.com](https://www.forescout.com/blog/new-ransomware-operator-exploits-fortinet-vulnerability-duo/) |
| LockBit | 24 February 2025 | [thedfirreport.com](https://thedfirreport.com/2025/02/24/confluence-exploit-leads-to-lockbit-ransomware/) |
| NailaoLocker | 20 February 2025  18 February 2025 | [orangecyberdefense.com](https://www.orangecyberdefense.com/global/blog/cert-news/meet-nailaolocker-a-ransomware-distributed-in-europe-by-shadowpad-and-plugx-backdoors)  [trendmicro.com](https://www.trendmicro.com/en_us/research/25/b/updated-shadowpad-malware-leads-to-ransomware-deployment.html) |
| RA World | 13 February 2025  22 July 2024 | [security.com](https://www.security.com/threat-intelligence/chinese-espionage-ransomware)  [unit42.paloaltonetworks.com](https://unit42.paloaltonetworks.com/ra-world-ransomware-group-updates-tool-set/) |
| Helldown | 7 November 2024 | [truesec.com](https://www.truesec.com/hub/blog/helldown-ransomware-group) |

## Tools Used by Multiple Groups

* EDRSandBlast and WKTools are relatively new tools that are
  being used by multiple groups to deactivate and overcome EDR tools that many victims
  will have on their networks to prevent ransomware attacks.
* Typical ransomware tools, such as PsExec, Mimikatz, and
  Rclone remain effective and still used by multiple ransomware gangs for the
  foreseeable future.

|  |  |  |
| --- | --- | --- |
| **Tool** | **Type** | **Groups Using It** |
| WinSCP | Exfiltration | NightSpire  Hunters International |
| Mimikatz | Credential Theft | RansomHub  Qilin  Helldown |
| Impacket | Offensive Security Tool | RansomHub  RA World  NailaoLocker |
| Rclone | Exfiltration | RansomHub  Hunters International Medusa |
| NetScan | Discovery | RansomHub  Medusa |
| WKTools | Discovery | RansomHub  BianLian  PLAY |
| Advanced IP Scanner | Discovery | Hunters International BianLian |
| Advanced Port Scanner | Discovery | Hunters International Helldown |
| AnyDesk | RMM Tool | Medusa  BianLian |
| EDRSandBlast | Defense Eva...
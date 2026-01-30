---
title: Dissecting UAT-8099: New persistence mechanisms and regional focus
url: https://blog.talosintelligence.com/uat-8099-new-persistence-mechanisms-and-regional-focus/
source: Over Security - Cybersecurity news aggregator
date: 2026-01-29
fetch_date: 2026-01-30T04:04:03.902445
---

# Dissecting UAT-8099: New persistence mechanisms and regional focus

[Blog](/)

[ ]

* [Intelligence Center](https://talosintelligence.com/reputation)

  [ ]

  + [# Intelligence Center](https://talosintelligence.com/reputation)
  + BACK
  + [Intelligence Search](https://talosintelligence.com/reputation_center)
  + [Email & Spam Trends](https://talosintelligence.com/reputation_center/email_rep)
* [Vulnerability Research](https://talosintelligence.com/vulnerability_info)

  [ ]

  + [# Vulnerability Research](https://talosintelligence.com/vulnerability_info)
  + BACK
  + [Vulnerability Reports](https://talosintelligence.com/vulnerability_reports)
  + [Microsoft Advisories](https://talosintelligence.com/ms_advisories)
* [Incident Response](https://talosintelligence.com/incident_response)

  [ ]

  + [# Incident Response](/incident_response)
  + BACK
  + [Reactive Services](https://talosintelligence.com/incident_response/services#reactive-services)
  + [Proactive Services](https://talosintelligence.com/incident_response/services#proactive-services)
  + [Emergency Support](https://talosintelligence.com/incident_response/contact)
* [Blog](https://blog.talosintelligence.com)
* [Support](https://support.talosintelligence.com)

More

* Security Resources

  [ ]

  # Security Resources

  + BACK

  Security Resources
  + [Open Source Security Tools](https://talosintelligence.com/software)
  + [Intelligence Categories Reference](https://talosintelligence.com/categories)
  + [Secure Endpoint Naming Reference](https://talosintelligence.com/secure-endpoint-naming)
* Media

  [ ]

  # Media

  + BACK

  Media
  + [Talos Intelligence Blog](https://blog.talosintelligence.com)
  + [Threat Source Newsletter](https://blog.talosintelligence.com/category/threat-source-newsletter/)
  + [Beers with Talos Podcast](https://talosintelligence.com/podcasts/shows/beers_with_talos)
  + [Talos Takes Podcast](https://talosintelligence.com/podcasts/shows/talos_takes)
  + [Talos Videos](https://www.youtube.com/channel/UCPZ1DtzQkStYBSG3GTNoyfg/featured)
* Company

  [ ]

  # Company

  + BACK

  Company
  + [About Talos](https://talosintelligence.com/about)
  + [Careers](https://talosintelligence.com/careers)

![](/content/images/2026/01/UAT-8099_Header.jpg)

# Dissecting UAT-8099: New persistence mechanisms and regional focus

By
[Joey Chen](https://blog.talosintelligence.com/author/joey/)

Thursday, January 29, 2026 06:00

* Cisco Talos has identified a new campaign by UAT-8099, active from late 2025 to early 2026, that is targeting vulnerable Internet Information Services (IIS) servers across Asia with a specific focus on victims in Thailand and Vietnam.
* Analysis confirms significant operational overlaps between this activity and the [WEBJACK](https://labs.withsecure.com/publications/webjack) campaign. This includes critical indicators of compromise including malware hashes, command and control (C2), and victimology.
* UAT-8099 uses web shells and PowerShell to execute scripts and deploy the GotoHTTP tool, granting the threat actor remote access to vulnerable IIS servers.
* New variants of BadIIS now hardcode the target region directly into the malware, offering customized features for each specific variant. These customizations include exclusive file extensions, corresponding dynamic page extensions, directory indexing configurations, and the ability to load HTML templates from local files.
* A Linux Executable and Linkable Format (ELF) variant of BadIIS was uploaded to VirusTotal on Oct. 1, 2025. The malware includes proxy mode, injector mode, and search engine optimization (SEO) fraud mode, similar to what Talos described in the [previous UAT-8099 blog](https://blog.talosintelligence.com/uat-8099-chinese-speaking-cybercrime-group-seo-fraud/).

---

## UAT-8099 new activity

Cisco Talos observed new activity from [UAT-8099](https://blog.talosintelligence.com/uat-8099-chinese-speaking-cybercrime-group-seo-fraud/) spanning from August 2025 through early 2026. Analysis of Cisco's file census and DNS traffic indicates that compromised IIS servers are located across India, Pakistan, Thailand, Vietnam, and Japan, with a distinct concentration of attacks in Thailand and Vietnam. Furthermore, this activity significantly overlaps with the [WEBJACK](https://labs.withsecure.com/publications/webjack) campaign; we have identified high-confidence correlations across malware hashes, C2 infrastructure, victimology, and the promoted gambling sites.

![](https://blog.talosintelligence.com/content/images/2026/01/Figure-1.png)

Figure 1. Content for crawlers.

While the threat actor continues to rely on web shells, SoftEther VPN, and EasyTier to control compromised IIS servers, their operational strategy has evolved significantly. First, this latest campaign marks a shift in their black hat SEO tactics toward a more specific regional focus. Second, the actor increasingly leverages red team utilities and legitimate tools to evade detection and maintain long-term persistence.

### Infection chain

Upon gaining initial access, the threat actor executes standard reconnaissance commands, such as `whoami` and `tasklist`, to gather system information. Following this, they deploy VPN tools and establish persistence by creating a hidden user account named “admin$”. UAT-8099 has further expanded their arsenal with the several new tools below:

* Sharp4RemoveLog: A .NET utility designed to clear all Windows event logs, effectively erasing forensic traces
* [CnCrypt Protect](https://www.52pojie.cn/thread-1397484-1-1.html): A Chinese-language file-protection utility. In this intrusion activity, it is abused to hide malicious files and facilitate dynamic-link library (DLL) redirection. This tool has been linked to previous IIS attacks since 2024, including SEO fraud campaigns targeting [Vietnam](https://sec.vnpt.vn/2024/09/part-2-hacker-thuc-hien-black-hat-seo-cac-trang-web-bat-hop-phap-bang-tan-cong-redirect-nhu-the-nao) and [China](https://mp.weixin.qq.com/s/TCrtN94jIMg7PLpfGquAYw), as well as the [WEBJACK](https://labs.withsecure.com/publications/webjack) campaign.
* [OpenArk64](https://github.com/c1earyy/OpenArk64): An open source anti-rootkit. The threat actor uses its kernel-level access to terminate security product processes that are otherwise protected from deletion.
* [GotoHTTP](https://gotohttp.com/): An online remote control tool. The threat actor uses VBscript to deploy this tool and let them remote control the compromised server. Talos provides more detail in the following section.

Subsequently, the threat actor deploys two archive files containing the latest version of the BadIIS malware. Notably, the file names of these archives are correlated with the specific geographic regions targeted by the BadIIS malware; for example, “VN” denotes Vietnam and “TH” denotes Thailand.

```
C:/Users/admin$/Desktop/TH.zip
C:/Users/admin$/Desktop/VN.zip
```

 Following the publication of our [previous research](https://blog.talosintelligence.com/uat-8099-chinese-speaking-cybercrime-group-seo-fraud/), Cisco Security products have widely flagged the “admin$” account name. In response, if this name is blocked, the threat actor  creates a new user account named “mysql$” to maintain access and sustain the BadIIS SEO fraud service.

![](https://blog.talosintelligence.com/content/images/2026/01/Figure-2..png)

Figure 2. New user account named “mysql$”.

Using the newly created account, the threat actor redeploys the updated BadIIS malware to the compromised machines. Notably, this marks a strategic shift from broad, global targeting to specific regional focus. This is evidencedby the directory naming conventions for the malware and its scripts, which use identifiers such as “VN” for Vietnam and “newth” for Thailand.

```
C:/Users/mssql$/Desktop/VN/fasthttp.dll
C:/Users/mssql$/Desktop/VN/cgihttp.dll
C:/Users/mssql$/Desktop/VN/install.bat
C:/Users/mssql$/Desktop/VN/uninstall.bat
C:/Users/mssql$/Desktop/newth/iis32.dll
C:/Users/mssql$/Desktop/newth/iis64.dll
C:/Users/mssql$/Desktop/newt...
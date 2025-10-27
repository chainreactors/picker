---
title: APT41 likely compromised Taiwanese government-affiliated research institute with ShadowPad and Cobalt Strike
url: https://blog.talosintelligence.com/chinese-hacking-group-apt41-compromised-taiwanese-government-affiliated-research-institute-with-shadowpad-and-cobaltstrike-2/
source: Over Security - Cybersecurity news aggregator
date: 2024-08-02
fetch_date: 2025-10-06T18:04:49.271531
---

# APT41 likely compromised Taiwanese government-affiliated research institute with ShadowPad and Cobalt Strike

# Cisco Talos Blog

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

![](/content/images/2024/08/threat-spotlight.webp)

# APT41 likely compromised Taiwanese government-affiliated research institute with ShadowPad and Cobalt Strike

By
[Joey Chen](https://blog.talosintelligence.com/author/joey/),
[Ashley Shen](https://blog.talosintelligence.com/author/ashley/),
[Vitor Ventura](https://blog.talosintelligence.com/author/vitor-ventura/)

Thursday, August 1, 2024 08:00

[Threat Spotlight](/category/threat-spotlight/)
[APT](/category/apt/)
[RAT](/category/rat/)

* Cisco Talos discovered a malicious campaign that compromised a Taiwanese government-affiliated research institute that started as early as July 2023, delivering the ShadowPad malware, Cobalt Strike and other customized tools for post-compromise activities.
* The activity conducted on the victim endpoint matches the hacking group [APT41](https://www.fbi.gov/wanted/cyber/apt-41-group), alleged by the U.S. government to be comprised of Chinese nationals. Talos assesses with medium confidence that the combined usage of malware, open-source tools and projects, procedures and post-compromise activity matches this group’s usual methods of operation.
* The ShadowPad malware used in the current campaign exploited an outdated vulnerable version of Microsoft Office IME binary as a loader to load the customized second-stage loader for launching the payload.
* We also discovered that APT41 created a tailored loader to inject a proof-of-concept for [CVE-2018-0824](https://codewhitesec.blogspot.com/2018/06/cve-2018-0624.html) directly into memory, utilizing a remote code execution vulnerability to achieve local privilege escalation.

# Taiwanese Government-Affiliated Research Institute compromised by Chinese Actor

In August 2023, Cisco Talos detected abnormal PowerShell commands connecting to an IP address to download and execute PowerShell scripts in the environment of a Taiwanese research institute. The nature of research and development work carried out by the entity makes it a valuable target for threat actors dedicated to obtaining proprietary and sensitive technologies of interest to them.

# Chinese Threat Actors likely Behind the Attacks

Cisco Talos assesses with medium confidence that this campaign is carried out by APT41, alleged by the U.S. government to be comprised of Chinese nationals. This assessment is based primarily on overlaps in tactics, techniques and procedures (TTPs), infrastructure and malware families used exclusively by Chinese APT groups. Talos’ analyses of the malware loaders used in this attack reveal that these are [ShadowPad](https://malpedia.caad.fkie.fraunhofer.de/details/win.shadowpad) loaders. However, Talos has been unable to retrieve the final ShadowPad payloads used by the attackers.

ShadowPad, widely considered the successor of PlugX, is a modular remote access trojan (RAT) only seen sold to Chinese [hacking](https://www.sentinelone.com/labs/shadowpad-a-masterpiece-of-privately-sold-malware-in-chinese-espionage/) [groups](https://www.sentinelone.com/labs/shadowpad-a-masterpiece-of-privately-sold-malware-in-chinese-espionage/). The malware was publicly reported being used by APT41, which is a hacking group believed to be based out of Chengdu, China, according to the [U.S. Department of Justice](https://www.justice.gov/opa/press-release/file/1317206/download).  Along with APT41 it has also been used by other Chinese hacking groups like Mustang Panda and the Tonto Team.

During the investigation, we observed a couple TTPs or IoC that were observed in previous reported campaigns, including the following:

* **The same second stage loader binary**: A second stage loader, that acts as a successor to the initial side-loaded ShadowPad loader, discovered by Talos was also linked to ShadowPad  and previously associated with [ShadowPad](https://www.secureworks.com/research/shadowpad-malware-analysis) publicly. We have also observed identical loading mechanisms, infection chains and file names being utilized in the current attacks with reliable previous [open-source reporting](https://www.secureworks.com/research/shadowpad-malware-analysis).
* **Infrastructure overlapping:** Beside the binary connection, we also found a C2 (103.56.114[.]69) that was reported by [Symantec](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/espionage-asia-governments). Although the campaign reportedly ran in April 2022, which is more than one year before the campaign we discovered, there were a few similarities between the TTPs observed in the two campaigns. This includes using the same ShadowPad Bitdefender loader, using similar file names for the tool, using Filezilla for moving files between endpoints and using the WebPass tool for dumping credentials.
* **The employment of Bitdefender executable for sideloading:** The malicious actor leverages Bitdefender where it uses an eleven year old executable to sideload the DLL-based ShadowPad loader. This technique has been seen in a variety of reports which have been attributed to APT41. This technique has been reported in multiple reports (Reports: [1](https://www.ptsecurity.com/ww-en/analytics/pt-esc-threat-intelligence/higaisa-or-winnti-apt-41-backdoors-old-and-new/#id6), [2](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/espionage-asia-governments), [3](https://www.elastic.co/security-labs/siestagraph-new-implant-uncovered-in-asean-member-foreign-ministry), [4](https://www.corecloud.com.tw/corecloud/pages/news/news_23.html)).

## Chinese Speaking Threat Actor

This attack saw the use of a unique Cobalt Strike loader, written in GoLang is meant to evade detection of Cobalt Strike by Windows Defender. This loader is based on an anti-AV loader named [CS-Avoid-Killing](https://github.com/Gality369/CS-Loader) hosted on GitHub and written in Simplified Chinese....
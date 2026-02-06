---
title: Knife Cutting the Edge: Disclosing a China-nexus gateway-monitoring AitM framework
url: https://blog.talosintelligence.com/knife-cutting-the-edge/
source: Over Security - Cybersecurity news aggregator
date: 2026-02-05
fetch_date: 2026-02-06T04:10:11.702746
---

# Knife Cutting the Edge: Disclosing a China-nexus gateway-monitoring AitM framework

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

![](/content/images/2026/02/DKnife-header--1-.jpg)

# Knife Cutting the Edge: Disclosing a China-nexus gateway-monitoring AitM framework

By
[Ashley Shen](https://blog.talosintelligence.com/author/ashley/)

Thursday, February 5, 2026 06:00

[Threat Spotlight](/category/threat-spotlight/)

* Cisco Talos uncovered “DKnife,” a fully featured gateway-monitoring and adversary-in-the-middle (AitM) framework comprising seven Linux-based implants that perform deep-packet inspection, manipulate traffic, and deliver malware via routers and edge devices. Based on the artifact metadata, DKnife has been used since at least 2019 and the command and control (C2) are still active as of January 2026.
* DKnife’s attacks target a wide range of devices, including PCs, mobile devices, and Internet of Things (IoT) devices. It delivers and interacts with the [ShadowPad](https://malpedia.caad.fkie.fraunhofer.de/details/win.shadowpad) and [DarkNimbus](https://www.trendmicro.com/en_us/research/24/l/earth-minotaur.html) backdoors by hijacking binary downloads and Android application updates.
* DKnife primarily targets Chinese-speaking users, indicated by credential harvesting for Chinese-language services, exfiltration modules for popular Chinese mobile applications and code references to Chinese media domains. Based on the language used in the code, configuration files and the [ShadowPad](https://blog.talosintelligence.com/chinese-hacking-group-apt41-compromised-taiwanese-government-affiliated-research-institute-with-shadowpad-and-cobaltstrike-2/) malware delivered in the campaign, we assess with high confidence that China-nexus threat actors operate this tool.
* We discovered a link between DKnife and a campaign delivering [WizardNet](https://www.welivesecurity.com/en/eset-research/thewizards-apt-group-slaac-spoofing-adversary-in-the-middle-attacks/), a modular backdoor known to be delivered by a different AiTM framework [Spellbinder](https://www.welivesecurity.com/en/eset-research/thewizards-apt-group-slaac-spoofing-adversary-in-the-middle-attacks/), suggesting a shared development or operational lineage.

---

## Background

Since 2023, Cisco Talos has continuously tracked the [MOONSHINE](https://citizenlab.ca/2019/09/poison-carp-tibetan-groups-targeted-with-1-click-mobile-exploits/) exploit kit and the [DarkNimbus](https://www.trendmicro.com/en_us/research/24/l/earth-minotaur.html) backdoor it distributes. The exploit kit and backdoor were historically used for delivering Android and iOS exploits. While hunting for DarkNimbus samples, Talos discovered an executable and linkable format (ELF) binary communicating with the same C2 server as the DarkNimbus backdoor, which retrieved a gzip-compressed archive. Analysis revealed that the archive contained a fully featured gateway monitoring and AiTM framework, dubbed “DKnife” by its developer. Based on the artifact metadata, the tool has been used since at least 2019, and the C2 is still active as of January 2026.

## Link between DKnife and WizardNet campaigns

During Talos' pivot on the C2 infrastructure associated with DKnife, we identified additional servers exhibiting open ports and configurations consistent with previously observed DKnife deployments. Notably, one host (43.132.205[.]118) displayed port activity characteristic of DKnife infrastructure and was additionally found hosting the WizardNet backdoor on port 8881.

WizardNet is a modular backdoor first [disclosed by ESET](https://www.welivesecurity.com/en/eset-research/thewizards-apt-group-slaac-spoofing-adversary-in-the-middle-attacks/) in April 2025, known to be deployed via Spellbinder, a framework that performs AitM attacks leveraging IPv6 Stateless Address Autoconfiguration (SLAAC) spoofing.

Network responses from the WizardNet server align closely with the tactics, techniques, and procedures (TTPs) documented in ESET’s analysis. Specifically, the server delivered JSON-formatted tasking instructions that included a download URL pointing to an archive named *minibrowser11\_rpl.zip*, which include the Wizardnet backdoor downloader.

```
{
  "CSoftID": 22,
  "CommandLine": "",
  "Desp": "1.1.1160.80",
  "DownloadUrl": "http://43.132.205.118:81/app/minibrowser11_rpl.zip",
  "ErrCode": 0,
  "File": "minibrowser11.zip",
  "Flags": 1,
  "Hash": "cd09f8f7ea3b57d5eb6f3f16af445454",
  "InstallType": 0,
  "NewVer": "1.1.1160.900",
  "PatchFile": "QBDeltaUpdate.exe",
  "PatchHash": "cd09f8f7ea3b57d5eb6f3f16af445454",
  "Sign": "",
  "Size": 36673429,
  "VerType": ""
}
```

Spellbinder’s TTPs, which involve hijacking legitimate application update requests and serving forged responses to redirect victims to malicious download URLs, are similar to DKnife’s method of compromising Android application updates. Spellbinder has also been observed distributing the DarkNimbus backdoor, whose C2 infrastructure previously led to the initial discovery of DKnife. The URL redirection paths (`http[:]//[IP]:81/app/[app name]`) and port configurations identified in these cases are identical to those used by DKnife, indicating a shared development or operational lineage.

## Targeting scope

Based on artifacts recovered from the DKnife framework, this campaign appears to primarily target Chinese-speaking users. Indicators supporting this assessment include data collection and processing logic explicitly designed for Chinese mail services , as well as parsing and exfiltration modules tailored for Chinese mobile applications and messaging platforms, including WeChat. In addition, code references to Chinese media domains were identified in both the binaries and configuration files. The screenshot below illustrates an Android application hijacking response that targeted a Chinese taxi service and rideshare application.

It is important to note that Talos obtained the configuration files f...
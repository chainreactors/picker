---
title: Uncovering Qilin attack methods exposed through multiple cases
url: https://blog.talosintelligence.com/uncovering-qilin-attack-methods-exposed-through-multiple-cases/
source: Over Security - Cybersecurity news aggregator
date: 2025-10-27
fetch_date: 2025-10-28T03:00:31.596919
---

# Uncovering Qilin attack methods exposed through multiple cases

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

![](/content/images/2025/10/qillin-1.jpg)

# Uncovering Qilin attack methods exposed through multiple cases

By
[Takahiro Takeda](https://blog.talosintelligence.com/author/takahiro/),
[Jordyn Dunk](https://blog.talosintelligence.com/author/jordyn/),
[James Nutland](https://blog.talosintelligence.com/author/james/),
[Michael Szeliga](https://blog.talosintelligence.com/author/michael/)

Sunday, October 26, 2025 22:00

[Threats](/category/threats/)

* In the second half of 2025, the ransomware group Qilin has continued to publish victim information on its leak site at a pace of more than 40 cases per month, making it one of the most impactful ransomware groups worldwide. The manufacturing sector has been the most affected, followed by professional and scientific services, and wholesale trade.
* Although this could be a false flag, some of the scripts used by the attacker contained character encodings that point to Eastern Europe or a Russian-speaking region.
* Talos identified an open-source tool named Cyberduck, which enables file transfers to cloud servers, among the tools used for data exfiltration. In recent trends, Cyberduck has been widely abused in cases involving Qilin ransomware. Artifact logs also show the use of notepad.exe and mspaint.exe, which were leveraged to view high-sensitivity information.
* In Qilin cases, we observed dual deployments: encryptor\_1.exe spreads via PsExec across hosts, while encryptor\_2.exe runs from one system to encrypt multiple network shares.

## Summary of Qilin Ransomware

The Qilin (formerly Agenda) ransomware group has been active since around [July 2022](https://blog.barracuda.com/2025/07/18/qilin-ransomware-growing). This group employs a double-extortion strategy, combining file encryption with the public disclosure of stolen information. Figure 1 illustrates the leak site used by the attackers to publish lists of compromised companies.

![](https://blog.talosintelligence.com/content/images/2025/10/leaksite.png)

Figure 1. Qilin ransomware leak site.

Over the past several years, Qilin has expanded its operations and now ranks among the most prolific and damaging ransomware threats on a global scale. The group adopts a Ransomware-as-a-Service (RaaS) business model, where it develops and distributes ransomware platforms and associated tools to affiliates. In turn, these affiliates attack organizations worldwide.

## Victimology and prevalence

Current reporting indicates that the countries most severely affected include the United States, followed by Canada, the United Kingdom, France, and Germany.

![](https://blog.talosintelligence.com/content/images/2025/10/Qilin_1.jpg)

Figure 2. Countries affected by Qilin ransomware.

Figure 3 illustrates the number of victims whose information was posted on Qilin ransomware leak site.

The data shows that the number of postings reached a peak of 100 cases in June 2025, with a nearly equivalent figure recorded again in August. Although the number of victims fluctuates from month to month, it is noteworthy that, except for January, every month recorded more than 40 cases. These findings indicate that Qilin continues to pose a persistent and significant threat.

![](https://blog.talosintelligence.com/content/images/2025/10/Qilin_2.jpg)

Figure 3. Number of victims listed on Qilin ransomware leak site.

The most heavily affected sector is manufacturing, which accounts for approximately 23% of all reported cases, significantly outpacing other industries. The second most impacted sector is professional and scientific services, representing around 18%. Wholesale trade ranks third, with about 10% of cases.

In the mid-range, several key sectors that form part of social infrastructure-healthcare, construction, retail, education, and finance-each report similar levels of impact, averaging around 5%.

At the lower end, sectors such as services and primary industries show relatively fewer incidents, remaining below 2% on average.

![](https://blog.talosintelligence.com/content/images/2025/10/Qilin_3.jpg)

Figure 4. Sectors experiencing damage/impact.

## Qilin ransomware attack flow

In 2025, Cisco Talos responded to multiple incidents related to Qilin ransomware. The overall attack flow is illustrated in Figure 5, and subsequent sections provide a detailed description of the tactics, techniques, and procedures (TTPs) observed in each phase.

![](https://blog.talosintelligence.com/content/images/2025/10/Qilin_4.jpg)

Figure 5. TTPs from VPN compromise to execution of Qilin ransomware.

## Latest Qilin TTPs

### Initial access

Talos was unable to definitively identify a single, confirmed initial intrusion vector. However, in some cases, we assess with moderate confidence that attackers abused administrative credentials leaked on the dark web to gain VPN access, and may have also used Group Policy (AD GPO) changes enabling RDP to reach victim networks.

In the incident illustrated in Figure 6, Talos confirmed that credentials had been exposed on the dark web. Approximately two weeks later, numerous NTLM authentication attempts were made against the VPN, possibly using the leaked credentials. The resulted in a successful intrusion. From the compromised VPN, the attackers performed RDP connections to the domain controller and the initially breached host. While the activity is temporally correlated with the previously observed credential exposure, there is insufficient evidence to establish a definitive causal link between the two events.

Notably, the VPN implicated in this case had no multi-factor authentication (MFA) configured, which would allow an attacker with credentials unfettered access.

![](https://blog.talosintelligence.com/content/images/2025/10/Qilin_6.jpg)

Figure 6. Example case of initial intrusion via VPN.

### Reconnaissance and discovery

After gai...
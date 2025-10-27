---
title: Scarcity signals: Are rare activities red flags?
url: https://blog.talosintelligence.com/scarcity-signals-are-rare-activities-red-flags/
source: Over Security - Cybersecurity news aggregator
date: 2025-05-24
fetch_date: 2025-10-06T22:29:26.882150
---

# Scarcity signals: Are rare activities red flags?

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

![](/content/images/2025/05/scarcity-signals-header.jpg)

# Scarcity signals: Are rare activities red flags?

By
[Cisco Talos](https://blog.talosintelligence.com/author/cisco/),
[Darin Smith](https://blog.talosintelligence.com/author/darin/)

Friday, May 23, 2025 06:00

[Threats](/category/threats/)

*By Darin Smith and John Arneson*

* Cisco Talos reviewed six months of network connection telemetry logs spanning June 1, 2024 – Dec. 31, 2024, containing 3,220,829 log events and 742 unique base domains, to explore if domains that PowerShell rarely contacts are more likely to be malicious.
* Key findings reveal that the odds of a rare domain being malicious were 3.18 times higher than for frequently contacted domains (95% CI: 0.39–25.9), suggesting a trend towards higher risk in rare domains.
* Notably, the non-rare domain ‘githubusercontent.com’ was flagged as malicious due to activity from its subdomain ‘raw.githubusercontent.com’. This is an example of why subdomains should be considered when looking for malicious network traffic, especially for cloud services where the service itself is legitimate, but the content hosted on it is not guaranteed to be.

---

## Research Methodology

### Hypothesis

At a sufficiently high volume of telemetry, domain names that PowerShell rarely connects to are more likely to be malicious than domains that are frequently connected to, regardless of PowerShell module.

### Data Collection

Talos queried telemetry for PowerShell network connection logs from a time period of June 1, 2024 to Dec. 31, 2024. This dataset included the following processes: ‘powershell.exe’, ‘powershell studio.exe’, ‘powershell\_ise.exe’, ‘powershelltools.exe’, ‘powershelltoolsx64.exe’, ‘pwsh’, and ‘pwsh.exe’. All of these processes are different versions of PowerShell. Talos excluded non-public top-level domains (TLDs), such as internal domains, to focus on external connections.

### Data Processing

Using the tldextract library, Talos extracted base domains (e.g., ‘automox.com’ from ‘api.automox.com’), resulting in 742 unique base domains. Rarity was defined as an average of ≤5 average contacts per full domain, calculated by dividing the total contacts by the number of unique full domains per base domain. This threshold identified 550 rare domains (74.1% of the total).

### Threat Intelligence and Manual Review

Talos assessed domain reputation using [ReversingLabs](https://docs.reversinglabs.com/SpectraAnalyze/9.1.0/API%20Documentation/network-threat-intelligence/) (RL), which flagged a domain as malicious if any third-party source indicated so. To mitigate false positives (e.g., ‘adobe.com’), 29 domains were manually reviewed and overridden as benign, and their process arguments were documented. For subdomains such as ‘raw.githubusercontent.com’ under ‘githubusercontent.com’, the process arguments in those logs were manually reviewed, flagging 5 out of 10 connections as malicious based on commands like downloading PowerSploit or executing Invoke-Mimikatz, ensuring comprehensive threat detection.

## Findings & Analysis

### Domain Contact Distribution

The distribution of contacts was heavily skewed:

* **Percentiles**: 60th percentile at 5.0 contacts, 90th at 82.0, 95th at 321.55, and 99th at 7,925.87
* **Top Domains**: ‘automox.com’ (2,282,308 contacts), ‘launchdarkly.com’ (493,812), and ‘amazonaws.com’ (166,536) accounted for most activity.
  + Automox is a service for automated endpoint configuration and patch management.
  + LaunchDarkly is a software development platform for managing feature flags and context-aware targeting of features.
  + Amazon Web Services (AWS) is the largest cloud service provider.
* **Rare Domains**: 550 of 742 domains fell into the rare category.

![](https://blog.talosintelligence.com/content/images/2025/05/contact-frequencies.jpg)

Figure 1. Cumulative distribution of domain contact frequencies.

### Malicious Domain Statistics

* **Rare Domains**: 9 malicious out of 550 (1.64%, 95% CI: 0.86%–3.08%)
* **Non-Rare Domains**: 1 malicious out of 192 (0.52%, 95% CI: 0.09%–2.89%), notably ‘githubusercontent.com’
* **Odds Ratio**: 3.18 (95% CI: 0.39–25.9), indicating a trend towards higher risk in rare domains, though not statistically significant (chi-square p=0.4291, Fisher’s exact p=0.4668), likely due to small sample sizes (9 rare, 1 non-rare)

![](https://blog.talosintelligence.com/content/images/2025/05/domain-rarity.jpg)

Figure 2. Malicious rates by domain rarity.

### Case Study: githubusercontent.com

The non-rare domain ‘githubusercontent.com’ (38 contacts, 2 full domains: ‘raw.githubusercontent.com’ and ‘objects.githubusercontent.com’, average 19.00 contacts per full domain) was flagged as malicious due to 5 manually identified malicious contacts from ‘raw.githubusercontent.com’. These contacts involved potentially malicious PowerShell commands, such as downloading and executing scripts like PowerSploit or Invoke-Mimikatz. The other subdomain, ‘objects.githubusercontent.com’ (28 contacts), showed no malicious activity. This finding illustrates that even frequently contacted domains can host malicious subdomains, emphasizing the need for subdomain-level analysis in threat detection.

### Comparison to other Processes

Another research question investigated was how the domains contacted by other similar processes would compare to those contacted by PowerShell. For the purposes of this research, Talos chose the following processes for analysis:

* ‘rundll32.exe’
* Python (including macOS and Windows versions)
* ‘cmd.exe’
* ‘cscript.exe’
* ‘wscript.exe’
* ‘bash’
* ‘zsh’

These processes are primarily other command line or script interpreters, as well as ‘rundll32.exe’, which allows executing Dynamically Linked Libraries (DLLs) from the command line.

When the same heuristics as were utilize...
---
title: Threat Advisory: 3CX Softphone Supply Chain Compromise
url: https://blog.talosintelligence.com/3cx-softphone-supply-chain-compromise/
source: Over Security - Cybersecurity news aggregator
date: 2023-03-31
fetch_date: 2025-10-04T11:15:58.725255
---

# Threat Advisory: 3CX Softphone Supply Chain Compromise

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

![](/content/images/2023/03/threat-advisory.png)

# Threat Advisory: 3CX Softphone Supply Chain Compromise

By
[Cisco Talos](https://blog.talosintelligence.com/author/cisco/)

Thursday, March 30, 2023 18:29

[Threat Advisory](/category/threat-advisory/)

* Cisco Talos is tracking and actively responding to a supply chain attack involving the 3CX Desktop Softphone application.
* This is a multi-stage attack that involves sideloading DLLs, seven-day sleep routines, and additional payloads dependent on a now-removed GitHub repository for Windows-based systems.
* MacOS systems used a different infection chain leveraging a hardcoded C2 domain, as opposed to the GitHub repo.
* This is just the latest supply chain attack threatening users, after the [SolarWinds incident in 2020](https://blog.talosintelligence.com/solarwinds-supplychain-coverage/) and the [REvil ransomware group exploiting Kaseya VSA](https://blog.talosintelligence.com/revil-ransomware-actors-attack-kaseya/) in 2021.

## Summary

Cisco Talos recently became aware of a [supply chain attack](https://www.3cx.com/blog/news/desktopapp-security-alert/) affecting Windows and MacOS users of the 3CX software-based phone application. This attack leveraged the legitimate update functionality of the 3CX application to deliver a set of malicious payloads to 3CX users.

The infection chain consists of several stages and involves sideloading DLLs along with a seven-day sleep cycle before the malware attempts to retrieve additional malicious artifacts from a now-removed GitHub repository for the Windows based infection. The GitHub repository hosted a series of icon files with encrypted data appended to the end of the files. These encrypted strings, once decrypted, contained the C2 domains for additional malicious artifacts.

The MacOS version used a hard coded C2 domain. These second-stage payloads are information stealers that attempt to obtain system information and the latest browsing history records, indicating this information may be used as a filtering mechanism to identify and discard some victims while maintaining unauthorized access to others.

During our investigation we were able to see file activity dating back to February 3, 2023. However, the GitHub repository has been active since December 2022. The full scope of the attack is uncertain at this point. The [3CX website](https://www.3cx.com/company/customers/) claims to have over 600,000 customers and 12 million daily users. It's unclear how many are users of the 3CX Desktop App versus the web app option that was not affected. 3CX is [currently asking users](https://www.3cx.com/blog/news/desktopapp-security-alert/) to use the web app while they work to release an update.

## Preparing since February 2022

Based on Cisco Talos investigation, it appears the infrastructure that supported this attack was being prepared as early as February 2022 when the domains were first registered. A second cluster of activity happened toward the end of 2022 when the GitHub repository was created, along with a few other domains. The sbmsa[.]wiki domain was also created on Feb. 9, 2023, which was found to be used by the second stage of the MacOS version.

The timeline below illustrates these clusters of activity.

![](https://blog.talosintelligence.com/content/images/2023/03/3CX-Domains_3.jpg)

Timeline of domain registration activity.

## Coverage

![](https://blog.talosintelligence.com/content/images/2023/03/endpoint-firewall-analytics-DNS-SIG-web.png)

[Cisco Secure Endpoint](https://www.cisco.com/c/en/us/products/security/amp-for-endpoints/index.html) (formerly AMP for Endpoints) is ideally suited to prevent the execution of the malware detailed in this post. Try Secure Endpoint for free [here.](https://www.cisco.com/c/en/us/products/security/amp-for-endpoints/free-trial.html?utm_medium=web-referral?utm_source=cisco&utm_campaign=amp-free-trial&utm_term=pgm-talos-trial&utm_content=amp-free-trial)

[Cisco Secure Email](https://www.cisco.com/c/en/us/products/security/email-security/index.html) (formerly Cisco Email Security) can block malicious emails sent by threat actors as part of their campaign. You can try Secure Email for free [here](https://www.cisco.com/c/en/us/products/security/cloud-mailbox-defense?utm_medium=web-referral&utm_source=cisco&utm_campaign=cmd-free-trial-request&utm_term=pgm-talos-trial).

[Cisco Secure Firewall](https://www.cisco.com/c/en/us/products/security/firewalls/index.html) (formerly Next-Generation Firewall and Firepower NGFW) appliances such as [Threat Defense Virtual](https://www.cisco.com/c/en/us/products/collateral/security/firepower-ngfw-virtual/datasheet-c78-742858.html), [Adaptive Security Appliance](https://www.cisco.com/c/en/us/products/security/adaptive-security-appliance-asa-software/index.html) and [Meraki MX](https://meraki.cisco.com/products/appliances) can detect malicious activity associated with this threat.

[Cisco Secure Network/Cloud Analytics](https://www.cisco.com/c/en/us/products/security/stealthwatch/index.html) (Stealthwatch/Stealthwatch Cloud) analyzes network traffic automatically and alerts users of potentially unwanted activity on every connected device.

[Cisco Secure Malware Analytics](https://www.cisco.com/c/en/us/products/security/threat-grid/index.html) (Threat Grid) identifies malicious binaries and builds protection into all Cisco Secure products.

[Umbrella](https://umbrella.cisco.com/), Cisco’s secure internet gateway (SIG), blocks users from connecting to malicious domains, IPs and URLs, whether users are on or off the corporate network. Sign up for a free trial of Umbrella [here](https://signup.umbrella.com/?utm_medium=web-referral?utm_source=cisco&utm_campaign=umbrella-free-trial&utm_term=pgm-talos-trial&utm_content=automated-free-trial).

[Cisco Secure Web Appliance](https://w...
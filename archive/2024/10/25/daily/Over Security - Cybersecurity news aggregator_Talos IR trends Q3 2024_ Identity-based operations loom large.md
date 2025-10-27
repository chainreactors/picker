---
title: Talos IR trends Q3 2024: Identity-based operations loom large
url: https://blog.talosintelligence.com/incident-response-trends-q3-2024/
source: Over Security - Cybersecurity news aggregator
date: 2024-10-25
fetch_date: 2025-10-06T18:55:25.751913
---

# Talos IR trends Q3 2024: Identity-based operations loom large

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

# Talos IR trends Q3 2024: Identity-based operations loom large

By
[Caitlin Huey](https://blog.talosintelligence.com/author/caitlin/)

Thursday, October 24, 2024 06:00

[Talos IR trends](https://blog.talosintelligence.com/category/ctir-trends/)
[Cisco Talos Incident Response](https://blog.talosintelligence.com/category/cisco-talos-incident-response/)

Threat actors are increasingly conducting identity-based attacks across a range of operations that are proving highly effective, with credential theft being the main goal in a quarter of incident response engagements.

These attacks were primarily facilitated by living-off-the-land binaries (LoLBins), open-source applications, command line utilities, and common infostealers, highlighting the relative ease at which these operations can be carried out. In addition to outright credential harvesting, we also saw password spraying and brute force attacks, adversary-in-the-middle (AitM) operations, and insider threats, underscoring the variety of ways in which actors are compromising users' identities.

Identity-based attacks are concerning because they often involve actors launching internal attacks from a compromised, valid account--making such activity difficult to detect. Moreover, once account compromise is achieved, an actor can carry out any number of malicious activities, including account creation, escalating privileges to gain access to more sensitive information, and launching social engineering attacks, like business email compromise (BEC), against other users on the network.

Watch the team discuss some of the major takeaways of the report, and recommendations for defenders

## Threats against identity

This quarter, Cisco Talos Incident Response (Talos IR) has responded to a growing number of engagements in which adversaries have leveraged password-spraying campaigns to obtain valid usernames and passwords to facilitate initial access. This quarter, 25 percent of incidents involved password spraying and/or brute force attempts to steal valid credentials. This method involves an adversary using a password, or a small list of commonly used passwords, against many different accounts on a network, a strategy that helps avoid account lockouts that would typically occur when brute-forcing a single account with many passwords. Although adversaries have been using password-spraying attacks for credential access for years, the activity illustrates that organizations should continue to stress the importance of multi-factor authentication (MFA) and strong password policies to limit unauthorized attempts.

Talos IR observed AitM phishing attacks play out in a number of ways this quarter, where adversaries attempted to trick users into entering their credentials into fake login pages. In one engagement, Talos IR investigated a phishing case where, after clicking a malicious link in a phishing email, the victim was redirected to a site prompting them to enter their credentials, and subsequently approved an MFA request. In another engagement, an initial phishing email redirected a user to a page that simulates a Microsoft O365 login and MFA portal, capturing the user's credentials and subsequently logging in on their behalf. The first login by the adversary was seen 20 minutes after the initial phishing email, highlighting the speed, ease, and effectiveness of these operations.

## Ransomware

Ransomware, pre-ransomware, and data theft extortion – in which cybercriminals steal and threaten to release victims’ files or other data without using any encryption mechanisms — accounted for nearly 40 percent of engagements this quarter. Talos IR observed RansomHub, RCRU64, and DragonForce ransomware variants for the first time this quarter, while also responding to previously seen ransomware variants, such as BlackByte, Cerber, and BlackSuit.

![](https://blog.talosintelligence.com/content/images/2024/10/data-src-image-0ad8aeb6-62f2-4df1-b658-6262f5f9ac58.png)

A third of these engagements involved exploitation of known vulnerabilities that are consistently leveraged by ransomware operators/affiliates to deploy ransomware, according to public reporting. For example, in one BlackByte ransomware engagement, we observed an admin account created and added to an “ESX Admin” group as part of exploitation of the ESXi hypervisor vulnerability, [CVE-2024-37085](https://support.broadcom.com/web/ecx/support-content-notification/-/external/content/SecurityAdvisories/0/24505). This vulnerability, which has reportedly been exploited by other ransomware operators, involves a domain group whose members are granted full administrative access to the ESXi hypervisor by default without proper validation.

As part of a years-long trend in greater democratization of ransomware adversaries, we continue to see new variants and ransomware operations emerging. In an incident involving the RCRU64 ransomware –a malware family that has received limited public reporting – the adversary used stolen credentials on an accidentally exposed remote desktop protocol (RDP) account to gain initial access. The threat actor then performed a dump of all domain credentials using publicly available tools, such as [fgdump](https://attack.mitre.org/software/S0120) and [pwdump](https://attack.mitre.org/software/S0006), to steal Windows hashes. The threat actor also deployed custom tools, including “saxcvz.exe” and “close.exe”, to kill processes and close SQL servers running on the host, respectively. Open-source tools such as Mimikatz, Advanced Port Scanner, and IObit Unlocker were also used to facilitate the compromise. Of note, Talos has not previously seen IObit Unlocker used in a ransomware incident, though the tool has been used in Play ransomware attacks, [according](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-352a) to the...
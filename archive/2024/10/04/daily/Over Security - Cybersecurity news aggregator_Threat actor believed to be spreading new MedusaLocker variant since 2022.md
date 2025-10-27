---
title: Threat actor believed to be spreading new MedusaLocker variant since 2022
url: https://blog.talosintelligence.com/threat-actor-believed-to-be-spreading-new-medusalocker-variant-since-2022/
source: Over Security - Cybersecurity news aggregator
date: 2024-10-04
fetch_date: 2025-10-06T18:53:45.097999
---

# Threat actor believed to be spreading new MedusaLocker variant since 2022

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

![](/content/images/2024/10/medusa-header.jpg)

# Threat actor believed to be spreading new MedusaLocker variant since 2022

By
[Tiago Pereira](https://blog.talosintelligence.com/author/tiago-pereira/),
[Arnaud Zobec](https://blog.talosintelligence.com/author/arnaud/)

Thursday, October 3, 2024 06:00

[ransomware](/category/ransomware/)
[Threats](/category/threats/)
[Threat Spotlight](/category/threat-spotlight/)

* Cisco Talos has discovered a financially motivated threat actor, active since 2022, recently observed delivering a MedusaLocker ransomware variant.
* Intelligence collected by Talos on tools regularly employed by the threat actor allows us to see an estimate of the amount and countries of origin of this group’s victims. This actor has been active since at least late 2022 and targets organizations worldwide, although the number of victims was higher than average in EU countries until mid-2023 and, since then, in Latin American countries.
* This threat actor was observed distributing a MedusaLocker ransomware variant known as “BabyLockerKZ.” This variant is compiled with a PDB path containing the word “paid\_memes” which is also present in other tools observed during the attacks, presumably by the same author.
* Talos has new information on the attacker’s tools, including BabyLockerKz and attacker TTPs and IOCs to assist in detecting and preventing further attacks.

Talos has recently observed an attack leading to the deployment of a MedusaLocker ransomware variant known as “BabyLockerKZ.” The distinguishable techniques — including consistently storing the same set of tools in the same location on compromised systems, the use of tools that have the PDB path with the string “paid\_memes,” and the use of a lateral movement tool named “checker” — used in the attack led us to take a deeper look to try to understand more about this threat actor.

This attacker uses several publicly known attack tools and living-off-the-land binaries (LoLBins), a set of tools built by the same developer (possibly the attacker) to assist in credential theft and lateral movement in compromised organizations. These tools are mostly wrappers around publicly available tools that include additional functionality to streamline the attack process and provide graphical or command-line interfaces.

The same developer built the MedusaLocker variant used in the initial attack. This variant that uses the same chat and leak site URLs contains several differences to the original MedusaLocker ransomware, such as a different autorun key or an extra public and private key set stored in the registry. Based on the name of the autorun key, the attackers call this variant “BabyLockerKZ.”

We assess with medium confidence that the actor is financially motivated, likely working as an IAB or an affiliate of a ransomware cartel, and has been carrying out attacks since at least 2022. Our telemetry indicates that the actor opportunistically targeted many victims worldwide. In late 2022 and early 2023, most victims were in European countries, but since the first quarter of 2023, the group’s focus shifted toward Latin American countries and, as a result, the number of victims per month almost doubled.

# Tracking BabyLockerKZ across the globe

Intelligence collected by Talos on tools regularly employed by the threat actor allows us to estimate the number of, and the countries of origin of the victims. Although this is unlikely to capture all of the adversary’s activities, it still provides a look at a specific window of activity.

The actor has been active since at least October 2022. At that time, the targets were mostly located in European countries such as France, Germany, Spain or Italy. During the second  quarter of 2023, the attack volume per month almost doubled, and the group shifted its focus toward Latin American countries such as Brazil, Mexico, Argentina and Colombia, as shown in the chart below. The attacks kept a steady volume of around 200 unique IPs compromised per month until the first quarter of 2024 when the attacks decreased.

![](https://blog.talosintelligence.com/content/images/2024/10/medusa-chart.jpg)

The actor has consistently compromised a large number of organizations, often more than 100 per month, since at least 2022. This reveals the professional and highly aggressive nature of the attacks and is coherent with the activity we would expect from an IAB or ransomware affiliate.

# Attacker TTPs and tools

During the attack leading to the deployment of the BabyLockerKZt, the adversary used several publicly known attack tools and others that could be unique to this actor. The group frequently used the Music, Pictures or Documents user folders of compromised systems to store attack tools. For example, the following paths were used to store tools during this attack:

* c:\users\<user>\music\advanced\_port\_scanner\_2.5.3869.exe
* c:\users\<user>\music\hrsword\hrsword install.bat
* c:\users\<user>\music\killav\build.004\disabler.exe
* c:/users/<user>/music/checker/checker(222).exe
* c:/users/<user>/music/checker/invoke-thehash.ps1
* c:/users/<user>/music/checker/checker (222).exe
* c:/users/<user>/music/checker/invoke-smbexec.ps1
* c:/users/<user>/music/checker/invoke-wmiexec.ps1
* c:/users/<user>/appdata/roaming/ntsystem/ntlhost.exe.exe
* c:/users/<user>/appdata/local/temp/advanced port scanner 2/advanced\_port\_scanner.exe
* c:/users/<user>/appdata/local/temp/is-juad3.tmp/advanced\_port\_scanner\_2.5.3869.tmp

These are similar to a previous attack leading to MedusaLocker ransomware, documented by [ASEC](https://asec.ahnlab.com/en/48940/) in February 2023, which our telemetry suggests was a more active period for this threat actor.

Some of the publicly known tools used by the attacker are:

* HRSword\_v5.0.1.1.rar: A tool used to disable AV and EDR sof...
---
title: Unmasking the new Chaos RaaS group attacks
url: https://blog.talosintelligence.com/new-chaos-ransomware/
source: Over Security - Cybersecurity news aggregator
date: 2025-07-25
fetch_date: 2025-10-06T23:51:16.786480
---

# Unmasking the new Chaos RaaS group attacks

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

![](/content/images/2025/07/chaos-header.jpg)

# Unmasking the new Chaos RaaS group attacks

By
[Anna Bennett](https://blog.talosintelligence.com/author/anna/),
[James Nutland](https://blog.talosintelligence.com/author/james/),
[Chetan Raghuprasad](https://blog.talosintelligence.com/author/chetan/)

Thursday, July 24, 2025 06:00

[ransomware](/category/ransomware/)

* Cisco Talos Incident Response (Talos IR) recently observed attacks by Chaos, a relatively new ransomware-as-a-service (RaaS) group conducting big-game hunting and double extortion attacks.
* Chaos RaaS actors initiated low-effort spam flooding, escalating to voice-based social engineering for access, followed by RMM tool abuse for persistent connection and legitimate file-sharing software for data exfiltration.
* The ransomware utilizes multi-threaded rapid selective encryption, anti-analysis techniques, and targets both local and network resources, maximizing impact while hindering detection and recovery.
* Talos believes the new Chaos ransomware is unrelated to previous Chaos builder-generated variants, as the group uses the same name to create confusion.
* Talos assesses with moderate confidence that the new group is likely formed by former members of the BlackSuit (Royal) gang, based on similarities in the ransomware's encryption methodology, ransom note structure, and the toolset used in the attacks.

# Victimology

The new Chaos has impacted a wide variety of business verticals and seems to be opportunistic without focusing on any specific verticals. Victims have been predominantly in the U.S. and a fewer in the UK, New Zealand and India according to the actor’s data leak site.

# Who is Chaos?

Chaos is a relatively new RaaS group that emerged as early as February 2025. The Chaos group is actively promoting their cross-platform ransomware software in the dark web Russian-speaking cybercriminal forum Ransom Anon Market Place (RAMP) and is seeking collaboration with affiliates. They emphasize that the new Chaos ransomware software is compatible with Windows, ESXi, Linux and NAS systems, with features such as individual file encryption keys, rapid encryption speeds and network resource scanning — all with a strong emphasis on high-speed encryption and robust security measures.

Additionally, the group provides an automated panel for managing targets and communications, which requires a paid entry fee that is refundable upon the first case of payment. They have also clearly stated in their dark web forum post that they explicitly avoid collaborating with BRICS/CIS countries, hospitals and government entities.

Furthermore, the group is offering an onion URL for potential affiliates to register for an account with the Chaos group and has provided a support email address at “win88@thesecure[.]biz”.

Talos IR observed that the group has been launching big-game hunting and double extortion attacks. Like other operators in the double extortion space, Chaos also runs a data leak site to disclose the stolen data of victims who fail to meet their ransom demands.

![Picture 1304301838, Picture](https://blog.talosintelligence.com/content/images/2025/07/data-src-image-2c480df0-00f1-4802-b020-4c144c2416fc.png)

Figure 2. Chaos data leak site homepage.

Chaos encrypts the victim's environment, uses “.chaos” as the file extension for the encrypted files, and drops the ransom note “readme.chaos[.]txt”. In the ransom note, the actor claims that they attempted to perform security testing in the victim's environment and were successful in compromising it. They also threaten the victims with the disclosure of their stolen confidential data if they fail to pay the ransom amount. The actor does not leave an initial ransom demand or payment instructions in their ransom note but provides instructions to contact them using an onion URL specific to each victim.

![Picture 1076263458, Picture](https://blog.talosintelligence.com/content/images/2025/07/data-src-image-1ec0e239-27fa-4709-a27c-32e937048953.png)

Figure 3. Chaos ransom note.

Talos IR observed that the actor demanded a ransom amount of $300K through the victim communication channel and offered two options. If the victim pays the amount, the actor will provide a decryptor application for targeted environments, along with a detailed report of the penetration test conducted on the victim's environment. They also assure the victim that the stolen data will not be disclosed and will be permanently deleted, ensuring that they will not conduct repeated attacks.

If the victim fails to pay the ransom, the actor threatens to disclose their stolen data and conduct a distributed denial-of-service (DDoS) attack on all the victim’s internet-facing services, as well as spread the news of their data breach to competitors and clients.

![Picture 1455394799, Picture](https://blog.talosintelligence.com/content/images/2025/07/data-src-image-a7076152-1f48-462b-855c-e0d387fcf9af-1.png)

Figure 4. Chaos actor demand.

The Chaos ransomware actor is a recent and concerning addition to the evolving threat landscape, having shown minimal historical activity before the current wave of intrusions. Importantly, this new Chaos ransomware gang is not connected to the variants produced by the Chaos ransomware builder tool or its developers. To hide their identity, these threat actors have exploited the confusion within the security community regarding the name "Chaos" and its various variants and associated builder tools. This deliberate obfuscation complicates the identification and mitigation of risks posed by this emerging threat.

![Picture](https://blog.talosintelligence.com/content/images/2025/07/data-src-image-bc13f8bb-852d-4a0d-84c0-4f9d26c215d2.jpeg)

Figure 5. Chaos RaaS diamond model.

# Recent attack methodologies and notable TTPs

During our investigat...
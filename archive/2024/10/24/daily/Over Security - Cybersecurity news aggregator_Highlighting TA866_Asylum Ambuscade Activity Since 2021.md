---
title: Highlighting TA866/Asylum Ambuscade Activity Since 2021
url: https://blog.talosintelligence.com/highlighting-ta866-asylum-ambuscade/
source: Over Security - Cybersecurity news aggregator
date: 2024-10-24
fetch_date: 2025-10-06T18:55:45.657006
---

# Highlighting TA866/Asylum Ambuscade Activity Since 2021

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

![](/content/images/2024/10/threat-spotlight-1.jpg)

# Highlighting TA866/Asylum Ambuscade Activity Since 2021

By
[Edmund Brumaghin](https://blog.talosintelligence.com/author/edmund-brumaghin/),
[Jordyn Dunk](https://blog.talosintelligence.com/author/jordyn/),
[Nicole Hoffman](https://blog.talosintelligence.com/author/nicole/),
[Holger Unterbrink](https://blog.talosintelligence.com/author/holger-unterbrink/)

Wednesday, October 23, 2024 06:02

[SecureX](/category/securex-3/)
[Threat Spotlight](/category/threat-spotlight/)
[TA866](/category/ta866/)
[Asylum Ambuscade](/category/asylum-ambuscade/)

* [TA866](https://malpedia.caad.fkie.fraunhofer.de/actor/ta866) (also known as Asylum Ambuscade) is a threat actor that has been conducting intrusion operations since at least 2020.
* TA866 has frequently relied on commodity and custom tooling to facilitate post-compromise activities. These tools often perform specific functions and are deployed and used as needed in the context of specific intrusions.
* Cisco Talos assesses with high [confidence](https://blog.talosintelligence.com/on-conveying-doubt/) that TA866 frequently leverages business relationships with other threat actors across various stages of their attacks to help them achieve their mission objective(s).
* We assess with high confidence that [recent](https://blog.talosintelligence.com/warmcookie-analysis/) post-compromise intrusion activity associated with [WarmCookie/BadSpace](https://malpedia.caad.fkie.fraunhofer.de/details/win.warmcookie) is related to previous post-compromise activity that we attribute to TA866.
* We assess that WarmCookie was likely developed by the same threat actor that developed the [Resident backdoor](https://www.esentire.com/blog/esentire-threat-intelligence-malware-analysis-resident-campaign) that was delivered in previous intrusions that we attribute to TA866.

# Who is TA866?

[TA866](https://www.proofpoint.com/us/blog/threat-insight/screentime-sometimes-it-feels-like-somebodys-watching-me), also called [Asylum Ambuscade](https://www.proofpoint.com/us/blog/threat-insight/asylum-ambuscade-state-actor-uses-compromised-private-ukrainian-military-emails), is a threat actor that has been observed conducting intrusion operations since at least [2020](https://www.trendmicro.com/en_us/research/20/l/stealth-credential-stealer-targets-us-canadian-bank-customers.html). TA866 has historically been associated with financially motivated malware campaigns. However, [prior reporting](https://www.welivesecurity.com/2023/06/08/asylum-ambuscade-crimeware-or-cyberespionage/) indicates that they may also conduct espionage-related activities. Cisco Talos has been monitoring and analyzing the malware distribution campaigns, and post-compromise intrusion activity associated with TA866 and has observed continued evolution in the tooling and tactics, techniques and procedures (TTPs) employed by this threat actor since early 2023.

Throughout 2023, these malware campaigns typically relied on malspam or malvertising to facilitate the delivery of malicious content to potential victims. In many cases, this content is used to redirect victims to traffic distribution systems (TDS), such as 404 TDS, operated by threat actors offering malware installation services.

This is followed by the deployment of a variety of malicious components. Since at least early 2023, this has typically included WasabiSeed, ScreenShotter and AHK Bot. Based on analysis of post-compromise activity associated with this tooling, we assess with high confidence that TA866 also sometimes deploys a persistent backdoor called [Resident,](https://www.esentire.com/blog/esentire-threat-intelligence-malware-analysis-resident-campaign) [CSharp-Streamer-RAT,](https://malpedia.caad.fkie.fraunhofer.de/details/win.csharpstreamer) [Cobalt Strike](https://www.cobaltstrike.com/) and [Rhadamanthys](https://malpedia.caad.fkie.fraunhofer.de/details/win.rhadamanthys) on compromised systems. To enable the performance of various post-compromise enumeration and reconnaissance activities, we have also observed the use of utilities such as [AdFind](https://www.joeware.net/freetools/tools/adfind/) and network scanners. TA866 also commonly deploys remote access solutions on infected systems such as AnyDesk and Remote Utilities.

We have observed continued ongoing evolution in the implementation of the malware tooling leveraged by TA866 that enables them to operate more effectively once they obtain initial access. This demonstrates an adversary that is constantly evolving as they attempt to gain access to corporate networks and pursue their mission objective(s).

While analyzing recent [WarmCookie/BadSpace](https://blog.talosintelligence.com/warmcookie-analysis/) activity, we observed a case in early 2024 where Cobalt Strike and CSharp-Streamer-RAT were deployed as follow-on payloads following the initial WarmCookie infection. The SSL certificate used on the CSharp-Streamer-RAT C2 server (`185[.]73[.]124[.]164`) appeared to have been generated using information programmatically populated using an algorithm defined by the threat actor. This same algorithm appears to have been used on three additional CSharp-Streamer-RAT C2 servers, one of which (`109[.]236[.]80[.]191`), was the C2 server for a CSharp-Streamer-RAT sample observed in a prior intrusion in 2023 that we attribute to TA866.

# Typical distribution campaigns

As previously mentioned, initial access to target environments is typically obtained by TA866 through successfully infecting systems via either malspam or malvertising. Throughout 2022 and 2023, we frequently observed TA866 relying on both methods for initiating the infection process.

In the case of malspam, we have observed TA866 relying on various lure themes and techniques, including email thread hijacking, a technique ...
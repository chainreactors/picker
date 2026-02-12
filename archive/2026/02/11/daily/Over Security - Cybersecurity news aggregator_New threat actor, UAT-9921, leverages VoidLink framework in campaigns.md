---
title: New threat actor, UAT-9921, leverages VoidLink framework in campaigns
url: https://blog.talosintelligence.com/voidlink/
source: Over Security - Cybersecurity news aggregator
date: 2026-02-11
fetch_date: 2026-02-12T04:23:08.048775
---

# New threat actor, UAT-9921, leverages VoidLink framework in campaigns

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

# New threat actor, UAT-9921, leverages VoidLink framework in campaigns

By
[Nick Biasini](https://blog.talosintelligence.com/author/nick-biasini/),
[Aaron Boyd](https://blog.talosintelligence.com/author/aaron/),
[Asheer Malhotra](https://blog.talosintelligence.com/author/asheer-malhotra/),
[Vitor Ventura](https://blog.talosintelligence.com/author/vitor-ventura/)

Tuesday, February 10, 2026 19:00

[Threat Advisory](https://blog.talosintelligence.com/category/threat-advisory/)

* Cisco Talos recently discovered a new threat actor, UAT-9921, leveraging VoidLink in campaigns. Their activities may go as far back as 2019, even without VoidLink.
* The VoidLink compile-on-demand feature lays down the foundations for AI-enabled attack frameworks, which can create tools on-demand for their operators.
* Cisco Talos found clear indications that implants also exist for Windows, with the capability to load plugins.
* VoidLink is a near-production-ready proof of concept for an enterprise grade implant management framework, and features auditability and oversight for non-operators.

---

VoidLink is a [new modular framework](https://research.checkpoint.com/2026/voidlink-the-cloud-native-malware-framework/) that targets Linux based systems. Modular frameworks are prevalent on the landscape today with the likes of Cobalt Strike, [Manjusaka](https://blog.talosintelligence.com/manjusaka-offensive-framework/), [Alchimist](https://blog.talosintelligence.com/alchimist-offensive-framework/), and SuperShell among the many operating today. This framework is yet another implant management framework denoting a consistent and concerning evolution with shorter development cycles.

Cisco Talos is tracking the threat actor first seen to be using the VoidLink framework as UAT-9921. This threat actor seems to have been active since 2019, although they have not necessarily used VoidLink over the duration of their activity.  UAT-9921 uses compromised hosts to install VoidLink command and control (C2) which are then used to launch scanning activities both internal and external to the network.

## Who is UAT-9921?

Cisco Talos assesses that this threat actor has knowledge of Chinese language based on the language of the framework, code comments and code planning done using the AI enabled IDE. We also assess with medium confidence that they have been active since at least 2019, not necessarily using VoidLink.

VoidLink development appears to be a more recent addition with the aid of large language model (LLM) based  integrated development environment (IDE). However, in their compromise and post-compromise operations, UAT-9921 does not seem to be using AI-enabled tools.

Cisco Talos was able to determine that the operators deploying VoidLink have access to the source code of some modules and some tools to interact with the implants without the C2. This indicates inner knowledge of the communication protocols of the implants.

While the development of VoidLink seems to be split into teams, it is unclear what level of compartmentalization exists between the development and the operation. We do know that UAT-9921 operators have access to VoidLink source code of kernel modules, as well as tools that enable interaction with the implant without the C2.

Talos assesses with high confidence that UAT-9921 compromises servers with the usage of pre-obtained credentials or exploiting Java serialization vulnerabilities which allow remote code execution, namely Apache Dubbo project. We also found indications of possible initial compromise via malicious documents, but no samples were obtained.

In their post-compromise activities, UAT-9921 deploys the VoidLink implant. This allows the threat actor to hide their presence and the VoidLink C2, once deployed.

To find new targets and perform lateral movement, UAT-9921 deploys a SOCKS server on their compromised servers, which is used by FSCAN to perform internal reconnaissance.

With regard to victimology, UAT-9921 appears to focus on the technology sector, but we have also seen victims from financial services. However, the cloud-aware nature of VoidLink and scanning of entire Class C networks indicates that there is no specific targeting.

Given VoidLink’s auditability and oversight features, it is worth noting that even though UAT-9921 activity involves usage of exploits and pre-obtained credentials, Talos cannot discount the possibility that this activity is part of red team exercises.

## Timeline

![](https://blog.talosintelligence.com/content/images/2026/02/voidlink_timeline.jpg)

Figure 1. Timeline of activities involving UAT-9921 and VoidLink.

Talos is aware of multiple VoidLink-related victims dating back to September with the activity continuing through to January 2026. This finding does not necessarily contradict the [Checkpoint Research](https://research.checkpoint.com/2026/voidlink-the-cloud-native-malware-framework/) mentions of late November since the presented documents show development dates from version 2.0 and Cisco Talos assesses that this was still version 1.0.

## The future of attack frameworks

Talos has been tracking fast deployment frameworks since 2022, with reports on [Manjusaka](https://blog.talosintelligence.com/manjusaka-offensive-framework/) and [Alchimist/Insekt](https://blog.talosintelligence.com/alchimist-offensive-framework/). These two projects were tightly linked in their development philosophy, features, and architectural design. There were obvious inspirations from CobaltStrike and Sliver; however, one fundamental difference was the single file infrastructure and the lack of integrated initial infector vector.

The VoidLink framework represents a giant leap in this predictable evolution, while keeping the same, single file infrastructure philosophy. This is a clear example of a “defense contractor grade” implan...
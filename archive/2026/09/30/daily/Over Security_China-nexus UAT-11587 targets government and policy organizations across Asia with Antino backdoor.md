---
title: China-nexus UAT-11587 targets government and policy organizations across Asia with Antino backdoor
url: https://blog.talosintelligence.com/china-nexus-uat-11587-targets-government-and-policy-organizations-across-asia-with-antino-backdoor/
source: Over Security
date: 2026-09-30
fetch_date: 2026-10-01T07:59:18.292373
---

# China-nexus UAT-11587 targets government and policy organizations across Asia with Antino backdoor

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

![](https://storage.ghost.io/c/af/a0/afa04ee3-414f-4481-8d23-7e7c146f192e/content/images/2026/09/antino-header.jpg)

# China-nexus UAT-11587 targets government and policy organizations across Asia with Antino backdoor

By
[Ashley Shen](https://blog.talosintelligence.com/author/ashley/)

Wednesday, September 30, 2026 06:00

[Threat Spotlight](/category/threat-spotlight/)

* Cisco Talos uncovered a cluster of activity we track as UAT-11587 targeting government and policy organizations across Asia, including in Taiwan, India, the Philippines, and Cambodia, to deliver a previously undocumented backdoor referred to as “Antino” in developer artifacts.
* Talos first observed UAT-11587 activity in September 2025. By July 2026, Talos had identified at least 16 affected or targeted institutional environments across eight Asian countries.
* Antino is a Rust-compiled Windows backdoor that supports host reconnaissance, shell and PowerShell execution, file transfer, in-memory shellcode loading and persistence. Its native command-and-control channel operates exclusively through Microsoft 365, using Microsoft Graph to interact with Outlook and OneDrive.
* Talos identified a recurring delivery branch that began with spear-phishing emails and tailored decoy documents, followed by a five-stage infection chain. The actor relied heavily on Cloudflare infrastructure for delivery, execution tracking, and payload staging.
* Based on the development, preparation-environment, and targeting indicators detailed in this report, Talos assesses with high confidence that UAT-11587 is China-nexus.

---

## Overview

Talos first identified UAT-11587’s campaign while investigating a spear-phishing campaign directed at Taiwan's academic, think tank, and civil society policy community in March 2026. The message recreated Gmail's attachment interface and directed the target into a cloud-hosted, multi-stage infection chain.

Across this activity, our researchers assessed that the actor used several delivery methods, loader families, and post-compromise tools. One recurring final-stage payload was a custom Rust backdoor that Talos tracks as Antino. Antino communicates with Microsoft 365 applications and uses Outlook and OneDrive objects as dead drops, rather than depending on a conspicuous dedicated command server.

Further investigation showed that the activity extended beyond the initial Taiwan operation. Talos subsequently identified confirmed or probable affected government and security environments across multiple Asian countries, alongside additional regional targeting supported by lure content.

While this report was being prepared, Symantec published research on an activity set it tracks as [Jewelbug](https://www.security.com/threat-intelligence/jewelbug-crypto-fraud-espionage). Talos identified overlaps between UAT-11587 and the Antino-related espionage activity attributed to Jewelbug. Although Symantec reported that Jewelbug conducted both espionage and cryptocurrency fraud, it assessed that “the SEO business supplied access, delivery and infrastructure into the espionage operation, rather than that one person performed both roles.” Talos could not independently verify a connection between the espionage campaign and Jewelbug’s financially motivated activity. We therefore track UAT-11587 as a separate activity set.

## Who is UAT-11587?

Talos assesses with high confidence that UAT-11587 is a China-nexus actor, based on the totality of corroborating technical and operational evidence, rather than any single indicator. The indicators discussed below are selected examples of the broader evidence supporting this assessment.

### Evidence supporting the attribution assessment

Decoy document metadata provides several preparation-environment clues. A Taiwan-focused decoy contains the zh-CN language tag, the Simplified Chinese author value 未定义 (“undefined”), and an explicit +08:00 creation timestamp. Both recovered spear-phishing messages also contain +08:00 date headers. UTC+8 alone is not geographically distinctive because it is used across mainland China, Taiwan, Hong Kong, Singapore, and other locations. However, the combination of the +08:00 offset, the zh-CN language tag and Simplified Chinese metadata is more consistent with a mainland Chinese environment than with Taiwan or Hong Kong, [where Traditional Chinese predominates.](https://en.wikipedia.org/wiki/Traditional_Chinese_characters)

![](https://storage.ghost.io/c/af/a0/afa04ee3-414f-4481-8d23-7e7c146f192e/content/images/2026/09/fig-01-decoy-metadata-2.png)

Figure 1. Decoy metadata.

The campaign’s lure theme and targeting provide additional contextual support. Its lures and observed targets include Taiwanese political, legislative, civil defense, and policy research subjects, together with regional government, maritime, diplomatic, and security themes. This collection focus is consistent with [China-nexus actor interests](https://en.wikipedia.org/wiki/Chinese_intelligence_activity_abroad).

Another supporting indicator appears in Antino’s development artifacts. Ten distinct Antino build outputs contain Cargo registry paths referencing rsproxy.cn, a Rust package mirror intended to improve dependency downloads within mainland China. The service’s public accessibility does not reveal the developer’s location, but its repeated use suggests reliance on a China-focused Rust mirror.

During our investigation, Talos also identified a JavaScript downloader associated with UAT-11587 that referenced “d32tpl7xt7175h[.]cloudfront[.]net”, the same CloudFront distribution previously reported by [Arctic Wolf](https://arcticwolf.com/resources/blog/unc6384-weaponizes-zdi-can-25373-vulnerability-to-deploy-plugx/) in China-nexus UNC6384 delivery activity. This shared infrastructure suggests possible delivery-layer overlap. However, beca...
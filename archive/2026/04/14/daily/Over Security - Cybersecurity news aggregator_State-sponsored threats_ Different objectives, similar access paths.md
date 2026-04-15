---
title: State-sponsored threats: Different objectives, similar access paths
url: https://blog.talosintelligence.com/state-sponsored-threats-different-objectives-similar-access-paths/
source: Over Security - Cybersecurity news aggregator
date: 2026-04-14
fetch_date: 2026-04-15T04:43:54.186591
---

# State-sponsored threats: Different objectives, similar access paths

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

![](https://storage.ghost.io/c/af/a0/afa04ee3-414f-4481-8d23-7e7c146f192e/content/images/2026/04/2025YiR-topic_APTs.jpg)

# State-sponsored threats: Different objectives, similar access paths

By
[Hazel Burton](https://blog.talosintelligence.com/author/hazel-burton/)

Tuesday, April 14, 2026 09:49

[2025YiR](/category/2025yir/)
[Year In Review](/category/year-in-review/)

Across the [Talos 2025 Year in Review](https://blog.talosintelligence.com/2025yearinreview/), state-sponsored threat activity from China, Russia, North Korea, and Iran all had varying motivations, such as espionage, disruption, financial gain, and geopolitical influence.

But when you look at how these operations actually unfold, similar tactics, techniques, and procedures (TTPs) keep appearing: access through vulnerabilities and identity, and access that remains under the radar for a considerable period of time.

Here are the dominant themes from the state-sponsored section of the Talos Year in Review, [available now.](https://blog.talosintelligence.com/2025yearinreview/)

## China

China-nexus threat activity stood out this year for both volume and efficiency, with Talos investigations increasing by nearly 75% compared to 2024.

Newly disclosed vulnerabilities were exploited almost immediately (e.g., ToolShell), sometimes before patches were widely available. At the same time, long-standing, unpatched vulnerabilities in networking devices and widely used software continued to provide reliable entry points for these types of adversary.

Once inside, the focus shifts to persistence. Web shells, custom backdoors, tunneling tools, and credential harvesting all support long-term access.

There’s also more overlap than ever before between state-sponsored and financially motivated activity. It is likely that in some cases, state-sponsored actors conducted operations for personal profit alongside espionage-focused missions, while in others, cybercriminals collected valuable information during an attack that could be sold to espionage-motivated actors for further exploitation, providing them dual revenue streams.

## Russia

Russian-linked cyber activity remains closely tied to their geopolitical objectives, particularly the war in Ukraine.

Many operations continue to rely on unpatched, older vulnerabilities (especially in networking devices) to gain initial access. These flaws provide a dependable way in for adversaries and support long-term intelligence gathering.

Russia’s offensive cyber activity is highly correlated with developments in the larger geopolitical sphere. For example, the announcement of sanctions intended to apply pressure on Russia by both the U.S. and E.U. often corresponded with our observed levels of Russian cyber activity.

![](https://storage.ghost.io/c/af/a0/afa04ee3-414f-4481-8d23-7e7c146f192e/content/images/2026/04/YiR_figsforblog_sanctions.jpg)

Common malware families like Dark Crystal RAT (DCRAT), Remcos RAT, and Smoke Loader appeared frequently in Talos investigations on operations against Ukraine in 2025. These families aren’t exclusive to Russia-nexus threat actors, but they continue to be effective in environments where patching and visibility are inconsistent, and should therefore be high priority targets for defense and monitoring.

## North Korea

North Korea cyber operations leaned heavily into social engineering and insider access in 2025. These operations were both for financial and espionage purposes.

Campaigns like Contagious Interview (orchestrated by [Famous Chollima](https://blog.talosintelligence.com/python-version-of-golangghost-rat/)) used fake recruiters from legitimate companies to socially engineering targets to execute code or hand over credentials. From there, actors stole cryptocurrency, exfiltrated data, and established persistent access.

North Korean cyber actors also pulled off the largest cryptocurrency heist in history in 2025, [stealing $1.5 billion](https://www.ic3.gov/psa/2025/psa250226). Additionally, thousands of IT workers used stolen identities and AI-generated profiles to secure positions at Fortune 500 companies, generating billions in annual revenue for North Korea’s nuclear weapons and ballistic missiles programs.

![](https://storage.ghost.io/c/af/a0/afa04ee3-414f-4481-8d23-7e7c146f192e/content/images/2026/04/YiR_figsforblog_worker_accounts.jpg)

## Iran

Iranian cyber threat activity in 2025 combined visible disruption with long-term access.

Hacktivist operations increased by 60% in response to geopolitical events, particularly the Israel-Hamas conflict. These campaigns, which include distributed denial-of-service (DDoS) attacks, defacements, and other disruptive operations, are often designed to generate attention and shape narratives.

At the same time, more traditional advanced persistent threat (APT) activity focused on persistence. Groups such as ShroudedSnooper targeted sectors like telecommunications, using custom compact backdoors designed to blend into normal traffic and remain undetected.

ShroudedSnooper is an APT that public reporting widely [attributes](https://cloud.google.com/blog/topics/threat-intelligence/unc1860-iran-middle-eastern-networks) to Iran’s Ministry of Intelligence and Security (MOIS). It is very likely an initial access group that passes operations off to secondary threat actors for long term espionage or destructive attacks.

For current threat intelligence related to the developing conflict in Iran, follow our coverage on the [Talos blog](https://blog.talosintelligence.com/talos-developing-situation-in-the-middle-east/).

## Guidance for defenders

Though the state-sponsored activity that we tracked for the Talos Year in Review have different objectives, they still have the same reliance on gaining and maintaining access. The following guidance is recommended for security team...
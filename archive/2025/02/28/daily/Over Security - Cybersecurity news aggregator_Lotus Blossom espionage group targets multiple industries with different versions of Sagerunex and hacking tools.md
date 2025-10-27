---
title: Lotus Blossom espionage group targets multiple industries with different versions of Sagerunex and hacking tools
url: https://blog.talosintelligence.com/lotus-blossom-espionage-group/
source: Over Security - Cybersecurity news aggregator
date: 2025-02-28
fetch_date: 2025-10-06T20:47:14.871630
---

# Lotus Blossom espionage group targets multiple industries with different versions of Sagerunex and hacking tools

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

![](/content/images/2025/02/LotusBlossomHeader.jpg)

# Lotus Blossom espionage group targets multiple industries with different versions of Sagerunex and hacking tools

By
[Joey Chen](https://blog.talosintelligence.com/author/joey/)

Thursday, February 27, 2025 06:00

[Threat Spotlight](/category/threat-spotlight/)
[APT](/category/apt/)
[Threats](/category/threats/)

* Cisco Talos discovered multiple cyber espionage campaigns that target government, manufacturing, telecommunications and media, delivering Sagerunex and other hacking tools for post-compromise activities.
* Talos attributes these attacks to the threat actor known as [Lotus Blossom](https://www.paloaltonetworks.com/apps/pan/public/downloadResource?pagePath=/content/pan/en_US/resources/research/unit42-operation-lotus-blossom). Lotus Blossom has actively conducted cyber espionage operations since at least 2012 and continues to operate today.
* Based on our examination of the tactics, techniques, and procedures (TTPs) utilized in these campaigns, alongside the deployment of Sagerunex, a backdoor family used exclusively by Lotus Blossom, we attribute these campaigns to the Lotus Blossom group with high confidence.
* We also observed Lotus Blossom gain persistence using specific commands to install their Sagerunex backdoor within the system registry and configuring it to run as a service on infected endpoints.
* Lotus Blossom has also developed new variants of Sagerunex that not only use traditional command and control (C2) servers but also use legitimate, third-party cloud services such as Dropbox, Twitter, and the Zimbra open-source webmail as C2 tunnels.

# A multi-campaign, multi-variant backdoor operation

Talos assesses with high confidence that Lotus Blossom (also referred to as [Spring Dragon](https://securelist.com/spring-dragon-updated-activity/79067/), [Billbug](https://www.security.com/threat-intelligence/espionage-asia-governments-cert-authority), [Thrip](https://www.fortinet.com/blog/threat-research/thrip-atp-attack-update)) threat actors are responsible for these campaigns. The group was previously publicly disclosed as an active espionage group operating since 2012. Our assessment is based on the TTPs, backdoors, and victim profiles associated with each activity. Our observations indicate that Lotus Blossom has been using the Sagerunex backdoor since at least 2016 and is increasingly employing long-term persistence command shells and developing new variants of the Sagerunex malware suite. The operation appears to have achieved significant success, targeting organizations in sectors such as government, manufacturing, telecommunications and media in areas including the Philippines, Vietnam, Hong Kong and Taiwan.

![](https://blog.talosintelligence.com/content/images/2025/02/data-src-image-23ce5782-73ef-42cd-8dc5-6d65c8a7db7b.jpeg)

Our investigation uncovered two new variants of the Sagerunex backdoor, which were detected during attacks on telecommunications and media companies, as well as many Sagerunex variants persistent in the government and manufacturing industries. These new variants no longer rely on the original Virtual Private Server (VPS) for their C2 servers. Instead, they use third-party cloud services such as [Dropbox](https://www.dropbox.com/), [Twitter](https://twitter.com/), and the [Zimbra](https://www.zimbra.com/) open-source webmail service as C2 tunnels to evade detection. In our malware analysis section, we will delve into the technical specifics of each Sagerunex backdoor variant and illustrate their configurations. Some configurations reveal the possible original file paths of the malware, providing insights into the threat actor’s host paths.

We also compiled a timeline for the evolution of Sagerunex by analyzing data from the campaigns we observed, third-party reports, malware compilation timestamps, and the timestamps of victim uploads on the C2 service:

![](https://blog.talosintelligence.com/content/images/2025/02/data-src-image-95766972-c8e2-4ab1-8552-8dc7798ac7c2.jpeg)

# Attributing the attacks to Lotus Blossom

Talos has identified strong evidence to attribute these campaigns to the Lotus Blossom group, primarily due to the presence of the [Sagerunex](https://www.security.com/threat-intelligence/thrip-apt-south-east-asia) backdoor within these operations. Sagerunex is a remote access tool (RAT) assessed to be an evolution of an older [Billbug tool known as Evora](https://geumgeumland.medium.com/part-2-5-versions-of-evora-c4bcc5db08cf). Sagerunex is designed to be dynamic link library (DLL) injected into an infected endpoint and executed directly in memory.

We also observed the Sagerunex backdoor employ various network connection strategies to ensure it remains under the actor's control. Despite the development of three distinct variants, the foundational structures and core functionalities of the backdoor remain consistent. These consistent elements enable us to confidently categorize all identified variant backdoors as part of the Sagerunex family.

Moreover, the consistent patterns in [victimology](https://www.paloaltonetworks.com/apps/pan/public/downloadResource?pagePath=/content/pan/en_US/resources/research/unit42-operation-lotus-blossom) and the TTPs identified across these campaigns strongly support our attribution to the Lotus Blossom espionage group. This consistency, seen in the selection of targets and the methods employed, aligns with the known operational characteristics of Lotus Blossom, providing compelling evidence that these campaigns are orchestrated by this specific threat actor.

# Lotus Blossom’s latest attack chain

We conducted research into the main elements of the attack including the specific functions of each malware strain and how Lotus Blossom managed to evade detection  for several months. We also obse...
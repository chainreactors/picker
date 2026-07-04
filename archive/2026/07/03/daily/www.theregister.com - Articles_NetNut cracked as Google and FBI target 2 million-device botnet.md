---
title: NetNut cracked as Google and FBI target 2 million-device botnet
url: https://www.theregister.com/security/2026/07/03/netnut-cracked-as-google-and-fbi-target-2-million-device-botnet/5266414
source: www.theregister.com - Articles
date: 2026-07-03
fetch_date: 2026-07-04T05:49:53.433171
---

# NetNut cracked as Google and FBI target 2 million-device botnet

[Jump to main content](#main)

Search

TOPICS

* Security
  + [All Security](/security)
  + [Cyber-crime](/cyber_crime)
  + [Patches](/patches)
  + [Research](/research)
  + [CSO](/cso)
* Off-Prem
  + [All Off-Prem](/off_prem)
  + [Edge and IoT](/edge_iot)
  + [Channel](/channel)
  + [PaaS and IaaS](/tag/paas-iaas)
  + [SaaS](/saas)
* On-Prem
  + [All On-Prem](/on_prem)
  + [Systems](/systems)
  + [Storage](/storage)
  + [Networks](/networks)
  + [HPC](/hpc)
  + [Personal Tech](/personal_tech)
  + [Cx0](/cxo)
  + [Public Sector](/public-sector)
* Software
  + [All Software](/software)
  + [AI and ML](/tag/ai%20and%20ml)
  + [Applications](/applications)
  + [Databases](/databases)
  + [DevOps](/devops)
  + [OS Platforms](/tag/os%20platforms)
  + [Virtualization](/virtualization)
* Offbeat
  + [All Offbeat](/offbeat)
  + [Columnists](/columnists)
  + [Science](/science)
  + [BOFH](/bofh)
  + [Legal](/legal)
  + [Site News](/site_news)
  + [About Us](https://www.theregister.com/about_us)

* Special Features
  + [All Special Features](/special_features)
  + [HPE: AI Explainers](/explainer/ai-explainer)
  + [RSA Conference](/special_features/rsa)
  + [Agentic AI](/special_features/agentic_ai)
  + [The Future of the Datacenter](/special_features/future_of_the_datacenter)
  + [AWS:Reinvent](/special_features/aws_reinvent)
  + [Nvidia GTC](/special_features/nvidia_gtc)
  + [Supercomputing Month](/special_features/2025_11_supercomputing_month)
  + [Computex 2026](/special_features/computex)
  + [AI Infrastructure Month 2026](/special_features/ai_infrastructure_month_2026)
* Vendor Voice
  + [All Vendor Voice](https://vendorvoice.theregister.com/)
  + [Modernizing Financial Services with FIS and AWS](https://vendorvoice.theregister.com/aws_fis_capital_markets/)
  + [Barco](https://vendorvoice.theregister.com/barco/)
  + [Infinidat](https://vendorvoice.theregister.com/infinidat/)
  + [Everpure](https://vendorvoice.theregister.com/everpure/)
  + [Rubrik](https://vendorvoice.theregister.com/rubrik/)
  + [Make it real with Capgemini and AWS](https://vendorvoice.theregister.com/aws_capgemini/)
  + [Money Movement Hub](https://vendorvoice.theregister.com/aws_fis/)
  + [ZTE](https://vendorvoice.theregister.com/zte_news_and_stories/)
  + [Nutanix: Scale Kubernetes. Not Chaos.](https://vendorvoice.theregister.com/nutantix_cloud_native_apps/)
  + [AWS New Horizon](https://vendorvoice.theregister.com/aws_new_horizon/)
* Resources
  + [Intelligence](https://intelligence.theregister.com)
  + [Webinars & Events](https://intelligence.theregister.com/events/list/)
  + [Newsletters](https://account.theregister.com/login?r=https%3A%2F%2Faccount.theregister.com%2Fedit%2Fnewsletter%2F)

Search

[![Go to frontpage. Logo, The Register](/view-resources/dachser2/public/theregister/logo.svg)](https://www.theregister.com)

[![Go to frontpage. Logo, The Register](/view-resources/dachser2/public/theregister/logo.svg)](https://www.theregister.com)

[![Go to frontpage. Logo, The Register](/view-resources/dachser2/public/theregister/logo.svg)](https://www.theregister.com)

* [Sign in](https://account.theregister.com/login)

* [AI](/tag/ai%20and%20ml)
* [Security](/security)
* [Microsoft](/tag/microsoft)
* [AWS](/tag/aws)
* [Developer](/tag/developer)
* [Open Source](/tag/open%20source)
* [Columnists](/tag/columnists)
* [BOFH](/tag/bofh)
* [Who, Me?](/tag/who%20me)
* [On Call](/tag/on%20call/)

REG AD

Security

# NetNut cracked as Google and FBI target 2 million-device botnet

Other residential proxy brands may rely on the same network

Connor Jones
[Connor
Jones](https://www.theregister.com/author/connor-jones)
Cybersecurity reporter

Published
fri 3 Jul 2026 // 13:03 UTC

Tech companies working with US law enforcement "significantly degraded" the NetNut residential proxy network as part of an ongoing effort to disrupt the tools cybercriminals use to conceal their activity, say researchers.

The work was carried out by Google, Lumen, Shadowserver, the FBI, and others, and marks a continuation of the [IPIDEA proxy network disruption](https://www.theregister.com/security/2026/01/29/google-cripples-ipidea-proxy-network-abused-by-crims/5050674) from January.

According to [Google](https://cloud.google.com/blog/topics/threat-intelligence/google-continued-disruption-residential-proxy-networks/) Cloud, those working on the operation believe NetNut was among the most popular residential proxy network providers and had at least 2 million devices enrolled in its botnet, comprising mainly small TV-streaming hardware. Crims often use residential proxy networks to make it look like their traffic is actually coming from legit homes and businesses.

REG AD

In the same way that other residential proxy networks expand their pool of enrolled devices, NetNut distributed its own SDK via these devices.

REG AD

Proxy providers often approach users under the guise of monetizing their spare bandwidth, paying them a fee in exchange for letting their SDK run on their devices.

The official advice is, of course, to refuse any offers of this kind. Not only does it help feed the cybercrime ecosystem, but it can also lead to vulnerabilities elsewhere in home networks.

NetNut offered its own standalone proxy networks, as well as mobile and datacenter proxies, and a slew of scrapers and datasets.

However, it also offered a reseller program, and experts believe many other residential proxy networks are powered by NetNut's own, which means the disruption may have further downstream effects.

"While we expect this disruption to have a larger ripple effect across the residential proxy ecosystem, observations after the disruption of IPIDEA proved that individual networks can appear resilient," Google's Threat Intelligence Group (GTIG) said.

"What we have observed is that when faced with the degradation of their own botnet, proxy operators begin buying capacity from their competitors, effectively becoming a reseller.

"We recognize that creating a lasting disruption in this fluid ecosystem means we must scale our efforts to target the infrastructure of several interconnected providers. We will continue to observe the composition of the NetNut network and map out how its peers adapt to this action."

Residential proxy networks are not illegal, although they are often abused for cybercrime.

REG AD

These networks are ostensibly pitched as a means to shore up online [privacy](https://www.theregister.com/security/2026/05/06/uk-age-gating-plans-risk-breaking-the-internet-privacy-groups-warn/5230732), and promote ideals such as freedom of expression without risk of being traced.

However, the same privacy-preserving features of these networks are used by cybercriminals to mask their malicious activity.

They enroll ordinary devices, which are connected to innocent residential networks, at scale and offer them to customers as exit nodes.

Cybercriminals can make use of these networks to channel their traffic through these nodes, making the traffic appear to originate from an IP address they do not control.

"In a single week during June 2026, GTIG observed 316 distinct threat clusters using suspected NetNut exit nodes, including cybercriminal and espionage groups," said Google.

"These bad actors can use NetNut to mask their origin IP address when accessing victim environments, accessing their own infrastructure, and conducting password spray attacks."

## MORE CONTEXT

* [### To stop crims, Google starts dismantling residential proxy network they use to hide](/security/2026/01/29/google-cripples-ipidea-proxy-network-abused-by-crims/5050674)
* [### Dutch cops wrest 17M devices from mystery botnet's clutches](/security/2026/05/29/dutch-cops-liberate-17m-devices-from-botnets-clutches/5248312)
* [### The Badbox botnet is back, powered by up to a million backdoored Androids](/security/2025/03/07/badbox-is-back-and-a-million-android-devices-were-backdoored/756832)
* [### Critical Wazuh bug exploited in growing Mirai botnet infect...
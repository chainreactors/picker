---
title: China's 'Fire Ant' campaign used compromised Cisco routers as platform for more attacks
url: https://therecord.media/router-hacks-fire-ant-group-china
source: Over Security
date: 2026-09-01
fetch_date: 2026-09-02T06:41:30.131507
---

# China's 'Fire Ant' campaign used compromised Cisco routers as platform for more attacks

![](https://recordedfuture.matomo.cloud/matomo.php?idsite=2&rec=1)

[![Cyber Security News  | The Record](https://cms.therecord.media/uploads/The_Record_Centered_9b27d79125.svg)](/)

* [Leadership](/news/leadership)
* [Cybercrime](/news/cybercrime)
* [Nation-state](/news/nation-state)
* [Influence Operations](/news/influence-operations)
* [Technology](/news/technology)

* [Cyber Daily®](https://therecord.media/subscribe)
* [Click Here Podcast](/podcast)

Go

Subscribe to The Record

[✉️ Free Newsletter](/subscribe)

![router cable](https://cms.therecord.media/uploads/large_ethernet_cable_pixabay2_3933d5cfed.jpg)

Image: Pixabay via Pexels

[Jonathan Greig](/author/jonathan-greig)September 1st, 2026

# China's 'Fire Ant' campaign used compromised Cisco routers as platform for more attacks

China-based hackers used an array of methods to compromise popular Cisco routers and use them as a jumping off point to monitor organizations, steal credentials and break into other organizations.

In its latest [report](https://www.sygnia.co/blog/fire-ant-evolves-from-hypervisors-to-trusted-infrastructure/) on a hacking operation it calls “Fire Ant,” cybersecurity firm Sygnia detailed a string of breaches that alarmed defenders due to its sophistication and effectiveness.

“Fire Ant didn’t just compromise systems. It compromised the trust layer those systems depend on. The routers, authentication servers, and management infrastructure many organizations overlook as legacy technology became the attacker’s vantage point for reach, visibility, and control,” said Asaf Perlman, director of incident response at Sygnia.

“That is what makes this research so important: the significance extended beyond the initially compromised environment, as the affected infrastructure could provide a path toward other connected high-value environments.”

Sygnia said Fire Ant overlaps with a group Google Cloud’s Mandiant unit called UNC3886 — which was [implicated](https://cloud.google.com/blog/topics/threat-intelligence/uncovering-unc3886-espionage-operations) in a string of attacks on prominent strategic organizations [from 2022 to 2024](https://therecord.media/stealthy-china-spies-fire-ant-virtualization-software).

Sygnia researchers said they saw Fire Ant hackers take over infrastructure and use those systems to collect intelligence and credentials before building durable access and concealing their activity.

The Israel-based company said the recent activity shows the actors are no longer focused only on endpoints, servers or cloud workloads. They want to target the infrastructure that sits between environments: routers, hypervisors, access appliances, Linux management hosts, and the systems that “create trust, reachability, and visibility.”

The latest campaign tracked by Sygnia focuses on attacks targeting Cisco IOS XR routers. The company uncovered new tools the group used for persistence and to collect critical credentials that enabled wider access to an organization.

The attackers also hid logs and took other measures to manipulate potential evidence of their activity, often deleting files and tampering with firewall rules.

Sygnia noted that after reporting on Fire Ant in 2025, the group remained active in 2026, evolving beyond compromising hypervisors. The 2026 compromises were seen to have impacted both victims and third-party environments — exploiting infrastructure relationships to breach high-value networks and critical infrastructure. Sygnia did not name the organizations impacted by the campaign.

## Routers provide ‘perspective’

The malware discovered during the campaign was built specifically to control routers and modify them so they would be more manageable for the hackers’ needs.

Fire Ant actors were seen capturing traffic from multiple Cisco routers and uploading data to external infrastructure. They were not satisfied with one point of access, opting to get network vantage points “from across the environment.”

This gave the attackers a broader view of how systems, administrators, and connected networks interacted.

“This activity reinforces one of the core observations from the investigation: when a threat actor controls routers, they do not only gain reach. They gain perspective,” the researchers wrote.

“Fire Ant used network infrastructure to observe the environment from the inside, collecting information that could support lateral movement, credential targeting, and cross-network access planning.”

The actors became adept at compromising specific servers called TACACS that serve as a de facto administrative checkpoints. They authenticate users, authorize commands and record activity, the researchers said.

Compromising this layer allowed the threat actors to harvest credentials as they were used, observe administrative activity and create ambiguity between legitimate accounts and malicious activity.

Sygnia warned that their report illustrated that routers, hypervisors and more need to be treated as “first-class” security forensic assets requiring monitoring, hardening and incident response readiness.

Governments and cybersecurity companies have long warned that Chinese state-backed groups have targeted Cisco firewalls and routers. In 2024, Volt Typhoon — a Chinese government espionage unit previously implicated in several high-profile incidents involving [U.S. critical infrastructure organizations](https://therecord.media/china-state-backed-hacking-group-compromises-us) — was seen targeting end-of-life Cisco routers and network devices in the U.S., U.K. and Australia.

Last year, defenders said more than 1,000 Cisco network devices [were targeted by Chinese actors](https://therecord.media/china-salt-typhoon-cisco-devices) as part of the Salt Typhoon campaign.

Between September and December 2025, [Palo Alto Networks’ Unit 42](https://therecord.media/chinese-hackers-scan-exploit-firewalls-government) and the [federal cyber defense agency](https://therecord.media/federal-cisco-patches-warning) repeatedly warned that China-based hackers were attacking Cisco Adaptive Security Appliances (ASA) — popular devices used by governments and large businesses to consolidate several different security tasks into a single appliance.

Several experts said Sygnia’s latest findings were instructive because of what it showed about the threat actors’ objectives. Andrew Obadiaru, vice president at Cobalt, said the thing that stood out most was how much effort Fire Ant put into staying invisible on infrastructure defenders rarely watch closely.

The devices being targeted are typically outside of the coverage of security tools and are attractive because they don't trigger alerts, he said.

“This pattern of long-dwell, infrastructure-level access lines up with what we've seen from other Chinese espionage clusters targeting telecom and network infrastructure, and it argues for continuous validation of trust relationships across management infrastructure rather than periodic checks,” Obadiaru said.

* [Technology](/news/technology)
* [News](/ukrainian-software-developer-court-switzerland)
* [China](/news/china)

[![Recorded Future](https://cms.therecord.media/uploads/2025_0514_Record_Ads_300x1050_1_0f2f11757e.png)](https://www.recordedfuture.com/?utm_source=therecord&utm_medium=referral&utm_content=post-sidebar-ad)

[![Recorded Future](https://cms.therecord.media/uploads/2025_0514_Record_Ads_970x250_1_d144dbf901.png)](https://www.recordedfuture.com/?utm_source=therecord&utm_medium=referral&utm_content=post-footer-ad)

No previous article

No new articles

[![Jonathan Greig](https://cms.therecord.media/uploads/DSC_0283_1_a6f4e4e315.jpg)](/author/jonathan-greig)

[Jonathan Greig](/author/jonathan-greig)

is a Breaking News Reporter at Recorded Future News. Jonathan has worked across the globe as a journalist since 2014. Before moving back to New York City, he worked for news outlets in South Africa, Jordan and Cambodia. He previously covered cybersecurity at ZDNet and TechRepub...
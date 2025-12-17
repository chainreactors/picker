---
title: Russia’s GRU hackers targeting misconfigured network edge devices in attacks on energy sector, Amazon says
url: https://therecord.media/russia-gru-hackers-target-energy-sector-sandworm
source: Over Security - Cybersecurity news aggregator
date: 2025-12-16
fetch_date: 2025-12-17T03:20:10.601504
---

# Russia’s GRU hackers targeting misconfigured network edge devices in attacks on energy sector, Amazon says

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

![power](https://cms.therecord.media/uploads/format_webp/large_american_public_power_association_TF_DL_2_L1_JM_unsplash_6716f0ac05.jpg)

Image: Unsplash

[Jonathan Greig](/author/jonathan-greig)December 16th, 2025

# Russia’s GRU hackers targeting misconfigured network edge devices in attacks on energy sector, Amazon says

While targeting Western energy companies, prominent Russian government hackers have switched from breaching organizations through novel vulnerabilities to targeting misconfigured network edge devices, according to security researchers from Amazon.

CJ Moses, CISO of Amazon Integrated Security, told Recorded Future News in an interview that the number of victim organizations is more than 10 and attributed the attacks to a well-known hacking operation known as APT44. Referred to colloquially as Sandworm or Seashell Blizzard, the group has been tied by U.S. officials to Russia’s Main Intelligence Directorate (GRU).

Moses said Amazon began tracking the campaign in 2021 and saw that it focused on Western critical infrastructure, particularly the energy sector. Amazon was able to detect the campaigns through its large network of honeypots that it calls Amazon MadPot.

Data Amazon obtained showed “coordinated operations against customer network edge devices hosted on AWS.”

“This was not due to a weakness in AWS; these appear to be customer misconfigured devices,” Moses claimed.

The campaign followed a similar pattern: hackers would compromise a customer network edge device hosted on AWS, steal credentials from intercepted traffic, use the information against victim online services and infrastructure before then establishing persistent access that enabled lateral movement.

In a press briefing this week, Amazon officials said the years-long campaign “represents a significant evolution in critical infrastructure targeting: a tactical pivot where what appear to be misconfigured customer network edge devices became the primary initial access vector, while vulnerability exploitation activity declined.”

“This tactical adaptation enables the same operational outcomes, credential harvesting, and lateral movement into victim organizations’ online services and infrastructure, while reducing the actor’s exposure and resource expenditure,” the experts said.

Amazon researchers [said](https://aws.amazon.com/blogs/security/amazon-threat-intelligence-identifies-russian-cyber-threat-group-targeting-western-critical-infrastructure/) the hackers accessed endpoints for multiple sectors in 2025, including electric utility organizations, energy providers and managed security service providers specializing in energy sector clients.

The campaign also involved attacks targeting telecom providers and technology companies.

Amazon says it notified affected customers if they found compromised network appliances and shared its findings with industry partners as well as affected vendors.

## ‘Low hanging fruit’

Amazon researchers found that the same group previously used novel vulnerabilities for years before switching to exploiting misconfigured customer network edge devices in 2025

From 2021 to 2022, the hackers exploited CVE-2022-26318 — a bug impacting a popular line of firewalls from WatchGuard. The next year, GRU attackers used CVE-2021-26084 and CVE-2023-22518 which [affect the Confluence Data Center and Confluence Server products](https://therecord.media/atlassian-ciso-warns-new-vulnerability-data-loss).

By 2024, the group shifted to exploiting vulnerabilities [from software company Veeam](https://therecord.media/veam-vulnerability-exploited-ransomware-cisa-kev), including CVE-2023-27532, before targeting “misconfigured customer network edge devices” in 2025, according to Amazon.

Both nation-states and cybercriminals have long targeted the “low-hanging fruit” of misconfigured devices with exposed management interfaces — either for persistent access to critical infrastructure networks or for credential harvesting.

The practice, according to Amazon, is in part to reduce the amount of financial investment needed to find and develop zero-day or N-day vulnerabilities.

Although Amazon did not provide details about the victims, they said the time gap between devices being compromised and attempted intrusions likely indicates the hackers were interested in passive information collection rather than active credential theft.

The hacking group has previously been [accused](https://therecord.media/sandworm-attack-ukraine-energy-facility-missile-strikes) of targeting critical infrastructure and energy companies globally, [particularly in Ukraine](https://therecord.media/russian-hackers-target-energy-facilities-ukraine). Sandworm, which researchers have tied to Russian Military Intelligence Unit 74455, has been active since at least 2013 and is responsible for some of Russia’s most high-profile destructive attacks, including [KillDisk](https://therecord.media/notpetya-reward-state-department-10-million-gru-sandworm) and FoxBlade as well as headline-grabbing incidents like [NotPetya](https://therecord.media/u-s-indicts-six-russian-officers-tied-to-one-of-the-worlds-most-destructive-hacking-groups/) and [Prestige](https://therecord.media/microsoft-attributes-prestige-ransomware-attacks-on-ukraine-and-poland-to-russian-group).

Aaron Beardslee, a security expert at Securonix, said Amazon’s findings are representative of a wider cultural shift within the cybersecurity industry.

Security teams have gotten dramatically better at vulnerability management, patch cycles have compressed from months to weeks, cyber protection platforms now catch exploitation artifacts reliably, he said.

According to Beardslee, threat intelligence sharing means exploits have shorter useful life spans before defenders adapt.

“The result is that traditional exploitation now requires more resources, carries higher detection risk and yields diminishing returns. So sophisticated actors did what sophisticated actors do: they pivoted to the path of least resistance,” he said.

“This shift isn't a failure of security programs; it's evidence they're working. Defenders made the traditional exploitation model too expensive and too risky, so attackers adapted. The problem is that configuration security has been treated as operational housekeeping instead of a critical security control, and that needs to change immediately.”

* [Cybercrime](/news/cybercrime)
* [Government](/news/government)
* [News](/)
* [Industry](/)

Get more insights with the

Recorded Future

Intelligence Cloud.

[Learn more.](https://www.recordedfuture.com/platform?mtm_campaign=ad-unit-record)

[![Recorded Future](https://cms.therecord.media/uploads/format_webp/2025_0514_Record_Ads_300x1050_1_0f2f11757e.png)](https://www.recordedfuture.com/?utm_source=therecord&utm_medium=ad)

[![Recorded Future](https://cms.therecord.media/uploads/format_webp/2025_0514_Record_Ads_970x250_1_d144dbf901.png)](https://www.recordedfuture.com/?utm_source=therecord&utm_medium=ad)

Tags

* [Russia](/tag/russia)
* [energy](/tag/energy)
* [GRU](/tag/gru)
* [Sandworm](/tag/sandworm)
* [Hack](/tag/hack)

No previous article

No new articles

[![Jonathan Greig](https://cms.therecord.media/uploads/format_webp/DSC_0283_1_a6f4e4e315.jpg)](/author/jonathan-greig)

[Jonathan Greig](/author/jonathan-greig)

is a Breaking News Reporter at Recorded Future News. Jonathan has worked across the globe as a journalist since 2014. Before moving back to New...
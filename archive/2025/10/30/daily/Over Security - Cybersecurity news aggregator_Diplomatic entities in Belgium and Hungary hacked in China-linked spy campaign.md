---
title: Diplomatic entities in Belgium and Hungary hacked in China-linked spy campaign
url: https://therecord.media/belgium-hungary-diplomatic-entities-hacked-unc6384
source: Over Security - Cybersecurity news aggregator
date: 2025-10-30
fetch_date: 2025-10-31T03:14:21.535922
---

# Diplomatic entities in Belgium and Hungary hacked in China-linked spy campaign

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

![Brussels, Belgium](https://cms.therecord.media/uploads/format_webp/large_tom_s_7k6_Az_QC_3nyg_unsplash_83cb155ee6.jpg)

Belgian and EU flags fly at Grand-Place in Brussels. Image: Tom S. via Unsplash

[Jonathan Greig](/author/jonathan-greig)October 30th, 2025

# Diplomatic entities in Belgium and Hungary hacked in China-linked spy campaign

Hungarian and Belgian diplomatic entities were allegedly targeted by a well-known Chinese hacking group in September and October.

Incident responders at Arctic Wolf Labs [discovered](https://arcticwolf.com/resources/blog/unc6384-weaponizes-zdi-can-25373-vulnerability-to-deploy-plugx/) an active cyber-espionage campaign they attributed to a China-affiliated threat actor tracked as UNC6384. In August, Google [spotlighted](https://cloud.google.com/blog/topics/threat-intelligence/prc-nexus-espionage-targets-diplomats) a nearly identical campaign by the same group targeting diplomats in Southeast Asia with documents mimicking EU Council meeting agendas.

Arctic Wolf tracked the latest campaign over the last two months, writing in a blog post on Thursday that the attacks began with spearphishing emails centered on European Commission meetings, NATO-related workshops and multilateral diplomatic coordination events.

In addition to the Hungarian and Belgian targets, Arctic Wolf said it saw documents targeting Serbian government aviation departments, as well as other diplomatic entities in Italy and the Netherlands. The diplomatic targets focused specifically on cross-border policy, defense cooperation and multilateral coordination activities.

The researchers noted that Belgium's role as host nation for NATO headquarters and numerous EU institutions “makes Belgian diplomatic entities valuable intelligence targets for monitoring alliance activities and policy development.” Arctic Wolf did not specify what those entities were.

The targeting indicates interest in NATO and EU defense initiatives, procurement decisions and military readiness assessments as well as European supply chain resilience, infrastructure development and trade policy evolution, the researchers explained.

“The expansion to European diplomatic targeting observed in this campaign indicates either broadened operational mandate or deployment of additional operational teams with geographic specialization,” Arctic Wolf said. “The consistency in tooling and techniques across both geographic theaters suggests centralized tool development with regional operational deployment.”

Panda’s PlugX

The emails contained embedded URLs that eventually led to the delivery of malicious files that exploit a Windows vulnerability [disclosed in March 2025](https://www.trendmicro.com/en_us/research/25/c/windows-shortcut-zero-day-exploit.html). The attacks culminate in the use of [PlugX](https://therecord.media/tag/plugx) — a brand of malware used by many Chinese nation-state groups.

Arctic Wolf argued that the campaign “represents a tactical evolution from the group's previously documented operations, introducing exploitation of a recently disclosed Windows vulnerability alongside refined social engineering approaches.”

The study links to research from Trend Micro that the Windows bug was being exploited as a zero-day by multiple government-backed hacking groups in North Korea, China, Russia and Iran — enabling widespread espionage and data theft activities.

Arctic Wolf noted that the exploitation of the vulnerability was concerning because it showed that UNC6384 was able to adopt the vulnerability into its tool set just six months after it was publicly disclosed.

The researchers warned that the timeline “suggests either direct monitoring of vulnerability disclosures with rapid development cycles, or potential pre-disclosure awareness through other intelligence channels.”

PlugX allowed the hackers to establish long-term access to a victim’s system and enabled them to exfiltrate classified documents, monitor policy discussions in real time, surveil diplomatic calendars and travel plans, and collect credentials that would enable further access to diplomatic networks.

The malware has been used in attacks since 2008 and remains a popular tool among Chinese espionage groups. It has evolved significantly since 2008 and several variations have been created, including versions known as Korplug, TIGERPLUG, and SOGU. Arctic Wolf found versions that have been developed and refined in the last six months.

It enables threat actors to conduct keylogging, upload and download files,, establish persistence and closely monitor system functions.

The latest version has been streamlined significantly, maintaining “essential functionality while dramatically reducing forensic footprint and analysis surface area,” Arctic Wolf said.

According to the company, UNC6384 has ties to [Mustang Panda](https://therecord.media/tag/mustang-panda) — one of China’s most prolific espionage groups. Both groups share operational tools, targets, overlapping infrastructure and more.

In January, the Justice Department [removed PlugX](https://therecord.media/doj-deletes-china-linked-plugx-malware) from more than 4,000 U.S. computers in an operation aimed at stopping a Mustang Panda campaign. The action was part of a global effort to address the spread of PlugX, which had been found on nearly [100,000 devices in about 170 countries](https://therecord.media/plugx-malware-infections-more-than-170-countries).

Mustang Panda was [previously accused](https://therecord.media/multiple-chinese-apts-are-attacking-european-targets-eu-cyber-agency-warns) by the European Union’s cybersecurity agency of targeting European businesses and organizations. The group was even seen targeting [diplomatic entities in Russia](https://therecord.media/chinese-hackers-targeting-russian-government-telecoms-report/).

Their other victims include the [African Union](https://www.reuters.com/article/us-ethiopia-african-union-cyber-exclusiv/exclusive-suspected-chinese-hackers-stole-camera-footage-from-african-union-memo-idUSKBN28Q1DB), [several telecommunications companies](https://therecord.media/chinese-cyberspies-go-after-telco-providers-5g-secrets/), [prime ministers across Asia](https://therecord.media/chinese-govt-hackers-using-diverse-toolset-to-target-asian-prime-ministers-telecoms/), [Myanmar’s president](https://therecord.media/backdoor-malware-found-on-the-myanmar-presidents-website-again/), [Indonesia’s intelligence agency](https://therecord.media/indonesian-intelligence-agency-compromised-in-suspected-chinese-hack/) and more.

* [Nation-state](/news/nation-state)
* [News](/)
* [China](/news/china)
* [Government](/news/government)
* [Malware](/news/malware)

Get more insights with the

Recorded Future

Intelligence Cloud.

[Learn more.](https://www.recordedfuture.com/platform?mtm_campaign=ad-unit-record)

[![Recorded Future](https://cms.therecord.media/uploads/format_webp/2025_0514_Record_Ads_300x1050_1_0f2f11757e.png)](https://www.recordedfuture.com/?utm_source=therecord&utm_medium=ad)

[![Recorded Future](https://cms.therecord.media/uploads/format_webp/2025_0514_Record_Ads_970x250_1_d144dbf901.png)](https://www.recordedfuture.com/?utm_source=therecord&utm_medium=ad)

Tags

* [espionage](/tag/espionage)
* [Plugx](/tag/plugx)
* [Belgium](/tag/belgium)
* [Hungary](/tag/hungary)
* [Europe](/tag/europe)
* [diplomacy](/tag/diplomacy)
* [China](/tag/china)

No previous article

No new articles

[![Jonathan Greig](https...
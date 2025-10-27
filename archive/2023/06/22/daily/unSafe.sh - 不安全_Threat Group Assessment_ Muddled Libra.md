---
title: Threat Group Assessment: Muddled Libra
url: https://buaq.net/go-169780.html
source: unSafe.sh - 不安全
date: 2023-06-22
fetch_date: 2025-10-04T11:44:37.776162
---

# Threat Group Assessment: Muddled Libra

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/b1106bb3d5f166b405777acbfc89f9fa.jpg)

Threat Group Assessment: Muddled Libra

Executive SummaryAt the inte
*2023-6-21 21:0:37
Author: [unit42.paloaltonetworks.com(查看原文)](/jump-169780.htm)
阅读量:40
收藏*

---

![Pictorial representation of a threat actor like Muddled Libra](https://unit42.paloaltonetworks.com/wp-content/uploads/2023/06/Threat-brief-r3d3.png)

## Executive Summary

At the intersection of devious social engineering and nimble technology adaptation stands Muddled Libra. With an intimate knowledge of enterprise information technology, this threat group presents a significant risk even to organizations with well-developed legacy cyber defenses.

Muddled Libra is a methodical adversary that poses a substantial threat to organizations in the software automation, BPO, telecommunications and technology industries.

Unit 42 researchers and responders have investigated more than half a dozen interrelated incidents from mid-2022 through early 2023, which we’ve attributed to the threat group Muddled Libra. This threat group favors targeting large outsourcing firms serving high-value cryptocurrency institutions and individuals. Thwarting Muddled Libra requires a combination of tight security controls, diligent security awareness training and vigilant monitoring.

Palo Alto Networks customers receive protection from the threats described in this blog through a modern security architecture built around [Cortex XSIAM](https://docs-cortex.paloaltonetworks.com/p/XSIAM) in concert with [Cortex XDR](https://docs-cortex.paloaltonetworks.com/p/XDR). The [Advanced URL Filtering](https://docs.paloaltonetworks.com/advanced-url-filtering/administration) and [DNS Security](https://docs.paloaltonetworks.com/dns-security) [Cloud-Delivered Security Services](https://docs.paloaltonetworks.com/cdss) can help protect against command and control (C2) infrastructure, while [App-ID](https://www.paloaltonetworks.com/technologies/app-id) can limit anonymization services allowed to connect to the network.

| **Related Unit 42 Topics** | [**Muddled Libra**](https://unit42.paloaltonetworks.com/tag/muddled-libra/) (related to **[Scattered Spider](https://unit42.paloaltonetworks.com/tag/scattered-spider/)**, [**Scatter Swine**](https://unit42.paloaltonetworks.com/tag/scatter-swine/)), [**0ktapus**](https://unit42.paloaltonetworks.com/tag/0ktapus) |
| --- | --- |

[Threat Overview](#post-128741-_pw43161vrd8q)

## Threat **Overview**

The attack style defining Muddled Libra appeared on the cybersecurity radar in late 2022 with the release of the 0ktapus phishing kit, which offered a prebuilt hosting framework and bundled templates. With large numbers of realistic fake authentication portals and targeted smishing, attackers were able to quickly gather credentials and multifactor authentication MFA codes.

The speed and breadth of these attacks caught many defenders off guard. While smishing is not new, the 0ktapus framework commoditized the establishment of a normally complex infrastructure in a way that granted even low-skilled attackers a high success rate.

These features included prebuilt templates and a built-in C2 channel via Telegram, all for a cost of only a few hundred US dollars. This improvement in functionality led to cybercriminals launching a massive attack campaign targeting a wide range of organizations.

The sheer number of targets being hit with this kit has created a fair amount of confusion in the research community about attributing these attacks. Previous reporting by [Group-IB](https://www.group-ib.com/blog/0ktapus/), [CrowdStrike](https://www.crowdstrike.com/blog/analysis-of-intrusion-campaign-targeting-telecom-and-bpo-companies/) and [Okta](https://sec.okta.com/scatterswine) has documented and mapped many of these attacks to the following intrusion groups: 0ktapus, Scattered Spider and Scatter Swine. While these have been treated in the media as three names for one group, in actuality, it's likely multiple actors using a common toolkit. Muddled Libra is a subset of these actors.

During the Unit 42 incident response investigations, we identified several cases with overlapping trade craft. This indicated a subset of the previously mentioned groups focusing on a complex series of supply chain attacks, ultimately leading to high-value cryptocurrency targets.

Defining characteristics of Muddled Libra include the following:

* Using the 0ktapus phishing kit
* Long-term persistence
* Nondestructive presence
* Persistent targeting of the business process outsourcing (BPO) industry
* Data theft
* Use of compromised infrastructure in downstream attacks

Muddled Libra investigations demonstrate the use of an unusually large attack toolkit. Their arsenal ranges from hands-on social engineering and smishing attacks to proficiency with niche penetration testing and forensics tools, giving this threat group an edge over even a robust and modern cyber defense plan.

In the incidents the Unit 42 team has investigated, Muddled Libra has been methodical in pursuing their goals and highly flexible with their attack strategies. When an attack path is blocked, they have either rapidly pivoted to another vector or modified the environment to allow their favored path.

The Muddled Libra threat group has also repeatedly demonstrated a strong understanding of the modern incident response (IR) framework. This knowledge allows them to continue progressing toward their goals even as incident responders attempt to expel them from an environment. Once established, this threat group is difficult to eradicate.

Muddled Libra has shown a penchant for targeting a victim’s downstream customers using stolen data and, if allowed, they will return repeatedly to the well to refresh their stolen dataset. Using this stolen data, the threat actor has the ability to return to prior victims even after initial incident response. This demonstrates the attacker’s tenacity even after initially being discovered.

Furthermore, Muddled Libra has appeared to have clear goals for their breaches versus just capitalizing on opportunistic access. They’ve rapidly sought and stolen information on downstream client environments and then used it to pivot into those environments. They have demonstrated a strong understanding of their victims’ high-value clients and what information would be most useful for follow-on attacks.

## Attack Chain

While each incident is unique, Unit 42 researchers have identified enough commonalities in tactics, techniques and procedures (TTPs) to attribute multiple incidents to Muddled Libra. The attack chain is shown in Figure 1.

![Image 1 is the attack chain for Muddled Libra following the MITRE ATT&CK framework. Steps one to 11 go through reconnaissance, resource development, initial access, persistence, defense, ovation, credential, access, discovery, execution, lateral movement, collection, and finally exfiltration.](https://unit42.paloaltonetworks.com/wp-content/uploads/2023/06/word-image-128741-1.png)

Figure 1. Muddled Libra attack chain.

We have mapped these to the MITRE ATT&CK framework, which is summarized below.

### **Reconnaissance**

Muddled Libra has consistently demonstrated an intimate knowledge of targeted organizations, including employee lists, job roles and cellular phone numbers. In some instances, this data was likely obtained during earlier breaches against upstream targets.

Threat actors also frequently obtain information packs from illicit data brokers such as the [now-defunct Genesis and Russian Markets](https://therecord.media/genesis-market-russian-market-2easy-shop-cybercrim...
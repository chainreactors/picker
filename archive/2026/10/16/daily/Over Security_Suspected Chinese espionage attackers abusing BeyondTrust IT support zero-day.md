---
title: Suspected Chinese espionage attackers abusing BeyondTrust IT support zero-day
url: https://therecord.media/beyond-trust-cyberattack-china
source: Over Security
date: 2026-10-16
fetch_date: 2026-10-17T06:37:39.299235
---

# Suspected Chinese espionage attackers abusing BeyondTrust IT support zero-day

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

![BeyondTrust](https://cms.therecord.media/uploads/large_BT_1_e667ba6c47.jpg)

Image: BeyondTrust / maks\_d via Unsplash

[Jonathan Greig](/author/jonathan-greig)October 16th, 2026

# Suspected Chinese espionage attackers abusing BeyondTrust IT support zero-day

An alleged Chinese state-backed group is using a new zero-day in BeyondTrust software to conduct espionage attacks.

BeyondTrust, Mandiant and Google Threat Intelligence Group (GTIG) confirmed the zero-day on Thursday evening, [publishing](https://www.beyondtrust.com/blog/entry/bt26-05) [incident reports](https://cloud.google.com/blog/topics/threat-intelligence/armory-castle-exploits-beyondtrust) detailing attacks involving the bug.

The identity security company said the vulnerability affects its Remote Support appliances that enable IT teams to securely access and troubleshoot remote endpoints. A patch has been [released](https://www.beyondtrust.com/trust-center/security-advisories/bt26-05) addressing the issue and several mitigations are available. Other cybersecurity firms have since [confirmed](https://x.com/watchtowrcyber/status/2110877295825002979) exploitation.

The company said it was first tipped off to the bug — tagged as CVE-2026-102764 — on September 27, when an attack against another vendor's edge appliances became public and sparked an investigation into a similar issue. Mandiant also warned BeyondTrust of a potential vulnerability, sending the company’s engineering team on a hunt that led them back to a zero-day exploited on August 29.

Mandiant incident responders said the attackers were able to escalate their privileges after exploiting the bug, moving laterally within the victim’s network and establishing a deeper foothold.

They noted that the group behind the attacks — which they call Armory Castle or UNC5221 — “leveraged a deep understanding of BeyondTrust appliance internals” due to their abuse of proprietary tools. Mandiant saw the group use custom malware they call Sawfly and Bareclaw.

The threat actors found a way to get every credential the appliance stored and were able to modify files that survive reboots and configuration resets.

Mandiant warned that any vulnerable appliance that was reachable from the internet should be treated as potentially compromised until it has been reviewed.

## ‘Long-term intelligence collection’

BeyondTrust confirmed Mandiant’s assessment that Armory Castle is a Chinese “state-sponsored espionage operation focused on long-term intelligence collection.”

“ARMORY CASTLE’s documented targets include legal services, SaaS providers, business-process outsourcers, technology companies, and government,” the company said, noting that researchers believe the group targets technology firms to help with the discovery of other zero-day exploits.

The group was previously responsible for [exploiting](https://cloud.google.com/blog/topics/threat-intelligence/china-nexus-exploiting-critical-ivanti-vulnerability?e=0) multiple vulnerabilities in popular edge devices and was known to use passive backdoors and other novel tools to sustain their access to breached systems.

The group has been active since October 2023 and Google said they have “targeted a wide range of countries and verticals during their operations.”

“In past campaigns, ARMORY CASTLE has conducted widespread and opportunistic exploitation following the public disclosure of vulnerabilities it had exploited selectively as zero-days, racing to infiltrate target organizations before patches are deployed,” they said.

“It is possible that we will observe similar widespread exploitation attempts associated with CVE-2026-102764.”

Google compared the situation to previous incidents where the same threat actors conducted widespread exploitation of [two bugs affecting products from IT firm Ivanti](https://cloud.google.com/blog/topics/threat-intelligence/ivanti-connect-secure-vpn-zero-day) following their disclosure.

Armory Castle was also previously implicated in exploiting zero-days affecting Citrix as well as multiple issues in Ivanti products, including [CVE-2023-46805](https://nvd.nist.gov/vuln/detail/cve-2023-46805), [CVE-2024-21887](https://nvd.nist.gov/vuln/detail/cve-2024-21887), and [CVE-2025-0282](https://nvd.nist.gov/vuln/detail/cve-2025-0282).

“In 2025, Mandiant reported that the actor took an Ivanti patch for a flaw that had been rated low risk, studied it, and turned it into working remote code execution against unpatched appliances,” BeyondTrust said.

“The actor uses a zero-day selectively against chosen targets, and once the vulnerability is public, the actor typically moves to broad exploitation of every instance still unpatched.”

Last year, Mandiant and multiple U.S. agencies [warned](https://therecord.media/china-linked-hackers-brickstorm-backdoor-ip) about activity from the group [targeting](https://therecord.media/cisa-nsa-warn-brickstorm-china) governments, legal firms, software-as-a-service providers and technology companies.

* [News](/ukraine-says-starshield-working-again-after-disruption)
* [Cybercrime](/news/cybercrime)
* [Nation-state](/news/nation-state)

[![Recorded Future](https://cms.therecord.media/uploads/2025_0514_Record_Ads_300x1050_1_0f2f11757e.png)](https://www.recordedfuture.com/?utm_source=therecord&utm_medium=referral&utm_content=post-sidebar-ad)

[![Recorded Future](https://cms.therecord.media/uploads/2025_0514_Record_Ads_970x250_1_d144dbf901.png)](https://www.recordedfuture.com/?utm_source=therecord&utm_medium=referral&utm_content=post-footer-ad)

No previous article

No new articles

[![Jonathan Greig](https://cms.therecord.media/uploads/DSC_0283_1_a6f4e4e315.jpg)](/author/jonathan-greig)

[Jonathan Greig](/author/jonathan-greig)

is a Breaking News Reporter at Recorded Future News. Jonathan has worked across the globe as a journalist since 2014. Before moving back to New York City, he worked for news outlets in South Africa, Jordan and Cambodia. He previously covered cybersecurity at ZDNet and TechRepublic.

## Briefs

* [Proofpoint lines up $6.3 billion deal for Varonis’ data securityOctober 16th, 2026](/proofpoint-varonis-cybersecurity-acquisition)
* [North Macedonian police arrest alleged administrator behind OLVX cybercrime marketOctober 14th, 2026](/olvx-cybercrime-marketplace-arrest-north-macedonia)
* [Russian travel booking platform suspends reservations after cyberattackOctober 14th, 2026](/russia-anywayanyday-travel-website-cyberattack)
* [Ledger says hardware implant in cryptocurrency wallets stole recovery phrasesOctober 13th, 2026](/ledger-cryptocurrency-wallet-implant-theft)
* [South African clothing retailer Foschini Group investigating cyberattack on British fashion brandsOctober 13th, 2026](/foschini-group-south-africa-cyber)
* [Cyberattack disrupts refrigeration at hundreds of French supermarketsOctober 11th, 2026](/cyberattack-disrupts-refridgeration-in-france)
* [Japan confirms arrest of Russian Qilin operative, extradition to GermanyOctober 9th, 2026](/japan-germany-ransomware-arrest)
* [Leader of vast money mule operation that laundered cybercriminal proceeds pleads guiltyOctober 9th, 2026](/leader-of-money-mule-operation-for-cybercriminals-pleads-guilty)
* [US posts $10 million reward for accused Chinese ‘Hafnium’ hackerOctober 7th, 2026](/accused-hafnium-hacker-zhang-yu-10million-reward)

[## Russia Is Tightening Internet Controls, Leading to Operational Risks

![Russia Is Tightening Internet Controls, Leading ...
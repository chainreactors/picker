---
title: Sality, one of the longest-running botnets, finally gets disrupted
url: https://therecord.media/sality-botnet-cyber-doj
source: Over Security
date: 2026-09-02
fetch_date: 2026-09-03T07:02:46.152556
---

# Sality, one of the longest-running botnets, finally gets disrupted

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

![Botnet](https://cms.therecord.media/uploads/large_botnet_f7c0c917d0.jpg)

Image: Alex Shuper / Unsplash

[Alexander Martin](/author/alexander-martin)September 2nd, 2026

# Sality, one of the longest-running botnets, finally gets disrupted

U.S. and European authorities announced the disruption of Sality, one of the internet’s longest-running botnets, after turning the malware’s peer-to-peer architecture against itself to cut thousands of infected computers off from the suspected Russian operators controlling the network.

Active since at least 2003, the botnet was disrupted Monday in an operation involving authorities in the U.S., Bulgaria, Hungary and Romania, alongside cybersecurity company CrowdStrike and the nonprofit Shadowserver Foundation.

The U.S. Justice Department [announced](https://www.justice.gov/usao-cdca/pr/sality-malware-disrupted-international-cyber-takedown) the operation Tuesday, crediting Crowdstrike and partners with executing “a peer-to-peer sinkhole operation.” Sinkholing refers to the practice of redirecting infected computers away from the criminals’ servers toward infrastructure controlled by cybersecurity defenders.

But unlike botnets built around a central command-and-control server, Sality relied on infected computers communicating directly with one another. The decentralized design made the network resilient to normal sinkholing as there was no single server that the network could have been redirected away from or toward.

CrowdStrike researcher Tillmann Werner [told](https://www.reuters.com/legal/government/russian-cybercrime-operation-being-dismantled-after-two-decades-us-officials-2026-09-01/) Reuters the disruption required extensive reverse-engineering and was the most complex botnet takeover the company had ever conducted. According to a post on the company’s [blog](https://www.crowdstrike.com/en-us/blog/inside-sality-botnet-disruption-operation/), it was ultimately able to sever the connection between more than 15,000 infected computers.

Investigators targeted the mechanism Sality used to maintain the decentralized network. Each infected machine keeps a list of publicly reachable systems known as “super peers” that help pass information between bots, and CrowdStrike said its researchers targeted these lists.

By injecting false information into the “super peer” lists, the company was able to cause infected computers to lose contact with other members of the botnet and, ultimately, its operator. The isolated machines could no longer receive commands or download new malware.

No arrests were announced and authorities have not publicly identified the operator. CrowdStrike assesses that the group behind Sality operates from the Bashkortostan region in Russia.

Authorities said they also moved against infrastructure outside the peer-to-peer network, with Sality-linked domains in the U.S. being seized, while authorities in Bulgaria, Hungary and Romania seized additional domains in Europe that infected systems could otherwise have used to retrieve new payloads.

Sality began in 2003 as a virus that infected executable files, spreading when compromised files were copied between computers. It later developed into a peer-to-peer botnet capable of distributing malware used for credential theft, spam, proxy services, network exploitation and denial-of-service attacks.

For roughly the past eight years, CrowdStrike said, Sality primarily distributed EggJagger, malware designed to monitor a computer’s clipboard for cryptocurrency wallet addresses. When one is detected, EggJagger can replace the copied address with one controlled by the attacker, redirecting a payment if the victim does not notice the substitution before completing the transaction.

CrowdStrike estimated the operator stole at least $150,000 in cryptocurrency through this technique. It said the total takings were enough to sustain a single criminal actor operating with minimal overhead, but noted payloads other than EggJagger may have provided additional revenue streams.

Shadowserver is working with internet service providers and national computer-security response teams to identify the more than 15,000 infected systems still connected to Sality when it was disrupted and to alert their owners.

David Watson, a director at Shadowserver, told Reuters that Sality was “quite old-school” but said the botnet remained dangerous because compromised machines could still provide attackers with a foothold inside organizations.

U.S. officials presented the action as an example of cooperation between law enforcement and the cybersecurity industry and linked it to the Trump administration’s [cyber strategy](https://therecord.media/trump-cyber-strategy-released-regulations), whose first pillar calls for the U.S.to shape adversary behavior.

Sality’s operator remains publicly unidentified and at large. It is not clear if the disruption will prevent them from attempting to rebuild the botnet or develop replacement infrastructure.

* [News](/ukrainian-software-developer-court-switzerland)
* [Cybercrime](/news/cybercrime)
* [Malware](/news/malware)

[![Recorded Future](https://cms.therecord.media/uploads/2025_0514_Record_Ads_300x1050_1_0f2f11757e.png)](https://www.recordedfuture.com/?utm_source=therecord&utm_medium=referral&utm_content=post-sidebar-ad)

[![Recorded Future](https://cms.therecord.media/uploads/2025_0514_Record_Ads_970x250_1_d144dbf901.png)](https://www.recordedfuture.com/?utm_source=therecord&utm_medium=referral&utm_content=post-footer-ad)

No previous article

No new articles

[![Alexander Martin](https://cms.therecord.media/uploads/headshot_79eb085f87.jpeg)](/author/alexander-martin)

[Alexander Martin](/author/alexander-martin)

is the UK Editor for Recorded Future News. He was previously a technology reporter for Sky News and a fellow at the European Cyber Conflict Research Initiative, now Virtual Routes. He can be reached securely using Signal on: AlexanderMartin.79

## Briefs

* [Health data of more than 9.5 million people leaked from Aesto record systemSeptember 2nd, 2026](/health-data-aesto-cyberattack-leak)
* [Slovenian casinos reopen after cyberattack knocked gaming systems offlineAugust 31st, 2026](/slovenia-cyberattack-casinos-reopen)
* [Large DDoS attack knocks Norwegian public services offlineAugust 25th, 2026](/norway-cyberattack-ddos-government)
* [New Zealand to pursue social media ban for children under 16August 24th, 2026](/new-zealand-to-pursue-social-media-ban-for-children)
* [Canada’s Hospital for Sick Children attacked by cybercriminals again as employee data stolenAugust 21st, 2026](/canada-hospital-for-sick-children-attacked-again-employee-data)
* [Electronic health record company CareCloud says 3.7 million people affected by breachAugust 19th, 2026](/electronic-health-record-company-carecloud-data-breach)
* [University of Texas forced to take systems offline in San Antonio after cyberattackAugust 18th, 2026](/university-of-texas-forced-to-take-systems-offline-cyberattack-san-antonio)
* [Ukraine says cyberattack hit Russian e-commerce giant Wildberries amid drone strikesAugust 17th, 2026](/russia-wildberries-cyberattack-ukraine)
* [New Mirai variant adds stealth capabilities to notorious botnet codeAugust 13th, 2026](/new-mirai-variant-adds-stealth-to-botnet-code)

[## BlueDelta Targets Defense and Diplomacy with HOOKEDGE

![BlueDelta Targets Defense and Diplomacy with HOOKEDGE](https://www.recordedfuture.com/research/med...
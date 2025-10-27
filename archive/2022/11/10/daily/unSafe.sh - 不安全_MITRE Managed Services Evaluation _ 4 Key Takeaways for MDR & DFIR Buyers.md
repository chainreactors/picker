---
title: MITRE Managed Services Evaluation | 4 Key Takeaways for MDR & DFIR Buyers
url: https://buaq.net/go-134930.html
source: unSafe.sh - 不安全
date: 2022-11-10
fetch_date: 2025-10-03T22:12:47.043289
---

# MITRE Managed Services Evaluation | 4 Key Takeaways for MDR & DFIR Buyers

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

![](https://8aqnet.cdn.bcebos.com/8272383f4499d390d9d7b59bafcd25bc.jpg)

MITRE Managed Services Evaluation | 4 Key Takeaways for MDR & DFIR Buyers

As the cyber threat landscape grows increasingly treacherous and sophisticated, more teams are look
*2022-11-9 22:44:4
Author: [www.sentinelone.com(查看原文)](/jump-134930.htm)
阅读量:15
收藏*

---

As the cyber threat landscape grows increasingly treacherous and sophisticated, more teams are looking to augment their often-limited internal cybersecurity resources with the expertise and hands-on assistance offered by managed detection and response (MDR) services and managed security service providers (MSSPs). Gartner estimates that by 2025, 50% of organizations using endpoint detection and response (EDR) technology will enlist the help of a managed security service partner.

## About the MITRE Engenuity ATT&CK® Evaluation of Managed Security Services

In response to the growing needs of today’s cybersecurity teams and buyers, MITRE Engenuity has just published its [debut ATT&CK Evaluation of Managed Security Services](https://attackevals.mitre-engenuity.org/managed-services/managed-services/). MITRE Engenuity has quickly evolved to become the industry standard for third party evaluation of cybersecurity solutions. The independent evaluations provide rigorous analysis based on the ATT&CK® framework and knowledge base with the intent to help organizations combat today’s sophisticated cyber threats and improve their threat detection capabilities.

SentinelOne has participated in more comprehensive MITRE evaluations than any other cybersecurity leader, being the only XDR vendor to have participated in three years of ATT&CK Enterprise Evaluations, the inaugural Deception evaluation, and the inaugural Managed Services evaluation. Learn more about SentinelOne’s leading performance in MITRE Engenuity’s Enterprise ATT&CK and Deception evaluations [here](https://www.sentinelone.com/lp/mitre/).

MITRE summarizes its newest Managed Services evaluation below:

*ATT&CK Evaluations for Managed Services will assess vendor participant capabilities in their ability to analyze and describe adversary behavior. Adversary activity emulated by the MITRE Engenuity red team, and correlating context provided by the participants will be mapped to the MITRE ATT&CK knowledge base.*

As part of the evaluation process, participants like SentinelOne were tasked with understanding adversary activity without prior knowledge of the emulated adversary, and provide their analysis as if MITRE Engenuity was a standard MDR customer.

In this blog post, we’ll outline the key takeaways from our Vigilance MDR team’s participation in the inaugural MITRE Engenuity ATT&CK Evaluation for Managed Services. These takeaways are especially relevant for those considering or actively evaluating MDR and digital forensics & incident response (DFIR) services.

![](https://www.sentinelone.com/wp-content/uploads/2022/11/MITRE-Managed-Services-Evaluation-4-Key-Takeaways-for-MDR-DFIR-Buyers-3.jpg)

## Takeaway 1: The Right Data Leads to the Right Decisions

While identifying the emulated adversary in this scenario seems like table stakes, proper adversary attribution unlocks *actionability*.

Based on the activity detected on this user endpoint, forensic artifacts collected, and the tactics, techniques, and procedures (TTPs) observed throughout the campaign, the SentinelOne Vigilance team was able to correctly attribute the attack to Iranian threat actor group APT 34, also known as OilRig.

Beyond just identifying the emulated adversary, the Vigilance team leveraged first party and open threat intelligence to provide additional insight into OilRig. The team’s reporting included a summary of the adversary and the group’s evolution over time, commonly exploited tools by the adversary, and all of their known associated TTPs.

As an MDR & DFIR buyer, it is important to consider whether the information you receive from your service partner is meaningful and actionable. While comprehensive reporting is a must, time and resource-constrained analysts benefit from analysis that is pertinent, timely, and distinguishes between insight and overwhelming detail.

In addition to the remediation guidance offered in-platform, Vigilance reporting focuses on what customers need to know to evaluate risk, assess incident impact, and mitigate threats for the immediate and long term.

## Takeaway 2: Detection Is Half the Battle, Protection Is the Endgame

For the purposes of the evaluation, participants were tasked with detecting and understanding adversary activity through the entire attack, without intervening to prevent or remediate the threat. Over a 10-step campaign, our Vigilance team was able to track the adversary from end to end as they infiltrated the simulated environment through a phishing attack with a malicious attachment, performed reconnaissance on the host and environment, moved laterally to a critical server, and exfiltrated corporate data.

It is crucial to note, however, that a real-life application of detection and response technology and MDR services should be aimed at preventing and mitigating such attacks as quickly as possible—before the adversary can perform recon, move laterally, or steal data.

In a live scenario of this incident, the SentinelOne Singularity platform and Vigilance services would have stopped the attack from the very first detection. If set to “Protect” mode rather than “Detect-Only”, the Sentinel Agent would be equipped to autonomously kill the entire chain in an instant, without analyst intervention, rather than allowing the attack to execute over the course of several days. This would have prevented any further movement or downstream business impacts associated with this campaign.

## Takeaway 3: Real-Time Response Maximizes Cyber Resilience

Time is of the essence in a real-world attack scenario. By a similar principle as our last takeaway, organizations should aim to eradicate malicious actors from their environment as soon as they’re detected, and have the confidence in their MDR partner to do just that.

Though the ATT&CK evaluation did not include a service level agreement (SLA) as part of its criteria, this should be a significant consideration for those evaluating MDR and DFIR services. The true efficacy of an MDR team often comes down to their ability to detect, contain, and mitigate a threat as quickly and effectively as possible, all with the goal of minimizing the impact of a cyber incident.

At SentinelOne, our Vigilance analysts are able to respond to events at often unmatched speeds. This is due in part to the robust autonomous capabilities of the Sentinel Agent, which can kill and quarantine threats at the endpoint level before a human ever intervenes. Additionally, Vigilance analysts take action on alerts that come with real-time, machine-generated context produced by SentinelOne’s patented Storyline™ technology. This allows an analyst to view and understand the entire progression of an attack in one pane of glass, instantly. On average, Vigilance minimizes attacker dwell time to just 20 minutes.

For many other MDR and MSSP-delivered services, the process of connecting the dots, building context, validating true vs. false positives, and containing threats is often a heavily manual effort, which may lead to longer overall response times.

## Takeaway 4: There is More to MDR — DFIR Is the Difference

Although the 24×7 security monitoring offered by MDR services provides organizations with a reliable safety blanket, the reality of today’s digital world is that no organization is 100% impen...
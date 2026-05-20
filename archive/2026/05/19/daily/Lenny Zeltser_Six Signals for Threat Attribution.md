---
title: Six Signals for Threat Attribution
url: https://zeltser.com/six-signals-for-threat-attribution
source: Lenny Zeltser
date: 2026-05-19
fetch_date: 2026-05-20T06:05:25.877750
---

# Six Signals for Threat Attribution

[Lenny Zeltser](/)Security builder & leader

 [Projects](/projects) [Writing](/writing) [About](/about)

×

# Six Signals for Threat Attribution

Intelligence analysts weigh six signals together to build defensible attribution to a threat actor. For each one, they use a disciplined methodology we can cite and stress-test.

![Six Signals for Threat Attribution - illustration](/assets/six-signals-for-threat-attribution.CmsZiaIv_18Fe8d.webp)

“A Chinese state-sponsored group.” “Tied to APT41.” “ShinyHunters.” Phrases like these appear in vendor advisories, government bulletins, and news coverage. We use them to inform response steps, vendor decisions, and conversations with leadership. The work that produces them is typically done by security vendors, government agencies, and enterprise threat intelligence teams. Some incident response teams track attribution signals when connecting an intrusion to a known cluster of activity.

Threat attribution is the process by which analysts link cyber intrusions to the actors behind them. They build attribution cases to defend against the next campaign, predict the actor’s next move, and share defensible findings with customers, regulators, and partners. Whether you produce such conclusions or rely on them, let’s look at how the work gets done when the picture is incomplete and the stakes are high.

## Three Levels of Attribution

Threat attribution has three levels, per Thomas Rid and Ben Buchanan’s [“Attributing Cyber Attacks”](https://ridt.co/d/rid-buchanan-attributing-cyber-attacks.pdf) (the Q Model), each requiring different evidence to support its claims:

* **Tactical:** We examine the incident’s technical aspects.
* **Operational:** We characterize the campaign and the actor running it.
* **Strategic:** We ask who is responsible and why the operation matters.

Across those levels, one way to build a defensible attribution case is to weigh six signals: *Victim*, *Targeting Intent*, *Tradecraft*, *Tooling*, *Identity Artifacts*, and *Infrastructure*.

## Victim: The Targeting Profile

When examining the Victim signal, we ask who was targeted and what sector the threat actor operates in. The [Diamond Model of Intrusion Analysis](https://www.activeresponse.org/wp-content/uploads/2013/07/diamond.pdf) by Sergio Caltagirone, Andrew Pendergast, and Christopher Betz treats *Victim* as one of four features for any intrusion. When targets share a profile, the Victim signal is a strong input to attribution.

The victim profile helps identify a potential threat actor and rule out one whose targets don’t fit. For example, a [CISA joint advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a) on Salt Typhoon identifies targets across telecom, government, transportation, lodging, and military networks. These sectors carry intelligence value and suggest a government-affiliated actor. A threat actor focused on e-commerce operations doesn’t fit this profile and is likely to be a different crew.

The Victim signal doesn’t work on its own, since threat actors can also pursue atypical or opportunistic targets.

## Targeting Intent: What the Threat Actor Pursued

Targeting Intent is what a threat actor pursued, meaning the data, access, or operational effects they prioritized. By examining what a threat actor collects, copies, or destroys, we narrow the field of suspects.

A US [Justice Department indictment](https://www.justice.gov/opa/pr/seven-international-cyber-defendants-including-apt41-actors-charged-connection-computer) of defendants tied to APT41 describes the theft of source code, software code-signing certificates, customer account data, and business information across a wide range of victim organizations. This combination of intelligence-style espionage and revenue-motivated theft became part of the attribution argument that APT41 operated with both state-aligned and criminally motivated objectives.

Motive can be hard to infer from Targeting Intent alone, and the signal gets stronger when infrastructure and tradecraft support the same conclusion.

## Tradecraft: The Threat Actor’s Method

[Tradecraft](https://en.wikipedia.org/wiki/Tradecraft) is an intelligence-community term for a threat actor’s habits, including lure documents, social-engineering pretexts, phishing tactics, and timing. MITRE ATT&CK organizes these behaviors under tactics such as [Initial Access](https://attack.mitre.org/tactics/TA0001/) and techniques such as [Phishing](https://attack.mitre.org/techniques/T1566/), with sub-techniques for spearphishing attachments, links, services, and voice. ATT&CK is useful for attribution because it gives analysts a shared vocabulary for behaviors that persist across campaigns.

A joint CISA-FBI-Treasury [advisory on TraderTraitor](https://www.cisa.gov/news-events/cybersecurity-advisories/aa22-108a) describes how the Lazarus Group approached cryptocurrency-company employees in system administration and DevOps across a variety of communication platforms, with spearphishing messages that “mimic a recruitment effort and offer high-paying jobs” to deliver trojanized cryptocurrency applications. The same recruitment-style lure pattern recurred across years and platforms, allowing intelligence analysts to attribute new campaigns to the group.

Tradecraft alone doesn’t settle attribution, and the signal gets stronger when tooling, identity artifacts, and infrastructure support the same conclusion.

## Tooling: The Threat Actor’s Toolchain

Tooling covers the malware families, frameworks, and custom code a threat actor uses. We can identify Tooling through toolmarks. Debug strings, embedded paths, language packs, compiler artifacts, custom encoding routines, and reused error-handling code all reveal fingerprints of the development environment. David Bianco’s [“Pyramid of Pain”](https://detect-respond.blogspot.com/2013/03/the-pyramid-of-pain.html) places tools close to the top of the indicator hierarchy because changing them is costly for the threat actor.

Public threat reports document the specific toolmarks of named campaigns. Some examples:

* The Salt Typhoon advisory mentioned earlier documents specific exploits and router-configuration commands the actors used, which lets defenders link new intrusions to the same group.
* [Citizen Lab’s review](https://citizenlab.ca/2021/07/amnesty-peer-review/) of Amnesty International’s Pegasus methodology walks through process names, installation-server traffic, and iOS backup patterns that attribute a compromise to NSO Group’s Pegasus spyware, narrowing the field to NSO’s government customers.

Defensible attribution requires Tooling evidence accumulated across multiple operations. The signals are consistent enough for defenders to hunt on and for analysts to cross-check. However, threat actors can strip compiler metadata, randomize string tables, and rotate their toolchain.

Threat actors can also forge toolmarks to mimic other groups. The Olympic Destroyer malware that hit the PyeongChang Winter Olympics carried a [forged header](https://www.wired.com/story/untold-story-2018-olympics-destroyer-cyberattack/) that mimicked the Lazarus Group’s fingerprints, and initial analysis pointed to North Korea. [Kaspersky’s GReAT team reconstructed the deception](https://securelist.com/olympicdestroyer-is-here-to-trick-the-industry/84295/), and a [US Justice Department](https://www.justice.gov/archives/opa/pr/six-russian-gru-officers-charged-connection-worldwide-deployment-destructive-malware-and) indictment later named six GRU officers for the attack.

## Identity Artifacts: The Threat Actor’s Trail

Identity Artifacts are the trail threat actors leave behind, including code-signing certificates, domain registrant data, email and persona reuse, and payment trails. They cut across operational and strategic levels. Reused identities can become some of the most durable evidence in an attribution case.

A persona-reuse trail can sometimes lead investigators to a threat...
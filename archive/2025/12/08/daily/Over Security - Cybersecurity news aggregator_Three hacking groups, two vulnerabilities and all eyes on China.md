---
title: Three hacking groups, two vulnerabilities and all eyes on China
url: https://therecord.media/three-hacking-groups-two-vulnerabilities-china-microsoft
source: Over Security - Cybersecurity news aggregator
date: 2025-12-08
fetch_date: 2025-12-09T03:18:10.981434
---

# Three hacking groups, two vulnerabilities and all eyes on China

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

![china](https://cms.therecord.media/uploads/format_webp/large_china4_1_2bf7a51ad5.jpg)

Image: Vmenkov/Choinowski via Wikimedia Commons (CC BY-SA 3.0/4.0)/Wesley Tingey via Unsplash+/Photomosh

[Alexander Martin](/author/alexander-martin)December 8th, 2025

# Three hacking groups, two vulnerabilities and all eyes on China

On the main stage at the Pwn2Own hacking competition in Berlin this March, researchers demonstrated it was possible to remotely compromise sensitive information via Microsoft’s on-premise SharePoint software — the first glimpse that the world got of two dangerous software vulnerabilities threatening governments and enterprises around the globe.

SharePoint is used by large organizations as a repository storing many kinds of confidential documents; from procurement data to internal memos and legal filings. It is also deeply integrated with Microsoft’s authentication services, meaning skillful enough hackers could use a foothold there to burrow deeper into their victims’ networks.

The plan to prevent hackers from ransacking these organizations, as per the rules of Pwn2Own, was for Viettel Cyber Security researchers to privately disclose their findings to Microsoft before discussing them publicly. Microsoft’s engineers would then issue patches for the bugs and deprive malicious actors of a foothold for attacking the company’s customers.

But instead, four months after the Pwn2Own demonstration, at least hundreds of Microsoft’s customers found their on-premise SharePoint servers being plundered in what researchers began to call the ToolShell campaign. Notably, it wasn’t just one group behind these cyberattacks but three distinct hacking organizations, all based in China, and all exploiting the same issues contemporaneously.

The incident has raised questions that researchers say need to be understood to defend against a growing threat posed by Beijing’s cyber apparatus. What does it mean that three separate China-linked groups all moved on the same SharePoint vulnerabilities at nearly the same time? Were the three threat clusters truly independent, how did they all obtain workable exploits so quickly, and what were their ultimate objectives? The answers remain unconfirmed — but some experts warn the emerging pattern is concerning.

## Sounding the alarm

On July 8, Microsoft issued patches for the flaws, formally acknowledged as CVE-2025-49704 and CVE-2025-49706. But less than two weeks later, the company made a rare and unusually urgent update about those patches. It warned that not only were hackers attempting to exploit on-premise SharePoint servers that hadn’t been patched, but that the company was issuing an additional fix. The hackers had found a way to bypass the first one.

Microsoft’s warning sent ripples of concern throughout the cybersecurity community. The first unusual observation from Microsoft was that the company said its telemetry suggested the SharePoint vulnerabilities were being exploited as early as July 7 — a day before the fixes were issued. And then the company named not one, but three separate hacking groups that it said had been attempting to use CVE-2025-49704 and CVE-2025-49706 since that date.

The groups — which Microsoft referred to as Linen Typhoon, Violet Typhoon and Storm-2603 — represented the breadth of the Chinese hacking ecosystem, with ties to the People’s Liberation Army (PLA), Ministry of State Security and ransomware groups.

Additionally, Microsoft acknowledged two new vulnerabilities, CVE-2025-53770 and CVE-2025-53771, both of them developments on the previous flaws it had attempted to fix. It said that the hacking groups had already been using the bypass, suggesting the attackers had a surprisingly deep understanding of the flaw and were well-resourced enough to attempt to exploit it to its full potential.

The government and industry responses confirmed the hacking campaigns were having a large impact. A Dutch cybersecurity firm called Eye Security said hackers had successfully breached at least 400 governments and businesses around the world, while an official from the U.S. Cybersecurity and Infrastructure Security Agency (CISA) told [Recorded Future News](https://therecord.media/microsoft-says-warlock-ransomware-deployed-in-sharepoint-attacks) federal and state agencies had been affected.

## The search for explanations

As Microsoft and government officials investigate the ToolShell campaign, a major question is how three different Chinese groups obtained working exploits so quickly. One theory involves Microsoft’s own efforts to keep customers safe. Before patching the flaws, the company quietly alerted a select group of partners through its Microsoft Active Protections Program (MAPP) to give defenders a heads-up and prepare their defences. Suspicions have turned towards the participation of Chinese companies in the program.

Under Chinese law, all organizations and individuals in the country have a legal duty to report new software vulnerabilities to the government — even before disclosing them to the vendor. Some of the MAPP participants in China are also partners of the China National Vulnerability Database (CNNVD), an apparatus operated by the MSS, which is considered to increase the risk of knowledge transfer to China’s intelligence services despite Microsoft’s non-disclosure agreements.

Sveva Vittoria Scenarelli, a principal threat intelligence analyst at Recorded Future, said the “possibility of leaks from participating partners” was one area of scrutiny. No such transfer between a MAPP partner and the MSS has been publicly confirmed. Microsoft announced in August that, after reviewing the ToolShell campaign, it was going to be restricting access to MAPP for several Chinese organizations.

“China is pretty unique in the way it handles vulnerability disclosure,” said Scenarelli, noting that no other country “by law mandates any individual or company to report zero-days to the state first before reporting it even to the impacted vendor.”

Beijing itself denies engaging in any offensive cyber operations. But even if external analysts believe the legal framework exists for vulnerabilities to be processed and distributed via the CNNVD, there are operational challenges around doing so and questions about the involvement of hacking groups linked to the PLA.

Rafe Pilling, the director of threat intelligence at Sophos, explained that normally, hacking groups don’t share tooling because of the risk one group’s operations would trip-up another’s. “Zero-days are valuable commodities, and every time you use one, you risk it becoming burned and its value rapidly dwindling, particularly for the targets that state-sponsored espionage groups are after.”

Feeding into this is the cadence driven by the patching cycle, said Scenarelli. “By the point a vulnerability is publicly disclosed, let alone a patch being released, the knowledge advantage is burned,” she said. “So if before that, there might have been opportunities for a threat group to conduct a low and slow campaign against a few dozen really high value targets. Suddenly that expands to, ‘I’ve got to establish my access to anything I can. I’ve got to take the opportunity, because otherwise I might not be able to capitalize on this capability’.”

Only after those threat actors have established their initial access at scale do they then triage and select which targets would be their priorities, and attempt “move on those befo...
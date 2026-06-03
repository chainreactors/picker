---
title: Red Hat removes tainted packages after software pipeline compromise
url: https://therecord.media/red-hat-removes-tainted-packages-after-software-pipeline-compromise
source: Over Security
date: 2026-06-02
fetch_date: 2026-06-03T06:46:47.946872
---

# Red Hat removes tainted packages after software pipeline compromise

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

![digital](https://cms.therecord.media/uploads/large_data_digital_2f719ba936.jpg)

Image: Unsplash+/Getty

[Alexander Martin](/author/alexander-martin)June 2nd, 2026

# Red Hat removes tainted packages after software pipeline compromise

Red Hat pulled dozens of packages from its software distribution pipeline on Monday after attackers used a compromised GitHub account to distribute credential-stealing malware to developers.

According to the company’s own [preliminary analysis](https://access.redhat.com/security/vulnerabilities/RHSB-2026-006), a compromised GitHub account was used to push the malicious code out to customers, hitting 32 packages downloaded roughly 117,000 times a week.

Red Hat said it had since removed the affected packages and that “based on current findings, no actions from customers are required.”

The attack used a variant of the Mini Shai-Hulud self-propagating worm whose complete source code was published online May 12 by a cybercriminal group tracked as TeamPCP. As cybersecurity company Tenable [noted](https://www.tenable.com/blog/mini-shai-hulud-frequently-asked-questions), the criminals “simultaneously announced a $1,000 contest on BreachForums for the largest supply chain attack using the code.”

Whether Monday's attack was carried out by TeamPCP itself or a separate actor using its published code could not be immediately determined, researchers said. Palo Alto Networks' Unit 42 [warned](https://unit42.paloaltonetworks.com/monitoring-npm-supply-chain-attacks/) that the open-sourcing of the worm's code had already spawned copycat activity, making definitive attribution harder, and that Mini Shai-Hulud “is no longer scoped to TeamPCP.”

The attack's malware, which its authors named Miasma, differed from the TeamPCP original only cosmetically, with references to the science-fiction series Dune replaced by Greek mythology while the underlying credential-stealing functionality remained intact.

Monday's attack is the latest in a cascading series of supply chain intrusions stretching back to September 2025 — when the original Shai-Hulud worm prompted [a CISA advisory](https://therecord.media/cisa-urges-software-reviews-malicious-packages) — that have struck some of the world's most widely used developer tools.

Recent incidents have included an attack in March on [LiteLLM](https://therecord.media/supply-chain-attack-hits-widely-used-ai-package), which allowed the cybercriminals to breach several organizations including [AI recruiting company Mercor](https://therecord.media/mercor-confirms-security-incident-tied-to-litellm). The attack on LiteLLM was followed by a separate wave of compromises [attributed to North Korean hackers](https://therecord.media/google-links-axios-supply-chain-attack-north-korea) targeting the axios JavaScript library.

That campaign prompted Mandiant chief technology officer Charles Carmakal to warn “the secrets stolen over the past two weeks will enable more software supply chain attacks, software-as-a-service environment compromises, ransomware and extortion events, and crypto heists over the next several days, weeks, and months.”

In May, [GitHub confirmed](https://therecord.media/github-confirms-teampcp-hack-customers-unaffected) it had been breached by TeamPCP after an employee's device was compromised via a malicious Visual Studio Code extension, with the group demanding $50,000 for stolen source code and threatening to leak it for free if no buyer came forward.

OpenAI had also [warned](https://therecord.media/openai-asks-macos-users-to-update-tanstack-npm) that two of its employee devices had been compromised in the same wave, following a supply chain attack on the open-source library TanStack.

Speaking at the time of the LiteLLM compromise, Adam Reynolds, senior security researcher at Sonatype, warned that because “the malware targets such a broad range of credentials … this creates the potential for second- and third-order effects that may ripple outward over time, leading to further breaches, service disruptions, or misuse of sensitive data well beyond the initial point of compromise.”

* [Cybercrime](/news/cybercrime)
* [Industry](/)
* [News](/)

Get more insights with the

Recorded Future

Intelligence Cloud.

[Learn more.](https://www.recordedfuture.com/platform?mtm_campaign=ad-unit-record)

[![Recorded Future](https://cms.therecord.media/uploads/2025_0514_Record_Ads_300x1050_1_0f2f11757e.png)](https://www.recordedfuture.com/?utm_source=therecord&utm_medium=ad)

[![Recorded Future](https://cms.therecord.media/uploads/2025_0514_Record_Ads_970x250_1_d144dbf901.png)](https://www.recordedfuture.com/?utm_source=therecord&utm_medium=ad)

No previous article

No new articles

[![Alexander Martin](https://cms.therecord.media/uploads/headshot_79eb085f87.jpeg)](/author/alexander-martin)

[Alexander Martin](/author/alexander-martin)

is the UK Editor for Recorded Future News. He was previously a technology reporter for Sky News and a fellow at the European Cyber Conflict Research Initiative, now Virtual Routes. He can be reached securely using Signal on: AlexanderMartin.79

## Briefs

* [Spain arrests suspected hacker for publishing personal data of police, prosecutors and cyber officialsJune 1st, 2026](/spain-arrests-suspected-hacker-for-publishing-data-on-sensitive-government-workers)
* [Canadian man gets 33 years for using social media to coerce US children into sending sexual contentMay 28th, 2026](/canadian-man-gets-33-years-social-media-luring-kids)
* [Chinese-speaking fraud gang could be stealing millions from 2026 World Cup fansMay 28th, 2026](/chinese-speaking-fraud-gang-fifa-world-cup-scam)
* [Romanian national sentenced to more than 4 years for hacking Oregon government systemsMay 27th, 2026](/romanian-national-sentenced-to-over-4-years-oregon-hack)
* [Dutch police arrest man over cyber breach at Ajax football clubMay 27th, 2026](/dutch-police-arrest-man-over-cyber-breach-ajax-football)
* [Ukraine probes teen suspect in cyber theft scheme targeting California online shoppersMay 20th, 2026](/ukraine-probes-teen-suspect-cyber-theft-scheme)
* [Discord migrates all users to end-to-end encryption by defaultMay 20th, 2026](/discord-migrates-users-to-end-to-end-encryption)
* [7-Eleven confirms breach after ShinyHunters claimsMay 20th, 2026](/7-eleven-reports-data-breach-shinyhunters)
* [Texas, Florida top list of states reporting millions of dollars lost through crypto ATMsMay 20th, 2026](/texas-florida-top-list-of-crypto-atm-scam-losses)

[## Iran Expands Handala Brand to Physical Threats

![Iran Expands Handala Brand to Physical Threats](https://www.recordedfuture.com/research/media_14c4348cdfe3e4e2b574896b502432695b25c37a9.gif?width=1200&format=pjpg&optimize=medium)](https://www.recordedfuture.com/research/iran-handala-physical-threats)

[## Quantum Risk Explained

![Quantum Risk Explained](https://www.recordedfuture.com/research/media_1163dd082af56f227c5eaa25ef0f7c257c8609133.gif?width=1200&format=pjpg&optimize=medium)](https://www.recordedfuture.com/research/quantum-risk-explained)

[## Hacking Embodied AI

![Hacking Embodied AI](https://www.recordedfuture.com/research/media_165d0d375ab46bd1deb3705cf840ece4d870213cb.gif?width=1200&format=pjpg&optimize=medium)](https://www.recordedfuture.com/research/hacking-embodied-ai)

[## Risk Scenarios for the US’s Strategic Pivot

![Risk Scenarios for the US’s Strategic Pivot](https://www.recordedfuture.com/research/media_131592ae03a082c06f...
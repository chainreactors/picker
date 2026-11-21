---
title: Amazon says Chinese hackers used Cairn AI tool to discover apparent zero-day during attack on university
url: https://therecord.media/amazon-research-cairn-ai-university-attacks-possible-zero-day
source: Over Security
date: 2026-11-20
fetch_date: 2026-11-21T09:02:14.849190
---

# Amazon says Chinese hackers used Cairn AI tool to discover apparent zero-day during attack on university

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

![AI illustration](https://cms.therecord.media/uploads/large_ai_planet_volumes_unsplash_79b8f00a24.jpg)

Image: Planet Volumes via Unsplash

[Jonathan Greig](/author/jonathan-greig)November 20th, 2026

# Amazon says Chinese hackers used Cairn AI tool to discover apparent zero-day during attack on university

Chinese hackers used an AI tool called Cairn to allegedly discover a zero-day while breaching several universities in Asia, according to a new report from Amazon’s Threat Intelligence team.

CJ Moses, CISO of Amazon Integrated Security, said their [investigation](https://aws.amazon.com/blogs/security/chinese-nexus-actors-cairn-ai-agents-found-a-zero-day-on-their-own/) began on September 10, when they discovered a publicly accessible server with a publicly hosted instance of Cairn — an open-source autonomous AI penetration-testing framework.

They were able to view the operational history of the platform, including previous prompts and more. The operator wrote their prompts in Simplified Chinese and the timestamps were configured to China Standard Time. The targeted victim organizations were universities in East Asia.

Moses explained that Cairn is ideal for attackers because, when given a starting point and objective in plain language, it can coordinate multiple AI agents to complete a task.

In this incident, the attacker provided IP addresses and asked Cairn to “obtain shell access” — meaning find a way to gain enough access to a system for various actions to be taken.

“Based on those inputs, the AI agents planned, executed, and adjusted their approach as they learned, without the operator choosing each next step,” Moses said.

One of the attempts involved 148 actions taken over 16 hours that were ultimately unsuccessful, including a failed attempt at exploiting the Log4Shell vulnerability. Another failed effort saw Cairn try for more than six hours to breach university servers by testing more than 30,000 credential combinations tied to 80 real usernames.

The only successful attempt occurred when the agents discovered a vulnerability in an open-source medical imaging AI application and exploited it.

“At the time of discovery, this path traversal vulnerability in the medical imaging application did not correspond to any assigned security advisory and was unpatched,” Moses said.

“Amazon Threat Intelligence assesses with high confidence that it was a zero-day based on the absence of any corresponding fix, issue, advisory, or prior mention in vulnerability databases for the affected open-source project.”

The attacker then used the same apparent zero-day to breach a second university.

Moses said Amazon Threat Intelligence contacted the maintainers behind the open-source medical imaging AI application and they [fixed the bug](https://github.com/Project-MONAI/MONAILabel/security/advisories/GHSA-qc22-rmgc-vg94) that was discovered.

He added that AWS “worked with a government partner to notify the organizations about the activity.” AWS declined to name the universities or the country they are in.

Moses said the campaign stood out because of the speed and operational tempo of the AI agents.

An agent that discovers and exploits a zero-day in minutes “completes its activity faster than many security operations centers can manually triage an alert,” Moses warned, noting that the agents “ran continuously for 16 hours without breaks, sleep, or working-hour constraints.”

## Artex vs. Cairn

Cybersecurity researchers and law enforcement agencies have released multiple warnings in recent weeks about AI-backed offensive cyber tools that are being used by attackers, particularly those from China.

The FBI [published an advisory](https://therecord.media/artex-ai-tool-fbi-flash-alert) about AI tool Artex one week ago, writing that it could take any large language model and turn it into a powerful hacking tool that can “automate multiple phases of cyber intrusions at machine speed, from reconnaissance through data exfiltration.”

Artex was [implicated](https://www.crowdstrike.com/en-us/blog/unknown-threat-actor-uses-artex-to-target-south-korean-finance/) in [multiple attacks](https://www.wsj.com/world/asia/hackers-use-chinese-ai-tool-to-hit-south-korean-banks-exposing-new-risk-5d4d3885) on South Korean and [Japanese](https://www.esecurityplanet.com/cybersecurity-threats/news-apac-artex-ai-cyberattacks-japan-companies/) financial institutions while Microsoft said Artex was used by Chinese state-backed actors in a recent [supply chain attack on IT management software company ConnectWise](https://therecord.media/connectwise-suspends-cloud-backup-service-supply-chain-attack). Moses [said](https://aws.amazon.com/blogs/security/amazon-threat-intelligence-observes-threat-actors-running-cybercrime-campaigns-with-artex-ai-agents/) last week that Artex was seen used in credential theft attacks on AI models and in campaigns targeting crypto exchanges.

Cairn was also [spotlighted by Google researchers on Tuesday](https://therecord.media/chinese-state-group-developing-automated-attack-tool-espionage) in a report about the evolving use of autonomous multi-agent offensive frameworks like Artex, CyberStrikeAI, PentAGI and others.

Google noted that it saw Cairn used in intrusions of companies in the U.S. aerospace sector and wrote, like AWS found, that it was adept at starting with a target’s IP address and ending with an operational objective.

The AWS report on Cairn cites a [study released in September](https://gambit.security/blog-posts/autonomous-ai-agents-online-retailers-25-a-company) by cybersecurity firm Gambit Security that documented the use of Cairn by a financially motivated hacking group using the tool to breach online retailers.

Eyal Sela, Director of Threat Intelligence at Gambit Security and the researcher behind the report, told Recorded Future News that Cairn is more significant than Artex because it is a general-purpose tool.

“While it is good at solving ‘red team’ or capture-the-flag tasks, it can also solve other problems and the main point is that it has no internal structuring for cybersecurity,” Sela said.

“When a tool is more generic, it is less predictable because it has less structuring around the way it solves a task.”

* [Technology](/news/technology)
* [News](/ukraine-says-starshield-working-again-after-disruption)
* [Cybercrime](/news/cybercrime)

[![Recorded Future](https://cms.therecord.media/uploads/2025_0514_Record_Ads_300x1050_1_0f2f11757e.png)](https://www.recordedfuture.com/?utm_source=therecord&utm_medium=referral&utm_content=post-sidebar-ad)

[![Recorded Future](https://cms.therecord.media/uploads/2025_0514_Record_Ads_970x250_1_d144dbf901.png)](https://www.recordedfuture.com/?utm_source=therecord&utm_medium=referral&utm_content=post-footer-ad)

No previous article

No new articles

[![Jonathan Greig](https://cms.therecord.media/uploads/DSC_0283_1_a6f4e4e315.jpg)](/author/jonathan-greig)

[Jonathan Greig](/author/jonathan-greig)

is a Breaking News Reporter at Recorded Future News. Jonathan has worked across the globe as a journalist since 2014. Before moving back to New York City, he worked for news outlets in South Africa, Jordan and Cambodia. He previously covered cybersecurity at ZDNet and TechRepublic.

## Briefs

* [West Virginia Legislature hit with cyber incident affecting IT systemsNovember 20th, 2026](/west-virginia-legislature-cyberattack)
* [NSA resumes normal operations following internal network disrup...
---
title: Microsoft blames ConnectWise attacks on Chinese state hacker using ARTEX AI agents
url: https://therecord.media/china-cyber-connectwise-ai
source: Over Security
date: 2026-10-22
fetch_date: 2026-10-23T06:46:31.268863
---

# Microsoft blames ConnectWise attacks on Chinese state hacker using ARTEX AI agents

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

![AI agents](https://cms.therecord.media/uploads/large_AI_agents_1_e0b6353553.jpg)

Image: Getty Images via Unsplash

[Jonathan Greig](/author/jonathan-greig)October 22nd, 2026

# Microsoft blames ConnectWise attacks on Chinese state hacker using ARTEX AI agents

A Chinese government-aligned hacking group used automated tools to carry out the recent [supply chain attack on IT management software company ConnectWise](https://therecord.media/connectwise-suspends-cloud-backup-service-supply-chain-attack) and is using the same techniques to try to compromise hundreds of other organizations around the globe, Microsoft said Wednesday.

Microsoft has been investigating a string of attacks conducted by a threat actor they call Storm-0940, which has used an AI penetration testing framework called ARTEX to breach organizations’ cloud infrastructure.

Since September, the group has been able to breach a wide variety of organizations across government, aerospace, defense, finance, manufacturing, technology and energy industries.

After gaining access to the companies, the hackers conducted reconnaissance, acquired credentials and tried to expand their privileges for expanded data collection.

Microsoft said the campaign stands out because of how AI has accelerated the hackers’ ability to quickly breach targets. In multiple instances it took the threat actors less than three hours from the initial targeting to gain privileged access.

“While the majority of the targeting wasn’t successful, Storm-0940 achieved privileged cloud persistence at many organizations in a brief time,” Microsoft [said](https://www.microsoft.com/en-us/security/blog/2026/10/21/storm-0940-uses-artex-agentic-ai-connectwise-supply-chain-compromise/).

Storm-0940 has been active since 2021, according to Microsoft, and typically conducts attacks for data theft purposes. It targets internet-facing applications and uses compromised accounts to expand access.

ARTEX is a penetration testing tool that allows users to deploy any AI model to automate offensive security actions. The platform coordinates a team of agents that can “run an autonomous penetration test from reconnaissance through data exfiltration with little needed human interaction,” Microsoft explained.

It was released on GitHub earlier this year as an open-source tool by an account known as "Autumn-27.”

The tool was recently [implicated](https://www.crowdstrike.com/en-us/blog/unknown-threat-actor-uses-artex-to-target-south-korean-finance/) in [multiple attacks](https://www.wsj.com/world/asia/hackers-use-chinese-ai-tool-to-hit-south-korean-banks-exposing-new-risk-5d4d3885) on South Korean and [Japanese](https://www.esecurityplanet.com/cybersecurity-threats/news-apac-artex-ai-cyberattacks-japan-companies/) financial institutions.

Researchers at Zscaler [released](https://www.zscaler.com/blogs/security-research/inside-global-ai-assisted-hacking-campaign) a report on Wednesday saying the ARTEX-backed attacks went far beyond South Korea and targeted dozens of industries across multiple countries.

The developer of the framework — [identified](https://www.wsj.com/world/asia/chinese-ai-tool-linked-to-hacks-in-japan-4813d13b) as Chinese cybersecurity engineer Li Puhua — released a statement on GitHub on October 8 saying the tool was abused by malicious actors.

“ARTEX was originally designed for learning and research purposes, aiming to help enterprises and organizations conduct security risk testing within their authorized assets and improve their security capabilities,” the developer [wrote](https://github.com/Autumn-27) in a machine translated message, denying any responsibility for crimes committed with it.

“Given the misuse of the tool, the ARTEX project will no longer be updated and will be converted to closed source. No further versions or maintenance support will be released to the public.”

Chinese Foreign Ministry spokesperson Mao Ning [denied](https://www.reuters.com/world/suspect-behind-south-korea-bank-hacks-may-be-26-year-old-china-cybersecurity-2026-10-08/) any knowledge of the incidents during a recent press briefing, according to Reuters.

## 2,900 sign-in attempts per minute

Over the weekend, ConnectWise was forced to shut down several of its services after Microsoft and other cybersecurity companies warned of a supply-chain attack impacting Cloud Backup.

The service is designed to help protect data in Microsoft 365 and Google Workspace. Attackers used stolen Cloud Backup credentials to gain wide access to any systems where the app is installed.

According to Microsoft, Storm-0940 used ARTEX to accelerate the “speed of compromised application abuse to authenticate to Microsoft 365 customer environments through applications that had already been granted access.”

“This activity demonstrates how threat actors are integrating agentic AI into existing offensive security workflows and allows them to scale their operations exponentially,” Microsoft said.

“Agents are not constrained by factors affecting humans — they can work around the clock, on weekends, and on holidays and attempt multiple breach paths simultaneously enabling significantly reduced time from selecting a target to achieving objectives, increasing the speed and impact of complex attacks like supply chain compromises.”

Microsoft said the ConnectWise incident involved 2,900 sign-in attempts per minute — a pace that leaves no time for human defenders to detect and respond. There were more than 111,000 failed log-on attempts on October 11 alone.

“The campaign blended broad, low-rate account spraying with sustained, high-volume authentication attempts against selected identities; 48 accounts received more than 1,000 failures, and lockout responses represented nearly 98% of all activity,” Microsoft said.

Microsoft said it was able to tie the campaign to Storm-0940 based on publicly reported IP addresses from ConnectWise that matched those seen in their own investigations.

* [News](/ukraine-says-starshield-working-again-after-disruption)
* [China](/news/china)
* [Malware](/news/malware)
* [Nation-state](/news/nation-state)

[![Recorded Future](https://cms.therecord.media/uploads/2025_0514_Record_Ads_300x1050_1_0f2f11757e.png)](https://www.recordedfuture.com/?utm_source=therecord&utm_medium=referral&utm_content=post-sidebar-ad)

[![Recorded Future](https://cms.therecord.media/uploads/2025_0514_Record_Ads_970x250_1_d144dbf901.png)](https://www.recordedfuture.com/?utm_source=therecord&utm_medium=referral&utm_content=post-footer-ad)

No previous article

No new articles

[![Jonathan Greig](https://cms.therecord.media/uploads/DSC_0283_1_a6f4e4e315.jpg)](/author/jonathan-greig)

[Jonathan Greig](/author/jonathan-greig)

is a Breaking News Reporter at Recorded Future News. Jonathan has worked across the globe as a journalist since 2014. Before moving back to New York City, he worked for news outlets in South Africa, Jordan and Cambodia. He previously covered cybersecurity at ZDNet and TechRepublic.

## Briefs

* [23andMe successor settles with California for $6 million over cybersecurity failings October 20th, 2026](/23andme-california-data-breach-settlement)
* [Ahold Delhaize confirms 'malicious actions' behind cyber outages affecting grocery brandsOctober 19th, 2026](/ahold-delhaize-cyberattack-grocery)
* [Hackers steal customer data from major Russian hosting provider FirstVDSOctober 19th, 2026](/russia-cyberattack-firstvds-cloud)
* [Proofpoint lines up...
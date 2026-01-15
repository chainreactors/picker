---
title: Federal agencies ordered to patch Microsoft Desktop Windows Manager bug
url: https://therecord.media/desktop-windows-manager-vulnerability-added-to-cisa-list
source: Over Security - Cybersecurity news aggregator
date: 2026-01-14
fetch_date: 2026-01-15T03:31:54.630329
---

# Federal agencies ordered to patch Microsoft Desktop Windows Manager bug

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

![microsoft windows logo on a keyboard](https://cms.therecord.media/uploads/format_webp/large_microsoft_computer_hack_6f4e8e4c9d.jpg)

Image: Tadas Sar via Unsplash

[Jonathan Greig](/author/jonathan-greig)January 14th, 2026

# Federal agencies ordered to patch Microsoft Desktop Windows Manager bug

U.S. government agencies have been ordered to patch a vulnerability impacting Microsoft’s Desktop Windows Manager after it was confirmed the bug has been exploited by threat actors.

The Cybersecurity and Infrastructure Security Agency (CISA) added the vulnerability, tracked as [CVE-2026-20805](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-20805), to its exploited bugs catalog on Tuesday.

It was one of 113 vulnerabilities [disclosed](https://x.com/msftsecresponse/status/2011136594582126963) by Microsoft as part of the first Patch Tuesday batch of 2026.

Federal civilian agencies will have until February 3 to patch the vulnerability. The Desktop Windows Manager (DWM) enables visual effects on a Microsoft desktop as well as various other features. It is a key part of how windows appear on a user’s screen.

Kev Breen, senior director of cyberthreat research at Immersive, said that while the bug’s severity score of 5.5 out of 10 is low, the flaw does lead to the leakage of information.

“Vulnerabilities of this nature are commonly used to undermine Address Space Layout Randomization (ASLR), a core operating system security control designed to protect against buffer overflows and other memory-manipulation exploits,” he explained.

“By revealing where code resides in memory, this vulnerability can be chained with a separate code execution flaw, transforming a complex and unreliable exploit into a practical and repeatable attack.”

He noted that Microsoft did not disclose what additional components may be involved in the exploit chain, “significantly limiting defenders’ ability to proactively threat hunt for related activity.”

Tenable’s Satnam Narang added that exploitation of CVE-2026-20805 requires the attacker to have local access to the targeted system. Narang told Recorded Future News that DWM is a “frequent flyer” on Patch Tuesday — with 20 CVEs patched since 2022. But this is the first time there has been an information disclosure bug in this component exploited in the wild.

The DWM process runs with elevated privileges because it needs them to do its job, according to Automox’s Ryan Braunstein, meaning attackers will not need administrative privileges to exploit it.

Braunstein said attackers will likely leverage any application capable of drawing windows to trigger the vulnerability before using the information disclosure to gather data for further attacks.

CISA has added three other bugs to the Known Exploited Vulnerabilities [catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) in 2026.

* [News](/)
* [Technology](/news/technology)
* [Government](/news/government)

Get more insights with the

Recorded Future

Intelligence Cloud.

[Learn more.](https://www.recordedfuture.com/platform?mtm_campaign=ad-unit-record)

[![Recorded Future](https://cms.therecord.media/uploads/format_webp/2025_0514_Record_Ads_300x1050_1_0f2f11757e.png)](https://www.recordedfuture.com/?utm_source=therecord&utm_medium=ad)

[![Recorded Future](https://cms.therecord.media/uploads/format_webp/2025_0514_Record_Ads_970x250_1_d144dbf901.png)](https://www.recordedfuture.com/?utm_source=therecord&utm_medium=ad)

Tags

* [Windows](/tag/windows)
* [CISA](/tag/cisa)
* [Vulnerability](/tag/vulnerability)
* [patch](/tag/patch)

No previous article

No new articles

[![Jonathan Greig](https://cms.therecord.media/uploads/format_webp/DSC_0283_1_a6f4e4e315.jpg)](/author/jonathan-greig)

[Jonathan Greig](/author/jonathan-greig)

is a Breaking News Reporter at Recorded Future News. Jonathan has worked across the globe as a journalist since 2014. Before moving back to New York City, he worked for news outlets in South Africa, Jordan and Cambodia. He previously covered cybersecurity at ZDNet and TechRepublic.

## Briefs

* [California AG to probe Musk’s Grok for nonconsensual deepfakesJanuary 14th, 2026](/california-grok-deepfakes-investigation)
* [Ugandan officials turn off internet on eve of national electionsJanuary 14th, 2026](/uganda-internet-shutdown-elections)
* [French data regulator fines telco subsidiaries $48 million over data breachJanuary 14th, 2026](/france-data-regulator-fine)
* [Poland says it repelled major cyberattack on power grid, blames RussiaJanuary 14th, 2026](/poland-cyberattack-grid-russia)
* [Cyberattack forces Belgian hospital to transfer critical care patients January 14th, 2026](/belgium-hospital-cyberattack-antwerp-az-monica)
* [California privacy agency appoints surveillance expert to boardJanuary 14th, 2026](/ccpa-appoints-new-board-member)
* [Tennessee man to plead guilty to hacking Supreme Court’s electronic case filing systemJanuary 13th, 2026](/guilty-plea-hacking-supreme-court-case-filing-system)
* [Kremlin-linked hackers pose as charities to spy on Ukraine’s militaryJanuary 13th, 2026](/kremlin-linked-hackers-pose-as-charities-spy-ukraine)
* [Armenia probes alleged sale of 8 million government records on hacker forumJanuary 12th, 2026](/armenia-probes-alleged-sale-government-records)

[## GRU-Linked BlueDelta Evolves Credential Harvesting

![GRU-Linked BlueDelta Evolves Credential Harvesting](https://www.recordedfuture.com/research/media_13adafe204e74a6a3976247e1c12b0466f536b86e.gif?width=1200&format=pjpg&optimize=medium)](https://www.recordedfuture.com/research/gru-linked-bluedelta-evolves-credential-harvesting)

[## BlueDelta’s Persistent Campaign Against UKR.NET

![BlueDelta’s Persistent Campaign Against UKR.NET](https://www.recordedfuture.com/research/media_11203fd322f018c8d0b5f9b3c85f34cb897128ad0.gif?width=1200&format=pjpg&optimize=medium)](https://www.recordedfuture.com/research/bluedeltas-persistent-campaign-against-ukrnet)

[## Palestine Action: Operations and Global Network

![Palestine Action: Operations and Global Network](https://www.recordedfuture.com/research/media_15526186964d3548d60e4a73cf876721d522ad671.gif?width=1200&format=pjpg&optimize=medium)](https://www.recordedfuture.com/research/palestine-action-operations-and-global-network)

[## Implications of Russia-India-China Trilateral Cooperation

![Implications of Russia-India-China Trilateral Cooperation](https://www.recordedfuture.com/research/media_1cac80654eeccc9254abd0ff29dc936da6d1b0a7f.gif?width=1200&format=pjpg&optimize=medium)](https://www.recordedfuture.com/research/implications-of-russia-india-china-trilateral-cooperation)

[## GrayBravo’s CastleLoader Activity Clusters Target Multiple Industries

![GrayBravo’s CastleLoader Activity Clusters Target Multiple Industries](https://www.recordedfuture.com/research/media_171fa690104f0a5274fe66bfe605332a13a3fc906.gif?width=1200&format=pjpg&optimize=medium)](https://www.recordedfuture.com/research/graybravos-castleloader-activity-clusters-target-multiple-industries)

[![The Record from Recorded Future News](https://cms.therecord.media/uploads/The_Record_Centered_9b27d79125.svg)](/)

* [Privacy](https://www.recordedfuture.com/privacy-policy)
* [About](/about)
* [Contact Us](/contact)

© Copyright 2026 | The Record from Recorded Future News
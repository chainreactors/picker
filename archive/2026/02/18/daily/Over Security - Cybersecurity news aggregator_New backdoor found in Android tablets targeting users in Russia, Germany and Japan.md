---
title: New backdoor found in Android tablets targeting users in Russia, Germany and Japan
url: https://therecord.media/new-backdoor-found-in-android-russia-japan-brazil
source: Over Security - Cybersecurity news aggregator
date: 2026-02-18
fetch_date: 2026-02-19T04:21:47.268338
---

# New backdoor found in Android tablets targeting users in Russia, Germany and Japan

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

![door](https://cms.therecord.media/uploads/format_webp/large_dima_pechurin_J_Ubj_Y_Fv_Cv00_unsplash_d6cfd67cd3.jpg)

Image: Dima Pechurin via Unsplash

[Daryna Antoniuk](/author/daryna-antoniuk)February 18th, 2026

# New backdoor found in Android tablets targeting users in Russia, Germany and Japan

Researchers have discovered a new Android backdoor embedded deep inside device firmware that infects tablets before they even reach consumers.

In a [report](https://securelist.com/keenadu-android-backdoor/118913/) released this week, Russian cybersecurity firm Kaspersky said it uncovered a previously undocumented backdoor dubbed Keenadu. Unlike typical malware that users inadvertently download, Keenadu is built directly into a device’s core software, allowing it to load into every application launched on the tablet.

“Keenadu represents a full-fledged backdoor that allows attackers to gain virtually unrestricted control over the victim’s device,” the researchers said.

Kaspersky reported that over 13,700 users worldwide encountered Keenadu or its modules. The highest number of detections occurred in Russia, Japan, Germany, Brazil and the Netherlands.

The malware was primarily used for advertising fraud. Modules linked to Keenadu were capable of hijacking browser search engines, monitoring the installation of new applications and interacting with advertising components to generate fraudulent revenue. In some cases, users have reported that infected tablets were adding items to marketplace shopping carts without their knowledge.

According to the report, the malware was found integrated into the firmware of tablets from multiple manufacturers, including Chinese device maker Alldocube. The company previously [acknowledged](https://www.alldocube.com/en/forums/topic/11680/) malware issues in one of its models, but Kaspersky said subsequent firmware updates for that device — including those released after the public disclosure — remained infected.

The researchers said Keenadu was also found in hardware from other manufacturers, though they did not name them. The company said it had notified the affected vendors.

Researchers believe the malware was inserted into targeted systems during the firmware build stage — likely through a compromised supply chain — meaning devices could have been infected before reaching customers.

“The vendors may have been unaware that their devices were infected prior to reaching the market,” Kaspersky said.

Several variants of the backdoor were identified. The most powerful version was embedded directly into device firmware. Other variants were hidden in applications, including a facial recognition app used for device unlocking, and even in apps distributed through official stores such as Google Play and third-party repositories.

Researchers did not attribute the campaign to a specific threat actor but said the developers demonstrated “a deep understanding of the Android architecture, the app startup process, and the core security principles of the operating system.”

The malware also appeared designed to avoid certain regions. It checks a device’s language settings and time zone and terminates if the interface language is set to a Chinese dialect and the device is located in a Chinese time zone. It also remains inactive on devices that lack Google Play Store or Google Play Services.

The Keenadu operation bears similarities to a 2025 [infection](https://securelist.com/triada-trojan-modules-analysis/116380/) involving the Triada backdoor, which embedded itself in the firmware of counterfeit Android devices sold through major online marketplaces, allowing attackers to steal credentials from messaging and social media apps.

Because Keenadu is embedded at the firmware level, it cannot be removed using standard Android security tools, researchers said. They recommend installing a clean firmware version from a trusted source. In some cases, they warn, replacing the device entirely may be the safest option.

* [Cybercrime](/news/cybercrime)
* [News](/)
* [News Briefs](/)
* [Technology](/news/technology)
* [Privacy](/news/privacy)

Get more insights with the

Recorded Future

Intelligence Cloud.

[Learn more.](https://www.recordedfuture.com/platform?mtm_campaign=ad-unit-record)

[![Recorded Future](https://cms.therecord.media/uploads/format_webp/2025_0514_Record_Ads_300x1050_1_0f2f11757e.png)](https://www.recordedfuture.com/?utm_source=therecord&utm_medium=ad)

[![Recorded Future](https://cms.therecord.media/uploads/format_webp/2025_0514_Record_Ads_970x250_1_d144dbf901.png)](https://www.recordedfuture.com/?utm_source=therecord&utm_medium=ad)

Tags

* [Kaspersky](/tag/kaspersky)
* [backdoor](/tag/backdoor)
* [malware](/tag/malware)
* [Android](/tag/android)

No previous article

No new articles

[![Daryna Antoniuk](https://cms.therecord.media/uploads/format_webp/d887de47708acda42945a172d61c0ca2_38f4568326.png)](/author/daryna-antoniuk)

[Daryna Antoniuk](/author/daryna-antoniuk)

is a reporter for Recorded Future News based in Ukraine. She writes about cybersecurity startups, cyberattacks in Eastern Europe and the state of the cyberwar between Ukraine and Russia. She previously was a tech reporter for Forbes Ukraine. Her work has also been published at Sifted, The Kyiv Independent and The Kyiv Post.

## Briefs

* [Poland bans Chinese-made cars from entering military sitesFebruary 18th, 2026](/poland-bans-chinese-made-cars-from-military-sites)
* [Canada Goose says leaked customer transaction data did not come from company systemsFebruary 17th, 2026](/canada-goose-says-leaked-customer-data-was-not-from-company)
* [Hackers target supporters of Iran protests in new espionage campaignFebruary 17th, 2026](/hackers-target-iran-protest-supporters-cyber-campaign)
* [Dutch police arrest man who refused to delete confidential files shared by mistakeFebruary 17th, 2026](/netherlands-arrest-confidential-files-police)
* [Over 500,000 VKontakte accounts hijacked through malicious Chrome extensionsFebruary 16th, 2026](/500000-vkontakte-accounts-hijacked-chrome-extensions)
* [China may be rehearsing a digital siege, Taiwan warnsFebruary 13th, 2026](/china-taiwan-digital-siege-munich)
* [US needs to impose ‘real costs’ on bad actors, State Department cyber official says February 13th, 2026](/usa-cyber-actors-consequences)
* [Dutch mobile phone giant Odido announces data breachFebruary 12th, 2026](/dutch-telecom-giant-announces-data-breach)
* [40 state AGs warn House KOSA bill falls short of protecting children onlineFebruary 11th, 2026](/40-state-ags-warn-house-kosa-bill-falls-short)

[## GrayCharlie Hijacks Law Firm Sites in Suspected Supply-Chain Attack

![GrayCharlie Hijacks Law Firm Sites in Suspected Supply-Chain Attack](https://www.recordedfuture.com/research/media_187b8e348054a7063fd37aec148dfc3337efc5d14.gif?width=1200&format=pjpg&optimize=medium)](https://www.recordedfuture.com/research/graycharlie-hijacks-law-firm-sites-suspected-supply-chain-attack)

[## State of Security Report | Recorded Future

![State of Security Report | Recorded Future](https://www.recordedfuture.com/research/media_188a8fbb5001e358d9837adb14d5fb0897434527c.gif?width=1200&format=pjpg&optimize=medium)](https://www.recordedfuture.com/research/state-of-security)

[## Rublevka Team: Anatomy of a Russian Crypto Drainer Operation

![Rublevka Team: Anatomy of a Russian Crypto Drainer Operation](https://www.recordedfuture.com/research/media_1f21796732ee17098dc9ea...
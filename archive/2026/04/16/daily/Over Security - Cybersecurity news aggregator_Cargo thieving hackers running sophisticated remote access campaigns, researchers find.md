---
title: Cargo thieving hackers running sophisticated remote access campaigns, researchers find
url: https://therecord.media/cargo-thieving-hackers-running-sophisticated-campaigns
source: Over Security - Cybersecurity news aggregator
date: 2026-04-16
fetch_date: 2026-04-17T04:50:46.854227
---

# Cargo thieving hackers running sophisticated remote access campaigns, researchers find

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

![shipping](https://cms.therecord.media/uploads/large_shipping_59776fef3a.jpg)

Image: Marcin Jozwiac via Unsplash

[James Reddick](/author/james-reddick)April 16th, 2026

# Cargo thieving hackers running sophisticated remote access campaigns, researchers find

Security researchers recently spent a month getting a first-hand look at the activity of cybercriminals targeting the trucking and logistics industry.

The researchers, from cybersecurity firm Proofpoint, [previously described](https://therecord.media/cargo-theft-hackers-remote-monitoring-tools) how threat actors gain access to companies in the shipping industry to steal cargo and siphon payments — but their [new research](https://www.proofpoint.com/us/blog/threat-insight/beyond-breach-inside-cargo-theft-actors-post-compromise-playbook) sought to answer the question of what exactly happens after they get their feet in the door.

The work sheds light on the growing threat of cyber-enabled cargo theft and its [links to organized crime](https://therecord.media/phishing-operation-russia-armenia-targeting-us-european-cargo). Losses from cargo theft in North America rose to $6.6 billion in 2025, driven largely by digital attacks, according to the fleet management company Geotab.

“It’s a huge problem beyond just one actor or one country,” said Ole Villadsen, one of the Proofpoint researchers.

Using a controlled decoy environment, his team intentionally downloaded a malicious payload sent by email to transportation carriers after the cybercriminals had compromised a load board platform, a marketplace where freight brokers and shippers connect to arrange the movement of cargo.

After getting access, the cybercriminals installed six separate remote access tools, including four ScreenConnect instances, which researchers believe was an attempt to maintain remote control in case any of them were taken down.

The last downloaded ScreenConnect tool presented a surprise: the use of a script that automatically queried an external certificate signing service. This enabled all installed components to be signed with a certificate that Windows perceived to be trusted.

“This was a new capability that we were lucky enough to encounter,” said Villadsen. He believes the “signing-as-a-service” tool is an adaptation to recent security efforts by ScreenConnect to revoke existing certificates and require new instances of the software to sign an installer, which “disrupted the whole RMM [remote monitoring and management] ecosystem significantly.”

“So rather than everybody trying to create their own certificate, we can have this kind of secret little signing-as-a-service process,” he said. “Not only was the MSI [Microsoft Installer] signed, but it would also go out and replace all the component files and re-sign them as well. The whole thing was thought out pretty well.”

Another thing that jumped out to Villadsen was the way in which the hackers seemed to not just be working to steal cargo but also to carry out “broader financial targeting and theft.”

They scanned for cryptocurrency wallets and manually checked for PayPal credentials. A PowerShell script on the infected device scanned for access points to financial institutions, money transfer services and online accounting platforms. It also searched for load management and freight brokerage platforms, as well as fuel card providers.

“They know the transportation industry really, really well for sure, and know how to target that particular space,” he said. “But they're also cybercriminals, and they're looking for any way that they can monetize a workstation that they've landed on.”

While this threat group is one of the most prolific at infiltrating load boards to deliver payloads, it is one of many cashing in on a vulnerable space. Villadsen says he and his team are tracking about a dozen different groups targeting the sector in North America and in Europe.

With the vast majority of carriers being small enterprises with fewer than 10 trucks, they may not have robust cybersecurity defenses. By targeting them through load boards, hackers can infiltrate dozens or even hundreds of carriers at a time.

“It’s an industry that unfortunately presents itself well to cyber intrusions and being able to escalate or scale the theft really well,” he said.

* [Cybercrime](/news/cybercrime)
* [Industry](/)
* [News](/)
* [News Briefs](/)

Get more insights with the

Recorded Future

Intelligence Cloud.

[Learn more.](https://www.recordedfuture.com/platform?mtm_campaign=ad-unit-record)

[![Recorded Future](https://cms.therecord.media/uploads/2025_0514_Record_Ads_300x1050_1_0f2f11757e.png)](https://www.recordedfuture.com/?utm_source=therecord&utm_medium=ad)

[![Recorded Future](https://cms.therecord.media/uploads/2025_0514_Record_Ads_970x250_1_d144dbf901.png)](https://www.recordedfuture.com/?utm_source=therecord&utm_medium=ad)

No previous article

No new articles

[![James Reddick](https://cms.therecord.media/uploads/Headshot_9468680de9.JPG)](/author/james-reddick)

[James Reddick](/author/james-reddick)

has worked as a journalist around the world, including in Lebanon and in Cambodia, where he was Deputy Managing Editor of The Phnom Penh Post. He is also a radio and podcast producer for outlets like Snap Judgment.

## Briefs

* [Cargo thieving hackers running sophisticated remote access campaigns, researchers findApril 16th, 2026](/cargo-thieving-hackers-running-sophisticated-campaigns)
* [Sweden says pro-Russian hackers attempted to breach thermal power plantApril 15th, 2026](/sweden-hackers-russia-power-plant)
* [Russia appears to block social media platform Bluesky amid wider internet restrictionsApril 14th, 2026](/russia-cracks-down-bluesky-internet)
* [Hack at Dutch gym chain Basic-Fit exposes customer data in several EU countriesApril 12th, 2026](/dutch-gym-chain-basic-fit-hit-by-hackers)
* [Cryptocurrency ATM giant Bitcoin Depot reports $3.6 million stolen in cyberattackApril 9th, 2026](/crypto-atm-bitcoin-depot-reports-cyberattack)
* [Cyberattack on telecom giant Rostelecom disrupts internet services across RussiaApril 6th, 2026](/rostelecom-cyberattack-disrupts-russian-internet-access)
* [FBI: Cyber fraud surges to $17.6 billion in losses as scams, crypto theft soarApril 6th, 2026](/cyber-fraud-surges-to-17-billion-fbi-ic3)
* [Big tech vows to continue CSAM scanning in Europe despite expiration of law allowing itApril 6th, 2026](/big-tech-vows-to-continue-csam-scanning)
* [First stalkerware maker prosecuted since 2014 receives no jail timeApril 6th, 2026](/stalkerware-maker-receives-no-jail-time)

[## Iran War: Future Scenario and Business Implications

![Iran War: Future Scenario and Business Implications](https://www.recordedfuture.com/research/media_1627d52be2bcdad9118913daf3e68f8df1cb60111.png?width=1200&format=pjpg&optimize=medium)](https://www.recordedfuture.com/research/iran-war-future-scenarios)

[## Understanding and Anticipating Venezuelan Government Actions

![Understanding and Anticipating Venezuelan Government Actions](https://www.recordedfuture.com/research/media_1d08f25ae63a57a954e41789fb5634f3df6f8a5c5.gif?width=1200&format=pjpg&optimize=medium)](https://www.recordedfuture.com/research/understanding-and-anticipating-venezuelan-government-actions)

[## Latin America and the Caribbean Cybercrime Landscape

![Latin America and the Caribbean Cybercrime Landscape](https://www.recordedfuture.com/research/media_170df75f7415b871f0e4a8ee069a6ce7922d8...
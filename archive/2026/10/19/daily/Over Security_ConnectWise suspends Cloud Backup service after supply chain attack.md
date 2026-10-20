---
title: ConnectWise suspends Cloud Backup service after supply chain attack
url: https://therecord.media/connectwise-suspends-cloud-backup-service-supply-chain-attack
source: Over Security
date: 2026-10-19
fetch_date: 2026-10-20T06:53:32.177921
---

# ConnectWise suspends Cloud Backup service after supply chain attack

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

![attack](https://cms.therecord.media/uploads/large_fernand_de_canne_Apfy_Uz5c5_Q0_unsplash_0367b9f48a.jpg)

Image: Fernand de Canne via Unsplash

[Jonathan Greig](/author/jonathan-greig)October 19th, 2026

# ConnectWise suspends Cloud Backup service after supply chain attack

IT management software company ConnectWise shut down several of its services this weekend after Microsoft and other cybersecurity companies warned of a supply chain attack impacting its cloud backup system.

ConnectWise initially said on Friday that it was investigating “attempts of unauthorized access associated with the ConnectWise Cloud Backup environment,” and confirmed such access on Saturday.

Incident responders at cybersecurity firm Huntress [said](https://www.huntress.com/blog/vendor-credential-enables-unauthorized-access) a credential belonging to ConnectWise Cloud Backup was compromised and used to gain access to the customers’ Microsoft 365 environment.

Microsoft [confirmed](https://x.com/msftsecintel/status/2111358888125878426) in its own statement that threat actors “likely abused permissions previously granted by customers to the application, including highly elevated permissions like Directory.ReadWrite.All.”

ConnectWise Cloud Backup is a cloud-based backup and recovery service designed to help protect data in Microsoft 365 and Google Workspace. The tool needs broad access to mailboxes, OneDrive, SharePoint, Teams and other data, according to Huntress.

An attacker using stolen ConnectWise Cloud Backup credentials will inherently have wide access to any systems where the app is installed, including places where no trail of evidence will be left.

ConnectWise did not respond to requests for comment about the attackers or about how many customers were impacted. A spokesperson told Recorded Future News that there is “no indication" that backup data was compromised.

The current service interruptions apply to the cloud backup system as well as the SaaS Security and Cloud Management platforms.

“We have remediated identified compromised credentials and identities, and we continue authentication monitoring, permission review, and forensic analysis,” the spokesperson said.

In multiple updates throughout Saturday and Sunday, ConnectWise [said](https://www.connectwise.com/company/trust/advisories) it revoked certificates used for affected application connections across all users. This removed ConnectWise’s access through those connections and all shared credentials previously used for Cloud Backup are no longer valid and cannot be used.

The company said they do not have visibility into partner and customer environments, so they cannot determine whether a particular customer’s Microsoft 365 environment was breached.

ConnectWise said since taking a range of actions, it has seen no successful threat activity. There is no timeline for a restoration of services, the spokesperson said.

## Waves of attacks

Huntress incident responders said they initially saw password spray attacks against four law firms on October 13 and 14. By October 15, about 50 systems monitored by Huntress saw attackers use ConnectWise's Cloud Management apps to assign themselves directory or administrative roles.

In total, Huntress saw unauthorized sign-ins in 162 tenants. Huntress also saw a second targeted wave of largely unsuccessful attacks targeting systems “in the policy, national security, trade, and critical mineral sectors.”

“Unlike the first wave of activity outlined in our initial blog below, most of these tenants do not rely on any ConnectWise products. In tenants without the relevant ConnectWise service principal, the attempts failed because the application was not present,” Huntress explained.

Like Huntress, Microsoft and [other cybersecurity firms](https://www.todyl.com/blog/investigation-unauthorized-access-through-the-connectwise-cloud-backup-microsoft-365-app) said they [observed](https://x.com/specterops/status/2111565631837327691) “broad” attacks starting on October 15.

Huntress warned that backup services like ConnectWise Cloud Backup normally hold read access to mail, files, Teams, and directory data so it can copy them and restore them.

“The larger risk is what happens when that access is used to gain more. If an application can assign directory roles, as we saw in one tenant, it can make itself a Global Administrator, and an administrator can add credentials to other applications, create new applications and grant them permissions, reset passwords and authentication methods for users, and change Conditional Access policies,” Huntress added.

“Each of those steps gives the attacker another way back in that does not depend on the original vendor credential, which is why rotating the vendor credential is necessary, but not enough.”

They noted that in managed service providers the effect can be even worse — with attackers using their foothold in one customer to gain access to all other customers.

ConnectWise has dealt with multiple security incidents in the past, including one last year involving a [nation-state attack](https://therecord.media/connectwise-nation-state-attack-targeted-some-customers) on its remote management and monitoring software that impacted some of its customers.

Cybercriminals previously [exploited](https://therecord.media/connectwise-screenconnect-bug-cybercrime-exploitation) [multiple vulnerabilities](https://therecord.media/connectwise-software-needs-immediate-patching) in the company’s products that led to ransomware attacks.

* [Cybercrime](/news/cybercrime)
* [News](/ukraine-says-starshield-working-again-after-disruption)
* [Technology](/news/technology)

[![Recorded Future](https://cms.therecord.media/uploads/2025_0514_Record_Ads_300x1050_1_0f2f11757e.png)](https://www.recordedfuture.com/?utm_source=therecord&utm_medium=referral&utm_content=post-sidebar-ad)

[![Recorded Future](https://cms.therecord.media/uploads/2025_0514_Record_Ads_970x250_1_d144dbf901.png)](https://www.recordedfuture.com/?utm_source=therecord&utm_medium=referral&utm_content=post-footer-ad)

No previous article

No new articles

[![Jonathan Greig](https://cms.therecord.media/uploads/DSC_0283_1_a6f4e4e315.jpg)](/author/jonathan-greig)

[Jonathan Greig](/author/jonathan-greig)

is a Breaking News Reporter at Recorded Future News. Jonathan has worked across the globe as a journalist since 2014. Before moving back to New York City, he worked for news outlets in South Africa, Jordan and Cambodia. He previously covered cybersecurity at ZDNet and TechRepublic.

## Briefs

* [Ahold Delhaize confirms 'malicious actions' behind cyber outages affecting grocery brandsOctober 19th, 2026](/ahold-delhaize-cyberattack-grocery)
* [Hackers steal customer data from major Russian hosting provider FirstVDSOctober 19th, 2026](/russia-cyberattack-firstvds-cloud)
* [Proofpoint lines up $6.3 billion deal for Varonis’ data securityOctober 16th, 2026](/proofpoint-varonis-cybersecurity-acquisition)
* [North Macedonian police arrest alleged administrator behind OLVX cybercrime marketOctober 14th, 2026](/olvx-cybercrime-marketplace-arrest-north-macedonia)
* [Russian travel booking platform suspends reservations after cyberattackOctober 14th, 2026](/russia-anywayanyday-travel-website-cyberattack)
* [Ledger says hardware implant in cryptocurrency wallets stole recovery phrasesOctober 13th, 2026](/ledger-cryptocurrency-wallet-implant-theft)
* [South African clothing retailer Foschini Group in...
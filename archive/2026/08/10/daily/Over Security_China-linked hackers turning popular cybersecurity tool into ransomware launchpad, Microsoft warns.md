---
title: China-linked hackers turning popular cybersecurity tool into ransomware launchpad, Microsoft warns
url: https://therecord.media/china-hackers-ransomware-microsoft
source: Over Security
date: 2026-08-10
fetch_date: 2026-08-11T03:31:32.390632
---

# China-linked hackers turning popular cybersecurity tool into ransomware launchpad, Microsoft warns

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

![Keyboard](https://cms.therecord.media/uploads/large_mohammad_mardani_MC_Pqw_Z_Exfx_M_unsplash_b240343335.jpg)

Image: Mohammad Mardani via Unsplash

[Alexander Martin](/author/alexander-martin)August 10th, 2026

# China-linked hackers turning popular cybersecurity tool into ransomware launchpad, Microsoft warns

A financially motivated threat actor linked to China is believed to be exploiting a critical vulnerability affecting widely used cybersecurity software in a supply-chain attack that could see the hackers deploy custom ransomware across a cascading list of victims’ networks.

Microsoft Threat Intelligence [warned](https://bsky.app/profile/threatintel.microsoft.com/post/3msjiybnb252n) this weekend that the Storm-1175 group began deploying a new ransomware strain on August 2 called StormEncryptor. The hackers previously [used](https://www.microsoft.com/en-us/security/blog/2026/04/06/storm-1175-focuses-gaze-on-vulnerable-web-facing-assets-in-high-tempo-medusa-ransomware-operations/) the Medusa ransomware to extort healthcare, professional services and finance organizations in Australia, Britain and the United States.

Back in April, the hackers were described as operating “high-velocity ransomware campaigns” exploiting both recently disclosed vulnerabilities and zero-day exploits, “in some cases a full week before public vulnerability disclosure.” Microsoft said it had seen the group move from initial access to full encryption in under 24 hours.

In this latest campaign, Microsoft said the group is likely exploiting [CVE-2026-18577](https://www.cve.org/CVERecord?id=CVE-2026-18577) — a vulnerability in N-central, a remote monitoring and management (RMM) console used by thousands of managed service providers to administer client endpoints.

Microsoft has not formally confirmed the access vector, but noted that StormEncryptor deployments began the same day the flaw was disclosed. The vulnerability gives attackers “unauthenticated, ‘god-mode’ access,” the cybersecurity firm Huntress [warned](https://www.huntress.com/blog/n-able-vulnerability-exploitation).

Practically, it allows attackers with no credentials whatsoever to gain full administrative control of an N-central server. Because MSPs use N-central to remotely manage their clients’ machines, that single compromised server becomes a gateway to every endpoint it controls. One breach at one provider can cascade into dozens of ransomware incidents across its entire client base.

In 2021, a similar [supply-chain attack](https://therecord.media/kaseya-more-than-1500-downstream-businesses-impacted-by-ransomware-attack) on an RMM tool from software provider Kaseya allowed the REvil ransomware gang to initially compromise 60 of Kaseya’s direct customers before subsequently hitting around 1,500 downstream businesses.

Another supply-chain attack in 2024 — again on an RMM — [impacted](https://therecord.media/connectwise-screenconnect-bug-cybercrime-exploitation) ConnectWise's ScreenConnect product. It similarly led to numerous downstream ransomware attacks. Microsoft said Storm-1175 was among the multiple threat actors targeting ScreenConnect at the time.

A rough count of impacted organizations has not been disclosed. N-able, the software company behind N-central, said it has contacted a “limited number” of affected customers. Huntress confirmed some of its own customers were impacted and published a timeline showing attackers moving rapidly across downstream hosts in two incidents, but again did not confirm how many downstream entities faced ransomware attacks.

N-able said the vulnerability behind the campaign was first detected in a zero-day attack on July 31 — although it is unclear whether the threat actor behind that initial attack was Storm-1175. The initial flaw proved difficult to fix. N-able said the attackers found a way around an initial patch and shipped an emergency hotfix on August 2 before then issuing a second emergency hotfix on August 6, [warning](https://www.n-able.com/blog/n-central-security-update-august-6-2026) customers the first was not enough.

Even after the patches were available, Huntress said it found more than half of reachable N-central cloud servers across its partner base were still unpatched, with 28.6% of self-hosted instances remaining exposed.

Huntress said that anyone running N-central in a “higher-risk” environment “where you cannot meaningfully reduce exposure” may need to consider turning the tool off. However, it cautioned “taking N-central offline means losing central visibility, patching, and remote access when they may be needed most.”

* [News](/)
* [China](/news/china)
* [Cybercrime](/news/cybercrime)

Get more insights with the

Recorded Future

Intelligence Cloud.

[Learn more.](https://www.recordedfuture.com/platform?mtm_campaign=ad-unit-record)

[![Recorded Future](https://cms.therecord.media/uploads/2025_0514_Record_Ads_300x1050_1_0f2f11757e.png)](https://www.recordedfuture.com?utm_source=therecord&utm_medium=referral&utm_content=display)

[![Recorded Future](https://cms.therecord.media/uploads/2025_0514_Record_Ads_970x250_1_d144dbf901.png)](https://www.recordedfuture.com?utm_source=therecord&utm_medium=referral&utm_content=display)

No previous article

No new articles

[![Alexander Martin](https://cms.therecord.media/uploads/headshot_79eb085f87.jpeg)](/author/alexander-martin)

[Alexander Martin](/author/alexander-martin)

is the UK Editor for Recorded Future News. He was previously a technology reporter for Sky News and a fellow at the European Cyber Conflict Research Initiative, now Virtual Routes. He can be reached securely using Signal on: AlexanderMartin.79

## Briefs

* [US cyber ambassador nominee Cassady confirmed in SenateAugust 7th, 2026](/adam-cassady-confirmed-senate-cyber-ambassador)
* [Military device manufacturer discloses cyber incident to SECAugust 7th, 2026](/military-device-manufacturer-discloses-cyber-incident)
* [Levi Strauss says hackers breached employee computers, accessed corporate dataAugust 7th, 2026](/levis-data-breach-social-engineering)
* [French rugby club Stade Français restores systems after cyberattack, probes data leakAugust 7th, 2026](/french-rugby-club-restores-systems-after-cyberattack)
* [Cyberattack on North Carolina Ports ‘contained’ as Coast Guard, state officials investigateAugust 6th, 2026](/cyberattack-north-carolina-ports)
* [Hackers steal 31,000 records identifying people behind Liechtenstein companies, foundationsAugust 3rd, 2026](/hackers-steal-records-liechtenstein-companies-foundations)
* [Biotech giant Amgen says patient data stolen from third-party cloud systemsAugust 3rd, 2026](/amgen-hackers-cyberattack-sec)
* [Semiconductor chip titan Analog Devices reports data breachJuly 30th, 2026](/analog-devices-semiconductor-company-data-breach)
* [Laundry Bear’s webmail hackers had more in store after February, report saysJuly 29th, 2026](/russia-hackers-outlook-webmail-malware)

[## Emerging Threats to Neurotechnology

![Emerging Threats to Neurotechnology](https://www.recordedfuture.com/research/media_1dbb6881e45cb8bc5cae598067b6d4915f2c0674c.gif?width=1200&format=pjpg&optimize=medium)](https://www.recordedfuture.com/research/emerging-threats-neurotechnology?utm_source=therecord&utm_medium=referral&utm_content=insikt)

[## Iran War’s Secondary Effects Shape 2026 US Violent Extremism

![Iran War’s Secondary Effects Shape 2026 US Violent Extremism](https://www.recordedfuture.com/research...
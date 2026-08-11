---
title: Poland uncovers second heat plant cyberattack that went hidden for months
url: https://therecord.media/poland-uncovers-critical-infrastructure-attack-hidden
source: Over Security
date: 2026-08-10
fetch_date: 2026-08-11T03:31:31.304035
---

# Poland uncovers second heat plant cyberattack that went hidden for months

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

![power plant](https://cms.therecord.media/uploads/large_poland_power_plant_028eff5123.jpg)

Image: Marcin Jozwiac via Unsplash

[Alexander Martin](/author/alexander-martin)August 10th, 2026

# Poland uncovers second heat plant cyberattack that went hidden for months

Poland’s cybersecurity authorities have revealed that a previously unknown cyberattack disrupted systems at a combined heat and power plant during last winter’s cold snap, threatening to leave tens of thousands of people exposed to freezing weather.

The incident occurred on the same day as coordinated cyberattacks struck more than 30 other renewable energy installations and a larger heat plant, as Poland [publicly disclosed](https://therecord.media/poland-cyberattack-grid-russia) in January. Those attacks came "very close" to causing a "blackout" for almost 500,000 people, a senior minister said at the time.

The attacks landed during one of the coldest European winters in more than a decade. They were [formally attributed](https://therecord.media/russia-blamed-for-poland-grid-cyberattack-in-joint-uk-eu-sanctions-package) in July to Russia’s Federal Security Service, although CERT Polska, the country's computer emergency response team, did not attribute the additional attack in its [supplementary report](https://cert.pl/en/posts/2026/08/incident-follow-up-report-energy-sector-2025/).

That report focuses instead on an attack on a smaller combined heat and power plant supplying heat to about 50,000 residents — an attack that went unrecognized as a cyberattack at the time, according to Marcin Dudek, the head of CERT Polska.

Speaking Saturday at the DEF CON cybersecurity conference in Las Vegas, Dudek said the attack struck during routine maintenance over the Christmas period. The plant’s operators initially blamed a contractor error for the shutdown of the steam turbine and water treatment system, rather than malicious hackers.

The disruption was caught quickly enough that customer heating was never interrupted, and it was reported only for informational purposes. But given the timing with the other attacks, CERT Polska launched a full investigation into the low-priority report.

The analysis, which took more than three months, uncovered what the agency described as the first known use of a private cellular data network as a pathway into an industrial control system.

"This case demonstrates the importance of reporting not only confirmed incidents but also unexplained failures and operational disruptions," the report said — sharply contrasting with the more limited reporting requirements set out by the European Union’s NIS2 law.

Wind farms and other distributed energy sites communicate with grid operators through private cellular networks; dedicated mobile data connections the industry treats as secure, walled-off infrastructure.

In the newly disclosed incident, the attackers moved from firewalls already compromised at wind farm substations to reach a cellular router connected to one of these private networks, and then used this router to hop across to a controller at the heat plant that was still running factory-default login credentials.

From there the hackers tunneled into the plant’s industrial control systems. The entire chain — wind farm to cellular network to heat plant — saw the hackers move across facilities with no direct relationship to one another besides their shared presence on the same private network.

Once inside, the attackers spent 11 days conducting reconnaissance before striking. They probed industrial equipment, tested credentials against the plant’s firewall and connected to controllers on Christmas Day to map their targets.

Before dawn on December 29, they disabled the Siemens controllers running the steam turbine and water treatment system and locked operators out of those controllers with new passwords.

The hackers then wiped the configurations of network equipment using automated scripts and set device addresses to unreachable values to slow recovery. Plant staff began restoring systems roughly two hours later — while the attackers were still active — and limited the disruption to a brief outage.

The attackers went on to destroy forensic evidence along their entire path, corrupting the device they had used as a gateway into the plant so thoroughly it could not be repaired, and resetting the firewalls and routers behind them.

Investigators were only able to reconstruct the attack because one router ran older software that preserved its event logs through a factory reset.

CERT Polska warned that the misconfiguration that made the attack possible, allowing any device on a private cellular network to communicate freely with any other, was common across Poland at the time and is believed to be widespread internationally.

The agency is urging energy operators to stop treating private cellular networks as trusted infrastructure and to apply the same controls they would use for any internet-facing connections. It called for immediate audits of network configurations, the removal of default passwords from connected devices and the inclusion of these networks in security testing programs.

* [Cybercrime](/news/cybercrime)
* [Government](/news/government)
* [News](/)

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
* [Laundry Bear’s webmail hackers had more in store after February, report saysJuly 29...
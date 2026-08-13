---
title: Three intrusions at UK criminal records office went undetected for two years
url: https://therecord.media/uk-criminal-records-office-acro-data-breaches
source: Over Security
date: 2026-08-12
fetch_date: 2026-08-13T04:05:00.748397
---

# Three intrusions at UK criminal records office went undetected for two years

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

![U.K. police](https://cms.therecord.media/uploads/large_britain_police_pexels_vision_plug_8ee385449d.jpg)

Image: Vision Plug via Pexels

[Alexander Martin](/author/alexander-martin)August 12th, 2026

# Three intrusions at UK criminal records office went undetected for two years

Britain's criminal records office has been reprimanded by the country’s data protection regulator after being repeatedly breached over nearly two years, exposing the personal data of thousands of people including victims of domestic violence.

The Information Commissioner’s Office (ICO) announced in the [reprimand notice](https://ico.org.uk/media2/njrjayzm/acro-reprimand-202608.pdf) Wednesday that it was censuring ACRO Criminal Records Office over a range of security shortcomings, among them alerts from antivirus software going unread and a critical system left unpatched for nearly four years.

Basic failures at ACRO — the national policing unit that handles a range of sensitive data stored on the Police National Computer — allowed hackers to successfully compromise the office in three separate intrusions between July 2021 and June 2023.

All three attacks exploited ACRO’s public-facing customer portal, built on the Kentico content management system, which had been running the same version since September 2019 despite containing multiple known and publicly documented vulnerabilities.

Although Kentico had shipped security fixes for these issues, ACRO applied none of them because neither itself nor the managed service provider nor the web development supplier knew who was meant to be watching for and applying the patches.

Similar issues took place around alert handling. Despite numerous warnings from the system’s Trend Micro cybersecurity solution during the attack period — including quarantining four separate detections of attempts to install the Mimikatz credential-harvesting tool — all of these went unheeded.

ACRO told the ICO it was unable to establish what business process had existed for assessing or handling security alerts, and did not know which roles had been responsible for reviewing and escalating these alerts. The ICO concluded that if the alerts had been acted upon, further malicious activity could have been prevented.

## Whodunit

It is not clear who perpetrated the three incidents, including whether separate threat actors were to blame or if they marked several stages in a single attack.

ACRO commissioned a forensic investigation that the ICO described as uncovering three distinct incidents titled Group A, Group B and Group C. It is not clear if these groupings refer to threat-actor activity clusters or suspected independent perpetrators.

In total, evidence for attacker activity was seen between July 9, 2021, and June 22, 2023, according to the report, although the ICO clarifies the latter date regards when the compromised infrastructure was decommissioned and not when the hackers last accessed the ACRO environment.

Group A, described as the most serious of the incidents, saw the attacker maintain persistent access to ACRO’s website and content management system for approximately seven months, between August 2022 and March 2023.

During that period, the attacker conducted reconnaissance and in February 2023 staged the sensitive data of just under 11,000 people for exfiltration. The ICO found that ACRO’s failure to retain sufficient logs also meant the office could not actually confirm whether data was exfiltrated.

The other incidents were not detailed at length, although one was said to involve an SQL injection that exposed employee credentials. The ICO did not specify when these occurred within the broader two-year window.

After initially claiming its website was down for essential maintenance, ACRO had [disclosed](https://therecord.media/acro-cybersecurity-incident-uk-criminal-records) in April 2023 — following contact by the Evening Standard newspaper — that it had been responding to a cybersecurity incident.

The [Medusa](https://therecord.media/tag/medusa) ransomware group subsequently claimed responsibility, although no stolen data was ever published on the group’s leak site. Whether this indicates that an extortion payment was quietly paid or that the claim itself was fabricated by Medusa for publicity remains unknown.

On a precautionary basis, ACRO notified more than 84,000 people in April 2023 who had submitted applications to the database during the at-risk window. More than 40 formal complaints followed, although the ICO said it did not investigate these.

Throughout the reprimand document, the ICO blames ACRO as an institution rather than any individual, even by management role or job title, who may have failed to carry out specific responsibilities. The key suppliers are redacted throughout.

According to the ICO, network segmentation ultimately prevented the attacker from moving beyond the compromised web environment into the core policing system — something the regulator cited as a mitigating factor in its decision to issue a reprimand, which carries no financial penalty.

ACRO has since decommissioned the compromised infrastructure and implemented a new security information and event management system. It did not respond to a request for comment before publication.

* [Government](/news/government)
* [Cybercrime](/news/cybercrime)
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

* [FBI: Hackers using social engineering to breach accounts and steal explicit contentAugust 12th, 2026](/social-engineering-hackers-explicit-photos-fbi-alert)
* [Microsoft’s massive Patch Tuesday releases continue as AI reshapes bug discoveryAugust 12th, 2026](/microsoft-massive-patch-tuesday-releases-continue-ai)
* [Ransomware group hijacks hospital system’s Facebook page amid ongoing cyberattack falloutAugust 11th, 2026](/ransomware-group-hijacks-hospital-facebook-amid-cyberattack-response)
* [US cyber ambassador nominee Cassady confirmed in SenateAugust 7th, 2026](/adam-cassady-confirmed-senate-cyber-ambassador)
* [Military device manufacturer discloses cyber incident to SECAugust 7th, 2026](/military-device-manufacturer-discloses-cyber-incident)
* [Levi Strauss says hackers breached employee computers, accessed corporate dataAugust 7th, 2026](/levis-data-breach-social-engineering)
* [French rugby club Stade Français restores systems after cyberattack, probes data leakAugust 7th, 2026](/french-rugby-club-restores-systems-after-cyberattack)
* [Cyberattack on North Carolina Ports ‘contained’ as Coast ...
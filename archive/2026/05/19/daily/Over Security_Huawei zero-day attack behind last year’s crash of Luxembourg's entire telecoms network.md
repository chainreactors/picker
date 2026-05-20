---
title: Huawei zero-day attack behind last year’s crash of Luxembourg's entire telecoms network
url: https://therecord.media/huawei-zero-day-behind-last-year-luxembourg-telecom-outage
source: Over Security
date: 2026-05-19
fetch_date: 2026-05-20T06:04:59.507120
---

# Huawei zero-day attack behind last year’s crash of Luxembourg's entire telecoms network

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

![huawei](https://cms.therecord.media/uploads/large_huawei_111c759701.jpg)

Image: Olaf Kosinsky via WIkimedia Commons (CC BYSA 3.0)

[Alexander Martin](/author/alexander-martin)May 19th, 2026

# Huawei zero-day attack behind last year’s crash of Luxembourg's entire telecoms network

An attack exploiting a previously unknown vulnerability in Huawei enterprise router software caused a nationwide telecoms outage in Luxembourg last year, according to multiple sources briefed on the matter, disrupting mobile, landline and emergency communications for more than three hours.

The vulnerability has never been publicly disclosed. No CVE identifier — used by cybersecurity professionals worldwide to track software flaws and protect their systems — has been filed in any public database in the ten months since the incident, and no public warning has been issued to other operators running the same equipment.

Paul Rausch, the head of communications at POST Luxembourg, the state-owned operator whose network failed, said the incident was a denial-of-service (DoS) attack targeting a network device. He confirmed it exploited “a non-public, non-documented behaviour, for which no patch was available at the time” and was “not related to the exploitation of any known or previously documented vulnerabilities.”

Rausch said Huawei told POST it had never encountered the attack among any of its customers and had no ready-made solution.

Multiple sources briefed on the matter, who spoke on condition of anonymity to discuss confidential briefings, described the incident as a zero-day attack. There is no evidence that the incident has recurred, but the flaw remains unexplained and has not been publicly acknowledged by the company.

Huawei received detailed questions from Recorded Future News ahead of publication but did not provide any statements in response.

## The outage

The incident began toward the end of the working day on July 23, 2025. POST’s landline, 4G and 5G mobile networks went down, leaving potentially hundreds of thousands of residents unable to contact emergency services.

It was caused by specially crafted network traffic that sent Huawei enterprise routers into a continuous restart loop, crashing critical parts of POST’s infrastructure. When connectivity was restored more than three hours later, the country’s emergency call center received hundreds of additional calls.

At the time, Luxembourg’s government described the incident as “an exceptionally advanced and sophisticated cyberattack.” POST said that description referred to the expertise required to exploit the vulnerability.

The government also initially described the incident as a DDoS attack, and POST later clarified that it was not the type of volumetric DDoS attack often used by hacktivists and cybercriminals.

The country’s public prosecutor said an investigation by police and cybersecurity experts identified that “corrupted data, which may be used to prepare an attack on a random server responding to it, had been relayed through POST Luxembourg acting in its role as internet service provider and caused their systems to stop and reboot instead of simply relaying the data.”

But investigators ultimately concluded there was “no evidence that an attack was specifically directed at POST Luxembourg as a chosen target,” a spokesperson for Luxembourg’s High Commission for National Protection told Recorded Future News. No criminal charges have been filed.

The findings suggest the outage may have been triggered by maliciously crafted network traffic simply passing through POST’s infrastructure. Instead of forwarding the data onward, Huawei routers appear to have hit an undocumented failure condition that caused them to repeatedly stop and reboot.

Huawei’s VRP network operating system has previously been affected by denial-of-service vulnerabilities involving specially crafted protocol traffic, including [CVE-2021-22359](https://nvd.nist.gov/vuln/detail/CVE-2021-22359) and [CVE-2022-29798](https://www.cve.org/CVERecord?id=CVE-2022-29798). Similar flaws have also affected other major networking platforms, where malformed network traffic could trigger crashes, reloads or remote compromise in systems processing otherwise routine communications.

POST said neither previously disclosed Huawei vulnerability was involved in the Luxembourg incident.

## The disclosure gap

While Huawei routinely files CVEs for consumer products, public disclosures involving vulnerabilities in its enterprise networking software have become rare in recent years, with many of the publicly documented cases instead originating from independent security researchers.

The company still publishes enterprise security advisories, but through a restricted customer portal rather than broad public advisories. One such advisory — that also did not include a CVE identifier — was published last month describing a denial-of-service flaw involving packet parsing. There is no evidence that the advisory was related to the Luxembourg incident.

After the attack, Luxembourg authorities and Huawei held a series of technical meetings to understand what had happened, according to Anne Jung, spokesperson for the High Commission for National Protection.

Luxembourg’s cybersecurity authorities also alerted partner incident response teams across Europe through established government channels. But no CVE was ever filed alerting the community at large.

Asked who was responsible for issuing a CVE, Jung said that decision rests with the vendor under standard disclosure procedures. POST separately told Recorded Future News it contributed technical information but did not control disclosure decisions.

Huawei did not respond to questions about why no public CVE had been issued for the vulnerability that caused Luxembourg’s nationwide telecoms outage. Ten months later, it remains unclear whether the vulnerability was ever fully patched, how many operators may have been exposed or whether similar Huawei systems remain vulnerable today.

* [Cybercrime](/news/cybercrime)
* [Government](/news/government)
* [News](/)
* [Technology](/news/technology)

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

* [UK regulator to require tech firms to tackle deepfakes, non-consensual intimate imagesMay 19th, 2026](/uk-regulator-to-require-tech-firms-to-tackle-deepfakes-nudification-ai)
* [More than 200 arrested in cyber raids aimed at Middle East scam networksMay 18th, 2026](/more-than-200-arrested-interpol-middle-east-scams)
* [Grafana refuses to pay ransom after codebase theftMay 18th,...
---
title: Low-Drama ‘Dark Angels’ Reap Record Ransoms
url: https://krebsonsecurity.com/2024/08/low-drama-dark-angels-reap-record-ransoms/
source: Over Security - Cybersecurity news aggregator
date: 2024-08-06
fetch_date: 2025-10-06T18:13:33.338778
---

# Low-Drama ‘Dark Angels’ Reap Record Ransoms

Advertisement

[![](/b-sysdig/1.png)](https://content.foleon.com/sysdig/sysdig-cloud-defense-report-2025/?utm_source=krebs-on-security&utm_medium=display&utm_campaign=aware_amer_the-right-way_na_ung_display&utm_content=AD000460_1240x110)

Advertisement

[![](/b-sysdig/2.png)](https://content.foleon.com/sysdig/sysdig-cloud-defense-report-2025/?utm_source=krebs-on-security&utm_medium=display&utm_campaign=aware_amer_the-right-way_na_ung_display&utm_content=AD000462_1240x160)

[![Krebs on Security](https://krebsonsecurity.com/wp-content/uploads/2021/03/kos-27-03-2021.jpg)](https://krebsonsecurity.com/ "Krebs on Security")

[Skip to content](#content "Skip to content")

* [Home](https://krebsonsecurity.com/)
* [About the Author](https://krebsonsecurity.com/about/)
* [Advertising/Speaking](https://krebsonsecurity.com/cpm/)

# Low-Drama ‘Dark Angels’ Reap Record Ransoms

August 5, 2024

[25 Comments](https://krebsonsecurity.com/2024/08/low-drama-dark-angels-reap-record-ransoms/#comments)

A ransomware group called **Dark Angels** made headlines this past week when it was revealed the crime group recently received a record $75 million data ransom payment from a Fortune 50 company. Security experts say the Dark Angels have been around since 2021, but the group doesn’t get much press because they work alone and maintain a low profile, picking one target at a time and favoring mass data theft over disrupting the victim’s operations.

![](https://krebsonsecurity.com/wp-content/uploads/2024/08/darkfeathers.png)

Security firm **Zscaler** **ThreatLabz** this month ranked Dark Angels as the top ransomware threat for 2024, noting that in early 2024 a victim paid the ransomware group $75 million — higher than any previously recorded ransom payment. ThreatLabz found Dark Angels has conducted some of the largest ransomware attacks to date, and yet little is known about the group.

[**Brett Stone-Gross**](https://krebsonsecurity.com/tag/brett-stone-gross/), senior director of threat intelligence at ThreatLabz, said Dark Angels operate using an entirely different playbook than most other ransomware groups. For starters, he said, Dark Angels does not employ the typical ransomware affiliate model, which relies on hackers-for-hire to install malicious software that locks up infected systems.

“They really don’t want to be in the headlines or cause business disruptions,” Stone-Gross said. “They’re about making money and attracting as little attention as possible.”

Most ransomware groups maintain flashy victim leak sites which threaten to publish the target’s stolen data unless a ransom demand is paid. But the Dark Angels didn’t even have a victim shaming site [until April 2023](https://x.com/threatlabz/status/1645455117024641024?s=46&t=N2Ox1VDbEK4tC6bNjFPKYw). And the leak site isn’t particularly well branded; it’s called **Dunghill Leak**.

![](https://krebsonsecurity.com/wp-content/uploads/2024/08/dunghill.png)

“Nothing about them is flashy,” Stone-Gross said. “For the longest time, they didn’t even want to cause a big headline, but they probably felt compelled to create that leaks site because they wanted to show they were serious and that they were going to post victim data and make it accessible.”

Dark Angels is thought to be a Russia-based cybercrime syndicate whose distinguishing characteristic is stealing truly staggering amounts of data from major companies across multiple sectors, including healthcare, finance, government and education. For large businesses, the group has exfiltrated between 10-100 terabytes of data, which can take days or weeks to transfer, ThreatLabz found.

Like most ransom gangs, Dark Angels will publish data stolen from victims who do not pay. Some of the more notable victims listed on Dunghill Leak include the global food distribution firm **Sysco**, which [disclosed a ransomware attack in May 2023](https://www.bleepingcomputer.com/news/security/food-distribution-giant-sysco-warns-of-data-breach-after-cyberattack/); and the travel booking giant **Sabre**, which was [hit by the Dark Angels in September 2023](https://techcrunch.com/2023/09/06/ransomware-gang-claims-credit-for-sabre-data-breach/).

Stone-Gross said Dark Angels is often reluctant to deploy ransomware malware because such attacks work by locking up the target’s IT infrastructure, which typically causes the victim’s business to grind to a halt for days, weeks or even months on end. And those types of breaches tend to make headlines quickly.

“They selectively choose whether they want to deploy ransomware or not,” he said. “If they deem they can encrypt some files that won’t cause major disruptions — but will give them a ton of data — that’s what they’ll do. But really, what separates them from the rest is the volume of data they’re stealing. It’s a whole order of magnitude greater with Dark Angels. Companies losing vast amounts of data will pay these high ransoms.”

So who paid the record $75 million ransom? **Bleeping Computer** [posited on July 30](https://www.bleepingcomputer.com/news/security/dark-angels-ransomware-receives-record-breaking-75-million-ransom/) that the victim was the pharmaceutical giant **Cencora** (formerly **AmeriSourceBergen Corporation**), which reported a data security incident to the **U.S. Securities and Exchange Commission** (SEC) on February 21, 2024.

The SEC requires publicly-traded companies to disclose a potentially material cybersecurity event within four days of the incident. Cencora is currently #10 on the Fortune 500 list, generating more than $262 billion in revenue last year.

Cencora did not respond to questions about whether it had made a ransom payment in connection with the February cybersecurity incident, and referred KrebsOnSecurity to expenses listed under “Other” in the restructuring section of their [latest quarterly financial report](https://d18rn0p25nwr6d.cloudfront.net/CIK-0001140859/668abd56-26dc-4495-8c63-32e7ee623633.pdf) (PDF). That report states that the majority of the $30 million cost in “Other” was associated with the breach.

Cencora’s quarterly statement said the incident affected a standalone legacy information technology platform in one country and the foreign business unit’s ability to operate in that country for approximately two weeks.

[![](https://krebsonsecurity.com/wp-content/uploads/2024/08/cencora-disc.png)](https://krebsonsecurity.com/wp-content/uploads/2024/08/cencora-disc.png)

Cencora’s 2024 1st quarter report documents a $30 million cost associated with a data exfiltration event in mid-February 2024.

In its most recent [State of Ransomware report](https://assets.sophos.com/X24WTUEQ/at/9brgj5n44hqvgsp5f5bqcps/sophos-state-of-ransomware-2024-wp.pdf) (PDF), security firm **Sophos** found the average ransomware payment had increased fivefold in the past year, from $400,000 in 2023 to $2 million. Sophos says that *in more than four-fifths (82%) of cases funding for the ransom came from multiple sources*. Overall, 40% of total ransom funding came from the organizations themselves and 23% from insurance providers.

Further reading: [ThreatLabz ransomware report](https://www.zscaler.com/resources/industry-reports/threatlabz-ransomware-report.pdf) (PDF).

*This entry was posted on Monday 5th of August 2024 03:52 PM*

[A Little Sunshine](https://krebsonsecurity.com/category/sunshine/) [Data Breaches](https://krebsonsecurity.com/category/data-breaches/) [Ransomware](https://krebsonsecurity.com/category/ransomware/)

[AmerisourceBergen Corporation](https://krebsonsecurity.com/tag/amerisourcebergen-corporation/) [Bleeping Computer](https://krebsonsecurity.com/tag/bleeping-computer/) [Brett Stone-Gross](https://krebsonsecurity.com/tag/brett-stone-gross/) [Cencora](https://krebsonsecurity.com/tag/cencora/) [Dark Angels](https://krebsonsecurity.com/tag/dark-angels/) [Dunghill Leak](https://krebsonsecurity.com/tag/dunghill-leak/) [ransomware](https://krebsonsecurity.com/tag/ransomware/) [Sabre](https://krebsonsecuri...
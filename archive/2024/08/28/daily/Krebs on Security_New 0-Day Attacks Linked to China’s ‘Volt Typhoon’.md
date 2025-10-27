---
title: New 0-Day Attacks Linked to China’s ‘Volt Typhoon’
url: https://krebsonsecurity.com/2024/08/new-0-day-attacks-linked-to-chinas-volt-typhoon/
source: Krebs on Security
date: 2024-08-28
fetch_date: 2025-10-06T18:12:21.272650
---

# New 0-Day Attacks Linked to China’s ‘Volt Typhoon’

Advertisement

[![](/b-knowbe4/40.png)](https://gateway.on24.com/wcc/eh/1815783/human-risk-management-summit?partnerref=krebs)

Advertisement

[![](/b-knowbe4/37.jpg)](https://www.knowbe4.com/resources/kits/cybersecurity-awareness-month?utm_source=Krebs&utm_medium=display&utm_campaign=cybersecurityawarenessmonth&utm_content=hrm+)

[![Krebs on Security](https://krebsonsecurity.com/wp-content/uploads/2021/03/kos-27-03-2021.jpg)](https://krebsonsecurity.com/ "Krebs on Security")

[Skip to content](#content "Skip to content")

* [Home](https://krebsonsecurity.com/)
* [About the Author](https://krebsonsecurity.com/about/)
* [Advertising/Speaking](https://krebsonsecurity.com/cpm/)

# New 0-Day Attacks Linked to China’s ‘Volt Typhoon’

August 27, 2024

[12 Comments](https://krebsonsecurity.com/2024/08/new-0-day-attacks-linked-to-chinas-volt-typhoon/#comments)

Malicious hackers are exploiting a zero-day vulnerability in **Versa Director**, a software product used by many Internet and IT service providers. Researchers believe the activity is linked to **Volt Typhoon**, a Chinese cyber espionage group focused on infiltrating critical U.S. networks and laying the groundwork for the ability to disrupt communications between the United States and Asia during any future armed conflict with China.

![](https://krebsonsecurity.com/wp-content/uploads/2024/08/ss-dissolvingsphere.png)

Versa Director systems are primarily used by Internet service providers (ISPs), as well as managed service providers (MSPs) that cater to the IT needs of many small to mid-sized businesses simultaneously. In [a security advisory](https://versa-networks.com/blog/versa-security-bulletin-update-on-cve-2024-39717-versa-director-dangerous-file-type-upload-vulnerability/) published Aug. 26, Versa urged customers to deploy a patch for the vulnerability ([CVE-2024-39717](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-39717)), which the company said is fixed in *Versa Director 22.1.4* or later.

Versa said the weakness allows attackers to upload a file of their choosing to vulnerable systems. The advisory placed much of the blame on Versa customers who “failed to implement system hardening and firewall guidelines…leaving a management port exposed on the internet that provided the threat actors with initial access.”

Versa’s advisory doesn’t say how it learned of the zero-day flaw, but its vulnerability listing at mitre.org acknowledges “there are reports of others based on backbone telemetry observations of a 3rd party provider, however these are unconfirmed to date.”

Those third-party reports came in late June 2024 from **Michael Horka**, senior lead information security engineer at **Black Lotus Labs**, the security research arm of **Lumen Technologies**, which operates one of the global Internet’s largest backbones.

In an interview with KrebsOnSecurity, Horka said Black Lotus Labs identified a web-based backdoor on Versa Director systems belonging to four U.S. victims and one non-U.S. victim in the ISP and MSP sectors, with the earliest known exploit activity occurring at a U.S. ISP on June 12, 2024.

“This makes Versa Director a lucrative target for advanced persistent threat (APT) actors who would want to view or control network infrastructure at scale, or pivot into additional (or downstream) networks of interest,” Horka [wrote](https://blog.lumen.com/taking-the-crossroads-the-versa-director-zero-day-exploitation/) in a blog post published today.

Black Lotus Labs said it assessed with “medium” confidence that Volt Typhoon was responsible for the compromises, noting the intrusions bear the hallmarks of the Chinese state-sponsored espionage group — including zero-day attacks targeting IT infrastructure providers, and Java-based backdoors that run in memory only.

In May 2023, the **National Security Agency** (NSA), the **Federal Bureau of Investigation** (FBI), and the **Cybersecurity Infrastructure Security Agency** (CISA) issued [a joint warning](https://media.defense.gov/2023/May/24/2003229517/-1/-1/0/CSA_Living_off_the_Land.PDF) (PDF) about Volt Typhoon, also known as “**Bronze Silhouette**” and “**Insidious Taurus**,” which described how the group uses small office/home office (SOHO) network devices to hide their activity.

In early December 2023, Black Lotus Labs [published its findings](https://blog.lumen.com/routers-roasting-on-an-open-firewall-the-kv-botnet-investigation/) on “**KV-botnet**,” thousands of compromised SOHO routers that were chained together to form a covert data transfer network supporting various Chinese state-sponsored hacking groups, including Volt Typhoon.

In January 2024, the **U.S. Department of Justice** disclosed the FBI had [executed a court-authorized takedown](https://www.justice.gov/opa/pr/us-government-disrupts-botnet-peoples-republic-china-used-conceal-hacking-critical) of the KV-botnet shortly before Black Lotus Labs released its December report.

In February 2024, CISA again joined the FBI and NSA in [warning](https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-038a) Volt Typhoon had compromised the IT environments of multiple critical infrastructure organizations — primarily in communications, energy, transportation systems, and water and wastewater sectors — in the continental and non-continental United States and its territories, including Guam.

“Volt Typhoon’s choice of targets and pattern of behavior is not consistent with traditional cyber espionage or intelligence gathering operations, and the U.S. authoring agencies assess with high confidence that Volt Typhoon actors are pre-positioning themselves on IT networks to enable lateral movement to OT [operational technology] assets to disrupt functions,” that alert warned.

In a speech at Vanderbilt University in April, FBI Director **Christopher Wray** [said](https://www.reuters.com/technology/cybersecurity/fbi-says-chinese-hackers-preparing-attack-us-infrastructure-2024-04-18/) China is developing the “ability to physically wreak havoc on our critical infrastructure at a time of its choosing,” and that China’s plan is to “land blows against civilian infrastructure to try to induce panic.”

**Ryan English**, an information security engineer at Lumen, said it’s disappointing his employer didn’t at least garner an honorable mention in Versa’s security advisory. But he said he’s glad there are now a lot fewer Versa systems exposed to this attack.

“Lumen has for the last nine weeks been very intimate with their leadership with the goal in mind of helping them mitigate this,” English said. “We’ve given them everything we could along the way, so it kind of sucks being referenced just as a third party.”

*This entry was posted on Tuesday 27th of August 2024 10:26 AM*

[A Little Sunshine](https://krebsonsecurity.com/category/sunshine/) [Internet of Things (IoT)](https://krebsonsecurity.com/category/internet-of-things-iot/) [Latest Warnings](https://krebsonsecurity.com/category/latest-warnings/) [The Coming Storm](https://krebsonsecurity.com/category/comingstorm/)

[Black Lotus Labs](https://krebsonsecurity.com/tag/black-lotus-labs/) [Bronze Silhouette](https://krebsonsecurity.com/tag/bronze-silhouette/) [Christopher Wray](https://krebsonsecurity.com/tag/christopher-wray/) [CVE-2024-39717](https://krebsonsecurity.com/tag/cve-2024-39717/) [Cybersecurity & Infrastructure Security Agency](https://krebsonsecurity.com/tag/cybersecurity-infrastructure-security-agency/) [Federal Bureau of Investigation](https://krebsonsecurity.com/tag/federal-bureau-of-investigation/) [Insidious Taurus](https://krebsonsecurity.com/tag/insidious-taurus/) [KV-botnet](https://krebsonsecurity.com/tag/kv-botnet/) [Lumen Technologies](https://krebsonsecurity.com/tag/lumen-technologies/) [Michael Horka](https://krebsonsecurity.com/tag/michael-horka/) [national security agency](https://krebsonsecurity.com/tag/national-security-agency/) [Ryan English](https://krebsonsecurity.com/tag/ryan-english/) [U.S. Departm...
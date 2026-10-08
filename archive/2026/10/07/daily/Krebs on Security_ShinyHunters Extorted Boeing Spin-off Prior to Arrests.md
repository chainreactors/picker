---
title: ShinyHunters Extorted Boeing Spin-off Prior to Arrests
url: https://krebsonsecurity.com/2026/10/shinyhunters-extorted-boeing-spin-off-prior-to-arrests/
source: Krebs on Security
date: 2026-10-07
fetch_date: 2026-10-08T08:08:37.257098
---

# ShinyHunters Extorted Boeing Spin-off Prior to Arrests

Advertisement

[![](/b-flashpoint/5.png)](https://flashpoint.io/ignite/?utm_source=krebsonsecurity&utm_medium=display&utm_campaign=brand-ignite&utm_content=noise-a)

Advertisement

[![](/b-doppel/18.png)](https://www.doppel.com/?utm_source=krebsonsecurity&utm_medium=display&utm_campaign=fy27brandcampaign&utm_content=detectdisrupt)

[![Krebs on Security](https://krebsonsecurity.com/wp-content/uploads/2021/03/kos-27-03-2021.jpg)](https://krebsonsecurity.com/ "Krebs on Security")

[Skip to content](#content "Skip to content")

* [Home](https://krebsonsecurity.com/)
* [About the Author](https://krebsonsecurity.com/about/)
* [Advertising/Speaking](https://krebsonsecurity.com/cpm/)

# ShinyHunters Extorted Boeing Spin-off Prior to Arrests

October 7, 2026

[9 Comments](https://krebsonsecurity.com/2026/10/shinyhunters-extorted-boeing-spin-off-prior-to-arrests/#comments)

A teenager from Amman, Jordan suspected of leading the prolific data theft and extortion group **ShinyHunters** has been detained and is reportedly cooperating with the FBI to identify other members of the hacking gang. KrebsOnSecurity has learned that the suspect, who uses the hacker handle “**Rey**,” was detained as ShinyHunters was in the process of extorting a business unit recently divested by the global aerospace company **Boeing**, which manufactures the fleet of planes used by the employer of Rey’s father — **Royal Jordanian Airlines**.

![](https://krebsonsecurity.com/wp-content/uploads/2026/10/Jeppesen.png)

The logo for Jeppesen ForeFlight, a business unit divested last year by the aerospace firm Boeing.

On October 3, **Reuters** [cited](https://www.reuters.com/world/middle-east/key-shinyhunters-hacker-detained-jordan-is-cooperating-sources-say-2026-10-03/) three unnamed sources saying a suspected ShinyHunters member in Amman named **Saif Al-din Khader** was detained by Jordanian authorities and was cooperating with the FBI. KrebsOnSecurity identified Rey as Khader in [a November 2025 profile](https://krebsonsecurity.com/2025/11/meet-rey-the-admin-of-scattered-lapsus-hunters/), in which the young man admitted working with multiple ransomware groups.

Rey was featured again in [a September 28 exclusive](https://krebsonsecurity.com/2026/09/dutch-police-arrest-reformed-hacker-in-shiny-hunters-investigation/) about the Dutch police arresting 24-year-old convicted cybercriminal **Pepijn van der Stap** on suspicion of aiding in data thefts and extortions by ShinyHunters. The story noted that immediately following the Dutchman’s arrest on the evening of September 15, Rey assumed control over the ShinyHunters brand and boasted publicly about stealing highly sensitive data from the **FBI** and extorting the ransomware group **Cl0p**.

Rey taunted both the FBI and Cl0p with memes posted to his longtime account on Twitter/X, while simultaneously including images of the avatar used by Van Der Stap’s former hacker alias “**Umbreon**” in an apparent attempt to frame the Dutchman for both hacks.

![](https://krebsonsecurity.com/wp-content/uploads/2026/09/rey-cl0p-fbi.png)

A taunting meme uploaded to Twitter/X by Rey on Sept. 22. A giant sized version of the Pokemon character Umbreon can be seen in the bottom left.

As noted in our September 28 report, ShinyHunters gained access to the FBI site and other victims by exploiting a vulnerability (CVE-2026-35273) in **PeopleSoft**, a software-as-a-service platform from the tech giant **Oracle** that is broadly used by companies to manage hiring and human resources, benefits and payroll. Oracle quickly issued a fix for CVE-2026-35273, which ShinyHunters first began exploiting as a zero-day in June, and at the time Mandiant released web application firewall rules intended for organizations that couldn’t apply the security update quickly enough.

ShinyHunters [told BleepingComputer in June](https://www.bleepingcomputer.com/news/security/oracle-peoplesoft-servers-hacked-in-shinyhunters-data-theft-attacks/) that the original goal behind exploiting the PeopleSoft vulnerability was to breach the FBI’s own PeopleSoft database, but the hackers said those attacks were unsuccessful for some reason. In recent weeks, however, ShinyHunters [turned to a well-known URL-encoding trick](https://www.bleepingcomputer.com/news/security/shinyhunters-uses-waf-bypass-trick-in-oracle-peoplesoft-attacks/) to bypass Mandiant’s suggested web application firewall rules.

In [a report](https://cloud.google.com/blog/topics/threat-intelligence/shinyhunters-renewed-mass-exploitation-campaign-targeting-oracle-peoplesoft) released Sept. 25, security experts at **Mandiant** and the **Google Threat Intelligence Group** (GTIG) confirmed that ShinyHunters had mass-exploited the PeopleSoft vulnerability to steal data from dozens of systems across a range of industries, including higher education, technology, healthcare, agriculture, transportation and government.

Reuters [reported October 5](https://www.reuters.com/technology/accenture-contractor-removed-fbi-following-damaging-data-breach-sources-say-2026-10-06/) that the FBI has removed a contractor at **Accenture** over their failure to patch the FBI recruitment website hacked by ShinyHunters, which exposed sensitive data on more than 5,000 FBI personnel, including each’s person’s unit and specialization, as well as medical and psychiatric records.

## ‘REY’ MEANS KING, AS IN ROYAL

According to two sources familiar with the ShinyHunters investigation, a navigation and digital aviation unit recently divested by the global aerospace company **Boeing** was among the victims that ShinyHunters was in the process of extorting when Rey was apprehended by Jordanian authorities.

Those sources said the FBI’s investigation into ShinyHunters gained renewed urgency with the group’s attempted extortion of the former Boeing unit, which allegedly included the theft of sensitive information that sources said could pose operational safety and security risks.

In a brief statement shared with KrebsOnSecurity, Boeing acknowledged the extortion attempts by ShinyHunters, and said the incident concerned data stolen from **Jeppesen ForeFlight**, a subsidiary that Boeing [sold in November 2025](https://www.reuters.com/business/aerospace-defense/buyout-firm-thoma-bravo-nears-deal-boeings-jeppesen-unit-bloomberg-news-reports-2025-04-22/) to the private equity firm Thoma Bravo for $10.55 billion.

“We are aware of claims by a threat actor regarding data allegedly associated with Boeing and our former subsidiary Jeppesen ForeFlight,” a Boeing spokesperson shared. “We are actively reviewing the matter with the Jeppesen ForeFlight team.”

A spokesperson for Jeppesen ForeFlight shared a written statement in response to questions, saying the company has seen no impact on their end. “Based on our investigation to date into this claim and proactive security posture, there was no impact to our operations or products.”

Rey’s alleged involvement in attempting to extort the former Boeing unit is noteworthy because there is strong evidence that his father works for **Royal Jordanian Airlines**, which is mostly controlled by the Jordanian government and operates its long-haul fleet on passenger planes built by Boeing. Rey claimed on Telegram in early 2025 that his father was an airline pilot, although that could not be independently confirmed.

However, as noted in [our November 2025 profile of Rey](https://krebsonsecurity.com/2025/11/meet-rey-the-admin-of-scattered-lapsus-hunters/), his family’s shared computer was at one point compromised by password-stealing malware, and the data collected by that malware clearly shows Rey’s father used the same credentials to log in at multiple online portals for Royal Jordanian Airlines employees.

Royal Jordanian Airlines has not yet responded to a request for comment. In advance of our September 28 story, KrebsOnSecurity once again emailed Rey’s father to seek comment and update him on his son’s alleged activities. Neither of the...
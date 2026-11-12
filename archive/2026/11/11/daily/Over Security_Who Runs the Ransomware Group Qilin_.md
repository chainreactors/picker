---
title: Who Runs the Ransomware Group Qilin?
url: https://krebsonsecurity.com/2026/11/who-runs-the-ransomware-group-qilin/
source: Over Security
date: 2026-11-11
fetch_date: 2026-11-12T09:02:28.570264
---

# Who Runs the Ransomware Group Qilin?

Advertisement

[![](/b-spycloud/5.png)](https://spycloud.com/check-your-exposure/?utm_medium=paid-ads&utm_source=third-party&utm_term=banner&utm_campaign=ads-cye-krebs-2026&cid=701UM00000o23RgYAI)

Advertisement

[![](/b-spycloud/2.png)](https://spycloud.com/check-your-exposure/?utm_medium=paid-ads&utm_source=third-party&utm_term=banner&utm_campaign=ads-cye-krebs-2026&cid=701UM00000o23RgYAI)

[![Krebs on Security](https://krebsonsecurity.com/wp-content/uploads/2021/03/kos-27-03-2021.jpg)](https://krebsonsecurity.com/ "Krebs on Security")

[Skip to content](#content "Skip to content")

* [Home](https://krebsonsecurity.com/)
* [About the Author](https://krebsonsecurity.com/about/)
* [Advertising/Speaking](https://krebsonsecurity.com/cpm/)

# Who Runs the Ransomware Group Qilin?

November 11, 2026

[4 Comments](https://krebsonsecurity.com/2026/11/who-runs-the-ransomware-group-qilin/#comments)

The cybercrime group **Qilin** has emerged as the world’s most active ransomware affiliate program, claiming at least 365 victim organizations in the past three months alone. But even top Russian hackers make operational security mistakes, and the administrator of Qilin has made a few key missteps over the last decade that all point to a 36-year-old man living in St. Petersburg, Russia.

Operating since September 2022, the Russia-based ransomware group Qilin is the currently the most industrious ransomware-as-a-service gang, according to [a report](https://insights.nccgroup.com/l/898251/2026-10-20/31p2gvf/898251/1792504020AatiUmdr/September_2026_Review_of_Q3_Cyber_Threat_Intelligence_Report_FREEMIUM.pdf) (PDF) this month by the cybersecurity firm **NCC Group** (KrebsOnSecurity profiled the administrator of the second most active ransomware group — [The Gentlemen](https://krebsonsecurity.com/2026/06/who-runs-the-ransomware-group-the-gentlemen/) — in June).

![](https://krebsonsecurity.com/wp-content/uploads/2026/11/haise-ramp-kela.png)

The Qilin ransomware administrator “Haise” advertising his affiliate program on the cybercrime forum RAMP. Image: Ke-la.com.

Qilin attracts affiliates to hack into companies and deploy ransomware by offering them at least 80 percent of any extortion amount paid by victims. Its members practice the “double extortion” model, stealing sensitive data before encrypting systems and threatening to publish the files online. Unlike most ransomware partnerships based out of Russia, Qilin is happy to team with English-speaking affiliates, and its leader has shared on Telegram that they’ve worked with cybercrime groups like [Scattered Spider](https://krebsonsecurity.com/tag/scattered-spider/) and [RansomHub](https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-242a).

The head of Qilin goes by the handle “**Haise**,” but they weren’t always known by this nickname. It is not uncommon for cybercriminals to change their handle periodically as an operational security (opsec) measure. Doing so is generally a smart move, because it helps to sever one’s ties to older identities that may not have been as careful on basic opsec, such as separating their real life identity from their cybercrime activities. But even those cautious criminals will sometimes have to reference their past monikers when applying for membership at a new forum. And forums eventually get hacked or seized. That is precisely what happened with Haise.

The cyber intelligence platform [Intel 471](https://intel471.com) records that in June 2022, Haise applied for membership to **RAMP**, a closely-guarded Russian cybercrime forum that was created as a haven for ransomware affiliate programs. Intel 471 has indexed direct messages from RAMP (the forum was [seized by the FBI](https://www.cloudsek.com/blog/the-rise-and-fall-of-ramp-inside-the-forum-where-ransomware-was-always-welcome) in January 2026), and those missives show the RAMP administrator approved Haise’s application, referring to this user as Haise and by their Telegram username: **Alexbigboss44**.

Searching Intel 471 for Alexbigboss44 reveals this was the Telegram account name shared by the user **Rjun** on the Russian cybercrime forums **Exploit** and **XSS** two years earlier in 2020. The cyber intelligence platform [Flashpoint](https://flashpoint.io) finds Alexbigboss44 is a prolific participant in cybercriminal forums and Telegram channels, primarily focused on the illicit trade of traffic, logs, and corporate access [full disclosure: Flashpoint is an advertiser on this blog].

![](https://krebsonsecurity.com/wp-content/uploads/2026/11/alexbigboss-rjun-kela.png)

The Qilin administrator once used the nickname “Rjun” on several forums, and shared their Telegram handle as “Alexbigboss44.” Image: Ke-la.com.

Flashpoint says this user was engaged in high-volume acquisition of Facebook logs and Google Ads accounts to facilitate fraudulent advertising and gambling schemes, and that they functioned as a broker and operator — managing a network of traffickers and purchasing compromised data to fuel their operations.

The link between the Qilin administrator Haise and the much older Rjun and Alexbigboss44 accounts was shared privately earlier this month by [IntelHawk](https://intelhawk.ai), which describes itself as an AI-based platform capable of de-anonymizing threat actors based on historical usernames, [stylometry](https://en.wikipedia.org/wiki/Stylometry) and other signals.

IntelHawk founder and chief technology officer **Leo Bogod** said an analysis of these identities shows a progression from novice arbitrageur and credit card fraudster in 2018–2019 to a more experienced participant and organizer of complex cybercrime-related activities in 2020–2023, with increasing attention to malware, botnets, and payment infrastructure.

Where does this connection between these threat actor identities lead? Intel 471 finds that by the time Alexbigboss44 was applying for membership to RAMP, Rjun was already a longtime member of several other Russian crime forums, including **Darkmarket**, **Verified**, and **Zloy**. Intel 471 says Rjun signed up at all of these sites with the email address **mail-30a@mail.ru**.

The identity threat protection firm [Spycloud](https://spycloud.com) found the email address mail-30a@mail.ru at one time used the password “Rjun132” [Spycloud is also an advertiser on this blog]. A search for that email at the breach tracking service [Constella Intelligence](https://constella.ai) shows that it appeared in records maintained by **gosuslugi.ru**, the official digital platform for state and municipal services in the Russian Federation.

Gosuslugi was breached in late 2025, reportedly exposing more than 20 million records with full names, birth dates, and mobile numbers. According to the leaked Gosuslugi records (via Constella), the address mail-30a@mail.ru belongs to 36-year-old **Aleksey Mikhailovich Yakovtsev** from St. Petersburg, Russia.

Flashpoint finds Haise has long used a Telegram account with the user **ID 118329521**, recording more than 5,000 messages from this user since 2018. Records from Russia’s education watchdog Rosobrnadzor reveal that Mr. Yakovtsev went to grade school in Murmansk and that he holds a master’s degree in computing and information systems.

A search on this Telegram ID in Constella shows it is linked to the Russian phone number +**79602347275**. Pivoting on that phone number in Constella reveals it is connected to the email addresses **aleksey1990yakov@mail.ru** and **rjun123321@mail.ru**. IntelHawk finds that +79602347275 belongs to Yakovtsev’s biological sister, and that Aleksey often used his sister’s email address when registering at different websites.

That phone number appears on several airline flight records at Russian travel agencies that have experienced a data breach in recent years, and those records show Aleksey Yakovtsev, born August 18, 1990, flew between St. Petersburg and Murmansk at least three times between 2013 and 2014.

More recent flight records ...
---
title: Who Got Arrested in the Raid on the XSS Crime Forum?
url: https://krebsonsecurity.com/2025/08/who-got-arrested-in-the-raid-on-the-xss-crime-forum/
source: Krebs on Security
date: 2025-08-07
fetch_date: 2025-10-07T00:53:13.728192
---

# Who Got Arrested in the Raid on the XSS Crime Forum?

Advertisement

[![](/b-knowbe4/36.jpg)](https://www.knowbe4.com/resources/kits/cybersecurity-awareness-month?utm_source=Krebs&utm_medium=display&utm_campaign=cybersecurityawarenessmonth&utm_content=hrm+)

Advertisement

[![](/b-knowbe4/37.jpg)](https://www.knowbe4.com/resources/kits/cybersecurity-awareness-month?utm_source=Krebs&utm_medium=display&utm_campaign=cybersecurityawarenessmonth&utm_content=hrm+)

[![Krebs on Security](https://krebsonsecurity.com/wp-content/uploads/2021/03/kos-27-03-2021.jpg)](https://krebsonsecurity.com/ "Krebs on Security")

[Skip to content](#content "Skip to content")

* [Home](https://krebsonsecurity.com/)
* [About the Author](https://krebsonsecurity.com/about/)
* [Advertising/Speaking](https://krebsonsecurity.com/cpm/)

# Who Got Arrested in the Raid on the XSS Crime Forum?

August 6, 2025

[22 Comments](https://krebsonsecurity.com/2025/08/who-got-arrested-in-the-raid-on-the-xss-crime-forum/#comments)

On July 22, 2025, the European police agency **Europol** [said](https://www.europol.europa.eu/media-press/newsroom/news/key-figure-behind-major-russian-speaking-cybercrime-forum-targeted-in-ukraine) a long-running investigation led by the French Police resulted in the arrest of a 38-year-old administrator of **XSS,** a Russian-language cybercrime forum with more than 50,000 members. The action has triggered an ongoing frenzy of speculation and panic among XSS denizens about the identity of the unnamed suspect, but the consensus is that he is a pivotal figure in the crime forum scene who goes by the hacker handle “**Toha**.” Here’s a deep dive on what’s knowable about Toha, and a short stab at who got nabbed.

![](https://krebsonsecurity.com/wp-content/uploads/2025/08/xss-sbu.png)

Europol did not name the accused, but published partially obscured photos of him from the raid on his residence in Kiev. The police agency said the suspect acted as a trusted third party — arbitrating disputes between criminals — and guaranteeing the security of transactions on XSS. A [statement](https://ssu.gov.ua/novyny/sbu-spilno-z-natspolitsiieiu-ta-pravookhorontsiamy-frantsii-vykryla-rozrobnyka-odniiei-z-naividomishykh-u-sviti-khakerskykh-platform) from Ukraine’s **SBU** security service said XSS counted among its members many cybercriminals from various ransomware groups, including **REvil**, **LockBit**, **Conti**, and **Qiliin**.

Since the Europol announcement, the XSS forum resurfaced at a new address on the deep web (reachable only via the anonymity network [Tor](https://en.wikipedia.org/wiki/Tor_%28network%29)). But from reviewing the recent posts, there appears to be little consensus among longtime members about the identity of the now-detained XSS administrator.

The most frequent comment regarding the arrest was a message of solidarity and support for Toha, the handle chosen by the longtime administrator of XSS and several other major Russian forums. Toha’s accounts on other forums have been silent since the raid.

Europol said the suspect has enjoyed a nearly 20-year career in cybercrime, which roughly lines up with Toha’s history. In 2005, Toha was a founding member of the Russian-speaking forum **Hack-All.** That is, until it got massively hacked a few months after its debut. In 2006, Toha rebranded the forum to [**exploit[.]in**](https://krebsonsecurity.com/tag/exploit-in/), which would go on to draw tens of thousands of members, including an eventual Who’s-Who of wanted cybercriminals.

Toha announced in 2018 that he was selling the Exploit forum, prompting rampant speculation on the forums that the buyer was secretly a Russian or Ukrainian government entity or front person. However, those suspicions were unsupported by evidence, and Toha vehemently denied the forum had been given over to authorities.

One of the oldest Russian-language cybercrime forums was **DaMaGeLaB**, which operated from 2004 to 2017, when its administrator “Ar3s” was arrested. In 2018, a partial backup of the DaMaGeLaB forum was [reincarnated as xss[.]is](https://www.own.security/en/ressources/blog/russian-language-cybercriminal-forums---chapter-iii-analyzing-the-most-active-and-renowned-communities-english-only), with Toha as its stated administrator.

## CROSS-SITE GRIFTING

Clues about Toha’s early presence on the Internet — from ~2004 to 2010 — are available in the archives of **Intel 471**, a cyber intelligence firm that tracks forum activity. Intel 471 shows Toha used the same email address across multiple forum accounts, including at Exploit, **Antichat**, **Carder[.]su** and **inattack[.]ru.**

**DomainTools.com** finds Toha’s email address — **toschka2003@yandex.ru** — was used to register at least a dozen domain names — most of them from the mid- to late 2000s. Apart from exploit[.]in and a domain called **ixyq[.]com**, the other domains registered to that email address end in .ua, the top-level domain for Ukraine (e.g. deleted.org[.]ua, lj.com[.]ua, and blogspot.org[.]ua).

![](https://krebsonsecurity.com/wp-content/uploads/2025/08/exploit-deleted-ua.png)

A 2008 snapshot of a domain registered to toschka2003@yandex.ru and to Anton Medvedovsky in Kiev. Note the message at the bottom left, “Protected by Exploit,in.” Image: archive.org.

Nearly all of the domains registered to toschka2003@yandex.ru contain the name **Anton Medvedovskiy** in the registration records, except for the aforementioned ixyq[.]com, which is registered to the name **Yuriy Avdeev** in Moscow.

This Avdeev surname came up in a lengthy conversation with [Lockbitsupp](https://krebsonsecurity.com/2024/05/u-s-charges-russian-man-as-boss-of-lockbit-ransomware-group/), the leader of the rapacious and destructive ransomware affiliate group **Lockbit**. The conversation took place in February 2024, when Lockbitsupp asked for help identifying Toha’s real-life identity.

![](https://krebsonsecurity.com/wp-content/uploads/2025/08/lcokbitsupp-convo.png)

In early 2024, the leader of the Lockbit ransomware group — Lockbitsupp — asked for help investigating the identity of the XSS administrator Toha, which he claimed was a Russian man named Anton Avdeev.

Lockbitsupp didn’t share why he wanted Toha’s details, but he maintained that Toha’s real name was **Anton Avdeev**. I declined to help Lockbitsupp in whatever revenge he was planning on Toha, but his question made me curious to look deeper.

It appears Lockbitsupp’s query was based on a now-deleted Twitter post from 2022, when a user by the name “[3xp0rt](https://x.com/3xp0rtblog/status/1585357689777164288)” asserted that Toha was a Russian man named **Anton Viktorovich Avdeev**, born October 27, 1983.

Searching the web for Toha’s email address toschka2003@yandex.ru reveals [a 2010 sales thread](https://www.bmwclub.ru/threads/bmw-x5-e70.398405/) on the forum **bmwclub.ru** where a user named Honeypo was selling a 2007 BMW X5. The ad listed the contact person as Anton Avdeev and gave the contact phone number **9588693.**

![](https://krebsonsecurity.com/wp-content/uploads/2025/08/bmw-toha.png)

A search on the phone number 9588693 in the breach tracking service **Constella Intelligence** finds plenty of official Russian government records with this number, date of birth and the name Anton Viktorovich Avdeev. For example, hacked Russian government records show this person has a Russian tax ID and SIN (Social Security number), and that they were flagged for traffic violations on several occasions by Moscow police; in 2004, 2006, 2009, and 2014.

Astute readers may have noticed by now that the ages of Mr. Avdeev (41) and the XSS admin arrested this month (38) are a bit off. This would seem to suggest that the person arrested is someone other than Mr. Avdeev, who did not respond to requests for comment.

## A FLY ON THE WALL

For further insight on this question, KrebsOnSecurity sought comments from **Sergeii Vovnenko**, a former cybercriminal from Ukraine who now works at the security startup **paranoidlab.com**. I reached out to Vov...
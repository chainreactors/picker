---
title: Ransoms Without Ransomware, Data Corruption and Other New Tactics in Cyber Extortion
url: https://buaq.net/go-131875.html
source: unSafe.sh - 不安全
date: 2022-10-21
fetch_date: 2025-10-03T20:27:00.259740
---

# Ransoms Without Ransomware, Data Corruption and Other New Tactics in Cyber Extortion

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/e6ea7800a1ccc7b863d54d122633719f.jpg)

Ransoms Without Ransomware, Data Corruption and Other New Tactics in Cyber Extortion

Much like legitimate businesses, ransomware operators adjust their operational strategies to achiev
*2022-10-20 21:9:47
Author: [www.sentinelone.com(查看原文)](/jump-131875.htm)
阅读量:28
收藏*

---

Much like legitimate businesses, ransomware operators adjust their operational strategies to achieve results while managing time and resources, and defenders are required to track these shifting strategies to maintain effective protection. Presently, we are observing an evolution in how cyber criminals approach the business of extorting money from organizations.

Ransomware actors have turned toward data theft instead of time-expensive encryption, and importantly, the anatomy of modern extortion attacks involves operators taking different approaches to data destruction from full encryption to partial encryption to no encryption – and, thus, no ransomware – at all. What the cybersecurity industry generally refers to as ‘ransomware operators’ must now be thought of as a subset of a larger group of data extortion actors who occupy different positions on this spectrum of data destructiveness.

In this post, we describe this emerging spectrum of data-focused threat actors to help defenders better understand the continuing development of data extortion tactics, techniques, and procedures (TTPs).

![](https://899029.smushcdn.com/2131410/wp-content/uploads/2022/10/Ransoms-Without-Ransomware-Data-Corruption-and-Other-New-Tactics-in-Cyber-Extortion-3.jpg?lossy=0&strip=1&webp=0)

## Data Destructiveness | A Growing Spectrum

Starting first from opportunistic attempts for easy profit, ransomware has morphed into full-scale cybercrime syndicates targeting governments and critical infrastructures globally. Ransomware-as-a-Service (RaaS) programs are now prolific on the dark web, connecting low to mid-level actors with ransomware developers. Not only are these programs easy to access and cheap, they are also mature, operating like any other legitimate organization by offering technical support and flexible service models.

Thinking of ransomware as simple encryption of randomly stolen data, however, is not an accurate representation of the plethora of data extortion strategies we see today. Trends now indicate that full encryption of victim data is often too arduous and slow for many threat actors, and increases the risk of detection. With [double](https://www.kaspersky.com/about/press-releases/2020_the-rise-of-ransomware-20-cybercriminals-shift-focus-from-encrypting-data-to-publishing-confidential-information-online) and [triple](https://heimdalsecurity.com/blog/triple-extortion-ransomware/) extortion becoming standard in the ransomware scene – the stolen data being the pivotal element  –  we see threat actors occupying different positions on a spectrum of data destructiveness.

At one end of the spectrum are threat actors that do not destroy data at all and therefore spend no time on this activity – they only steal data that is valuable to victims as a means to extort them. At the other end of this spectrum are actors that use traditional ransomware to do full, but relatively slow, encryption to destroy data completely. The rest of the spectrum is populated by actors that steal data and either partially or fully destroy it to damage their victim’s infrastructure, thus gaining additional leverage over them.

![Data Destructiveness Spectrum](https://899029.smushcdn.com/2131410/wp-content/uploads/2022/10/data_spectrum.jpg?lossy=0&strip=1&webp=0)

The data destructiveness spectrum

## Ransoms Without Ransomware

This strategy is exemplified by two relatively recent threat groups, Karakurt and Lapsus$. Both leverage data extortion-only methods in their campaigns. Neither group deploys ransomware on compromised systems. Instead, they exfiltrate data and use the stolen data as leverage, joining the ranks of groups such as [Marketo](https://www.digitalshadows.com/blog-and-research/marketo-a-return-to-simple-extortion/) and [email protected]

![The Twitter profile @Mannus Gott introducing Marketo (source: Digital Shadows)](https://899029.smushcdn.com/2131410/wp-content/uploads/2022/10/Data_destruction_4.jpg?lossy=0&strip=1&webp=0)

The Twitter profile @Mannus Gott introducing Marketo (source: [Digital Shadows](https://www.digitalshadows.com/blog-and-research/marketo-a-return-to-simple-extortion/))

Karakurt typically gains [access](https://www.cisa.gov/uscert/sites/default/files/publications/AA22-152A_Karakurt_Data_Extortion_Group.pdf) to networks through [initial access brokers](https://www.sentinelone.com/blog/more-evil-markets-how-its-never-been-easier-to-buy-initial-access-to-compromised-networks/) (IABs) or by exploiting vulnerabilities in internet-exposed network services such as outdated Fortinet FortiGate SSL VPN appliances. The threat group is considered to be the data extortion [arm](https://www.bleepingcomputer.com/news/security/karakurt-revealed-as-data-extortion-arm-of-conti-cybercrime-syndicate/) of the now defunct Conti syndicate. Karakurt has targeted victims across all industries and geographical regions.

Karakurt sends victim-specific emails to employees revealing that data has been stolen while threatening that the data will be leaked to competitors or auctioned online. The extortion note contains employee names and indicates that Karakurt has spent a considerable amount of time locating data that is valuable to the victim organization to ensure the group’s extortion leverage.

![Karakurt extortion note](https://899029.smushcdn.com/2131410/wp-content/uploads/2022/10/Data_destruction_7.jpg?lossy=0&strip=1&webp=0)

Karakurt extortion note (trimmed for brevity)

In contrast to Karakurt, Lapsus$ uses stolen credentials and phishing to gain initial access to networks. The group then uses SIM-swapping, social engineering, and solicitation methods to bypass multi-factor authentication (MFA).

Lapsus$ has recently targeted victims in the high-tech [industry](https://unit42.paloaltonetworks.com/lapsus-group/), notably Nvidia, Samsung, Okta, Microsoft, and Ubisoft. The threat group is also known to attack organizations specifically to gain access to their customers. Such has been the case with the Okta breach in early 2022. It is interesting to note that Lapsus$ conducts data extortion campaigns not only for financial gains, but also to increase their notoriety.

## Extortion Through Data Corruption

Some ransomware operators are now implementing data destruction techniques that are more lightweight and time-efficient than data encryption. Through data corruption,  operators are capable of driving urgency in their victims as well as escalating their ransom request.

Exemplifying this is the new version of the Exmatter data exfiltration tool which [corrupts](https://stairwell.com/news/threat-research-report-exmatter-future-of-data-extortion/) data by replacing a data chunk of a file with a data chunk from another file. This change in the implementation of Exmatter strongly suggests the beginning of a new [trend](https://www.csoonline.com/article/3674848/ransomware-operators-might-be-dropping-file-encryption-in-favor-of-corrupting-files.html) in ransomware operations where threat actors seek to corrupt data instead of encrypting it.

![Exmatter corrupts a file ](https://899029.smushcdn.com/2131410/wp-content/uploads/2022/10/Data_destruction_5.jpg?lossy=0&strip=1&webp=0)

Exmatter corrupts a file (source: [Stairwell](https://stairwell.com/news/threat-research-report-exmatter...
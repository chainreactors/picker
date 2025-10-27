---
title: 5 facts about Vice Society, the ransomware group wreaking havoc on the education sector
url: https://buaq.net/go-146807.html
source: unSafe.sh - 不安全
date: 2023-01-27
fetch_date: 2025-10-04T04:56:37.856050
---

# 5 facts about Vice Society, the ransomware group wreaking havoc on the education sector

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

![](https://8aqnet.cdn.bcebos.com/352dca71fd98034b0d21551ecf95ad6e.jpg)

5 facts about Vice Society, the ransomware group wreaking havoc on the education sector

Move over Lockbit, there's a new ransomware-as-a-service (RaaS) player
*2023-1-26 21:30:0
Author: [www.malwarebytes.com(查看原文)](/jump-146807.htm)
阅读量:21
收藏*

---

Move over [Lockbit](https://www.malwarebytes.com/blog/news/2022/09/lockbit-builder-leaked-by-disgruntled-developer), there's a new [ransomware-as-a-service (RaaS)](https://www.malwarebytes.com/blog/business/2022/10/what-is-ransomware-as-a-service-and-how-is-it-evolving) player in town attacking the education sector—and its name is Vice Society.

Vice Society is believed to be a Russian-based intrusion, exfiltration, and extortion group. And their ideal prey? You guessed it: universities, colleges, and K-12 schools. The Federal Bureau of Investigation (FBI) has even [released a joint Cybersecurity Advisory (CSA)](https://www.malwarebytes.com/blog/news/2022/09/authorities-issue-warning-about-vice-society-ransomware-targeting-the-education-sector) after observing that Vice Society has disproportionately targeted the education sector.

But with knowledge comes power. The more the education sector knows about Vice Society, the better prepared they get to defend against them.

In this article, we’ll arm you with five facts about Vice Society so you can get the upper-hand against this persistent threat.

## 1. In 2022 they were far and away the biggest attackers on the education sector

If you’re a regular reader of our [monthly ransomware review](https://www.malwarebytes.com/blog/authors/threatintelligence), you know that the education sector has gotten plenty of attention from ransomware gangs in the last year, to say the least.

It wasn't until Vice Society, however, that we saw a gang taking their love for the sector to a whole new level.

Like many other ransomware gangs, Vice Society is known to steal information from victims' networks before encryption for the purposes of double extortion—threatening to publish the data on the dark web unless you pay up the ransom they demand.

A few of the institutions published on their leak site last year include De Montfort School, Cincinnati State, and one that made national headlines in September: [Los Angeles Unified, the second largest school district in the US.](https://www.malwarebytes.com/blog/news/2022/10/public-school-district-has-data-leaked-by-ransomware-gang)

![](https://www.malwarebytes.com/blog/business/2023/01/easset_upload_file79715_255817_e.png)

*Around 40% of the victims shared on the Vice Society leak site are educational institutions, a large proportion compared to other gangs.*

## 2. And they have shown no signs of slowing down in 2023

As of January 2023, Vice Society has already published the data of six schools on their leak site. That’s more than any other RaaS gang so far this year.

![](https://www.malwarebytes.com/blog/business/2023/01/easset_upload_file36885_255817_e.png)

*The Vice Society leak site*

## 3. They leverage living off the land techniques to sneak past detection

Living off the land (LOTL) attacks are when threat actors use legitimate tools for malicious purposes, which effectively allows them to hide in plain sight as they carry out their attack.

Vice Society actors leverage one such legitimate tool, Windows Management Instrumentation (WMI), as a means of living off the land to execute malicious commands. WMI allows administrators to manage and monitor various aspects of a computer, such as hardware and software, from a remote location.

See where we’re going with this?

Vice Society and other adversaries can use WMI to gain access to a system and then execute malicious code, install malware, or steal sensitive information.

That means you won’t be able to detect them using traditional signature-based detection mechanisms—hash values, IOCs and signatures do not detect living off the land attacks. Instead, you’ll need to turn to an [Endpoint Protection Platform (EPP)](https://www.malwarebytes.com/cybersecurity/business/what-is-endpoint-protection) that uses a combination of machine learning, behavioral analysis, and sandboxing.

## 4. We know how they get initial access to networks

So we know what Vice Society is doing once they’re in school networks and how to detect it. But how can we stop them from entering in the first place?

Using a combination of data from [Unit 42](https://unit42.paloaltonetworks.com/vice-society-targets-education-sector/#:~:text=TA0001%20Initial%20Access) and the [Cybersecurity Advisory (CSA)](https://www.cisa.gov/uscert/ncas/alerts/aa22-249a#:~:text=MITRE%20ATT%26CK%20TECHNIQUES) posted on CISA.org, we can paint a pretty good picture of how Vice Society is getting initial access to their targets.

Vice Society is not reinventing the wheel: these threat actors are using familiar techniques such as phishing, compromised credentials, and exploits to establish a foothold in victim networks.

![](https://www.malwarebytes.com/blog/business/2023/01/easset_upload_file66746_255817_e.png)

*Three ways Vice Society is known to get initial access (with MITRE IDs)*

Our advice is as old as time, but always worth reiterating:

* **Address phishing** with employee training, web-based protection, [and DNS filtering](https://www.malwarebytes.com/blog/business/2022/08/how-it-teams-can-prevent-phishing-attacks-with-malwarebytes-dns-filtering)
* **Address compromised accounts** by removing [dormant accounts, enforcing the principle of least privilege, and having strict password policies.](https://www.malwarebytes.com/blog/news/2022/04/why-identity-management-matters)
* **Address exploits** by maintaining regular [vulnerability assessment and patching](https://www.malwarebytes.com/cybersecurity/business/what-is-patch-management), preferably using an automated tool.

## 5. It seems like they’re open to negotiating their initial ransoms

First things first, [the FBI recommends never paying the ransom to attackers](https://www.malwarebytes.com/blog/news/2016/05/fbi-announcement-paying-the-ransom-is-a-bad-idea).

There’s a good argument for not paying too: doing so encourages more attacks and there’s no guarantee you’ll get your data back either way. There is no honor among thieves, after all.

But sometimes not paying is easier said than done. Paying the ransom might be the [only option left for some organizations](https://ransomware.org/why-should-we-pay-the-ransom/#:~:text=ransom%2C%E2%80%9D%20read%20on.-,You%20Have%20To%20Pay%20the%20Ransom%2C%C2%A0,%3F,-First%3A%20Hire%20a) for various reasons.

![](https://www.malwarebytes.com/blog/business/2023/01/easset_upload_file8757_255817_e.png)

*A Vice Society ransom note.*

We know that Vice Society isn’t the most aggressive gang when it comes to their ransom demands. The difference between their initial demands and final demands could be [as large as 60%](https://unit42.paloaltonetworks.com/vice-society-targets-education-sector/#:~:text=of%20initial%20discovery.-,Ransom%20Demands,-When%20tracking%20ransomware) after negotiations take place.

## Getting the upper-hand against RaaS gangs

Vice Society is currently the most severe RaaS threat to the education sector. Still, to say ransomware attacks on schools is a Vice Society problem purely is missing the forest for the trees.

We don’t want to say launching ransomware on K-12 schools, colleges, and universities is as easy as taking candy from a baby, but unfortunately that’s how many RaaS gangs see it. The reality is that tight budgets of many educational institutions force them to struggle with outd...
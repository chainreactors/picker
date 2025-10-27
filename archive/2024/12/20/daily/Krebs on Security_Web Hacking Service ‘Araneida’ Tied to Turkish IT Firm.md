---
title: Web Hacking Service ‘Araneida’ Tied to Turkish IT Firm
url: https://krebsonsecurity.com/2024/12/web-hacking-service-araneida-tied-to-turkish-it-firm/
source: Krebs on Security
date: 2024-12-20
fetch_date: 2025-10-06T20:02:12.924917
---

# Web Hacking Service ‘Araneida’ Tied to Turkish IT Firm

Advertisement

[![](/b-sysdig/1.png)](https://content.foleon.com/sysdig/sysdig-cloud-defense-report-2025/?utm_source=krebs-on-security&utm_medium=display&utm_campaign=aware_amer_the-right-way_na_ung_display&utm_content=AD000460_1240x110)

Advertisement

[![](/b-gartner/4.jpg)](https://www.gartner.com/en/conferences/na/identity-access-management-us?utm_source=krebs&utm_medium=banner&utm_campaign=EVT_NA_2025_IAM20_PP_MP6_KREBSONSECURITY)

[![Krebs on Security](https://krebsonsecurity.com/wp-content/uploads/2021/03/kos-27-03-2021.jpg)](https://krebsonsecurity.com/ "Krebs on Security")

[Skip to content](#content "Skip to content")

* [Home](https://krebsonsecurity.com/)
* [About the Author](https://krebsonsecurity.com/about/)
* [Advertising/Speaking](https://krebsonsecurity.com/cpm/)

# Web Hacking Service ‘Araneida’ Tied to Turkish IT Firm

December 19, 2024

[11 Comments](https://krebsonsecurity.com/2024/12/web-hacking-service-araneida-tied-to-turkish-it-firm/#comments)

Cybercriminals are selling hundreds of thousands of credential sets stolen with the help of a cracked version of **Acunetix**, a powerful commercial web app vulnerability scanner, new research finds. The cracked software is being resold as a cloud-based attack tool by at least two different services, one of which KrebsOnSecurity traced to an information technology firm based in Turkey.

![](https://krebsonsecurity.com/wp-content/uploads/2024/12/araneida-scanner.png)

Cyber threat analysts at **Silent Push** said they recently received reports from a partner organization that identified an aggressive scanning effort against their website using an Internet address previously associated with a campaign by [FIN7](https://resources.prodaft.com/fin7-cybercrime-gang), a notorious Russia-based hacking group.

But on closer inspection they discovered the address contained an HTML title of “**Araneida Customer Panel**,” and found they could search on that text string to find dozens of unique addresses hosting the same service.

It soon became apparent that Araneida was being resold as a cloud-based service using a cracked version of Acunetix, allowing paying customers to conduct offensive reconnaissance on potential target websites, scrape user data, and find vulnerabilities for exploitation.

Silent Push also learned Araneida bundles its service with a robust proxy offering, so that customer scans appear to come from Internet addresses that are randomly selected from a large pool of available traffic relays.

The makers of Acunetix, Texas-based application security vendor **Invicti Security**, confirmed Silent Push’s findings, saying someone had figured out how to crack the free trial version of the software so that it runs without a valid license key.

“We have been playing cat and mouse for a while with these guys,” said **Matt Sciberras**, chief information security officer at Invicti.

Silent Push said Araneida is being advertised by an eponymous user on multiple cybercrime forums. The service’s Telegram channel boasts nearly 500 subscribers and explains how to use the tool for malicious purposes.

In a “Fun Facts” list posted to the channel in late September, Araneida said their service was used to take over more than 30,000 websites in just six months, and that one customer used it to buy a Porsche with the payment card data (“dumps”) they sold.

![](https://krebsonsecurity.com/wp-content/uploads/2024/12/araneida-tg.png)

“They are constantly bragging with their community about the crimes that are being committed, how it’s making criminals money,” said **Zach Edwards**, a senior threat researcher at Silent Push. “They are also selling bulk data and dumps which appear to have been acquired with this tool or due to vulnerabilities found with the tool.”

Silent Push also found a cracked version of Acunetix was powering at least 20 instances of a similar cloud-based vulnerability testing service catering to Mandarin speakers, but they were unable to find any apparently related sales threads about them on the dark web.

Rumors of a cracked version of Acunetix being used by attackers surfaced [in June 2023 on Twitter/X](https://x.com/FalconFeedsio/status/1665690661377691649), when researchers [first posited a connection between observed scanning activity and Araneida](https://x.com/TLP_R3D/status/1665777020767293447).

According to [an August 2023 report](https://www.hhs.gov/sites/default/files/china-based-threat-actor-profiles-tlpclear.pdf) (PDF) from the **U.S. Department of Health and Human Services** (HHS), Acunetix (presumably a cracked version) is among several tools used by [APT 41](https://krebsonsecurity.com/2020/09/chinese-antivirus-firm-was-part-of-apt41-supply-chain-attack/), a prolific Chinese state-sponsored hacking group.

## THE TURKISH CONNECTION

Silent Push notes that the website where Araneida is being sold — **araneida[.]co** — first came online in February 2023. But a review of this Araneida nickname on the cybercrime forums shows they have been active in the criminal hacking scene since at least 2018.

A search in the threat intelligence platform [Intel 471](https://www.intel471.com) shows a user by the name Araneida promoted the scanner on two cybercrime forums since 2022, including **Breached** and **Nulled**. In 2022, Araneida told fellow Breached members they could be reached on Discord at the username “**Ornie#9811**.”

According to Intel 471, this same Discord account was advertised in 2019 by a person on the cybercrime forum **Cracked** who used the monikers “**ORN**” and “**ori0n**.” The user “ori0n” mentioned in several posts that they could be reached on Telegram at the username “**@sirorny**.”

![](https://krebsonsecurity.com/wp-content/uploads/2024/12/orn-araneida.png)

The Sirorny Telegram identity also was referenced as a point of contact for a current user on the cybercrime forum Nulled who is selling website development services, and who references araneida[.]co as one of their projects. That user, “**Exorn**,” has posts dating back to August 2018.

In early 2020, Exorn promoted a website called “**orndorks[.]com**,” which they described as a service for automating the scanning for web-based vulnerabilities. A passive DNS lookup on this domain at [DomainTools.com](https://www.domaintools.com) shows that its email records pointed to the address **ori0nbusiness@protonmail.com**.

[Constella Intelligence](https://www.constella.ai), a company that tracks information exposed in data breaches, finds this email address was used to register an account at **Breachforums** in July 2024 under the nickname “**Ornie**.” Constella also finds the same email registered at the website netguard[.]codes in 2021 using the password “**ceza2003**” [full disclosure: Constella is currently an advertiser on KrebsOnSecurity].

A search on the password ceza2003 in Constella finds roughly a dozen email addresses that used it in an exposed data breach, most of them featuring some variation on the name “**altugsara**,” including **altugsara321@gmail.com**. Constella further finds altugsara321@gmail.com was used to create an account at the cybercrime community **RaidForums** under the username “**ori0n**,” from an Internet address in Istanbul.

According to DomainTools, altugsara321@gmail.com was used in 2020 to register the domain name **altugsara[.]com**. [Archive.org’s history for that domain](https://web.archive.org/web/20211125114845/http%3A//altugsara.com/) shows that in 2021 it featured a website for a then 18-year-old **Altuğ Şara** from Ankara, Turkey.

![](https://krebsonsecurity.com/wp-content/uploads/2024/12/altugsaradotcom.png)

Archive.org’s recollection of what altugsara dot com looked like in 2021.

**LinkedIn** finds this same **altugsara[.]com** domain listed in the “contact info” section of [a profile](https://www.linkedin.com/in/altu%C4%9F-%C5%9Fara-58957b212/) for an **Altug Sara** from Ankara, who says he has worked the past two years as a senior software develo...
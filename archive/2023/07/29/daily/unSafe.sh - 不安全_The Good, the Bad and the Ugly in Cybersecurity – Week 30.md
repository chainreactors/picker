---
title: The Good, the Bad and the Ugly in Cybersecurity – Week 30
url: https://buaq.net/go-173159.html
source: unSafe.sh - 不安全
date: 2023-07-29
fetch_date: 2025-10-04T11:51:09.660921
---

# The Good, the Bad and the Ugly in Cybersecurity – Week 30

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

![](https://8aqnet.cdn.bcebos.com/34e8e2aa16daa6e7b393d9f15f724d0f.jpg)

The Good, the Bad and the Ugly in Cybersecurity – Week 30

The Good | SEC Says Cyber Incidents Must Be Disclosed Within 4 DaysThe Securities and Exchange Com
*2023-7-28 21:0:23
Author: [www.sentinelone.com(查看原文)](/jump-173159.htm)
阅读量:15
收藏*

---

## The Good | SEC Says Cyber Incidents Must Be Disclosed Within 4 Days

The Securities and Exchange Commission has announced that it is adopting new rules that will require companies to disclose cyberattacks within four days.

In a [press release](https://www.sec.gov/news/press-release/2023-139) on Wednesday, the SEC said the new rules require “registrants to disclose material cybersecurity incidents they experience and to disclose on an annual basis material information regarding their cybersecurity risk management, strategy, and governance.”

It is hoped prompt reporting will increase transparency for investors and potentially accelerate improvements in cyber defenses as details of breaches become more widely shared.

![CISA announced new rules to report cyber incidents in 4 days](https://www.sentinelone.com/wp-content/uploads/2023/07/breach-chain.jpg)

The new incident response rules require that publicly-traded companies reveal:

* The date of discovery and status of the incident (ongoing or resolved)
* A concise description of the incident’s nature and extent
* Any data that may have been compromised, altered, accessed, or used without authorization
* The impact of the incident on the company’s operations
* Information about ongoing or completed remediation efforts by the company

Companies are not required to reveal specifics about their [incident response plans](https://www.sentinelone.com/blog/the-first-line-of-defense-crafting-an-impactful-incident-response-plan/) or vulnerabilities such as zero days or n-days that could influence their response or remediation actions. The rules also allow for postponement of disclosure if it would pose “a significant risk to national security or public safety”. That determination is at the discretion of the US Attorney General.

Other caveats include allowing smaller companies an additional 180 days before they are required to provide Form 8-K disclosures. The [rules](https://www.sec.gov/files/rules/final/2023/33-11216.pdf), first proposed last year, are set to come into force in December.

## The Bad | Millions of Cloud Container Workloads Vulnerable to New Ubuntu Bugs

Researchers this week disclosed two kernel-level vulnerabilities impacting, they say, up to 40% of Ubuntu cloud workloads. The bugs, dubbed ‘GameOver(lay), are said to be easy to exploit and allow for local privilege escalation.

The two flaws, CVE-2023-2640 and CVE-2023-32629, relate to the OverlayFS module in Ubuntu, a popular Linux filesystem widely used in [cloud containers](https://www.sentinelone.com/resources/cloud-workload-security-trends-and-best-practices/). OverlayFS is a file system commonly used with [Docker](https://www.sentinelone.com/blog/create-docker-image-2/) that lays one filesystem on top of another. This allows users to modify the upper file system while keeping the base system intact, useful in [cloud workloads](https://www.sentinelone.com/resources/the-cwpp-revolution-autonomous-detection-engines-for-cloud-workload-security/) where it is often desirable to provide an isolated layer for an application to run in that will not affect or modify the host system.

Researchers at [Wiz](https://www.wiz.io/blog/ubuntu-overlayfs-vulnerability) discovered that Ubuntu’s modifications to OverlayFS make it possible to ‘trick’ the kernel into copying a privileged executable from one layer and writing it to another where it no longer requires privileges to execute.

![Wiz discovers Ubuntu GameOverlay bug](https://www.sentinelone.com/wp-content/uploads/2023/07/image.png)

Worse, the researchers say that exploits written in 2020 for a similar vulnerability will now work on any Ubuntu instance vulnerable to the two newly discovered flaws, providing local attackers with ready-made weapons.

Versions susceptible to the bugs range from Ubuntu 18.04 to 23.04. The researchers say that the number of releases available for Ubuntu make it challenging to determine all impacted versions, but a work-in-progress list is available [here](https://www.wiz.io/blog/ubuntu-overlayfs-vulnerability).

Ubunutu has issued patches for the vulnerabilities as of July 24th and admins are urged to update as soon as possible.

## The Ugly | Federal Agencies Urged to Patch Actively Exploited Zero Day

CISA has this week told federal agencies to patch by August 15th a maximum severity bypass vulnerability found in Ivanti’s Endpoint Manager Mobile (EPMM) software, previously branded MobileIron Core. The warning comes after the bug was used to compromise twelve Norwegian government ministries.

EPMM is used by organizations to allow access to [enterprise email](https://www.sentinelone.com/blog/understanding-the-evolution-of-modern-business-email-compromise-attacks/) and other applications on mobile devices. The zero-day vulnerability, patched this week and tagged as [CVE-2023-35078](https://nvd.nist.gov/vuln/detail/CVE-2023-35078), allows remote attackers to obtain Personally Identifiable Information (PII), add admin accounts, and make configuration changes through certain exposed API paths, which can be reached remotely without authentication.

> Norway government breach traces to zero-day vulnerability in Ivanti Endpoint Manager Mobile (née MobileIron Core) <https://t.co/K2VVoVzRDl>
>
> — Mathew J Schwartz (@euroinfosec) [July 26, 2023](https://twitter.com/euroinfosec/status/1684215748435013633?ref_src=twsrc%5Etfw)

It has been reported that there may be almost 3000 vulnerable instances of the software exposed on the public internet, with dozens belonging to U.S. local and state agencies. CISA has added the vulnerability to its [Known Exploited Vulnerabilities](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) catalog, noting that it poses a significant risk to the federal enterprise as malicious [cyber actors](https://www.sentinelone.com/resources/threat-actor-basics-understanding-the-5-main-threat-types/) are known to be exploiting the bug in the wild.

CISA’s warning to federal agencies should also be heeded by enterprise users of the EPMM/MobileIron Core software. Ivanti has released security patches and warned that all supported, unsupported and end-of-life releases are impacted. Users who cannot upgrade are urged to discontinue use of the product. A security [advisory](https://success.ivanti.com/customers/Community_RegStep1_Page?inst=Do&startURL=%2Fservlet%2Fnetworks%2Fswitch%3FnetworkId%3D0DB1B000000PBGy%26startURL%3D%2Fs%2Farticle%2FKB-Remote-unauthenticated-API-access-vulnerability-CVE-2023-35078) with further details is available to Ivanti customers.

文章来源: https://www.sentinelone.com/blog/the-good-the-bad-and-the-ugly-in-cybersecurity-week-30-5/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)
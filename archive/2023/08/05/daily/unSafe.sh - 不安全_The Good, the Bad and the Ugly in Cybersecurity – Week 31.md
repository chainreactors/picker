---
title: The Good, the Bad and the Ugly in Cybersecurity – Week 31
url: https://buaq.net/go-173710.html
source: unSafe.sh - 不安全
date: 2023-08-05
fetch_date: 2025-10-04T12:00:13.922341
---

# The Good, the Bad and the Ugly in Cybersecurity – Week 31

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

![](https://8aqnet.cdn.bcebos.com/80fcd37aef0bcce9398dcf990f1b69b5.jpg)

The Good, the Bad and the Ugly in Cybersecurity – Week 31

The Good | High-Severity Flaws Patched in Firefox and Chrome UpdatesBrowsers are our windows to th
*2023-8-4 21:0:41
Author: [www.sentinelone.com(查看原文)](/jump-173710.htm)
阅读量:13
收藏*

---

## The Good | High-Severity Flaws Patched in Firefox and Chrome Updates

Browsers are our windows to the internet and due to both their ubiquity and the amount of information they collect, they are often [prime targets](https://thehackernews.com/2023/03/2023-browser-security-report-uncovers.html) for threat actors, so there’s good news for [Firefox](https://www.sentinelone.com/blog/how-two-firefox-zero-days-led-to-two-macos-backdoors/) and [Chrome](https://www.sentinelone.com/blog/6-real-world-threats-to-chromebooks-and-chromeos/) users this week as new security patches have been rolled out for both.

On Tuesday, Mozilla [released](https://www.mozilla.org/en-US/security/advisories/mfsa2023-29/) new versions of Firefox 116, Firefox ESR 115.1, and Firefox ESR 102.14, which all include patches for several high-severity vulnerabilities, most prominently [CVE-2023-4045](https://nvd.nist.gov/vuln/detail/CVE-2023-4045), [CVE-2023-4046](https://nvd.nist.gov/vuln/detail/CVE-2023-4046), and [CVE-2023-4047](https://nvd.nist.gov/vuln/detail/CVE-2023-4047). The new iterations prohibit HTML and JavaScript code displayed on one site from accessing content on another site, correct a potentially exploitable crash caused by wrong values during WASM compilation, and resolve a clickjacking issue where users are tricked into giving up risky permissions for microphone, location, and notification services.

![](https://www.sentinelone.com/wp-content/uploads/2023/08/Screenshot-2023-08-04-at-10.09.26-AM.jpg)

On the Google side, the tech firm handed out over $60,000 in bug bounties for three high-severity type confusion vulnerabilities in Chrome’s V8 engine. The latest [update](https://chromereleases.googleblog.com/2023/07/stable-channel-update-for-desktop.html), Chrome 115, addresses six other severe flaws relating to issues such as a heap buffer overflow problem which often results in unpredictable behavior or generates incorrect results, crashes, or memory access errors, an insufficient data validation bug, and an inappropriate implementation issue. Users are encouraged to update to versions 115.0.5790.170 for Mac and Linux and to versions 115.0.5790.170/.171 for Windows.

## The Bad | More Vulnerabilities Found in Ivanti’s Mobile Device Management Product

Following a maximum severity bypass vulnerability [reported](https://www.sentinelone.com/blog/the-good-the-bad-and-the-ugly-in-cybersecurity-week-30-5/) last week by Ivanti, the Utah-based IT firm has since issued warnings for two more vulnerabilities also found in its Endpoint Manager Mobile (EPMM) software.

The first of the two is a new path traversal vulnerability, tracked as [CVE-2023-35081](https://forums.ivanti.com/s/article/CVE-2023-35081-Arbitrary-File-Write?language=en_US) (CVSS 7.2), allowing arbitrary file write capabilities. Threat actors exploiting this vulnerability could potentially bypass admin authentication and ACL restrictions to execute OS commands. All supported versions of EPMM, including releases 11.10, 11.9, 11.8, and older are impacted.

The company says that this new vulnerability differs from July’s [CVE-2023-35078](https://nvd.nist.gov/vuln/detail/CVE-2023-35078); however, it acknowledged that attackers could chain the two together for malicious purposes. A joint cybersecurity [advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-213a) from both CISA and the Norwegian National Cyber Security Centre (NCSC-NO) explains that chaining the two flaws could translate to privileged access across EPMM systems and the ability to execute uploaded files such as webshells.

> 👇 Another one for the same product: CVE-2023-35082, CVSS 10.0 😳
>
> — Netlas.io (@Netlas\_io) [August 3, 2023](https://twitter.com/Netlas_io/status/1687015100471738368?ref_src=twsrc%5Etfw)

The second vulnerability announced this week is tracked as [CVE-2023-35082](https://forums.ivanti.com/s/article/CVE-2023-35082-Remote-Unauthenticated-API-Access-Vulnerability-in-MobileIron-Core-11-2-and-older?language=en_US) (CVSS 10.0) and could allow unauthenticated attackers to access the API in older, unsupported versions of the product (11.2 and below).

If exploited, attackers could access users’ personally identifiable information (PII) and make unauthorized changes to the server. Security [researchers](https://www.rapid7.com/blog/post/2023/08/02/cve-2023-35082-mobileiron-core-unauthenticated-api-access-vulnerability/) noted the bug’s close relation to last week’s remote unauthorized API access flaw in that both target the permissive qualities of certain entries in the `mifs` web application’s security filter chain.

Ivanti has released patches for all three vulnerabilities within the span of two weeks and urged its customers to upgrade to the latest version of EPMM and monitor their systems for signs of breaches.

## The Ugly | Microsoft Domains Leveraged in Russian-Backed Teams Phishing Campaigns

Cyber threat group [APT29](https://attack.mitre.org/groups/G0016/), attributed to Russia’s Foreign Intelligence Service (SVR), was linked this week to a series of attacks on dozens of organizations. Likely indicative of an espionage campaign, the [group](https://www.sentinelone.com/labs/noblebaron-new-poisoned-installers-could-be-used-in-supply-chain-attacks/) targeted [government agencies](https://www.sentinelone.com/blog/why-governments-and-agencies-are-targeted-by-cyber-attacks-a-deep-dive-into-the-motives/), non-government organizations (NGOs), IT and tech services, private manufacturing, and media sectors through phishing messages sent via Microsoft Teams.

According to a [report](https://www.microsoft.com/en-us/security/blog/2023/08/02/midnight-blizzard-conducts-targeted-social-engineering-over-microsoft-teams/) released Wednesday, the attackers used compromised Microsoft 365 tenants to create tech support-themed domains and sent various social engineering lures to trick victims into granting approval for [multi-factor authentication](https://www.sentinelone.com/cybersecurity-101/what-is-multi-factor-authentication-mfa/) (MFA) prompts. The new domains were part of a legitimate Microsoft domain ‘onmicrosoft.com’ that is used when a custom domain is not successfully created.

Using this domain, the spoofed tech support messages would have appeared more trustworthy to the targeted users.

![A fake Microsoft Teams message request used in APT29's latest campaign (Source: Microsoft).](https://www.sentinelone.com/wp-content/uploads/2023/08/Teams-masquerade.jpeg)

A fake Microsoft Teams message request used in APT29’s latest campaign (Source: Microsoft).

[APT29](https://www.sentinelone.com/resources/using-mitres-2020-attck-evaluation-data-to-show-how-an-advanced-endpoint-detection-response-product-mitigated-apt29/) has been operating since at least 2008, crafting attacks against government networks in NATO member countries and in Europe, think tanks, and research institutes. Notoriously, the group is attributed to the [SolarWinds](https://www.sentinelone.com/blog/software-management-a-guide-for-every-business-using-open-source-in-2023/) [supply chain](https://www.sentinelone.com/cybersecurity-101/what-is-supply-chain-attack/) attack that led to the compromise of as many as 18,000 government entities and Fortune 500 companies, at least nine federal agencies, and mo...
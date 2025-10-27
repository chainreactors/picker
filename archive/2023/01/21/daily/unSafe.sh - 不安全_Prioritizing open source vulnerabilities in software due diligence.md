---
title: Prioritizing open source vulnerabilities in software due diligence
url: https://buaq.net/go-146346.html
source: unSafe.sh - 不安全
date: 2023-01-21
fetch_date: 2025-10-04T04:27:14.974224
---

# Prioritizing open source vulnerabilities in software due diligence

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

![]()

Prioritizing open source vulnerabilities in software due diligence

Posted by on Friday, January 20, 2023
*2023-1-20 21:30:27
Author: [www.synopsys.com(查看原文)](/jump-146346.htm)
阅读量:18
收藏*

---

Posted by on Friday, January 20, 2023

*Black Duck Security Advisories provide actionable advice and details about open source vulnerabilities to help you improve your remediation activities.*

A vulnerability is a software bug that hackers can exploit to attack an application. Ideally, software is written so as to proactively thwart the efforts of bad actors, but that is often not the case. With the heightened sensitivity to cybersecurity in general, and in merger and acquisition (M&A) transactions in particular, understanding how vulnerable software assets are is an important component of software due diligence.

## Zero vulnerabilities: A pipe dream

That said, in modern software applications, there will never be a state of “zero vulnerabilities.” When evaluating the software quality of a potential acquisition target’s software, this is a very important point to remember. However, this is not a recommendation to ignore vulnerabilities or an excuse for vulnerable applications. Rather, it is meant to underscore the importance of arming yourself with the information needed to effectively understand which vulnerabilities present the biggest threats and how to prioritize remediation.

Vulnerabilities do not all present equal risk. Some might be exploited remotely, and some might have no proven exploit at all. Some vulnerabilities might be found in code called directly by an application, while others exist in a library that never makes it to production. Some might have easy, one-click fixes, while others require dozens of development hours to patch. The ability to confidently understand the particulars of a vulnerability is the key to understanding how it impacts an application, its users, and the data it handles.

## Obtaining the “so what?” of vulnerability reports

While I might have made the process sound simple, there is nothing simple about it. It can be difficult to understand all the aspects of a vulnerability, and most organizations don’t have the in-house expertise or resources to do so. This is why Synopsys provides Black Duck® customers with [Black Duck Security Advisories](https://www.synopsys.com/software-integrity/security-testing/software-composition-analysis/vulnerability-reporting.html) (BDSAs) about the vulnerabilities we identify in target codebases.

But just handing over a large list of components and vulnerabilities would be confusing and burdensome, so we augment it with information that has been researched, confirmed, and curated by our team of cybersecurity experts. Details such as severity scoring, descriptions, exploits, remediation guidance, reachability, and impacted versions give [security teams](https://www.synopsys.com/software-integrity/solutions/security-teams.html) the information needed to understand the impact of a vulnerability on an application. This is key to understanding the “so what?” of the findings, so you can best evaluate the security of the software you acquire and what it will take to bring it up to snuff.

Some of the information you get from a BDSAs in your audit report include

* **Component.** The name of the actual open source component. For example, Apache Log4J.
* **Version.** Think of the component as a vehicle model, and the version as the year. A safety recall will only affect certain versions/years. Very rarely will it impact the entire model.
* **Severity.** Low, medium, or high, as determined by the common vulnerability scoring standard (CVSS) explained below. This is crucial for understanding the impact of the vulnerability.
* **Date published.** Are there a lot of old, lingering vulnerabilities? This could signal an open source risk management issue.
* **Description.** A plain English description of what the vulnerability does. For example, it might open an application up to a cross-site scripting attack.
* **CVSS score.** The CVSS aggregates several metrics about the vulnerability, such as how easy it is for hackers to exploit and the environment it impacts, to determine severity. Audit reports break these metrics down further than base scores to paint clearer pictures of the risk.
* **CWE.** The common weakness enumeration (CWE) categorizes specific vulnerabilities into common types so that they can more easily be identified, evaluated, and fixed.
* **Patch reference.** If there is a patch, this is where it can be found. This offers a quick solution while longer-term solutions are considered.
* **Suggested upgrade.** The version of the component that fixes the vulnerability.
* **Workaround.** Upgrading might not always be an immediate option since it can have downstream impacts. Workarounds protect an application while upgrades can be planned.

These details are only a subset of what is provided by BDSAs in our [open source risk analysis](https://www.synopsys.com/software-integrity/resources/analyst-reports/open-source-security-risk-analysis.html?intcmp=sig-blog-bdsaos). Many audit and application security vendors claim to have some capability in this area, but BDSAs provide the most accurate and actionable security advisories offered.

## Providing advisement through actionable results

With the heightened dependence on software assets, software due diligence is only getting more difficult. By not simply dropping a virtual box full of audit results on our customers, we are easing the burden of risk evaluation and planning for mitigation. At Synopsys, we aim to be your trusted advisors in evaluating the quality of the assets that you’re acquiring or selling. BDSAs are one example of insights we provide to enable our customers to put audit results to work.

If you’re involved in technical due diligence or tech company acquisitions at all, check out how the [Black Duck Audit group](https://www.synopsys.com/software-integrity/open-source-software-audit.html?intcmp=sig-blog-bdsaos) has become a trusted partner by both acquirers and target companies alike.

文章来源: https://www.synopsys.com/blogs/software-security/prioritizing-open-source-vulnerabilities-in-software-due-diligence/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)
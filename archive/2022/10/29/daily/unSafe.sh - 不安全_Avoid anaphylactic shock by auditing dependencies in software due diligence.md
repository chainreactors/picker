---
title: Avoid anaphylactic shock by auditing dependencies in software due diligence
url: https://buaq.net/go-133144.html
source: unSafe.sh - 不安全
date: 2022-10-29
fetch_date: 2025-10-03T21:11:19.961872
---

# Avoid anaphylactic shock by auditing dependencies in software due diligence

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

Avoid anaphylactic shock by auditing dependencies in software due diligence

Posted by on Friday, October 28, 2022
*2022-10-28 21:20:59
Author: [www.synopsys.com(查看原文)](/jump-133144.htm)
阅读量:22
收藏*

---

Posted by on Friday, October 28, 2022

*Ignoring dependencies of a seller’s source code during an audit could lead to missed license compliance and security issues.*

*By: Julie Courtnay, software security consultant with Synopsys, and Shyam Sundar, software security consultant with Synopsys.*

Say you are allergic to peanuts. While out to dinner, you order a plate of spaghetti with meatballs. The server lets you know that there are no peanuts in the spaghetti with meatballs. Unfortunately, the server has no knowledge that the onions within the meatballs were fried in peanut oil. The indirect dependency on the peanut oil that was included in the meatballs by way of the fried onions left you vulnerable to an attack.

Similarly dangerous is finding big license and security problems in an acquisition’s software after the close because no one analyzed the software’s dependencies.

## How software is built

Modern software is a mix of proprietary code, off-the-shelf commercial code, and open source code. Open source often includes many dependencies.

The Linux Foundation describes direct and indirect dependencies in the following way:

* A direct dependency is a package that you included in your own directory.
* An indirect dependency is a package that you are not using directly, but one that is used by one of your direct dependencies.

Mergers and acquisitions (M&As) often have extremely tight timelines, so it may seem that performing due diligence only on a seller’s source code/proprietary code is sufficient to identify all the [compliance and security risks](https://www.synopsys.com/blogs/software-security/manage-risks-with-software-due-diligence/). But buyers should also be concerned about the components upon which the seller’s application depends. If components under copyleft licenses are nested in the application’s direct and indirect dependencies, the buyer is taking on the responsibility to comply with those copyleft licenses as part of the whole work. Similarly, security vulnerabilities in dependencies may expose the entire application.

If an open source project is licensed under a permissive license such as MIT, a common belief is that there is no need for concern. However, in the audits we perform for M&A due diligence, we frequently find copyleft-licensed components within permissively licensed open source projects. This might not represent a compliance risk if the open source project is not being used for commercial purposes. However, when our customers are acquiring assets as part of an M&A transaction, they are almost always interested in using these assets for commercial purposes, and that is where the compliance risk resides.

## Examples of license compliance issues from dependencies

* [Ostermiller Java utilities](https://mvnrepository.com/artifact/org.ostermiller/utils): This is a GPL-licensed artifact that we have seen used in multiple codebases, often pulled into an application as either a direct or indirect dependency. For example, Facebook Java Library, which is MIT licensed, uses these Java utilities.
* [MixItUp](https://github.com/patrickkunka/mixitup): This is an example of an open source library nested in a commercial license that requires a separate commercial license for commercial use. It is a high-performance JavaScript library for animated filtering, sorting, insertion, removal, and more. MixItUp is free for noncommercial, educational, and nonprofit use. In commercial projects, however, a commercial license is required. We recently found a dependency in a seller’s codebase as part of a WordPress theme that is commercially licensed.
* [MinIO](https://github.com/minio/minio) and [Grafana](https://github.com/grafana/loki): MinIO is a high-performance object storage and Grafana is a multiplatform open source analytics and interactive visualization web application. MinIO and Grafana are licensed under AGPL and were found in dependencies for Golang (GO). Even with modern languages like GO, components get pulled in through package managers that can be licensed under copyleft licenses like AGPL. Because of this, teams need to have visibility into what components are being pulled in through package managers.
* [WordPress](https://wordpress.com/) and [phpMyAdmin](https://www.phpmyadmin.net/): WordPress is an open source website creation platform and phpMyAdmin is a free software tool written in PHP. Both are licensed under GPL, so any codebases that use them may be subject to GPL obligations. When we audit codebases written in PHP, we regularly find commonly used frameworks and the dependencies that come along with them. WordPress and phpMyAdmin, for example, often show up in the direct dependency tree.
* [Zlib](https://zlib.net/): This is one of the most commonly used general purpose data compression libraries for embedded applications. It contains [Zlib for Ada](https://github.com/madler/zlib/blob/master/contrib/ada/zlib.ads) thick binding. Zlib as a whole is licensed under a permissive license; however, the subcomponent is licensed under GNU General Public License with an exception clause. Most code owners do not realize that they are shipping a codebase that might be subject to GPL obligations because Ada thick binding is a dependency of Zlib.

## Examples of security vulnerabilities from dependencies

Security vulnerabilities can reside within dependencies as well. Here are some common examples.

* [A06 – Outdated and Vulnerable Components](https://owasp.org/Top10/A06_2021-Vulnerable_and_Outdated_Components/): This is the sixth category listed in the OWASP Top 10. You can update the versions in your dependency tree, but you have minimal control over all the versions of the indirect dependencies being pulled in through your direct dependencies. It is extremely difficult to update all those versions if you don’t have visibility into all the indirect dependencies.
* [Python Pillow](https://python-pillow.org/): This is a friendly Python imaging library fork that is a commonly pulled in as a dependency from PyPi. [Pillow](https://nvd.nist.gov/vuln/detail/CVE-2022-22817) is vulnerable to remote code execution (RCE). More than [6,000 Python packages](https://www.wheelodex.org/projects/pillow/) have the dependency of Python Pillow.
* [Minimist version 1.2.5](https://nvd.nist.gov/vuln/detail/CVE-2021-44906): This is vulnerable to prototype pollution as part of its dependency. Some versions of Mocha and mkdirp were impacted because they were dependent on Minimist. Forty-nine percent of the audits we performed in 2021 as part of M&A due diligence contained the vulnerable Minimist component.

Some of the most commonly used frameworks have [security vulnerabilities](https://www.synopsys.com/software-integrity/cybersecurity-research-center/software-vulnerabilities.html) associated with them. We can call these frameworks out for review because we can identify the frameworks in the dependency tree. We are only able to identify specific frameworks by the dependencies that are pulled in at build. Without the dependencies, we could not identify the frameworks, and subsequently, the security vulnerabilities present in the frameworks.

* Spring framework is commonly used in Java development, and it was reported to have a [high/critical RCE vulnerability](https://nvd.nist.gov/vuln/detail/cve-2022-22965).
* Laravel is a framework that we commonly find in PHP-based codebases, and it was [reported...
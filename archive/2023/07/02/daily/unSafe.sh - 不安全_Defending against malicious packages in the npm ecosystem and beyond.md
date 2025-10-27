---
title: Defending against malicious packages in the npm ecosystem and beyond
url: https://buaq.net/go-170928.html
source: unSafe.sh - 不安全
date: 2023-07-02
fetch_date: 2025-10-04T11:51:21.884053
---

# Defending against malicious packages in the npm ecosystem and beyond

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

![](https://8aqnet.cdn.bcebos.com/8ab9fc1d7c03c299f6f72593c22199f9.jpg)

Defending against malicious packages in the npm ecosystem and beyond

Posted by on Friday, June 30, 2023
*2023-7-1 00:25:30
Author: [www.synopsys.com(查看原文)](/jump-170928.htm)
阅读量:19
收藏*

---

Posted by on Friday, June 30, 2023

*Learn how to shield your organization from the danger of malicious packages in the npm ecosystem and beyond.*

![malicious packages](https://www.synopsys.com/blogs/software-security/wp-content/uploads/2023/06/NewsCredBanner_19x5tsk9445v2.png)

Software packages are a popular means to distribute open source and third-party software. They are often pulled from an outside source through a package manager or installer program, and they typically include source code, libraries, documentation, and other files needed to build and run the software.

A *malicious package* contains malware disguised as a legitimate package, and it is intended to infiltrate and infect software. Once a malicious package’s malware enters a system, it can potentially steal sensitive data, disable security software, modify or delete files, and even take over an entire system or network for its own nefarious purposes.

Unlike code weaknesses and vulnerabilities—which can exist in software for months or years without being exploited—a malicious package is almost always a direct and immediate threat that you need to address, especially when it comes to the software supply chain. [According to Gartner](https://www.gartner.com/en/newsroom/press-releases/2022-03-07-gartner-identifies-top-security-and-risk-management-trends-for-2022), 45% of organizations worldwide have experienced attacks on their software supply chains, a three-fold increase from 2021. Attackers have found that supply chains offer a near-limitless attack surface that can be vulnerable through automatic software updates, software-as-a-service (SaaS) tools, the cloud, and even [AI-generated false information](https://www.darkreading.com/application-security/chatgpt-hallucinations-developers-supply-chain-malware-attacks) (popularly known as “hallucinations”) that can be exploited to trick developers into downloading malicious packages.

## Popular vectors for malicious packages

The most common vectors for malicious packages include brandjacking, typosquatting, dependency hijacking, and dependency confusion. *Brandjacking* means an attacker assumes the online identity of the legitimate owner of a package. In *typosquatting*, an attacker publishes a malicious package with a name similar to a popular package in the hope that a downloader will unintentionally fetch the malicious version. *Dependency* *hijacking* and *dependency* *confusion* attacks also rely on substitutions of malicious packages for the real versions. In 2018, for example, a malicious package was published to npm, the world’s largest software registry, and added as a dependency to the widely used “event-stream” package. It was downloaded more than 8 million times in less than three months.

## The four major open source ecosystems

There are four major open source ecosystems: Java, Python, .NET, and the largest and most popular of them all, JavaScript. Each has its own package distribution and management system. The default package manager for JavaScript’s runtime node.js is npm. JavaScript and npm are not any less secure than the other three ecosystems, but their ubiquity has made them a target of choice for malicious actors. Whatever open source ecosystem you prefer, malicious packages can pose serious risks to the integrity and security of your applications.

## Identifying malicious code and preventing it from entering your SDLC

The threat of malicious packages in npm requires proactive measures to mitigate the risks. Here are three strategies that developers should adopt to defend against inadvertently installing malicious packages.

* **Validate the libraries you download**. Double-check the reputation and trustworthiness of the package. Look for signs of fake accounts or impersonations, and verify the legitimacy of the package’s source before installing it.
* **Review package ownership and maintenance.** Be cautious when using packages that have recently changed maintainers. Be wary of significant changes in functionality among different versions.
* **Use npm security tools.** These include the npm audit and npm shrinkwrap commands, which can help prevent the installation of a malicious package.

Proactively, consider implementing one of the many [software composition analysis (SCA) tools](https://www.synopsys.com/software-integrity/security-testing/software-composition-analysis.html) available today. Look for one that will automate the creation and maintenance process for a [Software Bill of Materials (SBOM](https://www.synopsys.com/blogs/software-security/building-sbom-with-black-duck/)) of open source and third-party code. Many SCA tools will continuously monitor for and advise of new security threats as they appear and will deliver [timely advisories of security threats](https://www.synopsys.com/blogs/software-security/prioritizing-open-source-vulnerabilities-in-software-due-diligence/) with actionable mitigation advice.

For a more detailed examination of the threat of malicious packages in the npm ecosystem with real-world examples and mitigations, please see our complimentary eBook at the link below.

[Learn more with our malicious code eBook](https://www.synopsys.com/software-integrity/resources/ebooks/malicious-npm-packages.html)

文章来源: https://www.synopsys.com/blogs/software-security/malicious-packages-npm/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)
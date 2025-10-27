---
title: The top three differences between an open source audit and an open source scan
url: https://buaq.net/go-135269.html
source: unSafe.sh - 不安全
date: 2022-11-13
fetch_date: 2025-10-03T22:36:35.138138
---

# The top three differences between an open source audit and an open source scan

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

![](https://8aqnet.cdn.bcebos.com/cf2357ee044f56a611ae1ea68c4291d7.jpg)

The top three differences between an open source audit and an open source scan

Posted by on Friday, November 11, 2022
*2022-11-12 01:0:8
Author: [www.synopsys.com(查看原文)](/jump-135269.htm)
阅读量:27
收藏*

---

Posted by on Friday, November 11, 2022

*Understanding the differences between an open source audit and an open source scan will help you determine which approach is best for your organization.*

One of the biggest challenges of helping organizations determine the correct approach to managing their open source usage is the range of risk profiles, standards, and even definitions of “audits” and “scans.” We frequently are asked, “Can you perform an open source scan?” or “Can you perform an open source audit?” The answer is we can do both, but we need to understand the use case to determine which approach makes the most sense.

Let’s start by defining what each of these terms mean. An open source scan is an entirely automated analysis, whereas an open source audit is a deeper analysis that involves experts reviewing and analyzing the results of an automated scan. The final output for both a scan and an audit is a [software Bill of Materials](https://www.synopsys.com/blogs/software-security/software-bill-of-materials-bom/) (SBOM)—an inventory of all the open source components in a codebase and the associated licenses and security vulnerabilities.

It’s important to note that most automated tools rely on information used by the build system. However, open source is often introduced into the code via other paths, so automated analysis comes up short. Also, build-oriented tools are designed to be integrated with the build system, so they are not suited to third-party analysis.

## Three main differences between an open source audit and an open source scan

###### Expert review

This is the biggest difference between an audit and a scan. An automated scan tool, even one like Black Duck® (which, unlike most, can discover open source snippets) is still just that—an automated tool. To create the most accurate SBOM, experts must review the results of any automated scan. Automated tools can’t always identify each open source component, often because open source components have additional open source components as dependencies. Automated tools take their best guess, but human experts can apply multiple techniques and judgment to accurately identify a component and find components that the tools are not designed to discover.

###### String search

String searching algorithms look for strings within source code text. This is a key part of an audit because it can discover easy-to-miss pieces of open source and essential information like copyright references in the codebase. An example of a string search might be, “Search for a string that includes the word ‘copyright’ within five words of the word ‘incorporated’ but does not include company name.” This capability uncovers copyrights in the software that may not belong to the developer. It also discovers references such as URLs that can identify code pulled from blogs, custom licenses, or code that requires a commercial license. Further, auditors may find evidence of code misuse by searching for phrases like “stolen from” or “taken from.”

###### Snippet identification

Snippets are small pieces of source code that have been copied from other works. A snippet of open source software can easily find its way into an organization’s proprietary code. For example, a developer may find a useful function from an open source program and paste it into their program. But because they did not use the entire component, only the most sophisticated automated tools can detect it. And even then, an expert eye is required to identify the component from which the code was copied. A small snippet of code may not create a security vulnerability, but it still carries [license compliance obligations](https://www.synopsys.com/blogs/software-security/top-open-source-licenses/). And copyleft licenses can be problematic and put proprietary IP at risk.

## Choosing the right approach for your organization

Deep analysis by skilled auditors using a range of world-class tools will always achieve the most accurate and complete SBOM. The downside is that it requires unusually skilled humans and time. So which approach is best? The answer depends on the use case and the associated risk profile. For internal development, regular, frequent [open source scans](https://www.synopsys.com/software-integrity/solutions/open-source-security.html) using an automated tool is the recommended approach. Once integrated into the software development toolchain and process, such tools can help continuously manage your open source usage and risk. When it comes to events like mergers and acquisitions where the stakes are high, it’s risky to depend on the output of an automated tool, perhaps one configured and run by the target. The recommended approach is to do an open source audit to ensure that no stone is left unturned.

[![Software due diligence checklist and guidelines | Synopsys](https://images-cdn.welcomesoftware.com/Zz1kN2UyN2JkMDYxZGExMWVkYWFjNmQ2NTUzNWM4YTU3Mg==?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOlsiZDdlMjdiZDA2MWRhMTFlZGFhYzZkNjU1MzVjOGE1NzIiXSwiZXhwIjoxNjY4MTkzODY4fQ.RyNk_KT_q4Ny0ZJTr3PWvSqsEqx9_Dn-DVIa30BQnvQ)](https://www.synopsys.com/software-integrity/resources/white-papers/software-due-diligence.html?intcmp=sig-blog-auditvsscan)

![](https://pixel.welcomesoftware.com/px.gif?key=YXJ0aWNsZT03ZWY0ODUwNDYxZDAxMWVkOTZhMzk2NTFlNzZjYWVlMg==)

文章来源: https://www.synopsys.com/blogs/software-security/differences-between-open-source-audit-vs-scans/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)
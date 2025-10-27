---
title: CyRC Special Report: How companies fared in the aftermath of Log4Shell
url: https://buaq.net/go-147859.html
source: unSafe.sh - 不安全
date: 2023-02-04
fetch_date: 2025-10-04T05:39:46.147563
---

# CyRC Special Report: How companies fared in the aftermath of Log4Shell

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

![](https://8aqnet.cdn.bcebos.com/ebb34899ea817e4363bb35bbdf879ffe.jpg)

CyRC Special Report: How companies fared in the aftermath of Log4Shell

Posted by on Friday, February 3, 2023
*2023-2-3 21:30:27
Author: [www.synopsys.com(查看原文)](/jump-147859.htm)
阅读量:32
收藏*

---

Posted by on Friday, February 3, 2023

*We examine the Log4Shell disclosure through the lens of the Black Duck Knowledge Base to understand how organizations respond to high-profile vulnerabilities.*

![CyrC Special Report: Log4Shell analysis | Synopsys](https://www.synopsys.com/blogs/software-security/wp-content/uploads/2023/02/cyrc-locks-1900x500-1.jpg)

Disclosed in December 2021, Log4Shell is an easy-to-exploit vulnerability in a popular open source component, log4j (CVE-2021-44228 and Black Duck Security Advisory BDSA-2021-3731).

Our analysis of the Log4Shell disclosure using data from the [Black Duck Knowledge Base](https://www.synopsys.com/software-integrity/security-testing/software-composition-analysis/knowledgebase.html) (KB) provides some interesting insights into how organizations respond to a high-profile vulnerability like Log4Shell.

## The Black Duck Knowledge Base and query data

The KB is a collection of vulnerability information about open source components that is meticulously collected and maintained by our tireless Black Duck security research team.

When our customers use Black Duck®, the tool makes queries to the KB to retrieve information about specific open source components.

We can’t look into the applications our customers are scanning and what they are finding, but we can observe the queries that come into the KB. A query is recorded for several reasons:

* When a customer uses Black Duck to scan one or more applications, a query is performed for each component found. For example, if log4j 2.14.0 was detected in a single application or in a hundred, Black Duck would use a single query to retrieve its information from the KB.
* If a customer uses the Black Duck user interface to examine a specific component, a query is sent to the KB to retrieve its information.
* Black Duck periodically checks to see if any KB updates are available for components in previously scanned applications. If the KB information has been updated, Black Duck generates a query to retrieve the latest information.

Our data about KB queries is entirely anonymized and cannot be linked to specific applications or specific customers.

Having said that, the KB query data does serve as a rough measure of usage, although that interpretation is diluted somewhat by the update process.

## The aftermath of the Log4Shell disclosure

Getting back to log4j, let’s see what happened to usage of vulnerable versions after the [Log4Shell](https://www.synopsys.com/blogs/software-security/mitigating-impact-of-log4j-log4shell/) disclosure.

Figure 1 shows the number of queries per week for a subset of the released versions of log4j, starting from two months before Log4Shell and continuing for a full year after.

[![Chart showing vulnerable versions of log4j | Synopsys](https://www.synopsys.com/blogs/software-security/wp-content/uploads/2023/02/Chart_vulnerable-log4j-versions.png)](https://www.synopsys.com/blogs/software-security/wp-content/uploads/2023/02/Chart_vulnerable-log4j-versions.png) *Figure 1: Vulnerable versions of log4j*

As expected, we see a fairly steady number of queries for these versions of log4j before the Log4Shell disclosure on December 10, probably reflecting normal component detection in customer applications.

But note the big spike of activity that accompanies the Log4Shell disclosure, probably reflecting frequent KB updates for the affected components.

Subsequently, as expected, the usage of the vulnerable components tapers off, punctuated by several spikes that probably correspond to KB updates.

Interestingly, we never seem to reach zero for any of the vulnerable versions. Why not? Several explanations are plausible:

* Organizations might have examined applications and decided that they weren’t using log4j in a vulnerable way.
* Organizations might have changed how they use log4j to mitigate the vulnerability.
* Quickly evolving mitigation advice might have caused confusion.

## Adopting the fixed versions of log4j

The fix for Log4Shell was rolled out in several releases in quick succession: 2.15.0, 2.16.0, 2.17.0 , and 2.17.1 were released over a frenetic time period of approximately one week (see Figure 2).

[![Tracking with various Log4Shell fixes | Synopsys](https://www.synopsys.com/blogs/software-security/wp-content/uploads/2023/02/Tracking-log4shell-fixes.png)](https://www.synopsys.com/blogs/software-security/wp-content/uploads/2023/02/Tracking-log4shell-fixes.png) *Figure 2: Tracking with various Log4Shell fixes*

The intermediate or incomplete fixes—versions 2.15.0, 2.16.0, and 2.17.0—all show the characteristic tapering that we saw before, indicating declining usage over time. Again, the spikes most likely correspond to updates in the KB being propagated to customers.

The fixed version that seems to have taken hold is 2.17.1, which shows sustained usage over time. We can even smooth out the data with a running average to better visualize the adoption of this version (see Figure 3).

[![chart of smoothing out data for log4j | Synopsys](https://www.synopsys.com/blogs/software-security/wp-content/uploads/2023/02/Smoothing-data-for-Log4j.png)](https://www.synopsys.com/blogs/software-security/wp-content/uploads/2023/02/Smoothing-data-for-Log4j.png%22) *Figure 3: Smoothing out the data for log4j 2.17.1*

## If it ain’t broke…

Version 2.17.1 of log4j definitively fixed Log4Shell and its follow-on vulnerabilities.

[![Chart of adoption of log4j and later versions | Synopsys](https://www.synopsys.com/blogs/software-security/wp-content/uploads/2023/02/Adoption-of-log4j-and-later-versions.png)](https://www.synopsys.com/blogs/software-security/wp-content/uploads/2023/02/Adoption-of-log4j-and-later-versions.png) *Figure 4: Adoption of log4j 2.17.1 and later versions.*

Development always continues, of course, and several versions of log4j have been released subsequent to 2.17.1. Figure 4 shows the adoption curves for these versions.

While these versions have a characteristically increasing trend in adoption rate, even 2.17.2 has not reached the same volume of queries as 2.17.1, suggesting that many organizations updated log4j only as long as they needed to be free of Log4Shell.

## Conclusions

While we’d like to be able to make statements about X number of applications containing vulnerable versions of log4j, the data we have is not that specific.

However, considering KB queries as a rough measure of applications containing specific versions of log4j, we can draw a couple of conclusions about how our customers handle a major vulnerability like Log4Shell:

* Our customers are quick to respond. The number of queries for vulnerable versions of log4j drops off quickly after Log4Shell was disclosed.
* The KB queries still show vulnerable versions of log4j, so it seems likely that in affected applications, our customers mitigated Log4Shell in some other way instead of updating to a newer version. Updating is not always an option due to cost, testing, or policy, so some customers might have decided to retire older applications rather than patch.
* While we see characteristic uptake for newer versions of log4j (2.17.2, 2.18.0, and 2.19.0), the rate is much slower and lower volume than for 2.17.1. This indicates that customers are much more likely to update a component to mitigate a vulnerability rather than simply as a matter of routi...
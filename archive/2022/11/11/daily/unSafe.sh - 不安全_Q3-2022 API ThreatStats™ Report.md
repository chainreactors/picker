---
title: Q3-2022 API ThreatStats™ Report
url: https://buaq.net/go-135087.html
source: unSafe.sh - 不安全
date: 2022-11-11
fetch_date: 2025-10-03T22:21:21.057182
---

# Q3-2022 API ThreatStats™ Report

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

Q3-2022 API ThreatStats™ Report

The latest quarterly review and analysis of API vulnerabilities and exploits is in. Our initia
*2022-11-10 21:0:0
Author: [lab.wallarm.com(查看原文)](/jump-135087.htm)
阅读量:20
收藏*

---

The latest quarterly review and analysis of API vulnerabilities and exploits is in. Our initial take had us thinking it was smooth sailing for the state of API vulnerabilities in Q3—or was it just a lull in the storm?

As it turns out, it’s neither.

Read on to learn more about Wallarm’s analysis of API vulnerabilities in Q3-2022—and be sure to attend our upcoming webinar on Thursday, November 10 at 11 AM PT where we’ll present all our findings. [**Register Now**](https://www.wallarm.com/webinars/q3-2022-api-threatstats) to reserve your seat!

At first blush, this quarter’s data appear to be a story about API vulnerabilities leveling off: the number of API vulnerabilities and impacted vendors – metrics that saw huge jumps in the [Q2 API Vulnerability Report](https://lab.wallarm.com/api-vulnerabilities-jump-up-3-7x-in-q2-2022/) – were basically unchanged during Q3. This combined with virtually unchanged CVSS scores (both average and % in the critical or high range) had Q3 looking like a nothingburger.

But digging deeper into the data revealed that these still waters run deep.

**Key Findings**

1. **Infrastructure**. A vast majority of the most impactful vulnerabilities analyzed in Q3 impacted DevOps tools and infrastructure – which clearly shifts your security focus.
2. **Injections**. While the OWASP Top-10 Injection categories ([A03:2021](https://owasp.org/Top10/A03_2021-Injection/) for web apps and [API8:2019](https://github.com/OWASP/API-Security/blob/master/2019/en/src/0xa8-injection.md) for APIs) top the charts at over 33% of all CVEs analyzed, further inspection reveals many, many variations that undoubtedly will require extra effort to remediate.
3. **Exploits**. A surprising finding was that the average gap between CVE and exploit POC publication was zero days! This will greatly impact your mitigation timeline.

All these findings will have significant implications on your organization’s API security program.

**Analysis Path**

As per usual, we analyzed the data to look for trends and insights from a variety of perspectives, including software type, vendor, [CVSS scores](https://www.wallarm.com/what/what-is-cvss#cvss_score_metrics), [CWEs](https://www.wallarm.com/what/cwe-common-weakness-enumeration) and both [OWASP Top-10](https://owasp.org/Top10/) (2021) for web apps and [OWASP API Security Top-10](https://owasp.org/www-project-api-security/) (2019). We also dug deeply into publicly disclosed exploit PoCs to extract payloads and validate if any threats have moved from a theoretical to an actual risk.

So how did we reach these conclusions? Here’s a brief look at the analysis path:

1. **API risks remain high**, both in terms of total CVEs and CVSS scores. As we drilled into this, we determined that nearly all of the [2022 CWE Top 25 Most Dangerous Software Weaknesses](https://cwe.mitre.org/top25/archive/2022/2022_cwe_top25.html) list from MITRE / CISA are included, and that injections are the top threat vector. Another double-click and we discover that these **injection weaknesses** cover a large number of CWEs – each of which will require different root-cause analysis and remediation.
2. The **composition of vulnerable products** was more fully investigated. In our research, we quickly found that the products impacted are about 2/3 Open Source vs. 1/3 commercial and that vulnerabilities follow the same pattern. An even closer look reveals that a critical number of products impacted involve **development infrastructure** – which if breached might have a very large blast radius.
3. Finally, we looked at **published exploit POCs** and found the number had dropped significantly from 61 to 30 (or 33% and 15%of all CVEs analyzed, respectively). However, looking more closely we learned that over 50% of these exploit POCs had been published **on or before the CVE release date**, resulting in an average time-to-exploit of zero (0) days – ouch!

**Infographic**

For more highlights from the final report, look at our [**Q3-2022 API ThreatStats™ Report infographic**](https://hubspot.wallarm.com/hubfs/Wallarm%20Q3-2022%20API%20ThreatStats%20Report%20Infographic.pdf). We hope you find it interesting and useful, and that it helps you improve your API vulnerability management and security posture.

**Deep-Dive Webinar**

[Register for the Live Event](https://www.wallarm.com/webinars/q3-2022-api-threatstats)

文章来源: https://lab.wallarm.com/q3-2022-api-threatstats-report/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)
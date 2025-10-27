---
title: Take the pressure off coding for your developers
url: https://buaq.net/go-151401.html
source: unSafe.sh - 不安全
date: 2023-03-01
fetch_date: 2025-10-04T08:19:01.802981
---

# Take the pressure off coding for your developers

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

![](https://8aqnet.cdn.bcebos.com/98a1cf68f1b202ec63230d4233333fee.jpg)

Take the pressure off coding for your developers

IDE security plug-in tools like Code Sight can help shift security left without slowing down your
*2023-2-28 22:0:48
Author: [www.synopsys.com(查看原文)](/jump-151401.htm)
阅读量:22
收藏*

---

*IDE security plug-in tools like Code Sight can help shift security left without slowing down your development teams.*

![](https://www.synopsys.com/blogs/software-security/wp-content/uploads/2023/02/Banner19x5_Dev2-1-300x79.png)

In 2022, Synopsys commissioned the SANS Institute to examine how organizations achieved improvements in their security posture and operational effectiveness by aligning development, security, and operations teams around the cultural ideals, practices, and tools that make up the secure DevOps, or DevSecOps, methodology.

Respondents to the survey were drawn from a geographically diverse group from organizations of all sizes, including many in security roles. The subsequent report showcases the progress made by the community, and ongoing challenges on the path to DevSecOps excellence.

In this series of blog posts, we’re going to examine what the “[SANS 2022: DevSecOps Survey: Creating a Culture to Significantly Improve Your Organization’s Security Posture](https://www.synopsys.com/software-integrity/resources/analyst-reports/2022-sans-devsecops-survey.html?intcmp=sig-blog-sansdso1)” report can tell us about how instituting good [DevSecOps practices](https://www.synopsys.com/blogs/software-security/devsecops-best-practices/) can help your organization achieve secure coding without sacrificing development velocity, automate security, and help those involved with triage and remediation work more efficiently.

## DevSecOps survey findings

Let’s begin by examining what we can learn from the SANS report. The good news is that the survey found that shifting left is being instituted across the DevSecOps community. Security testing increased at the architecture and design stage, the requirements and use case stage, the code commit and pull request stage, and the QA and acceptance stage. The bad news for secure coding is that the only stage where security testing fell was at the interactive development environment (IDE) security plug-ins stage. While 44% of respondents surveyed in 2021 were using IDE security plug-ins, by 2022 that number had fallen to 30%. Reducing risk awareness and testing in the IDE increases the likelihood that issues will go undetected and persist downstream into the main product.

![](https://www.synopsys.com/blogs/software-security/wp-content/uploads/2023/02/Percent-using-security-plug-in-300x137.jpg)

However, 82.3% of respondents reported that they found secure coding training for developers useful, and ranked it higher than [penetration testing](https://www.synopsys.com/software-integrity/penetration-testing.html), software composition analysis ([SCA](https://www.synopsys.com/software-integrity/security-testing/software-composition-analysis.html)), automated static application security testing ([SAST](https://www.synopsys.com/software-integrity/security-testing/static-analysis-sast.html)), [threat modeling](https://www.synopsys.com/software-integrity/software-security-services/software-architecture-design/threat-modeling.html), container/image security scanning, dynamic application security testing ([DAST](https://www.synopsys.com/software-integrity/security-testing/dast.html)), third-party compliance reviews or audits, interactive application security testing ([IAST](https://www.synopsys.com/software-integrity/security-testing/interactive-application-security-testing.html)), [fuzz testing](https://www.synopsys.com/software-integrity/security-testing/fuzz-testing.html), and bug bounties. Clearly, secure coding training is crucial, but coding is complicated and tight development timelines and extensive technology landscapes mean that even the most well-trained developers can overlook best practices when they are working at speed. This is where tools come in. Good tools, available right from the IDE, allow developers to incorporate secure coding practices at the speed businesses need to remain competitive.

It is a positive development that in the 2022 survey, more than half of respondents reported that they consider shared security ownership a key success factor to instituting DevSecOps. When asked about improving communications across development, operations, and security, 56% responded that this was a priority—up from 51% in 2021.

To truly move from a DevOps to a [DevSecOps](https://www.synopsys.com/software-integrity/solutions/devsecops.html) model though, automation is crucial. Even the most well-trained developers cannot produce secure code at the rate businesses demand without tooling help. So it’s encouraging that 55% of respondents (up from 43% in 2021) agree that automating build, test, deployment, and provisioning workflows is essential to this endeavor. Integrating automated security testing into developer tools and workflows also increased in importance to 53% from 45%.

Automation can also help organizations ensure secure coding. Although organizations can’t automate coding, they can automate testing at the point where developers are coding. Providing real-time alerts to developers enables them to identify and fix weaknesses in proprietary code or vulnerable open source components directly from the IDE, without requiring extraneous workflows.

Finally, 52% of respondents reported that securing developer buy-in is key to building a solid DevSecOps environment, up from 46% in 2021. The only element where we saw a downward trend was in training developers in secure coding, which fell to 48% from 52%.

## Developers still struggle with security

These numbers indicate that there are still issues with shifting from DevOps to DevSecOps. Specifically, we see issues with training developers in secure coding practices and in getting them to adopt security tools in the IDE. Across the industry, we see that developers resist shifting security left when they feel that an extra burden is being added to their workflows.

Most developers aren’t security experts, and tools that are optimized for the needs of the security team can be too complex and disruptive to be embraced by developers. To make matters worse, these solutions often require developers to leave their IDE to analyze issues and determine potential fixes. All this tool and context-switching kills developer productivity, so even though teams recognize the upside of checking their code and open source dependencies for security issues, they avoid using the security tools they’ve been given due to the downside of decreased productivity.

## Eliminate friction in developer pipelines with Code Sight

Adding a simple, easy-to-use tool like [Code Sight](https://www.synopsys.com/software-integrity/code-sight.html)™ to the IDE can help relieve developers of what feels like an extra testing burden. When IDE-based tools like Code Sight detect an issue, it’s highlighted directly in the editor window for easy identification, much in the same way that spellcheckers highlight errors as you type. Hovering over a highlighted line of code displays details including issue description and remediation guidance. Developers never have to leave the IDE; the tool provides detailed guidance to speed remediation, and many issues can be fixed automatically.

Automated tools can not only scan for weaknesses in custom code and known common vulnerabilities and exposures (CVEs), but also deliver remediation advice to developers a...
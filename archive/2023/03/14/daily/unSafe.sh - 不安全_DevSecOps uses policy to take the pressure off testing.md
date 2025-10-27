---
title: DevSecOps uses policy to take the pressure off testing
url: https://buaq.net/go-153235.html
source: unSafe.sh - 不安全
date: 2023-03-14
fetch_date: 2025-10-04T09:28:04.135538
---

# DevSecOps uses policy to take the pressure off testing

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

![](https://8aqnet.cdn.bcebos.com/c2c08f6af5f0fc4badcee93a072bca85.jpg)

DevSecOps uses policy to take the pressure off testing

Application Security Orchestration and Correlation uses processes and automation to help accelerat
*2023-3-13 21:0:7
Author: [www.synopsys.com(查看原文)](/jump-153235.htm)
阅读量:20
收藏*

---

*Application Security Orchestration and Correlation uses processes and automation to help accelerate vulnerability testing and mitigation.*

![Orchestrating application policy and testing | Synopsys](https://www.synopsys.com/blogs/software-security/wp-content/uploads/2023/03/Banner_long8553v1.png)

In 2022, Synopsys commissioned the SANS Institute to investigate how firms are aligning their development, security, and operations teams with the organizational values, practices, and tools that compose the secure DevOps, or DevSecOps, approach.

In this series of blog posts, we’ll look at what the [SANS study](https://www.synopsys.com/software-integrity/resources/analyst-reports/2022-sans-devsecops-survey.html?intcmp=sig-blog-sansdso2) can teach us about how implementing effective [DevSecOps](https://www.synopsys.com/blogs/software-security/devsecops-best-practices/) can help organizations institute secure coding without sacrificing development velocity, institute policies and testing to automate security, and help those involved with triage and remediation work more efficiently.

Let’s start by looking at what the SANS study reveals about automating security testing and remediation, and setting policies as code.

## Identifying important aspects of DevSecOps

When asked which elements they thought were crucial to their security programs, respondents identified shared security ownership as the most important. Increasing communication between the development, operations, and security teams was highlighted as a key to success by 56% of respondents, up from 51% in the 2021 results. Accordingly, 52% of respondents said ensuring developer buy-in was crucial, while 48% identified training developers on secure coding practices as vital to their program.

Effective DevSecOps depends on contributors owning their role in security, so developers who have a recognized role in an organization’s security risk posture help ensure that a DevSecOps program does not underperform and an organization’s risk does not rise.

A significant change in 2022 is that respondents appear to be increasingly convinced of the importance of automation. According to the SANS 2022 report, 55% of respondents thought that automating their build, test, deployment, and provisioning workflows was important, up from 43%, while 53% thought that integrating automated security testing into developer tools and workflows was important, up from 45%.

[Continuous security testing](https://www.synopsys.com/glossary/what-is-continuous-testing.html) is a key practice to secure DevOps. When the rates of software assets moving through the pipeline increase, more security testing will be needed. Automating application security testing (AST) throughout the software development life cycle (SDLC) is your best bet for increasing the success of your security program. DevOps integration reduces friction and moves security left in the workflow, helping firms uncover security risks sooner. Integration provides security risk insight at numerous points in the process, and automation offers the scalability, efficiency, and governance consistency required.

## Understanding ASOC

[Application security orchestration and correlation](https://www.synopsys.com/glossary/what-is-application-security-orchestration-and-correlation.html) (ASOC) is a category of AppSec solution that uses process automation to accelerate vulnerability testing and mitigation. Data from diverse AppSec sources is gathered by ASOC solutions and combined into a single database. ASOC solutions then correlate findings and prioritize critical remediation efforts, enabling security teams to streamline their AppSec activities in an informed and efficient way.

The introduction of AI, machine learning, and other data science methodology and tools will improve DevSecOps, and the use of ASOC tools is likely to rise in the coming years. The SANS survey, however, reports that only 10% of organizations have fully integrated ASOC tools at this time, while 19% have partially done so. ASOC remains on the radar of 17% of organizations that report preliminary investigations, and 14% of organizations are experimenting or running pilot projects. Another 23% of respondents to the SANS study are unsure whether their company has made an investment in ASOC tools. And despite the potential of ASOC tools, 14% of organizations report that they are not investing in ASOC technologies at all.

## Using policy-as-code to automate AppSec

[Policy-as-code](https://www.synopsys.com/glossary/what-is-policy-as-code.html) is a method of defining and managing security rules, criteria, and conditions using code and scripts. It programmatically establishes security gates in a continuous integration, continuous delivery, and continuous deployment (CI/CD) pipeline. It codifies guidelines for risk evaluation, response, and notification in application security testing, allowing security teams to automate testing workflows without sacrificing control or compromising on risk tolerance.

Writing policies in high-level programming languages enables security and DevOps professionals to quickly query them via the policy engine. Security checks and related security gates can be activated based on the specified criteria, depending on what they write in the policy script. Naturally, carrying out this task in the most technology-neutral manner attainable aids in scalability and resilience as best practices develop. This has made YAML and Python linchpins to policy-as-code.

Using policy-as-code to determine what testing tool should be used, or whether a test is needed in the application or environment, can streamline testing cycles and achieve greater accuracy and relevance in the results. This makes it possible to consistently and automatically enforce security policies, which eventually makes it possible to improve software quality without slowing down development.

## Running the right test at the right time

When selecting the appropriate application security testing tool to use, it is important to consider the environment where the tool is deployed, the types of security issues it searches for, the programming languages the tool is compatible with, and the stage of the SDLC when testing is carried out. Most enterprises use a variety of technologies including interactive application security testing (IAST), dynamic application security testing (DAST), and static application security testing (SAST).

Organizations report using an average of 11 AST tools, and many report using more than two dozen. Although many technologies can be incorporated directly into DevOps pipelines, teams frequently struggle with complicated initial configurations and resulting changes to existing workflows. Automating extensive scans with every build can clog pipelines and overload developers with test results that may not relate to the job at hand.

## Orchestrating application policy and testing solutions

Taking the pressure off your developers means finding a way to orchestrate your AST solutions so that your tools and processes work together and execute automatically. Application Security Orchestration and Correlation solutions integrate security tooling throughout the SDLC and connect development, operations, and security teams. Implementing orchestration solution...
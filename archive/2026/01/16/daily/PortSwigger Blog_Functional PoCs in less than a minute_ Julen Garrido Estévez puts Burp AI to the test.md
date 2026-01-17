---
title: Functional PoCs in less than a minute? Julen Garrido Estévez puts Burp AI to the test
url: https://portswigger.net/blog/functional-pocs-in-less-than-a-minute
source: PortSwigger Blog
date: 2026-01-16
fetch_date: 2026-01-17T03:26:47.967339
---

# Functional PoCs in less than a minute? Julen Garrido Estévez puts Burp AI to the test

[Login](/users)

[ ]

Products

Solutions

[Research](/research)
[Academy](/web-security)

Support

Company

[Customers](/customers)
[About](/about)
[Blog](/blog)
[Careers](/careers)
[Legal](/legal)
[Contact](/contact)
[Resellers](/support/reseller-faqs)

[My account](/users/youraccount)
[Customers](/customers)
[About](/about)
[Blog](/blog)
[Careers](/careers)
[Legal](/legal)
[Contact](/contact)
[Resellers](/support/reseller-faqs)

[![Burp Suite DAST](/content/images/svg/icons/enterprise.svg)
**Burp Suite DAST**
The enterprise-enabled dynamic web vulnerability scanner.](/burp/enterprise)
[![Burp Suite Professional](/content/images/svg/icons/professional.svg)
**Burp Suite Professional**
The world's #1 web penetration testing toolkit.](/burp/pro)
[![Burp Suite Community Edition](/content/images/svg/icons/community.svg)
**Burp Suite Community Edition**
The best manual tools to start web security testing.](/burp/communitydownload)
[View all product editions](/burp)

[**Burp Scanner**

Burp Suite's web vulnerability scanner

![Burp Suite's web vulnerability scanner'](/mega-nav/images/burp-suite-scanner.jpg)](/burp/vulnerability-scanner)

[**Attack surface visibility**
Improve security posture, prioritize manual testing, free up time.](/solutions/attack-surface-visibility)
[**CI-driven scanning**
More proactive security - find and fix vulnerabilities earlier.](/solutions/ci-driven-scanning)
[**Application security testing**
See how our software enables the world to secure the web.](/solutions)
[**DevSecOps**
Catch critical bugs; ship more secure software, more quickly.](/solutions/devsecops)
[**Penetration testing**
Accelerate penetration testing - find more bugs, more quickly.](/solutions/penetration-testing)
[**Automated scanning**
Scale dynamic scanning. Reduce risk. Save time/money.](/solutions/automated-security-testing)
[**Bug bounty hunting**
Level up your hacking and earn more bug bounties.](/solutions/bug-bounty-hunting)
[**Compliance**
Enhance security monitoring to comply with confidence.](/solutions/compliance)

[View all solutions](/solutions)

[**Product comparison**

What's the difference between Pro and Enterprise Edition?

![Burp Suite Professional vs Burp Suite Enterprise Edition](/mega-nav/images/burp-suite.jpg)](/burp/enterprise/resources/enterprise-edition-vs-professional)

[**Support Center**
Get help and advice from our experts on all things Burp.](/support)
[**Documentation**
Tutorials and guides for Burp Suite.](/burp/documentation)
[**Get Started - Professional**
Get started with Burp Suite Professional.](/burp/documentation/desktop/getting-started)
[**Get Started - Enterprise**
Get started with Burp Suite Enterprise Edition.](/burp/documentation/enterprise/getting-started)
[**User Forum**
Get your questions answered in the User Forum.](https://forum.portswigger.net/)
[**Downloads**
Download the latest version of Burp Suite.](/burp/releases)

[Visit the Support Center](/support)

[**Downloads**

Download the latest version of Burp Suite.

![The latest version of Burp Suite software for download](/mega-nav/images/latest-burp-suite-software-download.jpg)](/burp/releases)

# Functional PoCs in less than a minute? Julen Garrido Estévez puts Burp AI to the test

[ ]

Hassan Ud-Deen |
16 January 2026 at 00:00 UTC

*Note: This is a guest post by pentester*[Julen Garrido Estévez](https://www.linkedin.com/in/julen-garrido-estevez/) *(@b3xal).*

![](/cms/images/7a/13/2696-article-julen-garrido-quote.png)

* [**Methodology**](#Methodology)
* [**Key results**](#KeyResults)
* [**Examples**](#Examples)
* [**Key learnings**](#KeyLearnings)
* [**Prompt template**](#PromptTemplate)
* [**A pentester's POV on Burp AI**](#PentesterPOV)

Pentester Julen Garrido Estévez (@b3xal) wanted to verify whether Burp AI could deliver real value in his day-to-day work. Would it speed up vector discovery, PoC generation, and contextual analysis? Is it worth the credits? Which types of prompts work best?

In this guest post, Julen walks us through how he set about methodically answering these questions. He also provides insights into how you can optimise your prompts to get the best results.

## Methodology

I tested Burp AI in Repeater against labs from PortSwigger's Web Security Academy, the deliberately vulnerable ginandjuice.shop, and my own environments, logging every interaction as a reproducible test case:

**Prompt + highlights + notes → Response → Time to PoC → Number of Requests → Hallucinations / Adherence to guidance → Credits consumed (estimated cost, €).**

### Prompt-style calibration

I was especially interested in comparing how different prompting styles affected the results, so I tested the following three prompting styles:

* **Free-form prompts based on the guidance in the official documentation.** For example:

`I am testing the "TrackingId" cookie to determine whether there is evidence of SQL injection. Focus on "TrackingId" and analyse the SQL query in the response. Perform specific tests, suggest payloads, and provide criteria that confirm the vulnerability. If any test confirms the vulnerability, stop immediately and do not issue further requests.`

* **Prompts with a custom structure.** For example:

`- Parameter: "TrackingId"
- Vulnerability type: SQL injection
- Focus: Focus on "TrackingId" and analyse the SQL query present in the response.
- Actions required: Perform specific tests, suggest payloads, provide criteria that confirm the vulnerability
- Stop on confirmation: yes`

* **Structured JSON.** For example:

`{
 "parameter": "TrackingId",
 "vulnerability_type": ["SQL injection"],
 "focus": "Focus on 'TrackingId' and analyse the SQL query present in the response",
 "actions_required": "Perform specific tests, suggest payloads, provide criteria that confirm the vulnerability",
 "stop_on_confirmation": true
}`

Overall, free-form prompts, as suggested in [Burp AI's official documentation](https://portswigger.net/burp/documentation/desktop/ai), offered the best balance of cost and accuracy. Crucially, they also seemed to produce the best results in terms of ensuring Burp AI followed the specified guidance.

The following are excerpts from the most representative sessions. The figures come from my tests in controlled environments, where I tuned the best way to write a prompt.

![](/cms/images/66/30/8fcd-article-image_3_1.png)

### Key results — Prompt-style calibration (Vulnerability: SSTI)

|  |  |  |  |
| --- | --- | --- | --- |
| **Metric / Prompt style** | **Free-form based on official docs** | **Custom structure** | **Structured JSON** |
| **Requests** | 18 | 17 | 44 |
| **Mean time** | 0:44 (44 s) | 1:05 (65 s) | 1:22 (82 s) |
| **Utility (0–5)** | 5/5 | 3/5 | 4/5 |
| **Resolved** | Yes | Yes | Yes |
| **Observations** | Precise and aligned with guidance; functional PoC in <1 min with lower consumption. | Detected code execution but continued with unnecessary steps that consumed credits. | More exhaustive; provided useful evidence but produced content outside guidance (exfiltration payloads). |

The free-form prompt stands out for its higher utility. By focusing Burp AI clearly, it reduces cost and time, delivers results aligned with instructions and produces reliable PoCs. Although it issues more requests than the prompt with a custom structure, its overall consumption remains the lowest.

### Key results — Prompt-style calibration (Vulnerability: Insecure Deserialization)

|  |  |  |  |
| --- | --- | --- | --- |
| **Metric / Prompt style** | **Free-form based on official docs** | **Custom structure** | **Structured JSON** |
| **Requests** | 6 | 7 | 20 |
| **Mean time** | 1:36 (96 s) | 1:19 (79 s) | 1:35 (95 s) |
| **Utility (0–5)** | 5/5 | 0/5 | 2/5 |
| **Resolved** | Yes | No | No |
| **Observations** | Correctly interpreted the [deserialization](/web-security/deserialization) logic and proposed a valid PoC. | Suffered from "hallucinations" on the fourth request. | Tried to modify the serialized cookie but again devolved int...
---
title: The Problem of Permissions and Non-Human Identities - Why Remediating Credentials Takes Longer Than You Think
url: https://thehackernews.com/2024/11/the-problem-of-permissions-and-non-human-identities.html
source: The Hacker News
date: 2024-11-19
fetch_date: 2025-10-06T19:26:03.565636
---

# The Problem of Permissions and Non-Human Identities - Why Remediating Credentials Takes Longer Than You Think

#1 Trusted Cybersecurity News Platform

Followed by 5.20+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Subscribe – Get Latest News](#email-outer)

* [** Home](/)
* [** Newsletter](#email-outer)
* [** Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Data Breaches](/search/label/data%20breach)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Vulnerabilities](/search/label/Vulnerability)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Contact](/p/submit-news.html)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Free eBooks](https://thehackernews.tradepub.com)

About Site

* [About THN](/p/about-us.html)
* [Jobs](/p/careers-technical-writer-designer-and.html)
* [Advertise with us](/p/advertising-with-hacker-news.html)

Contact/Tip Us

[**

Reach out to get featured—contact us to send your exclusive story idea, research, hacks, or ask us a question or leave a comment/feedback!](/p/submit-news.html)

Follow Us On Social Media

[**](https://www.facebook.com/thehackernews)
[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.youtube.com/c/thehackernews?sub_confirmation=1)
[**](https://www.instagram.com/thehackernews/)

[** RSS Feeds](https://feeds.feedburner.com/TheHackersNews)
[** Email Alerts](#email-outer)

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjWa8tsMNqlevi1HGF1ALQRGIq7hROPFAbHd3R1RTEOe73T8_Q2xW_-91t2jSGjU5peiPb8QYblGp4igNW-u2Qmlxbp2BKzTVMSvyXDZJmC-BYpiiJHrcnG5drmSP97iZ9PVIf1DeEr7U-7vWpe4HXwfMjt8FGNgq5mOycOJluYr9wF7YOKrQY9MfArwgjt/s728-e100/ai-agent-security-d.png)](https://thehackernews.uk/ai-agent-security-d)

# [The Problem of Permissions and Non-Human Identities - Why Remediating Credentials Takes Longer Than You Think](https://thehackernews.com/2024/11/the-problem-of-permissions-and-non-human-identities.html)

**Nov 18, 2024**The Hacker NewsDevOps / Identity Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgN_RYNOemOZrhKe-HXIqkTzYqHDAG7u9doGZ0j_IiVtUBytAK49QhAEMnYkLD4ul5XXzwFoH0Opo1BMkAucjwuHKPdfS94jZ3sBVK14CZJ93wOauPrF7Msul35kxD4dHT27mcg1bXCtc9j9iBpWUXIinJkudk4m7ginLfqGBEDpw4TcD9bgLBm5pp-Zs8/s790-rw-e365/git.png)

According to research from GitGuardian and CyberArk, [79% of IT decision-makers reported having experienced a secrets leak](https://blog.gitguardian.com/voice-of-practitioners-2024/), up from 75% in the previous year's report. At the same time, the number of leaked credentials has never been higher, with over [12.7 million hardcoded credentials in public GitHub repositories alone](https://www.gitguardian.com/state-of-secrets-sprawl-report-2024). One of the more troubling aspects of this report is that over 90% of valid secrets found and reported remained valid for more than 5 days.

According to the same [research, on average, it takes organizations 27 days](https://blog.gitguardian.com/voice-of-practitioners-2024/#:~:text=However%2C%20the%20average%20estimated%20time%20to%20remediate%20a%20leaked%20secret%20stands%20at%2027%20days) to remediate leaked credentials. Combine that with the fact that [non-human identities outnumber human identities by at least 45:1](https://www.cyberark.com/threat-landscape/?prevItm=682892538&prevCol=6824667&ts=11085), and it is easy to see why many organizations are realizing stopping secrets sprawl means finding a way to deal with this machine identity crisis. Unfortunately, the research also shows that many teams are confused about who owns the security of these identities. It is a perfect storm of risk.

## Why Does Rotation Take So Long

So, why are we taking so long to rotate credentials if we know they are one of the easiest attack paths for adversaries? One major contributing factor is a lack of clarity on how our credentials are permissioned. Permissions are what authorize what specific things one entity, such as a Kubernetes workload or a microservice, can successfully request from another service or data source.

Let's remember what remediation of a secrets sprawl incident means: you need to safely replace a secret without breaking anything or granting new, too-wide permissions, which would potentially introduce more security risks to your company. If you already have full insight into the lifecycle of your non-human identities and their associated secrets, this is a fairly straightforward process of replacing them with new secrets with the same permissions. This can take considerable time if you don't already have that insight, as you need to hope the developer who originally created it is still there and has documented what was done.

Let's look at why permissions management is especially challenging in environments dominated by NHIs, examine the challenges developers and security teams face in balancing access control and productivity, and discuss how a shared responsibility model might help.

## Who Really Owns Secrets Sprawl?

Secrets sprawl generally refers to the proliferation of access keys, passwords, and other sensitive credentials across development environments, repositories, and services like Slack or Jira. GitGuardian's latest Voice of the Practitioners report highlights that 65% of respondents place the responsibility for remediation squarely on the IT security teams. [At the same time, 44% of IT leaders reported developers are not following best practices](https://blog.gitguardian.com/voice-of-practitioners-2024/#:~:text=Only%2044%25%20of%20developers%20are%20reported%20to%20follow%20security%20best%20practices) for secrets management.

Secrets sprawl and the underlying issues of over-permissioned long-lived credentials will continue to fall in this gap until we figure out how to better work together in a [shared responsibility model](https://blog.gitguardian.com/devsecops-and-the-appsec-shared-responsibility-model/).

### The Developer's Perspective On Permissions

Developers face enormous pressure to build and deploy features quickly. However, managing permissions carefully, with security best practices, can be labor-intensive. Each project or application often has its own unique access requirements, which take time to research and properly set, almost feeling like a full-time job on top of the work making and deploying their applications. Best practices for creating and managing permissions too commonly do not get applied evenly across teams, are seldom documented appropriately, or are forgotten altogether after the developer gets the application working.

Compounding the issue, in too many cases, developers are simply granting too wide of permissions to these machine identities. [One report found that only 2% of granted permissions are actually used](https://www.csoonline.com/article/2132294/what-are-non-human-identities-and-why-do-they-matter.html). If we take a closer look at what they are up against, it is easy to see why.

For instance, think about managing permissions within Amazon Web Services. AWS's Identity and Access Management (IAM) policies are known for their flexibility but are also complex and confusing to navigate. IAM supports various policy types—identity-based, resource-based, and permission boundaries—all of which require precise configurations. AWS also offers multiple access paths for credentials, including IAM roles and KMS (Key Management Service) grants, which each come with its own unique access configurations. Learning this system is no small feat.

Another common example of a service where permissions can become difficult to manage is GitHub. API keys can grant permissions to repositories across various organizations, making it challenging to ensure appropriate access boundaries. A...
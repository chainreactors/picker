---
title: The Persistence Problem: Why Exposed Credentials Remain Unfixed—and How to Change That
url: https://thehackernews.com/2025/05/the-persistence-problem-why-exposed.html
source: The Hacker News
date: 2025-05-13
fetch_date: 2025-10-06T22:37:00.283905
---

# The Persistence Problem: Why Exposed Credentials Remain Unfixed—and How to Change That

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

# [The Persistence Problem: Why Exposed Credentials Remain Unfixed—and How to Change That](https://thehackernews.com/2025/05/the-persistence-problem-why-exposed.html)

**May 12, 2025**The Hacker NewsSecrets Management / DevSecOps

[![](data:image/png;base64...)](https://www.gitguardian.com/files/the-state-of-secrets-sprawl-report-2025)

Detecting leaked credentials is only half the battle. The real challenge—and often the neglected half of the equation—is what happens after detection. New research from GitGuardian's State of Secrets Sprawl 2025 report reveals a disturbing trend: the vast majority of exposed *company* secrets discovered in public repositories remain valid for years after detection, creating an expanding attack surface that many organizations are failing to address.

According to GitGuardian's analysis of exposed secrets across public GitHub repositories, an alarming percentage of credentials detected as far back as 2022 remain valid today:

[![](data:image/png;base64...)](https://www.gitguardian.com/files/the-state-of-secrets-sprawl-report-2025)

"Detecting a leaked secret is just the first step," says GitGuardian's research team. "The true challenge lies in swift remediation."

## Why Exposed Secrets Remain Valid

This persistent validity suggests two troubling possibilities: either *organizations are unaware their credentials have been exposed* (a security visibility problem), or they lack the resources, processes, or urgency to properly *remediate them* (a security operations problem). **In both cases, a concerning observation is that those secrets are not even routinely revoked, neither automatically from default expiration, nor manually as part of regular rotation procedures.**

Organizations either remain unaware of exposed credentials or lack the resources to address them effectively. Hardcoded secrets proliferate across codebases, making comprehensive remediation challenging. Secret rotation requires coordinated updates across services and systems, often with production impact.

Resource constraints force prioritization of only the highest-risk exposures, while legacy systems create technical barriers by not supporting modern approaches like ephemeral credentials.

This combination of limited visibility, operational complexity, and technical limitations explains why hardcoded secrets often remain valid long after exposure. Moving to [modern secrets security solutions with centralized, automated systems](https://www.gitguardian.com/nhi-governance) and short-lived credentials is now an operational necessity, not just a security best practice.

## Which Services Are Most At Risk? The trends

Behind the raw statistics lies an alarming reality: critical production systems remain vulnerable due to exposed credentials that persist for years in public repositories.

Analysis of exposed secrets from 2022-2024 reveals that database credentials, cloud keys, and API tokens for essential services continue to remain valid long after their initial exposure. These are **not test or development credentials but authentic keys to production environments**, representing direct pathways for attackers to access sensitive customer data, infrastructure, and business-critical systems.

#### **Sensitive Services Still Exposed (2022–2024):**

* MongoDB: Attackers can use these to exfiltrate or corrupt data. These are highly sensitive, offering potential attackers access to **personally identifiable information** or technical insight that can be used for privilege escalation or lateral movement.
* Google Cloud, AWS, Tencent Cloud: these cloud keys grant potential attackers access to infrastructure, code, and customer data.
* MySQL/PostgreSQL: these database credentials persist in public code each year as well.

**These are not test credentials, but keys to live services.**

[![](data:image/png;base64...)](https://www.gitguardian.com/files/the-state-of-secrets-sprawl-report-2025)

Over the past three years, the landscape of exposed secrets in public repositories has shifted in ways that reveal both progress and new risks, especially for cloud and database credentials. Once again, these trends reflect only the ones that have been found and are still valid—meaning **they have not been remediated or revoked despite being publicly exposed.**

For cloud credentials, the data shows a marked upward trend. In 2023, valid cloud credentials accounted for just under 10% of all still-active exposed secrets. **By 2024, that share had surged to almost 16%.** This increase likely reflects the growing adoption of cloud infrastructure and SaaS in enterprise environments, but it also underscores the ongoing struggle many organizations face in managing cloud access securely—especially as developer velocity and complexity increase.

In contrast, database credential exposures moved in the opposite direction. In 2023, **valid database credentials made up over 13% of the unremediated secrets detected, but by 2024, that figure dropped to less than 7%**. This decline could indicate that awareness and remediation efforts around database credentials—particularly following high-profile breaches and increased use of managed database services—are starting to pay off.

The overall takeaway is nuanced: while organizations may be getting better at protecting traditional database secrets, the rapid rise in valid, unremediated cloud credential exposures suggests that new types of secrets are taking their place as the most prevalent and risky. As cloud-native architectures become the norm, the need for automated secrets management, short-lived credentials, and rapid remediation is more urgent than ever.

## Practical Remediation Strategies for High-Risk Credentials

To reduce the risk posed by exposed **MongoDB credentials**, organizations should act quickly to rotate any that may have leaked and set up IP allowlisting to strictly limit who can access the database. Enabling audit logging is also key for detecting suspicious activity in real time and helping with inve...
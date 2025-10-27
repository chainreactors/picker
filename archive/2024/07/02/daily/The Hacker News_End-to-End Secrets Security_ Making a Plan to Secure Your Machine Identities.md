---
title: End-to-End Secrets Security: Making a Plan to Secure Your Machine Identities
url: https://thehackernews.com/2024/07/end-to-end-secrets-security-making-plan.html
source: The Hacker News
date: 2024-07-02
fetch_date: 2025-10-06T17:47:00.604299
---

# End-to-End Secrets Security: Making a Plan to Secure Your Machine Identities

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

# [End-to-End Secrets Security: Making a Plan to Secure Your Machine Identities](https://thehackernews.com/2024/07/end-to-end-secrets-security-making-plan.html)

**Jul 01, 2024**The Hacker NewsDevOps / Identity Protection

[![End-to-End Secrets Security](data:image/png;base64... "End-to-End Secrets Security")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiOPDQjFUUw2KlZCfxrfaRWuZmMagyWQDE6oHkUhRpgFozMh5jwlJp6PlGZNniJr8-Y8pOLA8Liyd70BQQ0UNPEfsHQfmnat5uAWgT5DH-txK9SQL_25K1ejGmBMRXfXoEfV-Lt8cNL0Bu1eY6XAyDf6gjsgQvRRDLUIeWMkuDI5ML2uJJ86dcDtRyMFw4/s790-rw-e365/git-key.png)

At the heart of every application are secrets. Credentials that allow human-to-machine and machine-to-machine communication. Machine identities outnumber human identities by a [factor of 45-to-1](https://www.cyberark.com/resources/blog/why-machine-identities-are-essential-strands-in-your-zero-trust-strategy#:~:text=Machine%20Identities%20Now%20Outnumber%20Human%20Identities%20by%20a%20Factor%20of%2045%20to%20One) and represent the majority of secrets we need to worry about. According to [CyberArk's recent research](https://www.cyberark.com/press/report-93-of-organizations-had-two-or-more-identity-related-breaches-in-the-past-year/), 93% of organizations had two or more identity-related breaches in the past year. It is clear that we need to address this growing issue. Additionally, it is clear that many organizations are OK with using plaintext credentials for these identities in private repos, thinking they will stay private. However, poor hygiene in private code leads to public leaks, as we see in the news too often. Given the scope of the problem, what can we do?

What we really need is a change in our processes, especially around the creation, storage, and working with machine identities. Fortunately, there is a clear path forward, combining existing secrets management solutions and secret detection and remediation tools, all while meeting the developers where they are.

## Making an end-to-end secrets security game plan

When we think of remediating the machine identity problem, also known as secrets sprawl, we can lay out the problem in a couple sentences.

"*We have an unknown number of valid long-lived plaintext secrets spread throughout our code, configurations, CI pipelines, project management systems, and other sources, which we can not account for, and without a coherent rotation strategy. Meanwhile, developers continue to work with secrets in plaintext since it is a reliable, although problematic, way to get the application to work.*"

Thinking through this working definition, we can make a multi-step plan to address each concern.

1. Secrets Detection - Search through code and systems involved in the software development lifecycle to identify existing plaintext credentials, gathering as much information as possible about each.
2. Secrets Management - Accounting for all known secrets through a centralized vault platform.
3. Developer Workflows - Adjust processes and tools to make it easier to properly create, store, and call secrets securely.
4. Secrets Scanning - Continuously monitoring for any new secrets that get added in plain text.
5. Automatic Rotation - Regular replacement of valid secrets shortens their potential exploitation by malicious actors.

You can take this journey one step at a time, treating this as a phased rollout. Before you know it, you will be much closer to eliminating secrets sprawl and securing all your machine identities.

## Finding your secrets

The first problem every team encounters when trying to get a handle on secret sprawl is determining what secrets they even have. A manual search effort to track down unknown secrets would quickly overwhelm any team, but fortunately, there are secrets scanning tools, such as [GitGuardian's](https://www.gitguardian.com/monitor-internal-repositories-for-secrets), that can automate this process and give insight into critical details. From a stable platform, you should provide a communication path to work with the developers for remediation.

## Implementing a centralized secrets vault

Central to any good secrets management strategy is managing how secrets are stored and utilized. Enterprise vaults transparently allow you to account for all known secrets, encrypting them at rest and in transit. A good vault solution, including [Conjure from Cyberark](https://www.conjur.org/) and [Hashicorp Vault Enterprise](https://www.hashicorp.com/products/vault). If all of your infrastructure is from the same provider, such as [AWS or GCP, those are very good options](https://www.gitguardian.com/secrets-management-guide) as well.

## Securing the developer workflow

Secrets management has historically been left in the hands of developers to figure out, leading to a wide variety of solutions like `.env` files and, unfortunately, hardcoding secrets into the codebase. Leveraging a centralized vault solution gives developers a consistent way to safely invoke the credentials from their applications throughout all environments. If you can offer a standardized approach that is just as easy to implement as what they are currently doing, you will find many developers will jump at the chance to guarantee their deployments are not blocked due to this security concern.

You will also want to consider shifting left. Command-line tools, such as ggshield, allow developers to add automatic Git hooks to scan for plaintext credentials before any commit is made. Stopping a secret from ever reaching a commit means no incident to deal with later and fixing the problem at the least expensive point in the software development life cycle.

## Secret scanning at every shared interaction

You also need a way to account for the reality that sometimes accidents happen. Ongoing monitoring is needed to watch for any new issues that come from existing devs making a mistake or when new teams or subcontractors are hired who simply don't know your processes yet. Just as when first doing secrets detection, using a platfo...
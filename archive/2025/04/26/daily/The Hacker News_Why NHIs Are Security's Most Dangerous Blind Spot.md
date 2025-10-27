---
title: Why NHIs Are Security's Most Dangerous Blind Spot
url: https://thehackernews.com/2025/04/why-nhis-are-securitys-most-dangerous.html
source: The Hacker News
date: 2025-04-26
fetch_date: 2025-10-06T22:13:20.584509
---

# Why NHIs Are Security's Most Dangerous Blind Spot

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

# [Why NHIs Are Security's Most Dangerous Blind Spot](https://thehackernews.com/2025/04/why-nhis-are-securitys-most-dangerous.html)

**Apr 25, 2025**The Hacker NewsSecrets Management / DevOps

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjpIJO-R6zuJbISIxRp9dJtmyVSgqJZmWm3Xld-QtyLs7HV5PQ6MAzDhocA5Q10E2xc_Yl9g6RpLvRwh6yblufJHTpKvelle_fFX4VgEoqqiVNf_X2VCV49PxixhtefQpylFsWsMPgNAvBoTbCd8BpN5LRzUm-Dpk8v5s3p3aMJI3oLuYP4cfiVX6OdlUk/s2800/NHI.jpg)

When we talk about identity in cybersecurity, most people think of usernames, passwords, and the occasional MFA prompt. But lurking beneath the surface is a growing threat that does not involve human credentials at all, as we witness the exponential growth of Non-Human Identities (NHIs).

At the top of mind when NHIs are mentioned, most security teams immediately think of **Service Accounts**. But NHIs go far beyond that. You've got **Service Principals**, **Snowflake Roles**, **IAM Roles**, and platform-specific constructs from AWS, Azure, GCP, and more. The truth is, NHIs can vary just as widely as the services and environments in your modern tech stack, and managing them means understanding this diversity.

The real danger lies in how these identities authenticate.

## **Secrets: The Currency of Machines**

Non-Human Identities, for the most part, authenticate using **secrets**: API keys, tokens, certificates, and other credentials that grant access to systems, data, and critical infrastructure. These secrets are what attackers want most. And shockingly, most companies have no idea how many secrets they have, where they're stored, or who is using them.

The **[State of Secrets Sprawl 2025](https://www.gitguardian.com/files/the-state-of-secrets-sprawl-report-2025?ref=blog.gitguardian.com)** revealed two jaw-dropping stats:

* **23.7 million** new secrets were leaked on public GitHub in 2024 alone
* And **70%** of the secrets leaked in 2022 are *still valid today*

Why is this happening?

A part of the story is that **there's no MFA for machines**. No verification prompt. When a developer creates a token, they often grant it wider access than needed, just to make sure things work.

Expiration dates? Optional. Some secrets are created with 50-year validity windows. Why? Because teams don't want the app to break next year. They choose speed over security.

This creates a massive blast radius. If one of those secrets leaks, it can unlock everything from production databases to cloud resources, without triggering any alerts.

Detecting compromised NHIs is much harder than with humans. A login from Tokyo at 2 am might raise red flags for a person, but machines talk to each other 24/7 from all over the world. **Malicious activity blends right in**.

Many of these secrets act like invisible backdoors, enabling lateral movement, supply chain attacks, and undetected breaches. [The Toyota incident](https://blog.gitguardian.com/toyota-accidently-exposed-a-secret-key-publicly-on-github-for-five-years/) is a perfect example — one leaked secret can take down a global system.

This is why **attackers love NHIs and their secrets**. The permissions are too often high, the visibility is commonly low, and the consequences can be huge.

## **The Rise of the Machines (and Their Secrets)**

The shift to cloud-native, microservices-heavy environments has introduced *thousands* of NHIs per organization. NHIs now outnumber human identities from **50:1 to a 100:1** ratio, and this is only expected to increase. These digital workers connect services, automate tasks, and drive AI pipelines — and every single one of them needs secrets to function.

But unlike human credentials:

* **Secrets are hardcoded in codebases**
* **Shared across multiple tools and teams**
* **Lying dormant in legacy systems**
* **Passed to AI agents with minimal oversight**

They often **lack expiration**, **ownership**, and **auditability**.

The result? Secrets sprawl. Overprivileged access. And one tiny leak away from a massive breach.

## **Why the Old Playbook Doesn't Work Anymore**

Legacy identity governance and PAM tools were built for human users, an era when everything was centrally managed. These tools still do a fine job enforcing password complexity, managing break-glass accounts, and governing access to internal apps. But NHIs break this model completely.

Here's why:

* **IAM and PAM** are designed for human identities, often tied to individuals and protected with MFA. NHIs, on the other hand, are decentralized — created and managed by developers across teams, often outside of any central IT or security oversight. Many organizations today are running multiple vaults, with no unified inventory or policy enforcement.
* **Secrets Managers** help you store secrets — but they won't help you when secrets are leaked across your infrastructure, codebases, CI/CD pipelines, or even public platforms like GitHub or Postman. They're not designed to detect, remediate, or investigate exposure.
* **CSPM tools** focus on the cloud, but secrets are everywhere. They're in source control management systems, messaging platforms, developer laptops, and unmanaged scripts. When secrets leak, it's not just a hygiene issue — it's a **security incident**.
* **NHIs don't follow traditional identity lifecycles**. There's often no onboarding, no offboarding, no clear owner, and no expiration. They linger in your systems, under the radar, until something goes wrong.

Security teams are left chasing shadows, manually trying to piece together where a secret came from, what it accesses, and whether it's even still in use. This reactive approach doesn't scale, and it leaves your organization dangerously exposed.

This is where **GitGuardian NHI Governance** comes into play.

## **GitGuardian NHI Governance: Mapping the Machine Identity Maze**

GitGuardian has taken its deep expertise in secrets detection and remediation and turned it into something much more powerful: a complete governance layer for machine identities ...
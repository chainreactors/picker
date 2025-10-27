---
title: Non-Human Identities: How to Address the Expanding Security Risk
url: https://thehackernews.com/2025/06/non-human-identities-how-to-address.html
source: The Hacker News
date: 2025-06-13
fetch_date: 2025-10-06T23:00:44.797993
---

# Non-Human Identities: How to Address the Expanding Security Risk

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

# [Non-Human Identities: How to Address the Expanding Security Risk](https://thehackernews.com/2025/06/non-human-identities-how-to-address.html)

**Jun 12, 2025**The Hacker NewsDevOps / AI Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjb-DvsnP30kW7FJWuN8iornuvBZ2uwFY_pNvq-7vae4P_ikiCbYscXqk4M0PhPgqu3lnSMPRbYUgiuZ7Q3748rYw96pBB5EOVh2rFW-GATNB0BfIa3kbSYu6tzpPq0enLjGQFdeWM5zM5peekiTJt8Uy7nNBoVQtyIWj1tCC3N6yuoFl6VjzBaTFX3klE/s790-rw-e365/nhi.png)

Human identities management and control is pretty well done with its set of dedicated tools, frameworks, and best practices. This is a very different world when it comes to Non-human identities also referred to as machine identities. GitGuardian's end-to-end NHI security platform is here to close the gap.

## Enterprises are Losing Track of Their Machine Identities

Machine identities–service accounts, API keys, bots, automation, and workload identities–that now outnumber humans by up to 100:1 are in fact a massive blind spot in companies' security landscape:

Without robust governance, NHIs become a prime target for attackers. Orphaned credentials, over-privileged accounts, and "zombie" secrets are proliferating—especially as **organizations accelerate cloud adoption, integrate AI-powered agents, and automate their infrastructure**.

### Secrets Sprawl: The New Attack Surface

GitGuardian's research shows that 70% of valid secrets detected in public repositories in 2022 remained active in 2025—a three-year window of vulnerability. These aren't just theoretical risks. Breaches at organizations like the U.S. Department of the Treasury, Toyota, and The New York Times all began with a leaked or unmanaged machine identity.

The problem isn't just about volume. Secrets and credentials are scattered across code, CI/CD pipelines, cloud environments, and ticketing systems— environments outside traditional security perimeters.

This proliferation of unmanaged secrets has caught the attention of security frameworks worldwide. The newly released **OWASP Top 10 Non-Human Identity Risks for 2025** specifically calls out 'Secret Leakage' as the #2 risk, noting that compromised credentials are implicated in over 80% of breaches.

## Why Secrets Managers Alone Aren't Enough

Traditional secrets managers (like HashiCorp Vault, CyberArk, AWS Secrets Manager, and Azure Key Vault) are essential for secure storage—but they don't address the full lifecycle of NHI governance. They can't discover secrets outside the vault, lack context around permissions, and don't automate remediation when secrets are leaked or misused.

GitGuardian's own analysis found that organizations using secrets managers are in fact more prone to secrets leakage. The secrets leakage incidence of repositories leveraging secrets managers is 5.1% compared with 4.6% for public repositories without secrets managers in place. And to add to this point, repositories with secret managers are more likely to handle sensitive information, increasing the risk of exposure.

## The Platform Filling the NHI Security Gap

To address these challenges, organizations must adopt a unified IAM strategy that

empowers DevOps and SRE teams to effectively govern and secure NHIs, on top of the deployment of secrets management solutions (vaults and or secrets managers). This requires investing in solutions that provide comprehensive secrets discovery, centralized visibility, and automated governance capabilities. By leveraging tools that can map relationships between secrets, enforce consistent policies, and streamline rotation and remediation processes, DevOps and SRE teams can reduce the burden of secrets lifecycle management and focus on delivering value to the business.

GitGuardian's [NHI Security Platform](https://www.gitguardian.com/nhi-security) is designed to address these exact blind spots and risks. Here's how:

### **1. Discovery and Inventory: Finding the Invisible**

Manual discovery of machine identities is a lost battle. Secrets exist across repositories, CI/CD pipelines, ticketing systems, messengers, and cloud environments—often in places security teams don't monitor. Traditional approaches can't keep pace with the dynamic nature of modern infrastructure, leading to incomplete inventories.

GitGuardian's automated discovery continuously scans these environments, maintaining a real-time inventory enriched with contextual metadata. This centralized view serves as the foundation for effective governance.

### **2. Onboarding and Provisioning: Securing from Day One**

Inconsistent provisioning processes create immediate risks—misconfigurations, over-permissioned identities, and manual errors. Organizations need standardized workflows that enforce the least privilege access and integrate with centralized secrets management.

A unified platform ensures consistency across teams and provides real-time visibility into permissions, maintaining a secure and compliant ecosystem from the start.

### **3. Continuous Monitoring: Staying Ahead of Threats**

Modern enterprises face a monitoring nightmare: machine identities interact across dozens of systems, each with separate logging mechanisms. With organizations averaging six different secret management instances (according to "Voice of Practitioners: The State of Secrets in AppSec"), maintaining consistent policies becomes nearly impossible.

GitGuardian aggregates and normalizes usage data from multiple sources, providing centralized visibility. Advanced analytics and anomaly detection enable rapid response to high-risk events and policy violations.

### **4. Rotation and Remediation: Keeping Credentials Fresh**

The stakes are high: CyberArk reports that 72% of organizations experienced certificate-related outages in the past year, with 34% suffering multiple incidents. Managing rotation at scale is complex, especially with system dependencies and inconsistent schedules.

GitGuardian integrates with popular secrets managers, providing contextual insigh...
---
title: Explosive Growth of Non-Human Identities Creating Massive Security Blind Spots
url: https://thehackernews.com/2025/04/explosive-growth-of-non-human.html
source: The Hacker News
date: 2025-04-10
fetch_date: 2025-10-06T22:09:35.557428
---

# Explosive Growth of Non-Human Identities Creating Massive Security Blind Spots

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

# [Explosive Growth of Non-Human Identities Creating Massive Security Blind Spots](https://thehackernews.com/2025/04/explosive-growth-of-non-human.html)

**Apr 09, 2025**The Hacker NewsSecrets Management / DevOps

[![Non-Human Identities](data:image/png;base64... "Non-Human Identities")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhV7Opj1EDcnT791C1jS8hO2aeIJ6HyeTlXLGxbZd1Z-3B3b0ov0tpvRNeNYMRNmKNILYEYfOcJUlVFE-H9Lsj5wojgQzkdAPABkVEpYf2_uJ27ibBsxFaivW4FECl-DFh8MeypdKnBCSceLpSH6GGGg_UTSXho0Q89U6NeObh_eYMAE5ZkLZJK6qc0T5k/s790-rw-e365/git.jpg)

[GitGuardian's State of Secrets Sprawl report for 2025](https://www.gitguardian.com/state-of-secrets-sprawl-report-2025) reveals the alarming scale of secrets exposure in modern software environments. Driving this is the rapid growth of non-human identities (NHIs), which have been outnumbering human users for years. We need to get ahead of it and prepare security measures and governance for these machine identities as they continue to be deployed, creating an unprecedented level of security risk.

This report reveals an astounding 23.77 million new secrets were leaked on GitHub in 2024 alone. This is a 25% surge from the previous year. This dramatic increase highlights how the proliferation of non-human identities (NHIs), such as service accounts, microservices, and AI agents, are rapidly expanding the attack surface for threat actors.

## **The Non-Human Identity Crisis**

NHI secrets, including API keys, service accounts, and Kubernetes workers, now outnumber human identities by at least 45-to-1 in DevOps environments. These machine-based credentials are essential for modern infrastructure but create significant security challenges when mismanaged.

Most concerning is the persistence of exposed credentials. GitGuardian's analysis found that 70% of secrets first detected in public repositories back in 2022 remain active today, indicating a systemic failure in credential rotation and management practices.

## **Private Repositories: A False Sense of Security**

Organizations may believe their code is secure in private repositories, but the data tells a different story. Private repositories are approximately 8 times more likely to contain secrets than public ones. This suggests that many teams rely on "security through obscurity" rather than implementing proper secrets management.

The report found significant differences in the types of secrets leaked in private versus public repositories:

* Generic secrets represent 74.4% of all leaks in private repositories versus 58% in public ones
* Generic passwords account for 24% of all generic secrets in private repositories compared to only 9% in public repositories
* Enterprise credentials like AWS IAM keys appear in 8% of private repositories but only 1.5% of public ones

This pattern suggests that developers are more cautious with public code but often cut corners in environments they believe are protected.

## **AI Tools Worsening the Problem**

GitHub Copilot and other AI coding assistants might boost productivity, but [they're also increasing security risks](https://blog.gitguardian.com/github-copilot-security-and-privacy/). Repositories with Copilot enabled were found to have a 40% higher incidence rate of secret leaks compared to repositories without AI assistance.

This troubling statistic suggests that AI-powered development, while accelerating code production, may be encouraging developers to prioritize speed over security, embedding credentials in ways that traditional development practices might avoid.

## **Docker Hub: 100,000+ Valid Secrets Exposed**

In an unprecedented analysis of 15 million public Docker images from Docker Hub, GitGuardian discovered more than 100,000 valid secrets, including AWS keys, GCP keys, and GitHub tokens belonging to Fortune 500 companies.

The research found that 97% of these valid secrets were discovered exclusively in image layers, with most appearing in layers smaller than 15MB. ENV instructions alone accounted for 65% of all leaks, highlighting a significant blind spot in container security.

## **Beyond Source Code: Secrets in Collaboration Tools**

Secret leaks aren't limited to code repositories. The report found that collaboration platforms like Slack, Jira, and Confluence have become significant vectors for credential exposure.

Alarmingly, secrets found in these platforms tend to be more critical than those in source code repositories, with 38% of incidents classified as highly critical or urgent compared to 31% in source code management systems. This happens partly because these platforms lack the security controls present in modern source code management tools.

Alarmingly, only 7% of secrets found in collaboration tools are also found in the code base, making this area of secrets sprawl a unique challenge that most secret scanning tools can not mitigate. It is also exasperated by the fact that the users of these systems cross all department boundaries, meaning everyone is potentially leaking credentials into these platforms.

## **The Permissions Problem**

Further exacerbating the risk, GitGuardian found that leaked credentials frequently have excessive permissions:

* 99% of GitLab API keys had either full access (58%) or read-only access (41%)
* 96% of GitHub tokens had write access, with 95% offering full repository access

These broad permissions significantly amplify the potential impact of leaked credentials, enabling attackers to move laterally and escalate privileges more easily.

## **Breaking the Cycle of Secrets Sprawl**

While organizations increasingly adopt secret management solutions, the report emphasizes these tools alone aren't enough. GitGuardian found that even repositories using secrets managers had a 5.1% incidence rate of leaked secrets in 2024.

The problem requires [a comprehensive approach that addresses the entire secrets lifecycle](https://blog.gitguardian.com/identity-lifecycle-management-for-nhis/), combining automated detection with swift remedi...
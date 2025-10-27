---
title: 5 BCDR Oversights That Leave You Exposed to Ransomware
url: https://thehackernews.com/2024/11/5-bcdr-oversights-that-leave-you-exposed-to-ransomware.html
source: The Hacker News
date: 2024-11-15
fetch_date: 2025-10-06T19:22:03.330166
---

# 5 BCDR Oversights That Leave You Exposed to Ransomware

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

# [5 BCDR Oversights That Leave You Exposed to Ransomware](https://thehackernews.com/2024/11/5-bcdr-oversights-that-leave-you-exposed-to-ransomware.html)

**Nov 14, 2024**The Hacker NewsRansomware / Disaster Recovery

[![Ransomware](data:image/png;base64... "Ransomware")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgdvqtw6KJ6n9gnTQuJGYxJp2Gnd2As3fKjx-HCOtS2Yf_YZDml-LSsS9-JXMRrW3ruA6uOqOsJoa5smXpOh9Ll8rLsoe8VkQqJ5EM-r4vI5jm7Cx9xs4JjcYpCFa-7bifoLUf2CGYaD2bqvxeQNXBz-k0YN_LZPmsN5kE4ISRB40pAWQKCzMPGyL4RpPI/s790-rw-e365/main.png)

Ransomware isn't just a buzzword; it's one of the most dreaded challenges businesses face in this increasingly digitized world. Ransomware attacks are not only increasing in frequency but also in sophistication, with new ransomware groups constantly emerging. Their attack methods are evolving rapidly, becoming more dangerous and damaging than ever. Almost all respondents (99.8%) in a recent survey said they are concerned about the risk of identity information, session cookies and other data being extracted from devices infected with malware, activities highly correlated to a future ransomware attack.[1]

The harsh reality is that ransomware threats aren't going away anytime soon. Despite organizations' best efforts to prevent these attacks, breaches still happen. As such, backup and disaster recovery become your critical last line of defense against these growing threats. However, many organizations overlook essential disaster recovery (DR) practices, leaving them vulnerable to cyberattacks and data disasters.

To combat cyberthreats effectively, your organization must develop a comprehensive DR plan and test it regularly to ensure its efficacy and reliability. Your organization's ability to respond to cyber incidents quickly depends on proactive preparation. The following three strategies are key to protecting your last line of defense and ensuring successful recovery.

**Audit the data:** This ensures that data scattered in multiple places is protected, confirms backup integrity and reduces blind spots.

**Create resilience:** Build robust systems that endure disruptions through local access controls, encryption, immutability and backup isolation.

**Recover with insight:** Enables informed, efficient recovery with minimized business impact through regular DR testing, measuring recovery effectiveness and detecting anomalies in backups.

This article will examine the five business continuity and disaster recovery (BCDR) mistakes businesses make that can result in catastrophic breaches and business disruptions.

## 5 BCDR oversights that leave you exposed

BCDR strategies are critical to safeguard your business against data loss, downtime and cyberthreats. However, even well-prepared organizations often tend to overlook critical aspects that leave them vulnerable. We'll explore five common BCDR oversights that could put your business at risk and offer insights to strengthen your resilience against evolving threats.

### 1. Thinking local immutability is safe enough

Although local immutability adds a layer of defense, ensuring data cannot be altered or changed, relying solely on local immutability can present significant risks. Internal threats, such as compromised credentials, misconfigured controls or insider actions, can allow threat actors to disable immutability settings. After that, they can lay dormant, waiting for immutability flags to expire before encrypting or deleting data.

In smaller environments with limited physical space or budget, performing multiple backup and recovery tasks on one server increases vulnerability, exposing backup data to potential system bugs or security breaches.

Additionally, physical access by an insider can directly bypass immutability by booting from a live CD or USB, allowing backups to be stolen, deleted or encrypted.

Here are a few recommendations to achieve true immutability and safeguard your data against ransomware.

* The most effective way to protect your backups from ransomware is to replicate them to a secure, immutable cloud storage location off-site.
* Partner with backup and DR solution providers like [Unitrends](https://www.unitrends.com/landing/request-a-demo?utm_source=701Rp00000FrjeP&utm_medium=Other&utm_campaign=Unitrends) that replicate backups to several cloud destinations, including Forever Cloud, where data is stored in an immutable format.
* Unitrends uses predictive analytics to check the presence of ransomware and alerts IT administrators if signs of ransomware are detected.
* Use advanced technologies like [Unitrends Recovery Assurance](https://www.unitrends.com/features/disaster-recovery-testing) that automatically performs disaster recovery tests to determine if backups are clean and recoverable.

[Download the Case Study Confidential eBook](https://www.unitrends.com/resources/case-study-confidential) to master data protection through lessons learned from real-world data disasters.

#### Relying on Windows-based backup software

Microsoft Windows is the world's most widely used computer operating system, with a whopping 67% OS market share.[2] Due to its widespread use and popularity, Windows is also a prime target among ransomware groups.

Although the Windows threat landscape is fragmented due to numerous versions and releases, certain commonalities pose risks. Many Windows services are configured to run by default, making them frequent targets for cybercriminals seeking access vectors within the Windows ecosystem.

Threat actors may use a mix of Windows Management Instrumentation (WMI) scripts, vssadmin.exe commands or PowerShell scripts to automatically delete backups. Windows-based backup infrastructure is just as susceptible to ransomware attacks as any other Windows-based component within the data center. Additionally, if the backup server is located in the same physical space as the infrastructure it protects, the risk becomes even greater.

Here are a few ways you can strengthen your defenses against Window-based ...
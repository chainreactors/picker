---
title: Backups Are Under Attack: How to Protect Your Backups
url: https://thehackernews.com/2025/06/how-to-protect-your-backups-from-ransomware-attacks.html
source: The Hacker News
date: 2025-06-18
fetch_date: 2025-10-06T23:00:34.075111
---

# Backups Are Under Attack: How to Protect Your Backups

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

# [Backups Are Under Attack: How to Protect Your Backups](https://thehackernews.com/2025/06/how-to-protect-your-backups-from-ransomware-attacks.html)

**Jun 17, 2025**The Hacker NewsCyber Threat / Business Continuity

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiHjf5J8LLXv1KwtintRctU_AmpJBYdEq5G-oPsV8Wo0EyxfQSvM7qJgq1Ghlf4wr9Y1Q3Dt_fGVLVY17881U19orj2rS7VbK37xKPfU4517BeY7bdAm0Igf_4gTCw9QtH2xU_YOSlHK7ojUqkKdsseA4Y7DKW-Fsk3Kgdmk2xxr10dkvuzx9zG9V4Y1GA/s790-rw-e365/MAIN.jpg)

Ransomware has become a highly coordinated and pervasive threat, and traditional defenses are increasingly struggling to neutralize it. Today's ransomware attacks initially target your last line of defense — your backup infrastructure. Before locking up your production environment, cybercriminals go after your backups to cripple your ability to recover, increasing the odds of a ransom payout.

Notably, these attacks are carefully engineered takedowns of your defenses. The threat actors disable backup agents, delete snapshots, modify retention policies, encrypt backup volumes (especially those that are network accessible) and exploit vulnerabilities in integrated backup platforms. They are no longer trying just to deny your access but erase the very means of recovery. If your backup environment isn't built with this evolving threat landscape in mind, it's at high risk of getting compromised.

How can IT pros defend against this? In this guide, we'll uncover the weak strategies that leave backups exposed and explore actionable steps to harden both on-site and cloud-based backups against ransomware. Let's see how to build a resilient backup strategy, one that you can trust 100% even in the face of sophisticated ransomware attacks.

## Common pitfalls that leave backups exposed

Inadequate separation and the lack of offsite or immutable copies are among the most common weaknesses in backup strategies. Snapshots or local backups alone aren't enough; if they reside in the same on-site environment as production systems, they can be easily discovered, encrypted or deleted by attackers. Without proper isolation, backup environments are highly susceptible to lateral movement, allowing ransomware to spread from compromised systems to backup infrastructure.

Here are some of the most common lateral attack techniques used to compromise backups:

* Active Directory (AD) attacks: Attackers exploit AD to escalate privileges and gain access to backup systems.
* Virtual host takeover: Malicious actors utilize a misconfiguration or vulnerability in the guest tools or hypervisor code to control the hypervisor and virtual machines (VMs), including those hosting backups.
* Windows-based software attacks: Threat actors exploit built-in Windows services and known behaviors across versions for entry points into backup software and backup repositories.
* Common vulnerabilities and exposures (CVE) exploit: High-severity CVEs are routinely targeted to breach backup hosts before patches are applied.

Another major pitfall is relying on a single cloud provider for cloud backups, which creates a single point of failure and increases the risk of total data loss. For instance, if you're backing up Microsoft 365 data in the Microsoft environment, your backup infrastructure and source systems share the same ecosystem, making them easy to discover. With stolen credentials or application programming interface (API) access, attackers can compromise both at once.

## Build backup resilience with the 3-2-1-1-0 strategy

The 3-2-1 backup rule has long been the gold standard in data protection. However, as ransomware increasingly targets backup infrastructure, it's no longer enough. Today's threat landscape calls for a more resilient approach, one that assumes attackers will try to destroy your ability to recover.

That's where the 3-2-1-1-0 strategy comes in. This approach aims to keep three copies of your data and store them on two different media, with one copy offsite, one immutable copy and zero backup errors.

|  |
| --- |
| [![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh7RQej39hMXYGwIsPe-NOci37qS3PDbwyprtyZC03zN6Z9HepgB72q-qLlHbsl2RxMmFv4ASdzYVNlR29YCrFNGfjs8bBOlG7H5fd9-oeCednP5CkSyajKqSWhO6nfM1paqnULpsuU8LFN1KI6ltMlHNeB7BoMoQBaKegEnX2RMMn64rlHy5Od5IFvzcA/s790-rw-e365/1.jpg) |
| Fig 1: The 3-2-1-1-0 backup strategy |

Here's how it works:

### **3 copies of data: 1 production + 2 backups**

When backing up, it's critical not to rely solely on file-level backups. Use image-based backups that capture the full system — the operating system (OS), applications, settings and data — for more complete recovery. Look for capabilities, such as bare metal recovery and instant virtualization.

Use a dedicated backup appliance (physical or virtual) instead of standard backup software for greater isolation and control. When looking for appliances, consider ones built on hardened Linux to reduce the attack surface and avoid Windows-based vulnerabilities and commonly targeted file types.

### **2 different media formats**

Store backups on two distinct media types — local disk and cloud storage — to diversify risk and prevent simultaneous compromise.

### **1 offsite copy**

Ensure one backup copy is stored offsite and geographically separated to protect against natural disasters or site-wide attacks. Use a physical or logical airgap wherever possible.

### **1 immutable copy**

Maintain at least one backup copy in an immutable cloud storage so that it cannot be altered, encrypted or deleted by ransomware or rogue users.

### **0 errors**

Backups must be regularly verified, tested and monitored to ensure they're error-free and recoverable when needed. Your strategy isn't complete until you have full confidence in recovery.

To make the 3-2-1-1-0 strategy truly effective, it's critical to harden the environment where your backups live. Consider the following best practices:

* Deploy the backup server in a secure local ...
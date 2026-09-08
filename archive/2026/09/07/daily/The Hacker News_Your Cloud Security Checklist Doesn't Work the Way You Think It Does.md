---
title: Your Cloud Security Checklist Doesn't Work the Way You Think It Does
url: https://thehackernews.com/2026/09/your-cloud-security-checklist-doesnt.html
source: The Hacker News
date: 2026-09-07
fetch_date: 2026-09-08T06:42:26.729820
---

# Your Cloud Security Checklist Doesn't Work the Way You Think It Does

#1 Trusted Cybersecurity News Platform

Followed by 5.70+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Get the Latest News](#email-outer)

* [Home](/)
* [Newsletter](#email-outer)
* [Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Threat Intelligence](/search/label/Threat%20Intelligence)
* [Vulnerabilities](/search/label/Vulnerability)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Awards](https://awards.thehackernews.com/)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Awards](https://awards.thehackernews.com/)
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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiHP9KRFkaxKFUKQNRU3CkfxCyJLEuIfmo6ov7iWHHRBE1ShJKfXdPvozMZMVuvOJipQ8Qbap3UBmtjKvZh-xBqLeUartPWmRuQj2W8nqdCk2_XlYLXpj15R4Du2oJ1nNVPqIuR-TwbMyPQe4gxxCcMYvUMbFO_Nin2OdhyzkJvX8Sn83aEbM1C5sgaaCqI/s728-nu-rw-lo-l85-e365/wiz-sep-d.png)](https://thehackernews.uk/claude-security-guide-d)

# [Your Cloud Security Checklist Doesn't Work the Way You Think It Does](https://thehackernews.com/2026/09/your-cloud-security-checklist-doesnt.html)

**The Hacker News**Sep 07, 2026Cloud Security / Data Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhAkHa8CDEfDzL0HknvyLE5eRK8r91iyhgzpCS1GmG3HRtriZYYFzCTP9_H433YsqJ80SAppgs9g6rOhsTWIzHPh_CFcZJS18DIj5ANgzFwSU0vfcyJofTEqEvjGGjNcqZdHU_54PENNzxawWHCZ2r_1K-A63x3P8CbuIiu8OHASjQV3OoglWTefAF2dZw/s1700-nu-rw-lo-l85-e365/intruder.jpg)

If managing security across multiple cloud providers wasn't hard enough, each one fails in a different way. For the [2026 Cloud Security Index](https://www.intruder.io/blog/cloud-security-index?utm_source=thehackernews&utm_medium=p_referral&utm_campaign=global%7Cfixed%7Ccloud_index), Intruder analyzed misconfiguration data from 3,000 organizations across AWS, Azure, and Google Cloud and found that risk profiles across providers have almost nothing in common. Here’s what the data looks like.

## How risk differs across cloud providers

Intruder grouped every misconfiguration into one of six categories: weak identity and access management (IAM), missing logging, misconfigured services, permissive firewalls, exposed services, and weak encryption. For each category, they compared how many accounts had at least one issue in it across the three providers.

Weak IAM controls and missing logging are near-universal, affecting between 80% and 98% of accounts regardless of provider. The other four categories are where things diverge:

* Exposed services: AWS **(76%)**, Azure **(64%)**, Google Cloud **(8%)**
* Permissive firewalls: AWS **(83%)**, Azure **(45%)**, Google Cloud **(34%)**
* Weak encryption: AWS **(49%)**, Azure **(35%)**, Google Cloud **(8%)**
* Misconfigured services: AWS **(68%)**, Azure **(80%)**, Google Cloud **(37%)**

The biggest gap is exposed services, at 76% on AWS versus 8% on Google Cloud. Permissive firewalls and weak encryption follow the same pattern with AWS highest and Google Cloud lowest. Misconfigured services is the exception to that pattern: Azure leads at 80%, with Google Cloud lowest at 37%.

One explanation for AWS leading in prevalence across five of the six categories is that it's the largest provider by range of services. More services means more configuration options, and more opportunity for misconfiguration.

Google Cloud has the lowest prevalence across five categories - it also offers the fewest services. The lower prevalence could also be explained by the different approach to shared responsibility, with a Shared Fate model that ships more secure defaults out of the box - particularly around network exposure and encryption.

Here's what those categories look like as actual misconfigurations on each platform.

### AWS: firewalls and encryption

Where AWS accounts go wrong most often:

1. S3 Does Not Enforce HTTPS — **87%**
2. Permissive Ingress to Sensitive Ports (via ACL) — **84%**
3. Overly Permissive Network ACL — **83%**
4. IAM Policy Allows Privilege Escalation — **83%**
5. VPC Endpoint Not Enabled for EC2 — **82%**

S3 buckets that don't enforce HTTPS is the issue that affects most AWS accounts. S3 is one of the most widely used cloud storage services, and while man-in-the-middle attacks against it are rare, there's little reason to leave plain HTTP available.

IAM policies that allow privilege escalation affect 83% of accounts. AWS IAM is notoriously complex, and a managed policy that looks safe can still grant broader permissions than intended. [In one recent incident](https://www.sysdig.com/blog/ai-assisted-cloud-intrusion-achieves-admin-access-in-8-minutes), an attacker went from exposed credentials to administrative privileges in under 10 minutes, compromising 19 AWS principals.

### Azure: storage and identity

The most common misconfigurations on Azure accounts:

1. Storage Account Key Rotation Not Enabled — **67%**
2. Storage Account Access Keys Enabled — **66%**
3. Storage Account Public Network Access Enabled — **61%**
4. Entra User Without MFA — **55%**
5. Trusted Launch Not Enabled — **45%**

The top three issues all relate to Azure Storage Accounts, which frequently hold sensitive data like personally identifiable information (PII). All three affect a similar share of accounts, which suggests that where storage accounts aren't hardened, several controls tend to be missing at once.

More than half of accounts also have Entra ID users without multi-factor authentication (MFA). That's worth noting because Entra ID governs access beyond just cloud resources - it covers Microsoft 365, third-party SaaS apps, and on-premises systems. The 2024 Midnight Blizzard breach of Microsoft's own network began with a password spray attack against a legacy test account without MFA.

### Google Cloud: IAM

Almost every top issue on Google Cloud comes down to identity and access management:

1. OS Login MFA Not Enabled — **77%**
2. OS Login Not Enabled — **76%**
3. Unused Service Account — **75%**
4. Overly Permissive Service Account — **53%**
5. Permissive Ingress to Sensitive Ports — **34%**

More than three-quarters of accounts are missing OS Login controls, which provide a more secure alternative to traditional SSH.

## How organization size changes the picture

For most categories, prevalence drops as organizations grow. Larger enterprises are less likely to have permissive firewalls, exposed services, or weak encryption.

The exception is IAM. Weak IAM controls affect 87% of SMEs (under 250 employees), 95% of midmarket organizations (251–10K employees), and 98% of large enterprises (10K-100K+ employees). This is significant as a single overprivileged identity is often all it takes to bypass controls that have been hardened elsewhere.

Midmarket organizations also take the longest to remediate cloud issues, at 35 days on average, compared to 8-16 for smaller businesses and 10 for large enterprises. It suggests midmarket tea...
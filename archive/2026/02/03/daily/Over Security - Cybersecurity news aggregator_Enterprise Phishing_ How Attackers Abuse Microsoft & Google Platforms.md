---
title: Enterprise Phishing: How Attackers Abuse Microsoft & Google Platforms
url: https://any.run/cybersecurity-blog/enterprise-phishing-analysis/
source: Over Security - Cybersecurity news aggregator
date: 2026-02-03
fetch_date: 2026-02-04T04:08:04.879475
---

# Enterprise Phishing: How Attackers Abuse Microsoft & Google Platforms

[![ANY.RUN's Cybersecurity Blog](/cybersecurity-blog/wp-content/uploads/2025/11/Logo-Blog_Header_238х46.svg)](/cybersecurity-blog/)

* [Register for free](https://app.any.run/#register)
* [Guides and tutorials](/cybersecurity-blog/guides/)
* [Research](/cybersecurity-blog/research/)
* Featured posts
  + [Malware Analysis in ANY.RUN:
    The Ultimate Guide](/cybersecurity-blog/malware-analysis-in-a-sandbox/)
  + [Salty2FA & Tycoon2FA Hybrid: A New Phishing Threat](/cybersecurity-blog/salty2fa-tycoon2fa-hybrid-phishing-2025/)
  + [How to Get Free Malware Samples and Reports](/cybersecurity-blog/free-malware-samples-reports/)
* Categories
  + [Analyst Training](/cybersecurity-blog/category/training/)
  + [Cybersecurity Lifehacks](/cybersecurity-blog/category/lifehacks/)
  + [Instructions on ANY.RUN](/cybersecurity-blog/category/instructions/)
  + [Interviews](/cybersecurity-blog/category/interviews/)
  + [Malicious History](/cybersecurity-blog/category/history/)
  + [Malware Analysis](/cybersecurity-blog/category/malware-analysis/)
  + [News](/cybersecurity-blog/category/news/)
  + [Service Updates](/cybersecurity-blog/category/service-updates/)
* [Write for us](/cybersecurity-blog/write-for-us/)
* [Go to service](https://app.any.run/)
* [Register for free](https://app.any.run/#register)

* + Search

[![ANY.RUN's Cybersecurity Blog](/cybersecurity-blog/wp-content/uploads/2025/11/Logo-Blog_Header_238х46.svg)](/cybersecurity-blog/)

* [Register for free](https://app.any.run/#register)
* [Guides and tutorials](/cybersecurity-blog/guides/)
* [Research](/cybersecurity-blog/research/)
* Featured posts
  + [Malware Analysis in ANY.RUN:
    The Ultimate Guide](/cybersecurity-blog/malware-analysis-in-a-sandbox/)
  + [Salty2FA & Tycoon2FA Hybrid: A New Phishing Threat](/cybersecurity-blog/salty2fa-tycoon2fa-hybrid-phishing-2025/)
  + [How to Get Free Malware Samples and Reports](/cybersecurity-blog/free-malware-samples-reports/)
* Categories
  + [Analyst Training](/cybersecurity-blog/category/training/)
  + [Cybersecurity Lifehacks](/cybersecurity-blog/category/lifehacks/)
  + [Instructions on ANY.RUN](/cybersecurity-blog/category/instructions/)
  + [Interviews](/cybersecurity-blog/category/interviews/)
  + [Malicious History](/cybersecurity-blog/category/history/)
  + [Malware Analysis](/cybersecurity-blog/category/malware-analysis/)
  + [News](/cybersecurity-blog/category/news/)
  + [Service Updates](/cybersecurity-blog/category/service-updates/)
* [Write for us](/cybersecurity-blog/write-for-us/)
* [Go to service](https://app.any.run/)
* [Register for free](https://app.any.run/#register)

* + Search

[![ANY.RUN's Cybersecurity Blog](/cybersecurity-blog/wp-content/uploads/2025/11/Logo-Blog_Header_238х46.svg)](/cybersecurity-blog/)

* + Search

![Enterprise Phishing: How Attackers Abuse Trusted Microsoft & Google Platforms ](/cybersecurity-blog/wp-content/uploads/2026/02/cover.png)

[Malware Analysis](/cybersecurity-blog/category/malware-analysis/)

# Enterprise Phishing: How Attackers Abuse Trusted Microsoft & Google Platforms

February 3, 2026

[Add comment](#comments-18224)
1139 views
8 min read

[Home](/cybersecurity-blog/)[Malware Analysis](/cybersecurity-blog/category/malware-analysis/)

Enterprise Phishing: How Attackers Abuse Trusted Microsoft & Google Platforms

#### Recent posts

* [![](/cybersecurity-blog/wp-content/uploads/2026/02/cover-1024x497.png)

  #### Enterprise Phishing: How Attackers Abuse Trusted Microsoft & Google Platforms

  1139
  0](/cybersecurity-blog/enterprise-phishing-analysis/)
* [![](/cybersecurity-blog/wp-content/uploads/2026/01/SOC-Business-Success-with-ANY.RUN_-1024x497.png)

  #### SOC & Business Success with ANY.RUN: Real-World Results & Cases

  2459
  0](/cybersecurity-blog/soc-business-success-cases-anyrun/)
* [![](/cybersecurity-blog/wp-content/uploads/2026/01/Enterprise-email-thread-phishing-1024x497.png)

  #### Attackers Are Taking Over Real Email Threads to Deliver Phishing: New Enterprise Risk

  5696
  0](/cybersecurity-blog/enterprise-email-thread-phishing/)

[Home](/cybersecurity-blog/)[Malware Analysis](/cybersecurity-blog/category/malware-analysis/)

Enterprise Phishing: How Attackers Abuse Trusted Microsoft & Google Platforms

[ANY.RUN](https://any.run/?utm_source=anyrunblog&utm_medium=article&utm_campaign=enterprise_phishing_analysis%20&utm_term=030226&utm_content=linktolanding) observes a growing trend of phishing kit infrastructure being hosted on legitimate cloud and CDN platforms, rather than on newly registered domains. These campaigns often target enterprise users specifically, creating a global threat to businesses. The shift creates serious visibility [challenges for security teams](https://any.run/cybersecurity-blog/solving-soc-challenges-with-ti/), as trusted platforms and valid indicators shield malicious activity from detection.

For a deeper dive, read on and see the breakdown of such cases, along with tips on what works and what doesn’t.

## Key Takeaways

* Modern phishing campaigns increasingly rely on**trusted cloud infrastructure**, not disposable domains.

* AiTM [phishing kits](https://any.run/cybersecurity-blog/phishkit-attacks-101/) dominate **enterprise-targeted attacks**.

* Cloudflare, Microsoft Azure, Google Firebase, and AWS are frequently abused.

* Traditional IOCs like IPs, TLS fingerprints, and certificates are becoming **unreliable**.

* [**Continuous threat intelligence**](https://any.run/cybersecurity-blog/threat-intel-board-cases/) and **behavioral analysis** are critical for detection.

## Enterprises Under Fire: AITM kits and Cloudflare Abuse

The most widespread and dangerous phishing campaigns today are powered by AiTM (Adversary-in-the-middle kits). These toolsets help unfold phishing attacks where threat actors become a proxy between the victim and a legitimate service.

* Follow ANY.RUN’s team on [LinkedIn](https://www.linkedin.com/company/any-run/) and [X](https://x.com/anyrun_app) to get weekly updates on the most widespread phishing kits

![](/cybersecurity-blog/wp-content/uploads/2026/02/image3-9-2048x1132-1-1024x566.png)

A typical phishkit attack starts with an email containing a link (including in the form of a QR code) leading to attackers’ infrastructure. Most campaigns also involve a CAPTCHA challenge and a string of redirects as a means to avoid detection by AVs and static systems.Advanced evasion leads to a high rate of missed attacks for organizations that suffer from data theft as a result of this.

![](/cybersecurity-blog/wp-content/uploads/2026/02/image18-1024x573.png)

[ANY.RUN’s Interactive Sandbox](https://any.run/features/?utm_source=anyrunblog&utm_medium=article&utm_campaign=enterprise_phishing_analysis%20&utm_term=030226&utm_content=linktosandboxlanding) provides security teams with the capabilities to quickly detect phishkit attacks thanks to interactive analysis. In addition to static detection, the sandbox lets SOC analysts safely follow the entire attack chain in an isolated VM and go past all the evasion layers to reveal the final malicious credential theft page or payload.

The result for businesses that have adopted ANY.RUN’s solutions in their infrastructure is a lower risk of a data breach and a more effective SOC team that can quickly identify phishing attempts with a high degree of certainty.

Faster decisions and lower workload:
Cut investigation time in half with ANY.RUN

[Integrate in your SOC](https://any.run/enterprise/?utm_source=anyrunblog&utm_medium=article&utm_campaign=enterprise_phishing_analysis&utm_term=030226&utm_content=linktoenterprise#contact-sales)

The top three most active phishing kits remain stable quarter to quarter. The list features:

* [Tycoon2FA](https://any.run/malware-trends/tycoon/): Phishing-as-a-service (PhaaS) platform designed to bypass multi-factor authentication (MFA).

* [Sneaky2FA](https://any.run/malware-trends/sneaky2fa/): Adversary-in-the-Middle (AiTM) threat used in Business Email Compromise (...
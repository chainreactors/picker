---
title: BlobPhish: The Phantom Phishing Campaign Hiding in Browser Memory
url: https://any.run/cybersecurity-blog/evasive-blob-phishing-detection/
source: Over Security - Cybersecurity news aggregator
date: 2026-04-16
fetch_date: 2026-04-17T04:50:51.376637
---

# BlobPhish: The Phantom Phishing Campaign Hiding in Browser Memory

[![ANY.RUN's Cybersecurity Blog](https://any.run/cybersecurity-blog/wp-content/uploads/2026/02/anyrun-logo.svg)](https://any.run)
/
[BLOG](https://any.run/cybersecurity-blog/)

* [Guides and tutorials](https://any.run/cybersecurity-blog/guides/)
* [Research](https://any.run/cybersecurity-blog/research/)
* Categories
  + [Analyst Training](https://any.run/cybersecurity-blog/category/training/)
  + [Cybersecurity Lifehacks](https://any.run/cybersecurity-blog/category/lifehacks/)
  + [Instructions on ANY.RUN](https://any.run/cybersecurity-blog/category/instructions/)
  + [Interviews](https://any.run/cybersecurity-blog/category/interviews/)
  + [Malicious History](https://any.run/cybersecurity-blog/category/history/)
  + [Malware Analysis](https://any.run/cybersecurity-blog/category/malware-analysis/)
  + [News](https://any.run/cybersecurity-blog/category/news/)
  + [Service Updates](https://any.run/cybersecurity-blog/category/service-updates/)
* [Write for us](https://any.run/cybersecurity-blog/write-for-us/)
* [Go to service](https://app.any.run/)
* [Register for free](https://app.any.run/#register)
* [Register for free](https://app.any.run/#register)

* + Search

[![ANY.RUN's Cybersecurity Blog](https://any.run/cybersecurity-blog/wp-content/uploads/2026/02/anyrun-logo.svg)](https://any.run)
/
[BLOG](https://any.run/cybersecurity-blog/)

* [Guides and tutorials](https://any.run/cybersecurity-blog/guides/)
* [Research](https://any.run/cybersecurity-blog/research/)
* Categories
  + [Analyst Training](https://any.run/cybersecurity-blog/category/training/)
  + [Cybersecurity Lifehacks](https://any.run/cybersecurity-blog/category/lifehacks/)
  + [Instructions on ANY.RUN](https://any.run/cybersecurity-blog/category/instructions/)
  + [Interviews](https://any.run/cybersecurity-blog/category/interviews/)
  + [Malicious History](https://any.run/cybersecurity-blog/category/history/)
  + [Malware Analysis](https://any.run/cybersecurity-blog/category/malware-analysis/)
  + [News](https://any.run/cybersecurity-blog/category/news/)
  + [Service Updates](https://any.run/cybersecurity-blog/category/service-updates/)
* [Write for us](https://any.run/cybersecurity-blog/write-for-us/)
* [Go to service](https://app.any.run/)
* [Register for free](https://app.any.run/#register)
* [Register for free](https://app.any.run/#register)

* + Search

[![ANY.RUN's Cybersecurity Blog](https://any.run/cybersecurity-blog/wp-content/uploads/2026/02/anyrun-logo.svg)](https://any.run)
/
[BLOG](https://any.run/cybersecurity-blog/)

* + Search

![BlobPhish: The Phantom Phishing Campaign Hiding in Browser Memory](https://any.run/cybersecurity-blog/wp-content/uploads/2026/04/BlobPhish-Campaign-2.png)

[Malware Analysis](https://any.run/cybersecurity-blog/category/malware-analysis/)

# BlobPhish: The Phantom Phishing Campaign Hiding in Browser Memory

April 16, 2026

[Add comment](#comments-20074)
1775 views
11 min read

[Home](https://any.run/cybersecurity-blog/)[Malware Analysis](https://any.run/cybersecurity-blog/category/malware-analysis/)

BlobPhish: The Phantom Phishing Campaign Hiding in Browser Memory

#### Recent posts

* [![](https://any.run/cybersecurity-blog/wp-content/uploads/2026/04/BlobPhish-Campaign-2-1024x497.png)

  #### BlobPhish: The Phantom Phishing Campaign Hiding in Browser Memory

  1775
  0](https://any.run/cybersecurity-blog/evasive-blob-phishing-detection/)
* [![](https://any.run/cybersecurity-blog/wp-content/uploads/2026/04/chile_blog_cover-1024x497.png)

  #### Chile’s Cybersecurity Framework Law: How SOCs Achieve Compliance and Response Readiness

  2232
  0](https://any.run/cybersecurity-blog/chile-cybersecurity-framework-law/)
* [![](https://any.run/cybersecurity-blog/wp-content/uploads/2026/04/Google-Storage-1-1024x497.png)

  #### When Trust Becomes a Weapon: Google Cloud Storage Phishing Deploying Remcos RAT

  4733
  0](https://any.run/cybersecurity-blog/phishing-google-drive-remcos/)

[Home](https://any.run/cybersecurity-blog/)[Malware Analysis](https://any.run/cybersecurity-blog/category/malware-analysis/)

BlobPhish: The Phantom Phishing Campaign Hiding in Browser Memory

ANY.RUN has observed a sustained surge in a credential-phishing campaign active since 2024. This campaign, dubbed BlobPhish, introduces a sneaky twist: instead of delivering phishing pages via traditional HTTP requests, it **generates them directly inside the victim’s browser using blob objects**. The result is a phishing payload that lives entirely in memory, leaving little to no trace in logs, caches, or network telemetry.

The campaign **targets credentials** across multiple platforms, including Microsoft 365, banking services, and webmail portals, making it both widespread and high-impact.

## Key Takeaways

* **Memory-resident evasion**: BlobPhish loads entire phishing pages as in-browser blob objects, bypassing file-based and network-based detection entirely.

* **Broad targeting:** The campaign hits Microsoft 365 alongside major U.S. banks (Chase, Capital One, FDIC, E\*TRADE, Schwab) and webmail services.

* **Persistent and active**: First observed in October 2024, the operation continues uninterrupted as of April 2026 with a major spike in February 2026.

* **Compromised infrastructure:** Attackers routinely abuse legitimate WordPress sites and reuse exfiltration endpoints (res.php, tele.php, panel.php).

* **High-value credential theft**: Stolen accounts enable BEC, data exfiltration, and lateral movement — threats that carry multimillion-dollar consequences.

* **Global but finance-focused:** One-third of victims are in the U.S.; phishing pages almost exclusively mimic premium financial and Microsoft services regardless of victim industry.

* [**ANY.RUN delivers proactive defense**](https://any.run/enterprise/?utm_source=anyrunblog&utm_medium=article&utm_campaign=evasive-blob-phishing-detection&utm_term=160426&utm_content=linktoenterprise)**:** Sandbox instantly reveals blob behavior in real browsers, while TI Lookup and TI Feeds provide real-time IOCs and YARA rules for automated blocking and hunting, turning reactive security into prevention.

## How BlobPhish works

The attack is based on the abuse of browser Blob objects to serve fake authentication forms. A JavaScript loader, fetched from an attacker-controlled page, constructs a Blob from a Base64-encoded payload and loads it directly into browser memory — never touching disk and never generating the traditional HTTP requests that security tools rely on to detect phishing.

![](https://any.run/cybersecurity-blog/wp-content/uploads/2026/04/blob_1-1024x489.png)

Targeted services include: Microsoft 365, OneDrive, SharePoint, Chase, FDIC, Capital One, E\*Trade, American Express, Charles Schwab, Merrill Lynch, PayPal, Intuit, and others.

Accelerate investigations and stop threats earlier.
Leverage sandbox visibility to improve SOC performance.

[Register now](https://app.any.run/?utm_source=anyrunblog&utm_medium=article&utm_campaign=evasive-blob-phishing-detection&utm_term=160426&utm_content=linktoregistration#register)

## Technical Deep Dive

Because the phishing page exists only in memory and is referenced by the scheme *blob:https://*, it cannot be blocked by URL reputation engines, does not appear in proxy logs as a suspicious request, and leaves no cache artefact. This makes BlobPhish significantly harder to detect and investigate than conventional phishing.

[View the observed analysis session in ANY.RUN sandbox](https://app.any.run/tasks/191b74fc-fb9f-455a-9492-ca872871d0e1/?utm_source=anyrunblog&utm_medium=article&utm_campaign=evasive-blob-phishing-detection&utm_term=160426&utm_content=linktoservice)

![](https://any.run/cybersecurity-blog/wp-content/uploads/2026/04/blob_2-1024x482.png)

### 1. Delivery Vector

The typical initial access point is a phishing email or a link to a trusted-looking service such as DocSend. Example phishing link: hxxps[://]docsend[.]com/view/vsrrknxprh2xt84n

Upon clicking, the victim...
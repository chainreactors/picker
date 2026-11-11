---
title: Formbook Targets European Manufacturing and Technology Businesses with Localized Order Lures
url: https://any.run/cybersecurity-blog/formbook-malware-analysis-november-2026/
source: Over Security
date: 2026-11-10
fetch_date: 2026-11-11T08:35:16.394307
---

# Formbook Targets European Manufacturing and Technology Businesses with Localized Order Lures

[![ANY.RUN's Cybersecurity Blog](https://any.run/cybersecurity-blog/wp-content/uploads/2026/02/anyrun-logo.svg)](https://any.run)
/
[BLOG](https://any.run/cybersecurity-blog/)

* [Guides and tutorials](https://any.run/cybersecurity-blog/guides/)
* [Research](https://any.run/cybersecurity-blog/research/)
* Categories
  + [Malware Analysis](https://any.run/cybersecurity-blog/category/malware-analysis/)
  + [SOC & MSSP Strategy](https://any.run/cybersecurity-blog/category/soc-mssp-strategy/)
  + [Customer Success Story](https://any.run/cybersecurity-blog/category/customer-success/)
  + [Service Updates](https://any.run/cybersecurity-blog/category/service-updates/)
  + [Instructions on ANY.RUN](https://any.run/cybersecurity-blog/category/instructions/)
  + [Cybersecurity Lifehacks](https://any.run/cybersecurity-blog/category/lifehacks/)
  + [News](https://any.run/cybersecurity-blog/category/news/)
* [Write for us](https://any.run/cybersecurity-blog/write-for-us/)
* [Go to service](https://app.any.run/)
* [Register for free](https://app.any.run/?register)
* [Register for free](https://app.any.run/?register)

* + Search

[![ANY.RUN's Cybersecurity Blog](https://any.run/cybersecurity-blog/wp-content/uploads/2026/02/anyrun-logo.svg)](https://any.run)
/
[BLOG](https://any.run/cybersecurity-blog/)

* [Guides and tutorials](https://any.run/cybersecurity-blog/guides/)
* [Research](https://any.run/cybersecurity-blog/research/)
* Categories
  + [Malware Analysis](https://any.run/cybersecurity-blog/category/malware-analysis/)
  + [SOC & MSSP Strategy](https://any.run/cybersecurity-blog/category/soc-mssp-strategy/)
  + [Customer Success Story](https://any.run/cybersecurity-blog/category/customer-success/)
  + [Service Updates](https://any.run/cybersecurity-blog/category/service-updates/)
  + [Instructions on ANY.RUN](https://any.run/cybersecurity-blog/category/instructions/)
  + [Cybersecurity Lifehacks](https://any.run/cybersecurity-blog/category/lifehacks/)
  + [News](https://any.run/cybersecurity-blog/category/news/)
* [Write for us](https://any.run/cybersecurity-blog/write-for-us/)
* [Go to service](https://app.any.run/)
* [Register for free](https://app.any.run/?register)
* [Register for free](https://app.any.run/?register)

* + Search

[![ANY.RUN's Cybersecurity Blog](https://any.run/cybersecurity-blog/wp-content/uploads/2026/02/anyrun-logo.svg)](https://any.run)
/
[BLOG](https://any.run/cybersecurity-blog/)

* + Search

![Formbook Targets European Manufacturing and Technology Businesses with Localized Order Lures](https://any.run/cybersecurity-blog/wp-content/uploads/2026/11/Formbook-scaled.png)

[Malware Analysis](https://any.run/cybersecurity-blog/category/malware-analysis/)

# Formbook Targets European Manufacturing and Technology Businesses with Localized Order Lures

November 10, 2026

[Add comment](#comments-24250)
2197 views
13 min read

[Home](https://any.run/cybersecurity-blog/)[Malware Analysis](https://any.run/cybersecurity-blog/category/malware-analysis/)

Formbook Targets European Manufacturing and Technology Businesses with Localized Order Lures

#### Recent posts

* [![](https://any.run/cybersecurity-blog/wp-content/uploads/2026/11/Formbook-1024x497.png)

  #### Formbook Targets European Manufacturing and Technology Businesses with Localized Order Lures

  2197
  0](https://any.run/cybersecurity-blog/formbook-malware-analysis-november-2026/)
* [![](https://any.run/cybersecurity-blog/wp-content/uploads/2026/11/First_Hand_Threat_Intelligence-1024x497.png)

  #### Your Threat Intelligence Stack Has Blind Spots. Here's How to Close Them

  9712
  0](https://any.run/cybersecurity-blog/how-to-close-threat-intelligence-stack-blind-spots/)
* [![](https://any.run/cybersecurity-blog/wp-content/uploads/2026/11/Major_Cyber-Attacks_in_October_2026-1024x497.png)

  #### Major Cyber Attacks in October 2026: Fake AI, Account Takeovers, and Remote Access Threaten US and EU

  20797
  0](https://any.run/cybersecurity-blog/major-cyber-attacks-october-2026/)

[Home](https://any.run/cybersecurity-blog/)[Malware Analysis](https://any.run/cybersecurity-blog/category/malware-analysis/)

Formbook Targets European Manufacturing and Technology Businesses with Localized Order Lures

European businesses, particularly in the UK and Italy, face malware campaigns that exploit routine business correspondence. A recent **Formbook (now also known as XLoader) campaign** uses localized order and procurement lures to deliver an information stealer.

Manufacturing and technology companies are especially exposed because employees regularly handle purchase orders, supplier documents, and payment requests. A seemingly routine attachment can hide a JavaScript loader that ultimately deploys malware to steal browser-stored credentials.

The [ANY.RUN](https://any.run/?utm_source=anyrunblog&utm_medium=article&utm_campaign=formbook-malware-analysis-november-2026&utm_term=101126&utm_content=linktolanding) team investigated the campaign, uncovering its infection chain, persistence methods, and links to other malware activity. These findings show how behavioral analysis and threat intelligence can help organizations strengthen their defenses.

## Key Takeaways

* **Localized order lures target European businesses.** Formbook campaigns use region-specific procurement, purchase order, and payment-related documents to make malicious attachments look like routine business correspondence.

* **The infection chain uses multiple layers of evasion.** Obfuscated JavaScript launches PowerShell stages, which decrypt and execute payloads in memory before deploying a .NET injector.

* **Process hollowing helps conceal the malware.** The injector uses aspnet\_compiler.exe to run Formbook, while a watchdog monitors the process and can reinject the payload.

* **The malware establishes persistence and steals browser data.** It creates scheduled startup mechanisms and targets browser databases to collect stored credentials.

* **C2 traffic contains useful detection clues.** HTTP communication, suspicious domains, and an Android User-Agent sent from a Windows host can help identify the activity.

* **ANY.RUN’s powerful new capability,** [**Related Threat Context**](https://any.run/cybersecurity-blog/related-threat-context-release/)**, reveals connections beyond the initial sample.** Correlating shared scripts, persistence artifacts, injection components, and C2 infrastructure helps uncover related malware activity and broaden the investigation.

## Why Formbook Is a Risk for European Organizations

The Formbook campaign relies on a familiar social engineering approach: making malicious attachments look like documents employees would normally receive as part of their work.

![](https://any.run/cybersecurity-blog/wp-content/uploads/2026/11/Formbook_info-819x1024.png)

*The Formbook attack overview*

One of the analyzed archives, **Nova narudžba 0148-712.zip**, contains a JavaScript file with a Croatian/Bosnian title meaning “New Order”. Other related samples use themes involving price lists, procurement requests, quotations, and bank transfers.

These lures reflect everyday business processes:

* **Manufacturing:** Purchase orders, supplier requests, and delivery documents are part of daily workflows. Malicious attachments can reach procurement, finance, or supply chain teams and infect corporate workstations.

* **Technology:** Vendor correspondence, equipment purchases, and commercial agreements provide convincing cover for malicious files. Compromised accounts could expose internal services, customer data, and technical documents accessible to the affected users.

* **Finance and administration:** Payment requests and SWIFT-themed attachments can trick employees who handle transactions and financial correspondence into opening malicious files.

The analyzed activity included submissions from the UK and Italy, alongside countries in the Balkans and South Caucasus. The language and themes of the lures indicate ...
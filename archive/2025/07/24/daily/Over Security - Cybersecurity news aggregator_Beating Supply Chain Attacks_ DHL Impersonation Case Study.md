---
title: Beating Supply Chain Attacks: DHL Impersonation Case Study
url: https://any.run/cybersecurity-blog/supply-chain-attacks-analysis/
source: Over Security - Cybersecurity news aggregator
date: 2025-07-24
fetch_date: 2025-10-06T23:54:15.321858
---

# Beating Supply Chain Attacks: DHL Impersonation Case Study

[![ANY.RUN's Cybersecurity Blog](/cybersecurity-blog/wp-content/uploads/2020/07/Logo-1.png)](/cybersecurity-blog/)

* [Register for free](https://app.any.run/#register)
* [Guides and Tutorials](/cybersecurity-blog/guides/)
* [Research](/cybersecurity-blog/research/)
* Featured posts
  + [Malware Analysis in ANY.RUN:
    The Ultimate Guide](/cybersecurity-blog/malware-analysis-in-a-sandbox/)
  + [Raccoon Stealer 2.0 Malware analysis](/cybersecurity-blog/raccoon-stealer-v2-malware-analysis/)
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

[![ANY.RUN's Cybersecurity Blog](/cybersecurity-blog/wp-content/uploads/2020/07/Logo-1.png)](/cybersecurity-blog/)

* [Register for free](https://app.any.run/#register)
* [Guides and Tutorials](/cybersecurity-blog/guides/)
* [Research](/cybersecurity-blog/research/)
* Featured posts
  + [Malware Analysis in ANY.RUN:
    The Ultimate Guide](/cybersecurity-blog/malware-analysis-in-a-sandbox/)
  + [Raccoon Stealer 2.0 Malware analysis](/cybersecurity-blog/raccoon-stealer-v2-malware-analysis/)
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

[![ANY.RUN's Cybersecurity Blog](/cybersecurity-blog/wp-content/uploads/2022/10/mini-logo.png)](/cybersecurity-blog/)

* + Search

![Beating Supply Chain Attacks: DHL Impersonation Case Study  ](/cybersecurity-blog/wp-content/uploads/2025/07/supply_blog.jpg)

[Malware Analysis](/cybersecurity-blog/category/malware-analysis/)

# Beating Supply Chain Attacks: DHL Impersonation Case Study

July 23, 2025

[Add comment](#comments-14953)
2361 views
11 min read

[Home](/cybersecurity-blog/)[Malware Analysis](/cybersecurity-blog/category/malware-analysis/)

Beating Supply Chain Attacks: DHL Impersonation Case Study

#### Recent posts

* [![](/cybersecurity-blog/wp-content/uploads/2025/09/Release-notes-1024x497.png)

  #### Release Notes: Palo Alto Networks, Microsoft, IBM Connectors and 2,300+ Suricata Rules

  1763
  0](/cybersecurity-blog/release-notes-september-2025/)
* [![](/cybersecurity-blog/wp-content/uploads/2025/10/FunkLocker_blog-1024x497.jpg)

  #### FunkSec’s FunkLocker: How AI Is Powering the Next Wave of Ransomware

  3178
  0](/cybersecurity-blog/funklocker-malware-analysis/)
* [![](/cybersecurity-blog/wp-content/uploads/2025/09/defender_blog-1024x497.jpg)

  #### ANY.RUN & MS Defender: Enrich Alerts Faster, Stop Attacks Early

  3267
  0](/cybersecurity-blog/ms-defender-connectors/)

[Home](/cybersecurity-blog/)[Malware Analysis](/cybersecurity-blog/category/malware-analysis/)

Beating Supply Chain Attacks: DHL Impersonation Case Study

[ANY.RUN’s services](http://any.run/?utm_source=anyrunblog&utm_medium=article&utm_campaign=supply_chain_attacks&utm_term=230725&utm_content=linktolanding) processes data on current threats daily, including attacks affecting supply chains. In this case study, we analyze examples of DHL brand abuse. The company is a leading global [logistic](https://any.run/cybersecurity-blog/how-transport-company-monitors-threats/) operator, and attackers exploit its recognition to send phishing emails, potentially targeting its partners.

We will demonstrate how ANY.RUN’s solutions can be used to identify such threats, collect technical indicators, and enhance security. Here are the key findings.

## Key Takeaways

* **Supply chain attacks are on the rise:** adversaries actively exploitthird-party relationships.

* **Real-world example**: attackers impersonated DHL in phishing emails targeting partner organizations, like Meralco, using fake domains and deceptive attachments to collect credentials.

* **HTML attachment bypasses filters:** lesser-known file extensions are used.

* **Credential theft via third-party form service:** analysis with HTTPS MITM revealed a POST request containing plaintext credentials sent to a unique endpoint.

* **Shared visual lures identified by image hash:** the DHL-themed image in the phishing email was reverse-searched via its SHA256 hash, revealing five other phishing campaigns using the same lure.

* **DHL-imitating domains and filenames as indicators:** analysts identified 39 phishing domains (e.g., dhlshipment\*, -dhl.) and over 300 malware samples with DHL-themed filenames (e.g., dhlreceipt\*.pdf) — exposing common obfuscation patterns and phishing themes used to trick users.

## Supply Chain Attack Growing Dynamics

A supply chain attack is a type of cyberattack where adversaries gain access to a target organization by compromising a less protected external participant in the interaction chain: a contractor, a supplier, a technology partner, or another link.

The [data from Cyble](https://cyble.com/blog/supply-chain-attacks-surge-in-april-may-2025) reveals supply chain attacks steady growth. From October 2024 to May 2025, an average of more than 16 incidents per month has been recorded, a 25% increase from the previous eight-month period. A sharp spike in activity was observed in April and May 2025. This dynamic indicates growing attacker interest in this attack model and its increasingly widespread use in real campaigns.

![](/cybersecurity-blog/wp-content/uploads/2025/07/image-12.png)

Real-world examples include the Scattered Spider group’s [attack](https://supplychaindigital.com/news/inside-the-cyberattack-that-hit-six-million-qantas-customers) on Australian airline Qantas. The attackers penetrated through a third party (contact center), which is typical for such attacks.

## DHL Brand Abuse in Phishing Campaigns

Suppose we are information security specialists at a company that collaborates with DHL and could be used by attackers as an intermediate link in the attack chain.

Our task is to detect timely phishing emails disguised as official correspondence from DHL. Such messages may target company employees, contractors, or other DHL partners.

To identify such activity, we use YARA Search inside ANY.RUN’s [Threat Intelligence Lookup](https://intelligence.any.run/analysis/lookup/?utm_source=anyrunblog&utm_medium=article&utm_campaign=supply_chain_attacks&utm_term=230725&utm_content=linktotilookup) — we’ll create a rule that allows us to find *.eml* files mentioning DHL in the From, To, and Subject headers. This will help collect indicators, identify malicious attachments, and assess potential risks to our infrastructure.

![](/cybersecurity-blog/wp-content/uploads/2025/07/image2-6-1024x596.png)

The search delivered over 110 files and associated analysis sessions (tasks) from the ANY.RUN’s [Interactive Sandbox](https://any.run/features/?utm_source=anyrunblog&utm_med...
---
title: Manufacturing Companies Targeted with New Lumma and Amadey Campaign
url: https://any.run/cybersecurity-blog/manufacturing-companies-targeted-with-lumma/
source: Over Security - Cybersecurity news aggregator
date: 2024-12-11
fetch_date: 2025-10-06T19:58:51.229680
---

# Manufacturing Companies Targeted with New Lumma and Amadey Campaign

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

![Manufacturing Companies Targeted with New Lumma and Amadey Campaign](/cybersecurity-blog/wp-content/uploads/2024/12/manufacturing_blog.jpg)

[News](/cybersecurity-blog/category/news/)

# Manufacturing Companies Targeted with New Lumma and Amadey Campaign

December 10, 2024

[Add comment](#comments-10278)
4047 views
4 min read

[Home](/cybersecurity-blog/)[News](/cybersecurity-blog/category/news/)

Manufacturing Companies Targeted with New Lumma and Amadey Campaign

#### Recent posts

* [![](/cybersecurity-blog/wp-content/uploads/2025/09/Release-notes-1024x497.png)

  #### Release Notes: Palo Alto Networks, Microsoft, IBM Connectors and 2,300+ Suricata Rules

  1421
  0](/cybersecurity-blog/release-notes-september-2025/)
* [![](/cybersecurity-blog/wp-content/uploads/2025/10/FunkLocker_blog-1024x497.jpg)

  #### FunkSec’s FunkLocker: How AI Is Powering the Next Wave of Ransomware

  3032
  0](/cybersecurity-blog/funklocker-malware-analysis/)
* [![](/cybersecurity-blog/wp-content/uploads/2025/09/defender_blog-1024x497.jpg)

  #### ANY.RUN & MS Defender: Enrich Alerts Faster, Stop Attacks Early

  3066
  0](/cybersecurity-blog/ms-defender-connectors/)

[Home](/cybersecurity-blog/)[News](/cybersecurity-blog/category/news/)

Manufacturing Companies Targeted with New Lumma and Amadey Campaign

The manufacturing industry has long been a target of cybercriminals. While data encryption has been a prevalent tactic in recent years, threat actors are now increasingly focusing on stealing sensitive information and gaining control over critical infrastructure.

One of the latest [campaigns](https://cyble.com/blog/threat-actor-targets-manufacturing-industry-with-malware/) on record involves the use of [Lumma](https://any.run/malware-trends/lumma) and [Amadey](https://any.run/malware-trends/amadey) malware.

## Campaign Uses Fake LogicalDOC URLs

This campaign heavily leverages Living Off the Land (LOLBAS) techniques to deliver malware as part of its operations.

Threat actors distribute phishing emails with URLs leading targets to download LNK files disguised as PDFs. These files are accessed via a domain name masquerading as one belonging to LogicalDOC, a service for managing documentation widely utilized in the manufacturing industry.

## Attack Involves Scripts to Aid Infection

The malicious LNK file, once activated, initiates [PowerShell](https://any.run/cybersecurity-blog/powershell-script-tracer/) via an ssh.exe command. Following a chain of scripts, a CPL file is downloaded from berb[.]fitnessclub-filmfanatics[.]com as a ZIP archive.

The malware utilizes both PowerShell and Windows Management Instrumentation (WMI) commands to collect detailed information about the victim’s system. This includes:

* Data such as language settings
* Antivirus software
* Operating system versions
* Hardware specifications

This reconnaissance allows attackers to tailor subsequent attacks and enhances their credibility when sending follow-up malicious emails within the targeted organization.

## DLL Sideloading Ensures Evasion

Attackers run malicious code in memory without leaving traces and abuse standard Windows tools to blend in with regular system activities. The downloaded ZIP file contains several malicious files used to carry out DLL sideloading.

## Key Objective

The primary purpose of this attack is to:

* Steal important information with Lumma Stealer
* Maintain control over the infected systems with Amadey Bot

Attackers gain the ability to continuously monitor and manipulate their targets, which poses a significant threat to manufacturing businesses.

## Why Businesses Need to Pay Attention

For manufacturing companies, the consequences of such attacks can be severe and include:

* Theft of intellectual property
* Disruption of operations
* Financial losses and compliance violations

Understanding and preparing for these threats is crucial for protecting valuable assets, maintaining operational integrity, and ensuring the safety of employees and customers.

## Analysis of the Attack with ANY.RUN Sandbox

To proactively identify malicious files belonging to this and other malware attacks, analyze them in the safe environment of [ANY.RUN’s Interactive Sandbox](https://any.run/?utm_source=anyrunblog&utm_medium=article&utm_campaign=lumma_targets_manufacturing&utm_term=101224&utm_content=linktolanding) that offers:

* **Real-time Insights:** In-depth view of malicious activities as they occur.
* **Interactivity:** Test threat responses in a live system.
* **Comprehensive Reporting:** Detailed reports on IOCs, malware families, and more.

![](/cybersecurity-blog/wp-content/uploads/2024/12/1image-1024x578.png)

By uploading a malicious LNK file to the sandbox and executing it we can observe how the entire chain of infection plays out.

[View analysis session](https://app.any.run/tasks/11a68474-4e9a-4070-9b23-b8d244c9fc02)

![](/cybersecurity-blog/wp-content/uploads/2024/12/2image.png)

First, the .lnk file initiates SSH, which starts PowerShell.

![](/cybersecurity-blog/wp-content/uploads/2024/12/3image.png)

PowerShell then launches Mshta with the AES-encrypted first-stage payload that it decrypts and executes.

![](/cybersecurity-blog/wp-content/uploads/2024/12/4image.png)

PowerShell executes an AES-encrypted command ...
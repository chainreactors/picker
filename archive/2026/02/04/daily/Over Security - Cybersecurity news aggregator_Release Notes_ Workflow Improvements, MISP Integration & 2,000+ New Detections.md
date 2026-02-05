---
title: Release Notes: Workflow Improvements, MISP Integration & 2,000+ New Detections
url: https://any.run/cybersecurity-blog/release-notes-january-2026/
source: Over Security - Cybersecurity news aggregator
date: 2026-02-04
fetch_date: 2026-02-05T04:10:08.027265
---

# Release Notes: Workflow Improvements, MISP Integration & 2,000+ New Detections

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

![Release Notes: Workflow Improvements, MISP Integration & 2,000+ New Detections ](/cybersecurity-blog/wp-content/uploads/2025/11/Release-notes.png)

[Service Updates](/cybersecurity-blog/category/service-updates/)

# Release Notes: Workflow Improvements, MISP Integration & 2,000+ New Detections

February 4, 2026

[Add comment](#comments-18285)
1029 views
6 min read

[Home](/cybersecurity-blog/)[Service Updates](/cybersecurity-blog/category/service-updates/)

Release Notes: Workflow Improvements, MISP Integration & 2,000+ New Detections

#### Recent posts

* [![](/cybersecurity-blog/wp-content/uploads/2025/11/Release-notes-1024x497.png)

  #### Release Notes: Workflow Improvements, MISP Integration & 2,000+ New Detections

  1029
  0](/cybersecurity-blog/release-notes-january-2026/)
* [![](/cybersecurity-blog/wp-content/uploads/2026/02/cover-1024x497.png)

  #### Enterprise Phishing: How Attackers Abuse Trusted Microsoft & Google Platforms

  2450
  0](/cybersecurity-blog/enterprise-phishing-analysis/)
* [![](/cybersecurity-blog/wp-content/uploads/2026/01/SOC-Business-Success-with-ANY.RUN_-1024x497.png)

  #### SOC & Business Success with ANY.RUN: Real-World Results & Cases

  3044
  0](/cybersecurity-blog/soc-business-success-cases-anyrun/)

[Home](/cybersecurity-blog/)[Service Updates](/cybersecurity-blog/category/service-updates/)

Release Notes: Workflow Improvements, MISP Integration & 2,000+ New Detections

First month of the year, and we’re starting it off with updates that support faster decisions and more predictable SOC operations.

In January, we introduced a major workflow enhancement with the new [ANY.RUN Sandbox](https://any.run/features/?utm_source=anyrunblog&utm_medium=article&utm_campaign=release-notes-january-2026&utm_term=040226&utm_content=linktosandboxlanding) integration with MISP, alongside expanded detection coverage across behavior signatures, YARA rules, and Suricata.

Let’s find out what this means for your team.

## Product Updates

January brought another solid round of improvements focused on practical SOC workflows: faster alert validation, less manual back-and-forth, and earlier decisions that help stop incidents from growing into bigger problems.

The main highlight of the month was the release of the ANY.RUN Sandbox [integration with MISP](https://any.run/cybersecurity-blog/anyrun-sandbox-misp-integration/); an important step for teams that use MISP daily for threat intelligence and investigations.

### ANY.RUN x MISP: Boost Your Triage & Response

Most SOC teams spend too much time validating alerts, moving samples between tools, and filling in missing context. When execution evidence is separated from threat intelligence platforms, investigations slow down, MTTR increases, and SLAs come under pressure.

With the [ANY.RUN Sandbox](https://any.run/features/?utm_source=anyrunblog&utm_medium=article&utm_campaign=release-notes-january-2026&utm_term=040226&utm_content=linktosandboxlanding) integration for MISP, analysts can now **bring real execution behavior directly into MISP**, turning it from a passive intelligence repository into an active investigation layer.

![MISP integration with ANY.RUN Sandbox](/cybersecurity-blog/wp-content/uploads/2026/01/MISP-integration-with-ANY.RUN-Sandbox-1024x580.png)

Using native MISP modules, suspicious files and URLs can be sent straight from MISP into the ANY.RUN Sandbox, without any context switching or manual handoffs.

You can easily integrate the modules, using the following links:

* [**Submit files/URLs for analysis**](https://misp.github.io/misp-modules/expansion/#anyrun-sandbox-submit)

* [**Get analysis reports**](https://misp.github.io/misp-modules/import_mod/#anyrun-sandbox-import)

Analysis runs automatically using [Automated Interactivity](https://any.run/cybersecurity-blog/automated-interactivity-stage-two/).This allows the sandbox to behave like a real user by clicking, opening files, and waiting when needed. This is critical for exposing modern threats that delay execution or hide behind user-driven actions.

![MITRE ATT&CK technique T1082 expanded inside MISP](/cybersecurity-blog/wp-content/uploads/2026/01/MITRE-ATTCK-technique-inside-MISP-1024x580.png)

Once execution completes, results are automatically returned to MISP, including, verdict and risk assessment, [extracted IOCs](https://any.run/cybersecurity-blog/enrich-iocs-with-threat-intelligence/), adirect link to the interactive sandbox session, HTML analysis report, mapped [MITRE ATT&CK techniques](https://any.run/cybersecurity-blog/mitre-attack/) and tactics.

This allows analysts to **validate alerts using real behavior**, not assumptions, directly inside their existing workflow.

Add behavior-based evidence to your MISP

Cut triage time and reduce noise

[Reach out for details](https://any.run/enterprise/?utm_source=anyrunblog&utm_medium=article&utm_campaign=release-notes-january-2026&utm_term=040226&utm_content=linktoenterprise#contact-sales)

#### Benefits for Your SOC and Business

For organizations using MISP as part of daily operations, this integration delivers clear operational gains:

* **Lower incident costs:** Shorter investigations reduce effort per case

* **Redu...
---
title: CastleLoader: A Deep Dive into Stealthy Loader Targeting Government Sector
url: https://any.run/cybersecurity-blog/castleloader-malware-analysis/
source: Over Security - Cybersecurity news aggregator
date: 2026-01-13
fetch_date: 2026-01-14T03:35:56.238204
---

# CastleLoader: A Deep Dive into Stealthy Loader Targeting Government Sector

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

![CastleLoader Analysis: A Deep Dive into Stealthy Loader Targeting Government Sector](/cybersecurity-blog/wp-content/uploads/2026/01/CastleLoader-Analysis.png)

[Malware Analysis](/cybersecurity-blog/category/malware-analysis/)

# CastleLoader Analysis: A Deep Dive into Stealthy Loader Targeting Government Sector

January 13, 2026

[Add comment](#comments-17626)
933 views
16 min read

[Home](/cybersecurity-blog/)[Malware Analysis](/cybersecurity-blog/category/malware-analysis/)

CastleLoader Analysis: A Deep Dive into Stealthy Loader Targeting Government Sector

#### Recent posts

* [![](/cybersecurity-blog/wp-content/uploads/2026/01/CastleLoader-Analysis-1024x497.png)

  #### CastleLoader Analysis: A Deep Dive into Stealthy Loader Targeting Government Sector

  933
  0](/cybersecurity-blog/castleloader-malware-analysis/)
* [![](/cybersecurity-blog/wp-content/uploads/2025/12/soar_sb_blog-1024x497.png)

  #### Integrating a Malware Sandbox into SOAR Workflows: Steps, Benefits, and Impact

  848
  0](/cybersecurity-blog/integrating-sandbox-into-soar-workflows/)
* [![](/cybersecurity-blog/wp-content/uploads/2025/12/mssp_win_blog-1024x497.png)

  #### 5 Ways MSSPs Can Win Clients in 2026

  726
  0](/cybersecurity-blog/how-mssps-win-clients/)

[Home](/cybersecurity-blog/)[Malware Analysis](/cybersecurity-blog/category/malware-analysis/)

CastleLoader Analysis: A Deep Dive into Stealthy Loader Targeting Government Sector

[ANY.RUN’s](https://any.run/?utm_source=anyrunblog&utm_medium=article&utm_campaign=castleloader_analysis&utm_term=130126&utm_content=linktolanding) team conducted an extensive malware analysis of CastleLoader, the first link in the chain of attacks impacting various industries, including government agencies and critical infrastructures.

It’s a unique walkthrough of its entire execution path, from a packaged installer to C2 server connection, as well as an overview of a parser developed to extract initialized local variables and automatically decode [indicators of compromise](https://any.run/cybersecurity-blog/iocs-iobs-ioas-explained/) (IOCs) featured in them.

## Key Takeways

* **CastleLoader**is a stealthy malware loader used as the first stage in attacks against government entities and multiple industries.

* It relies on a**multi-stage execution chain** (Inno Setup → AutoIt → process hollowing) to evade detection.

* The final malicious payload only manifests in memory after the controlled process has been altered,**making traditional static detection ineffective.**

* CastleLoader delivers **information [stealers](https://any.run/malware-trends/stealer/) and [RATs](https://any.run/malware-trends/rat/)**, enabling credential theft and persistent access.

* A **full-cycle analysis**allowed us to [extract runtime configuration](https://any.run/cybersecurity-blog/malware-configuration/), C2 infrastructure, and high-confidence IOCs.

## CastleLoader as an Initial Access Threat

CastleLoader is a malicious loader malware built to deliver and install other malicious components. It lays the groundwork for the attack, becoming its starting point.

This loader has commonly occurred in cyber attacks since early 2025. It gained popularity due to its high infection rate and universal nature, making it a powerful yet evasive tool.

In several observed campaigns, CastleLoader is delivered through the [ClickFix social-engineering technique](https://any.run/cybersecurity-blog/click-fix-attacks-eric-parker-analysis/), where victims are tricked into manually executing malicious commands via fake verification or update prompts. In these cases, ClickFix acts as the initial access vector, while CastleLoader serves as the second-stage loader that deploys follow-on payloads directly in memory, helping attackers evade traditional file-based detection.

One of CastleLoader’s malicious campaigns is known to impact a total of 469 devices. It became a significant threat to organizations, especially US-based government entities. Its broader scope includes industries like IT, [logistics](https://any.run/cybersecurity-blog/how-transport-company-monitors-threats/), travel, and critical infrastructures across Europe.

CastleLoader is dangerous as a link in the chain delivering information stealers and RATs, making credential theft and persistent network access a high risk.

The loader’s popularity has inspired ANY.RUN’s malware analysis team to break down its malicious sample in order to uncover what it’s made of, retrieve signatures, and retrieve malware configurations.

## Detect CastleLoader and More with Threat Intelligence Feeds

![](/cybersecurity-blog/wp-content/uploads/2025/12/TI-Feeds-1920-v1-1024x656.png)

Modern malware like CastleLoader is designed to evade traditional detection. To keep up with the pace of adversaries, security teams need threat intelligence that reflects what attackers are using right now.

[ANY.RUN’s Threat Intelligence Feeds](https://any.run/threat-intelligence-feeds/?utm_source=anyrunblog&utm_medium=article&utm_campaign=castleloader_analysis&utm_term=130126&utm_content=linktotifeedslanding) provide real-time indicators extracted from live malware executions performed by thousands of SOC teams worldw...
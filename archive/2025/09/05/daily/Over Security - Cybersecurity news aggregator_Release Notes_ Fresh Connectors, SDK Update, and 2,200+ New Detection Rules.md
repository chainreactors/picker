---
title: Release Notes: Fresh Connectors, SDK Update, and 2,200+ New Detection Rules
url: https://any.run/cybersecurity-blog/release-notes-august-2025/
source: Over Security - Cybersecurity news aggregator
date: 2025-09-05
fetch_date: 2025-10-02T19:41:25.689551
---

# Release Notes: Fresh Connectors, SDK Update, and 2,200+ New Detection Rules

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

![Release Notes: Fresh Connectors, SDK Update, and 2,200+ New Detection Rules ](/cybersecurity-blog/wp-content/uploads/2025/09/Release-notes.png)

[Service Updates](/cybersecurity-blog/category/service-updates/)

# Release Notes: Fresh Connectors, SDK Update, and 2,200+ New Detection Rules

September 4, 2025

[Add comment](#comments-15734)
2546 views
5 min read

[Home](/cybersecurity-blog/)[Service Updates](/cybersecurity-blog/category/service-updates/)

Release Notes: Fresh Connectors, SDK Update, and 2,200+ New Detection Rules

#### Recent posts

* [![](/cybersecurity-blog/wp-content/uploads/2025/09/Release-notes-1024x497.png)

  #### Release Notes: Palo Alto Networks, Microsoft, IBM Connectors and 2,300+ Suricata Rules

  8
  0](/cybersecurity-blog/release-notes-september-2025/)
* [![](/cybersecurity-blog/wp-content/uploads/2025/10/FunkLocker_blog-1024x497.jpg)

  #### FunkSec’s FunkLocker: How AI Is Powering the Next Wave of Ransomware

  1572
  0](/cybersecurity-blog/funklocker-malware-analysis/)
* [![](/cybersecurity-blog/wp-content/uploads/2025/09/defender_blog-1024x497.jpg)

  #### ANY.RUN & MS Defender: Enrich Alerts Faster, Stop Attacks Early

  1444
  0](/cybersecurity-blog/ms-defender-connectors/)

[Home](/cybersecurity-blog/)[Service Updates](/cybersecurity-blog/category/service-updates/)

Release Notes: Fresh Connectors, SDK Update, and 2,200+ New Detection Rules

August was a busy month at ANY.RUN. We expanded our list of connectors with **Microsoft Sentinel** and **OpenCTI**, added **Linux Debian (ARM) support** to the SDK, and strengthened detection across hundreds of new malware families and techniques. With fresh signatures, rules, and product updates, your SOC can now investigate faster, detect more threats in real time, and keep defenses sharp against the latest campaigns.

Let’s dive into the details now.

## Product Updates

### New Connectors: Bringing Threat Intelligence into Your Existing Stack

We continue to expand ANY.RUN connectors so teams can work with familiar tools while boosting threat visibility. Our goal is simple: reduce setup friction and deliver fresh, high-fidelity IOCs directly into your workflows; no extra tools, no complex scripts, no wasted analyst time.

### Microsoft Sentinel

ANY.RUN now delivers [**Threat Intelligence (TI) Feeds**](https://intelligence.any.run/feeds?utm_source=anyrunblog&utm_medium=article&utm_campaign=release_notes_august_25&utm_term=040925&utm_content=linktofeeds) directly to Microsoft Sentinel via the [built-in STIX/TAXII connector](https://any.run/cybersecurity-blog/threat-intelligence-feeds-ms-sentinel-connector/). That means:

* **Effortless setup:** [Connect TI Feeds](https://learn.microsoft.com/en-us/azure/sentinel/connect-threat-intelligence-taxii) with your custom API key.

* **Enhanced automation:** Sentinel’s playbooks automatically correlate IOCs with your logs, trigger alerts, and even block IPs.

* **Cost efficiency:** Maximize your existing Sentinel setup, cut false positives, and reduce breach risks with high-fidelity indicators.

* **Rich context:** Every IOC links back to a sandbox session with full TTPs for faster investigations and informed responses.

* **Faster detection:** Fresh IOCs stream into Sentinel in real time, accelerating threat identification before impact.

* **Seamless interoperability:** TI Feeds work natively within your Sentinel environment, so no workflows need to change.

![](/cybersecurity-blog/wp-content/uploads/2025/09/image5-1.png)

Investigations become faster and responses more precise with IOCs enriched by full sandbox context. Unlike static or delayed threat feeds, **ANY.RUN’s TI Feeds are powered by real-time detonations of fresh malware samples** observed across attacks on [15,000+ organizations](https://any.run/cybersecurity-blog/threat-intelligence-from-organizations/) worldwide. The data is updated continuously and pre-processed by analysts to ensure high fidelity and near-zero false positives, so your SOC can act on threats that truly matter.

Want to integrate TI Feeds from ANY.RUN?
Reach out to us and we’ll help you set it up

[Contact us](https://intelligence.any.run/plans/?utm_source=anyrunblog&utm_medium=article&utm_campaign=release_notes_august_25&utm_term=040925&utm_content=linktotiplans)

### OpenCTI

For SOC teams using [**Filigran’s OpenCTI**](https://any.run/cybersecurity-blog/opencti-integration/), ANY.RUN now provides dedicated connectors that bring interactive analysis and fresh threat intelligence directly into your workflows. Instead of juggling multiple tools, analysts can analyze files, enrich observables, and track emerging threats inside the OpenCTI interface they already use.

![](/cybersecurity-blog/wp-content/uploads/2025/09/image-4-2048x1062-1-1024x531.png)

* [Interactive Sandbox](https://any.run/features/?utm_source=anyrunblog&utm_medium=article&utm_campaign=release_notes_august_25&utm_term=040925&utm_content=linktolanding): Automate analysis of suspicious files and URLs to quickly understand their threat level, TTPs, and [collect IOCs](https://any.run/cybersecurity-blog/indicators-of-compromise/).

* [Threat Intelligence Lookup](https://any.run/threat-intelligence-lookup/?utm_source=anyrunblog&utm_medium=article&utm_campaign=release_notes_august_25&utm_term...
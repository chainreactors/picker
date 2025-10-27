---
title: Release Notes: Detonation Actions, Enhanced QR Extraction, and 1,400+ New Detection Rules
url: https://any.run/cybersecurity-blog/release-notes-june-2025/
source: Over Security - Cybersecurity news aggregator
date: 2025-07-03
fetch_date: 2025-10-06T23:55:51.947307
---

# Release Notes: Detonation Actions, Enhanced QR Extraction, and 1,400+ New Detection Rules

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

![Release Notes: Detonation Actions, Enhanced QR Extraction, and 1,400+ New Detection Rules ](/cybersecurity-blog/wp-content/uploads/2024/04/new_updates_blog.jpg)

[Service Updates](/cybersecurity-blog/category/service-updates/)

# Release Notes: Detonation Actions, Enhanced QR Extraction, and 1,400+ New Detection Rules

July 2, 2025

[Add comment](#comments-14592)
4483 views
7 min read

[Home](/cybersecurity-blog/)[Service Updates](/cybersecurity-blog/category/service-updates/)

Release Notes: Detonation Actions, Enhanced QR Extraction, and 1,400+ New Detection Rules

#### Recent posts

* [![](/cybersecurity-blog/wp-content/uploads/2025/09/Release-notes-1024x497.png)

  #### Release Notes: Palo Alto Networks, Microsoft, IBM Connectors and 2,300+ Suricata Rules

  1763
  0](/cybersecurity-blog/release-notes-september-2025/)
* [![](/cybersecurity-blog/wp-content/uploads/2025/10/FunkLocker_blog-1024x497.jpg)

  #### FunkSec’s FunkLocker: How AI Is Powering the Next Wave of Ransomware

  3180
  0](/cybersecurity-blog/funklocker-malware-analysis/)
* [![](/cybersecurity-blog/wp-content/uploads/2025/09/defender_blog-1024x497.jpg)

  #### ANY.RUN & MS Defender: Enrich Alerts Faster, Stop Attacks Early

  3268
  0](/cybersecurity-blog/ms-defender-connectors/)

[Home](/cybersecurity-blog/)[Service Updates](/cybersecurity-blog/category/service-updates/)

Release Notes: Detonation Actions, Enhanced QR Extraction, and 1,400+ New Detection Rules

We’ve packed June with updates designed to make your day-to-day analysis faster, clearer, and easier than before. Whether you’re just getting started or deep into reverse engineering every day, these improvements are here to save you time and help you catch more threats.

In this update:

* Real-time Detonation Action hints that guide you through the steps needed to keep the analysis forward

* Enhanced QR code extraction, making it easier to detect phishing links hidden in documents, images, or dropped during runtime

* Expanded threat coverage, including 120 new behavior signatures, 12 YARA rules, and 1,320 Suricata rules across Windows, Linux, and Android

Scroll down to see what’s new and how these updates can help your team work faster, spot threats earlier, and get more from your [ANY.RUN sessions](https://any.run/?utm_source=anyrunblog&utm_medium=article&utm_campaign=release_notes_june_25&utm_term=020725&utm_content=linktolanding).

## Product Updates

### Detonation Actions: Faster, Clearer Malware Analysis with Real-Time Guidance

In June, we focused on helping analysts work faster and with more clarity, especially during high-pressure investigations. That’s why we introduced [**Detonation Actions**](https://any.run/cybersecurity-blog/detonation-actions/): real-time execution hints that keep your analysis moving forward without guesswork.

Now, when a sample requires interaction to detonate, like opening a file or following a link, Detonation Actions will show exactly what needs to be done.

![](/cybersecurity-blog/wp-content/uploads/2025/07/image-2-1024x580.png)

Whether you’re clicking through manually or relying on automation, you’ll see helpful hints to understand how the threat at hand unfolds.

[See example](https://app.any.run/tasks/069d90f5-58e5-4178-90f6-7b1626847d5f/?utm_source=anyrunblog&utm_medium=article&utm_campaign=release_notes_june_25&utm_term=020725&utm_content=linktoservice)

* **Manual Mode** (Community plan):
  You’ll see suggested actions during the session and can approve or reject them individually, helping you uncover hidden behavior faster.

![](/cybersecurity-blog/wp-content/uploads/2025/07/image2-1.png)

* **Automated Interactivity** (Paid plans):
  Detonation Actions are automatically followed as part of a guided flow. Each step is logged and visible, so your team gets full transparency, even when analysis is fully hands-off.

You’ll find Detonation Actions inside the Actions tab, right next to the process tree. They work across all samples and help analysts of any skill level trigger and observe malware behavior with confidence.

* **Speeds up threat analysis** by guiding analysts through key detonation steps.

* **Improves SOC handover** with action-based insights for smoother investigations.

* **Accelerates incident response** by automating detonation and surfacing behavior fast.

* **Simplifies onboarding** by helping junior analysts learn through guided workflows.

* **Enables smarter decisions** with clearer behavioral context during investigations.

* **Supports automation** by integrating with existing workflows and API-based pipelines.

Test Automated Interactivity with 14-day trial
See how you can streamline analysis and boost detection

[Get 14-day trial](https://any.run/demo/?utm_source=anyrunblog&utm_medium=article&utm_campaign=release_notes_june_25&utm_term=020725&utm_content=linktodemo)

You can activate Detonation Actions by clicking the new **Auto** button when launching your VM or toggle **Automated Interactivity (ML)** manually in Advanced Settings.

![](/cybersecurity-blog/wp-content/uploads/2025/07/image3-1024x797.png)

### Enhanced QR Code Auto-Extraction for Broader Use Cases

We’ve improved how the sandbox detects and extracts [QR codes](https://any.run/cybersecurity-blog/qr-extractor/), making it easier to inv...
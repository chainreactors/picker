---
title: Release Notes: Cross-Platform Threat Analysis with macOS, SSL Decryption, and 1,300+ New Detections
url: https://any.run/cybersecurity-blog/release-notes-march-2026/
source: Over Security - Cybersecurity news aggregator
date: 2026-03-31
fetch_date: 2026-04-01T04:47:34.595778
---

# Release Notes: Cross-Platform Threat Analysis with macOS, SSL Decryption, and 1,300+ New Detections

[![ANY.RUN's Cybersecurity Blog](/cybersecurity-blog/wp-content/uploads/2026/02/anyrun-logo.svg)](https://any.run)
/
[BLOG](/cybersecurity-blog/)

* [Guides and tutorials](/cybersecurity-blog/guides/)
* [Research](/cybersecurity-blog/research/)
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
* [Register for free](https://app.any.run/#register)

* + Search

[![ANY.RUN's Cybersecurity Blog](/cybersecurity-blog/wp-content/uploads/2026/02/anyrun-logo.svg)](https://any.run)
/
[BLOG](/cybersecurity-blog/)

* [Guides and tutorials](/cybersecurity-blog/guides/)
* [Research](/cybersecurity-blog/research/)
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
* [Register for free](https://app.any.run/#register)

* + Search

[![ANY.RUN's Cybersecurity Blog](/cybersecurity-blog/wp-content/uploads/2026/02/anyrun-logo.svg)](https://any.run)
/
[BLOG](/cybersecurity-blog/)

* + Search

![Release Notes: Cross-Platform Threat Analysis with macOS, SSL Decryption, and 1,300+ New Detections ](/cybersecurity-blog/wp-content/uploads/2025/09/Release-notes.png)

[Service Updates](/cybersecurity-blog/category/service-updates/)

# Release Notes: Cross-Platform Threat Analysis with macOS, SSL Decryption, and 1,300+ New Detections

March 31, 2026

[Add comment](#comments-19659)
529 views
7 min read

[Home](/cybersecurity-blog/)[Service Updates](/cybersecurity-blog/category/service-updates/)

Release Notes: Cross-Platform Threat Analysis with macOS, SSL Decryption, and 1,300+ New Detections

#### Recent posts

* [![](/cybersecurity-blog/wp-content/uploads/2025/09/Release-notes-1024x497.png)

  #### Release Notes: Cross-Platform Threat Analysis with macOS, SSL Decryption, and 1,300+ New Detections

  529
  0](/cybersecurity-blog/release-notes-march-2026/)
* [![](/cybersecurity-blog/wp-content/uploads/2026/03/RSAC_cover-1024x497.png)

  #### ANY.RUN at RSAC™ 2026: Highlights & Industry Recognition

  761
  0](/cybersecurity-blog/rsac-2026-highlights/)
* [![](/cybersecurity-blog/wp-content/uploads/2026/03/Magecart-1024x497.png)

  #### Active Magecart Campaign Targets Spain, Steals Card Data via Hijacked eStores for Bank Fraud

  6988
  0](/cybersecurity-blog/banks-magecart-campaign/)

[Home](/cybersecurity-blog/)[Service Updates](/cybersecurity-blog/category/service-updates/)

Release Notes: Cross-Platform Threat Analysis with macOS, SSL Decryption, and 1,300+ New Detections

March was a packed month for [ANY.RUN](https://any.run/?utm_source=anyrunblog&utm_medium=article&utm_campaign=release-notes-march-2026&utm_term=310326&utm_content=linktolanding). We rolled out major product improvements that help security teams investigate phishing inside encrypted traffic, expand cross-platform analysis with macOS, and bring Windows Server into the sandbox workflow.

At the same time, our detection team continued to strengthen threat coverage with new behavior signatures, Suricata rules, and fresh threat intelligence reports focused on active malware and attack techniques.

Here’s a closer look at what’s new.

## Product Updates

This month’s updates are all about helping security teams see more and investigate with less friction. We improved phishing detection inside encrypted traffic, expanded [sandbox coverage](https://any.run/features/?utm_source=anyrunblog&utm_medium=article&utm_campaign=release-notes-march-2026&utm_term=310326&utm_content=linktosandboxlanding) to macOS, and added Windows Server analysis so teams can work across more of the environments they protect every day.

### Automatic SSL Decryption for Stronger Phishing Detection

Encrypted HTTPS traffic remains one of the main reasons phishing is harder to confirm quickly. It hides credential theft, redirect chains, and token-based attacks inside traffic that often appears legitimate, forcing teams to spend more time on validation and increasing the chance of missed compromise.

In March, ANY.RUN introduced [**automatic SSL decryption**](https://any.run/cybersecurity-blog/automatic-ssl-decryption/) in the [Interactive Sandbox](https://any.run/features/?utm_source=anyrunblog&utm_medium=article&utm_campaign=release-notes-march-2026&utm_term=310326&utm_content=linktosandboxlanding) across all subscription tiers. By extracting encryption keys directly from process memory, the sandbox can now inspect decrypted traffic during analysis and apply Suricata rules, detection signatures, and IOC extraction immediately.

Check real-world example: [Detecting Salty2FA phishing campaign with SSL decryption](https://app.any.run/tasks/73fb8a10-2721-4da4-9f9b-a340a6eac370?utm_source=anyrunblog&utm_medium=article&utm_campaign=release-notes-march-2026&utm_term=310326&utm_content=linktoservice)

![](/cybersecurity-blog/wp-content/uploads/2026/03/image2-2048x1152-1-1024x576.png)

This significantly expands phishing visibility across every sandbox session. After implementing the technology, ANY.RUN saw a 5x increase in SSL-decrypted phishing detection and added 60,000 more confirmed malicious URLs to [TI Lookup](https://any.run/threat-intelligence-lookup/?utm_source=anyrunblog&utm_medium=article&utm_campaign=release-notes-march-2026&utm_term=310326&utm_content=linktotilookuplanding) each month.

For your SOC, this means:

* **Higher detection rate:** Analysts can now identify phishing activity that would otherwise stay hidden inside encrypted traffic.

* **Faster MTTD and MTTR:** Teams confirm malicious behavior earlier and respond before phishing causes broader damage.

* **Reduced Tier 1-to-Tier 2 escalation volume:** Tier 1 can close more cases independently and escalate only the incidents that truly need deeper investigation.

### Expanding Your SOC’s Cross-Platform Analysis with macOS

As enterprise environments grow more complex, SOC teams are expected to investigate threats across multiple operating systems without slowing down triage. But when analysis is split across separate tools and environments, investigations take longer, alert backlogs grow, and the risk of delayed or missed detection increases.

To help solve this, ANY.RUN expanded its **sandbox OS coverage with**[**macOS virtual machine**](https://any.run/cybersecurity-blog/anyrun-macos-sandbox/), now available in beta for [Enterprise Suite](https://any.run/plans/?utm_source=anyrunblog&utm_medium=article&utm_campaign=release-notes-march-2026&utm_term=310326&utm_content=linktoplans) users. This gives teams one environment to investigate threats across [Windows](https://any.run/cybersecurity-blog/windows-10-sandbox/), [Linux](https://any.run/cybersecurity-blog/linux-malware-analysis-sandbox/), [Android](https://any.run/cybersecurity-blog/android-malware-analysis/), and now macOS.

[View analysis of macOS threat](https://app.any.run/tasks/65678bab-2c5f-47b8-b0d4-...
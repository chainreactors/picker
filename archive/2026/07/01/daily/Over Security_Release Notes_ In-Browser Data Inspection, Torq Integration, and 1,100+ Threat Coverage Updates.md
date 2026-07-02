---
title: Release Notes: In-Browser Data Inspection, Torq Integration, and 1,100+ Threat Coverage Updates
url: https://any.run/cybersecurity-blog/release-notes-june-2026-2/
source: Over Security
date: 2026-07-01
fetch_date: 2026-07-02T05:58:09.550979
---

# Release Notes: In-Browser Data Inspection, Torq Integration, and 1,100+ Threat Coverage Updates

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

![Release Notes: In-Browser Data Inspection, Torq Integration, and 1,100+ Threat Coverage Updates](https://any.run/cybersecurity-blog/wp-content/uploads/2026/07/Release-notes-scaled.png)

[Service Updates](https://any.run/cybersecurity-blog/category/service-updates/)

# Release Notes: In-Browser Data Inspection, Torq Integration, and 1,100+ Threat Coverage Updates

July 1, 2026

[Add comment](#comments-21857)
1781 views
5 min read

[Home](https://any.run/cybersecurity-blog/)[Service Updates](https://any.run/cybersecurity-blog/category/service-updates/)

Release Notes: In-Browser Data Inspection, Torq Integration, and 1,100+ Threat Coverage Updates

#### Recent posts

* [![](https://any.run/cybersecurity-blog/wp-content/uploads/2026/07/Release-notes-1024x497.png)

  #### Release Notes: In-Browser Data Inspection, Torq Integration, and 1,100+ Threat Coverage Updates

  1781
  0](https://any.run/cybersecurity-blog/release-notes-june-2026/)
* [![](https://any.run/cybersecurity-blog/wp-content/uploads/2026/06/Supply-Chain-Security-with-ANY.RUN_-1024x497.png)

  #### Closing the Supplier Security Gap: How a US Manufacturer Cut Third-Party Risk and Doubled SOC Triage Speed

  1950
  0](https://any.run/cybersecurity-blog/us-manufacturer-security-risk/)
* [![](https://any.run/cybersecurity-blog/wp-content/uploads/2026/06/torq_blog-1024x497.png)

  #### ANY.RUN & Torq Integration: Scale Triage & Respond with Confidence

  6817
  0](https://any.run/cybersecurity-blog/torq-integration/)

[Home](https://any.run/cybersecurity-blog/)[Service Updates](https://any.run/cybersecurity-blog/category/service-updates/)

Release Notes: In-Browser Data Inspection, Torq Integration, and 1,100+ Threat Coverage Updates

Phishing pages don’t sit still anymore. They redirect, load scripts, harvest credentials through dynamic forms, and rebuild their DOM after the initial load — and most URL analysis workflows still only see the finish line, not the race. This June, ANY.RUN closed that gap directly inside the Interactive Sandbox and extended its automation reach with a new integration built for scale.

Here’s what your team can put to work this month: full browser-level visibility for every URL analysis, a no-code path to embed ANY.RUN in Torq playbooks, and over 1,100 new detections across behavior signatures, Suricata rules, and YARA rules.

## Product Updates

June’s releases focus on closing the visibility gap in phishing investigations and giving SOC and MSSP teams a faster route from alert to automated response. The headline update is in-browser data inspection, a new investigation layer in the Interactive Sandbox, alongside a new integration with the Torq AI SOC Platform.

### Closing the Phishing Blind Spot with In-Browser Data Inspection

Modern phishing campaigns rarely stop at a malicious URL. They rely on dynamic content, JavaScript, multi-stage redirects, credential harvesting forms, and browser-based tricks that often remain invisible to traditional analysis methods.

This month, ANY.RUN [introduced In-Browser Data Inspection](https://any.run/cybersecurity-blog/in-browser-data-inspection/), a new capability that captures browser-rendered content during URL analysis, revealing exactly what users would experience when interacting with a suspicious website.

Instead of relying solely on page source or network data, analysts can now inspect:

* Fully rendered web pages and dynamic content;
* Phishing forms and credential collection attempts;
* Client-side JavaScript execution;
* Redirect chains and browser behavior;
* Hidden elements designed to evade detection.

![](https://any.run/cybersecurity-blog/wp-content/uploads/2026/07/unfo1-1662x2048-1-831x1024.png)

*See all URL details, DOM changes, network requests, and IOCs in one place*

For SOC analysts, this means fewer blind spots during phishing investigations and faster validation of suspicious URLs.

For security managers and CISOs, it means higher confidence in phishing detection, quicker incident triage, and better protection against increasingly sophisticated browser-based attacks.

### Scaling Triage and Response with the ANY.RUN & Torq Integration

Alert volume keeps growing faster than SOC headcount, and every alert that lands without context costs an analyst time they don’t have. ANY.RUN’s [new integration with the Torq AI SOC Platform](https://any.run/cybersecurity-blog/torq-integration/) puts conclusive malware and phishing verdicts directly into the automated workflows teams already build in Torq: no custom code, no months-long rollout.

The integration ships with five ready-to-use [Torq HyperAgents](https://torq.io/hyperagents/)™ covering two workflow types: case-based templates that pull observables straight from an open Torq case for enrichment, and standalone sandbox workflows that accept a URL or file as input and return a full verdict, IOC list, and report link anywhere in a custom automation chain. Results — reputation data, threat names, tags, and structured JSON — land directly in Torq Case Management, ready to branch on.

**Teams integrating ANY.RUN into Torq gain:**

* Faster incident resolution, with an average MTTR reduction of 21 minutes per case.
* Operational scaling without added headcount, as HyperAgents absorb routine Tier 1 enrichment work.
* Zero development overhead, with a no-code setup that’s live in minutes rather than months.
* Standardized investigation logic, so every alert is...
---
title: Smile, You’re on Camera: A Live Stream from Inside Lazarus Group’s IT Workers Scheme
url: https://any.run/cybersecurity-blog/lazarus-group-it-workers-investigation/
source: Over Security - Cybersecurity news aggregator
date: 2025-12-04
fetch_date: 2025-12-05T03:18:50.872499
---

# Smile, You’re on Camera: A Live Stream from Inside Lazarus Group’s IT Workers Scheme

[![ANY.RUN's Cybersecurity Blog](/cybersecurity-blog/wp-content/uploads/2025/11/Logo-Blog_Header_238х46.svg)](/cybersecurity-blog/)

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

[![ANY.RUN's Cybersecurity Blog](/cybersecurity-blog/wp-content/uploads/2025/11/Logo-Blog_Header_238х46.svg)](/cybersecurity-blog/)

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

[![ANY.RUN's Cybersecurity Blog](/cybersecurity-blog/wp-content/uploads/2025/11/Logo-Blog_Header_238х46.svg)](/cybersecurity-blog/)

* + Search

![Smile, You’re on Camera: A Live Stream from Inside Lazarus Group’s IT Workers Scheme ](/cybersecurity-blog/wp-content/uploads/2025/12/Lazarus-APT-Caught-Live-on-Camera.png)

[Malware Analysis](/cybersecurity-blog/category/malware-analysis/)

# Smile, You’re on Camera: A Live Stream from Inside Lazarus Group’s IT Workers Scheme

December 4, 2025

[Add comment](#comments-17149)
8628 views
20 min read

[Home](/cybersecurity-blog/)[Malware Analysis](/cybersecurity-blog/category/malware-analysis/)

Smile, You’re on Camera: A Live Stream from Inside Lazarus Group’s IT Workers Scheme

#### Recent posts

* [![](/cybersecurity-blog/wp-content/uploads/2025/12/Lazarus-APT-Caught-Live-on-Camera-1024x497.png)

  #### Smile, You're on Camera: A Live Stream from Inside Lazarus Group’s IT Workers Scheme

  8628
  0](/cybersecurity-blog/lazarus-group-it-workers-investigation/)
* [![](/cybersecurity-blog/wp-content/uploads/2025/12/Salty2FA-Tycoon2FA-chimera-samples_-shutdown-or-operational-shift_-1024x497.png)

  #### Salty2FA & Tycoon2FA Hybrid: A New Phishing Threat to Enterprises

  9218
  0](/cybersecurity-blog/salty2fa-tycoon2fa-hybrid-phishing-2025/)
* [![](/cybersecurity-blog/wp-content/uploads/2025/12/Threat-coverage-updates-1024x497.png)

  #### Threat Coverage Digest: New Malware Reports and 5K+ Detection Rules

  556
  0](/cybersecurity-blog/threat-coverage-digest-november-2025/)

[Home](/cybersecurity-blog/)[Malware Analysis](/cybersecurity-blog/category/malware-analysis/)

Smile, You’re on Camera: A Live Stream from Inside Lazarus Group’s IT Workers Scheme

***Editor’s note:****This work is a collaboration between Mauro Eldritch from BCA LTD, a company dedicated to threat intelligence and hunting, Heiner García from NorthScan, a threat intelligence initiative uncovering North Korean IT worker infiltration, and*[ANY.RUN](https://any.run/?utm_source=anyrunblog&utm_medium=article&utm_campaign=interview_with_Chollima_exposed&utm_term=041225&utm_content=linktolanding)*, the leading company in malware analysis and threat intelligence*.

*The article was written by Mauro and Heiner.*

In this article, we’ll uncover an entire **North Korean infiltration operation** aimed at deploying [**remote IT workers**](https://www.reuters.com/legal/government/doj-announces-arrest-indictments-north-korean-it-worker-scheme-2025-06-30/) across different companies in the American **financial and crypto/Web3 sectors**, with the objective of conducting **corporate espionage**and generating **funding** for the sanctioned regime. We attributed this effort to the **state-sponsored APT** (Advanced Persistent Threat) [**Lazarus**](https://any.run/cybersecurity-blog/lazarus-group-attacks-2025/), specifically the [**Famous Chollima**](https://www.crowdstrike.com/adversaries/famous-chollima/) division.

## Key Takeaways

* **North Korean operators are infiltrating companies** by posing as remote IT workers and using stolen or rented identities.

* **Famous Chollima relies on social engineering**, not advanced malware, convincing stories, pressure, and identity fraud drive the operation.

* **Recruitment is wide-scale**, using GitHub spam, Telegram outreach, and fake job-seeking setups.

* **Victims are pushed to hand over full identity data**, including SSNs, bank accounts, and device access.

* **Extended**[**ANY.RUN sandbox**](https://any.run/features/?utm_source=anyrunblog&utm_medium=article&utm_campaign=interview_with_Chollima_exposed&utm_term=041225&utm_content=linksandboxlanding)**environments enabled real-time monitoring**, capturing every click, file action, and network request.

* **Operators used a predictable toolkit**, including AnyDesk, Google Remote Desktop, AI-based interview helpers, and OTP extensions.

* **Shared infrastructure and repeated mistakes** revealed their poor operational security and overlapping roles.
* Controlled crashes and resets kept them contained, preventing any real malicious activity while intelligence was gathered.

* **The investigation provides a rare inside view** of how these operatives work, communicate, and attempt to maintain access.

## How the Investigation Was Set Up

We divided this effort into two stages: approaching one of their **recruiters**, building a trusted relationship, and receiving an offer to help them set up **laptops** “to work” (conducted by **Heiner García**from**NorthScan**), and then setting up a simulated **laptop farm** using **sandboxed environments** provided by [**ANY.RUN**](https://any.run/?utm_source=anyrunblog&utm_medium=article&utm_campaign=interview_with_Chollima_exposed&utm_term=041225&utm_content=linktolanding), to record their activity in real-time and analyze their **toolchain and TTPs** (conducted by **Mauro Eldritch** from **BCA LTD**).

Controlled crashes and resets kept them contained. This prevented any malicious activity.

All interviews with DPRK agents and their activities on the laptop farm were recorded from start to finish, in an unprecedented effort that publicly documents their operations from the inside**for the first time.**

![](/cybersecurity-blog/wp-content/uploads/2025/12/A-1024x591.png)

## Introduction: The Spies

*Introducing Famous Chollima | Mauro Eldritch (BCA LTD)*

There’s a long sto...
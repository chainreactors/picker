---
title: EvilTokens: How “Ghost” Code Threatens US and European Businesses
url: https://any.run/cybersecurity-blog/eviltokens-ghost-code-analysis/
source: Over Security
date: 2026-06-23
fetch_date: 2026-06-24T06:06:04.887848
---

# EvilTokens: How “Ghost” Code Threatens US and European Businesses

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

![EvilTokens: How “Ghost” Code Threatens US and European Businesses](https://any.run/cybersecurity-blog/wp-content/uploads/2026/06/EvilTokens-scaled.png)

[Malware Analysis](https://any.run/cybersecurity-blog/category/malware-analysis/)

# EvilTokens: How “Ghost” Code Threatens US and European Businesses

June 23, 2026

[Add comment](#comments-21730)
1599 views
9 min read

[Home](https://any.run/cybersecurity-blog/)[Malware Analysis](https://any.run/cybersecurity-blog/category/malware-analysis/)

EvilTokens: How “Ghost” Code Threatens US and European Businesses

#### Recent posts

* [![](https://any.run/cybersecurity-blog/wp-content/uploads/2026/06/EvilTokens-1024x497.png)

  #### EvilTokens: How “Ghost” Code Threatens US and European Businesses

  1599
  0](https://any.run/cybersecurity-blog/eviltokens-ghost-code-analysis/)
* [![](https://any.run/cybersecurity-blog/wp-content/uploads/2026/06/The-Hacker-News-Award_blog-1024x497.png)

  #### The Hacker News Recognizes ANY.RUN as the Best Security Investigation Platform 2026

  3428
  0](https://any.run/cybersecurity-blog/best-security-platform/)
* [![](https://any.run/cybersecurity-blog/wp-content/uploads/2025/10/High-Speed-Triage-with-ANY.RUN_-1024x497.png)

  #### Faster Triage, Clearer Evidence, Lower Risk: A SOC Guide to Better Alert Handling

  6543
  0](https://any.run/cybersecurity-blog/triage-analyst-guide/)

[Home](https://any.run/cybersecurity-blog/)[Malware Analysis](https://any.run/cybersecurity-blog/category/malware-analysis/)

EvilTokens: How “Ghost” Code Threatens US and European Businesses

[EvilTokens](https://any.run/malware-trends/eviltokens/) can hide serious account takeover risk from your SOC through “ghost” code that appears only after browser-side decryption.

As a result, static URL analysis may miss the most important part of the attack, leaving teams with incomplete evidence, slower triage, and longer exposure to a potential Microsoft 365 compromise.

[Full browser-level inspection](https://any.run/cybersecurity-blog/in-browser-data-inspection/) closes this gap by revealing how the page behaves after execution in a dynamic environment. This gives teams the evidence they need to validate the threat and respond faster.

## Key Takeaways

* EvilTokens hides key parts of its phishing flow behind browser-side decryption, creating a visibility gap for static URL analysis.
* The kit abuses Microsoft’s legitimate device login flow to gain account access without directly stealing the victim’s password.
* Browser-level evidence helps SOC teams reduce manual checks, avoid unnecessary escalations, and make faster containment decisions.
* [Threat Intelligence](https://any.run/threat-intelligence-lookup/?utm_source=anyrunblog&utm_medium=article&utm_campaign=eviltokens-ghost-code-analysis&utm_term=230626&utm_content=linktotilookuplanding) pivots connect one EvilTokens session to related phishing kits, infrastructure, indicators, and wider device-code [phishing activity](https://any.run/phishing/?utm_source=anyrunblog&utm_medium=article&utm_campaign=eviltokens-ghost-code-analysis&utm_term=230626&utm_content=linktophishing).
* Decrypted code and behavioral patterns can also support stronger phishing signatures, threat hunting, and custom detection rules.

## EvilTokens Targeting: Regions and Industries at Risk

According to ANY.RUN Threat Intelligence data, recent EvilTokens activity is concentrated mainly in the United States and Europe.

[View recent EvilTokens activity in ANY.RUN Threat Intelligence](https://intelligence.any.run/analysis/lookup?utm_source=anyrunblog&utm_medium=article&utm_campaign=eviltokens-ghost-code-analysis&utm_term=230626&utm_content=linktotilookup#{%22query%22:%22threatName:%5C%22eviltokens%5C%22%22,%22dateRange%22:7})

![](https://any.run/cybersecurity-blog/wp-content/uploads/2026/06/EvilTokens-1-1024x576.png)

*EvilTokens targeting specific industries*

The kit has been observed targeting organizations in:

* Managed security services
* Technology
* Manufacturing
* Education
* Banking
* Consulting and financial services

These findings show that EvilTokens is aimed largely at organizations where access to a single Microsoft 365 account can expose sensitive data, internal communications, and connected business services.

## Why EvilTokens Creates a Blind Spot for SOC Teams

EvilTokens continues to rank among the most frequently observed phishing kits in ANY.RUN’s weekly threat reports.

A recent analysis session showed how the kit uses Microsoft Device Code Phishing to compromise accounts without stealing credentials directly. Instead, it convinces the victim to complete Microsoft’s legitimate device login flow and unknowingly authorize access to their account.

[Check analysis session with recent EvilTokens attack](https://app.any.run/tasks/55d3ead7-c07a-4fb1-aa42-8c397d1a0f8a?utm_source=anyrunblog&utm_medium=article&utm_campaign=eviltokens-ghost-code-analysis&utm_term=230626&utm_content=linktoservice](https://app.any.run/tasks/55d3ead7-c07a-4fb1-aa42-8c397d1a0f8a?utm_source=anyrunblog&utm_medium=article&utm_campaign=eviltokens-ghost-code-analysis&utm_term=230626&utm_content=linktoservice)

![Recent EvilTokens attack analyzed inside ANY.RUN sandbox ](https://any.run/cybersecurity-blog/wp-content/uploads/2026/06/Screenshot-2026-06-23-at-11.08.07-1024x570.png)

*Recent EvilTokens attack analyzed inside ANY.RUN sandbox*

What makes the attack difficult to investig...
---
title: Attackers Taking Over a Real Enterprise Email Thread to Deliver Phishing
url: https://any.run/cybersecurity-blog/enterprise-email-thread-phishing/
source: Over Security - Cybersecurity news aggregator
date: 2026-01-28
fetch_date: 2026-01-29T04:05:49.052576
---

# Attackers Taking Over a Real Enterprise Email Thread to Deliver Phishing

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

![Attackers Are Taking Over Real Email Threads to Deliver Phishing: New Enterprise Risk](/cybersecurity-blog/wp-content/uploads/2026/01/Enterprise-email-thread-phishing.png)

[Malware Analysis](/cybersecurity-blog/category/malware-analysis/)

# Attackers Are Taking Over Real Email Threads to Deliver Phishing: New Enterprise Risk

January 28, 2026

[Add comment](#comments-18033)
1724 views
8 min read

[Home](/cybersecurity-blog/)[Malware Analysis](/cybersecurity-blog/category/malware-analysis/)

Attackers Are Taking Over Real Email Threads to Deliver Phishing: New Enterprise Risk

#### Recent posts

* [![](/cybersecurity-blog/wp-content/uploads/2026/01/Enterprise-email-thread-phishing-1024x497.png)

  #### Attackers Are Taking Over Real Email Threads to Deliver Phishing: New Enterprise Risk

  1724
  0](/cybersecurity-blog/enterprise-email-thread-phishing/)
* [![](/cybersecurity-blog/wp-content/uploads/2026/01/soc_burnout_blog-1024x497.png)

  #### Fix Staff Shortage & Burnout in Your SOC with Better Threat Intelligence

  610
  0](/cybersecurity-blog/soc-staff-shortage-burnout/)
* [![](/cybersecurity-blog/wp-content/uploads/2026/01/Intagration-ANYRUN-MISP-1024x497.png)

  #### ANY.RUN Sandbox & MISP Integration: Confirm Alerts Faster, Stop Incidents Early

  3148
  0](/cybersecurity-blog/anyrun-sandbox-misp-integration/)

[Home](/cybersecurity-blog/)[Malware Analysis](/cybersecurity-blog/category/malware-analysis/)

Attackers Are Taking Over Real Email Threads to Deliver Phishing: New Enterprise Risk

Think you can trust every email that comes from a business partner?

Unfortunately, that’s no longer guaranteed; attackers now slip into legitimate threads and send messages that look fully authentic.

That’s exactly what happened in a new case uncovered by [ANY.RUN researchers](https://any.run/?utm_source=anyrunblog&utm_medium=article&utm_campaign=Enterprise-email-thread-phishing&utm_term=280126&utm_content=linktolanding); a trust takeover inside a real executive discussion about a document awaiting final approval.

By detonating the suspicious message, the investigation [exposed the full execution chain](https://any.run/features/?utm_source=anyrunblog&utm_medium=article&utm_campaign=Enterprise-email-thread-phishing&utm_term=280126&utm_content=linktosandboxlanding) and linked it to a broader phishing campaign already active since 2025.

Let’s find out how this attack worked, and how your team can detect similar threats faster, safely, and without disrupting business processes.

**TL;DR**

* **Initial access:** Likely compromise of a contractor mailbox already involved in the thread, enabling **conversation hijacking** inside a real C-suite approval flow.

* **Attack chain:** SCA phishing email → 7x forwards → phishing link → Cloudflare Turnstile antibot page → Turnstile-protected phishing page → [**EvilProxy**](https://any.run/malware-trends/evilproxy/) AiTM for Microsoft credential theft.

* **Evasion:** Multi-step redirects + Turnstile mean the final phishing content is only exposed during **real execution**, not simple URL or static checks.

* **Detection:** Behavioral detonation is required to see the full chain and confirm intent; static analysis alone is unlikely to flag it reliably.

* **Campaign context:** Pivoting domains, URL paths (/bot, /robot), and patterns like loginmicrosoft\* in [TI Lookup](https://app.any.run/?utm_source=anyrunblog&utm_medium=article&utm_campaign=Enterprise-email-thread-phishing&utm_term=280126&utm_content=linktoregistration#register?redirect-ref=intelligence.any.run/analysis/lookup) maps this incident to a broader EvilProxy campaign, and supports hunting + detection engineering with both IOCs and IOBs.

## New Phishing Attack Overview

This incident started as something that looked completely normal from the outside: a live email discussion about a document waiting for final approval. It didn’t contain any strange subject line or a cold intro. Just a reply that appeared to belong in the thread.

![A phishing email sent from contractor’s sales manager account](/cybersecurity-blog/wp-content/uploads/2026/01/Attackers-Taking-Over-a-Real-Enterprise-Email-Thread-to-Deliver-Phishing--1024x667.png)

**What made it dangerous was the access path.** The attacker likely got into a supplier-side mailbox (a contractor’s sales manager account) and used that trusted identity to respond directly inside the active discussion among C-suite executives about a document pending final approval.

* **Initial access (suspected):** Compromised contractor account that was already involved in business correspondence.

* **Delivery method:** Conversation hijacking inside an existing C-suite thread.

* **Goal:** Steal Microsoft credentials through a fake authentication page.

* **Protection evasion:** Layered redirects and anti-bot gating designed to keep the content “clean” until a real user interacts.

* **Campaign link:** Indicators connected to a broader operation consistent with the **EvilProxy** phishkit, active since early **December 2025**, with primary targeting in the **Middle East.**

## Execution Chain Observed Step-by-Step

SCA phishing email → 7 forwarded messages → phishing link → anti-bot landing pag...
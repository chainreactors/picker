---
title: When Trust Becomes a Weapon: Google Cloud Storage Phishing Deploying Remcos RAT
url: https://any.run/cybersecurity-blog/phishing-google-drive-remcos/
source: Over Security - Cybersecurity news aggregator
date: 2026-04-14
fetch_date: 2026-04-15T04:43:57.603836
---

# When Trust Becomes a Weapon: Google Cloud Storage Phishing Deploying Remcos RAT

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

![When Trust Becomes a Weapon: Google Cloud Storage Phishing Deploying Remcos RAT](https://any.run/cybersecurity-blog/wp-content/uploads/2026/04/Google-Storage-1.png)

[Malware Analysis](https://any.run/cybersecurity-blog/category/malware-analysis/)

# When Trust Becomes a Weapon: Google Cloud Storage Phishing Deploying Remcos RAT

April 14, 2026

[Add comment](#comments-19993)
2210 views
12 min read

[Home](https://any.run/cybersecurity-blog/)[Malware Analysis](https://any.run/cybersecurity-blog/category/malware-analysis/)

When Trust Becomes a Weapon: Google Cloud Storage Phishing Deploying Remcos RAT

#### Recent posts

* [![](https://any.run/cybersecurity-blog/wp-content/uploads/2026/04/Google-Storage-1-1024x497.png)

  #### When Trust Becomes a Weapon: Google Cloud Storage Phishing Deploying Remcos RAT

  2210
  0](https://any.run/cybersecurity-blog/phishing-google-drive-remcos/)
* [![](https://any.run/cybersecurity-blog/wp-content/uploads/2026/04/Phishing-Targeting-Germany-1024x497.png)

  #### How Phishing Is Targeting Germany’s Economy: Active Threats from Finance to Manufacturing

  9225
  0](https://any.run/cybersecurity-blog/german-industries-attack-cases/)
* [![](https://any.run/cybersecurity-blog/wp-content/uploads/2026/04/Phishing-Detection-that-Works-1024x497.png)

  #### Building Phishing Detection That Works: 3 Steps for CISOs

  3628
  0](https://any.run/cybersecurity-blog/phishing-detection-steps-for-cisos/)

[Home](https://any.run/cybersecurity-blog/)[Malware Analysis](https://any.run/cybersecurity-blog/category/malware-analysis/)

When Trust Becomes a Weapon: Google Cloud Storage Phishing Deploying Remcos RAT

Modern phishing campaigns increasingly abuse legitimate services. Cloud platforms, file-sharing tools, trusted domains, and widely used SaaS applications are now part of the attacker’s toolkit. Instead of breaking trust, attackers borrow it.

This shift creates a dangerous asymmetry. Security controls often whitelist or inherently trust these services, while users are far less likely to question them. The result is a smoother path from inbox to infection.

## Key Takeaways

* Attackers are shifting to trusted cloud infrastructure (Google Storage) to bypass email filters and reputation checks.

* The multi-stage chain uses obfuscated JS/VBS/PowerShell and legitimate RegSvcs.exe for process injection, making static detection ineffective.

* Remcos RAT provides full remote control, keylogging, and data exfiltration — turning one compromised endpoint into a persistent foothold.

* Credential harvesting combined with malware delivery creates dual risk: immediate data theft plus long-term network compromise.

* Traditional EDR relying on file reputation misses these attacks; behavioral sandboxing and real-time TI are required.

* ANY.RUN’s [Interactive Sandbox, TI Lookup, and TI Feeds](https://any.run/enterprise/?utm_source=anyrunblog&utm_medium=article&utm_campaign=phishing-google-drive-remcos&utm_term=140426&utm_content=linktoenterprise) enable proactive detection and rapid response, closing the gap before damage occurs.

## The New Face of Phishing: When “Legitimate” Becomes Lethal

According to ANY.RUN’s annual [Malware Trends Report](https://any.run/cybersecurity-blog/malware-trends-2025/) for 2025, phishing driven by multi-stage redirect chains and trusted-cloud hosting has become the dominant attack vector, with [RATs](https://any.run/malware-trends/rat/) and backdoors rising 28% and 68% respectively. The abuse of legitimate platforms has made traditional reputation-based filtering fundamentally unreliable.

Early detection is no longer simply a technical performance metric. It is a business continuity imperative. When threats hide inside trusted infrastructure, the window between initial infection and serious organizational impact can be measured in hours, not days. Security teams that cannot identify and contain an attack in its earliest stages — before the payload executes, before the C2 channel is established, before the attacker pivots deeper into the network — face an exponentially harder response challenge.

## Phishing Campaign Hiding Remcos RAT Inside Google Cloud Storage

In April 2026, ANY.RUN’s threat research team identified a sophisticated multi-stage phishing campaign that perfectly exemplifies this new breed of attack. The campaign abuses Google Cloud Storage to host HTML phishing pages themed as Google Drive document viewers, ultimately delivering the Remcos Remote Access Trojan (RAT).

[View the attack in real time in a live sandbox session](https://app.any.run/tasks/0efd1390-c17a-49ce-baef-44b5bd9c4a97/?utm_source=anyrunblog&utm_medium=article&utm_campaign=phishing-google-drive-remcos&utm_term=140426&utm_content=linktoservice)

![](https://any.run/cybersecurity-blog/wp-content/uploads/2026/04/googleremcos_2-1024x486.png)

The attackers parked their phishing pages on a legitimate, widely-trusted Google domain. This single architectural choice allowed the campaign to bypass a wide range of conventional email security gateways and web filtering tools.

Convincing Google Drive-themed phishing pages are hosted on storage.googleapis.com subdomains such as pa-bids, com-bid, contract-bid-0, in-bids, and out-bid. Examples include URLs like hxxps://storage[.]googleapis[.]com/com-bid/GoogleDrive.html. These pages mimic legitimate Google Workspace sign-in flows, complete with branded logos, file-type icons (PDF, ...
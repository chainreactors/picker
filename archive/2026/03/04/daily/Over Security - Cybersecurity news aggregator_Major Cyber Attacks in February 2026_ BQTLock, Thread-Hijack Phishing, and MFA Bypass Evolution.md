---
title: Major Cyber Attacks in February 2026: BQTLock, Thread-Hijack Phishing, and MFA Bypass Evolution
url: https://any.run/cybersecurity-blog/february-26-attacks/
source: Over Security - Cybersecurity news aggregator
date: 2026-03-04
fetch_date: 2026-03-05T04:07:25.772759
---

# Major Cyber Attacks in February 2026: BQTLock, Thread-Hijack Phishing, and MFA Bypass Evolution

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

![Major Cyber Attacks in February 2026: BQTLock, Thread-Hijack Phishing, and MFA Bypass Evolution](/cybersecurity-blog/wp-content/uploads/2026/03/5-Major-Cyber-Attacks-in-February-2026_cover.png)

[Cybersecurity Lifehacks](/cybersecurity-blog/category/lifehacks/)

# Major Cyber Attacks in February 2026: BQTLock, Thread-Hijack Phishing, and MFA Bypass Evolution

March 4, 2026

[Add comment](#comments-18892)
195 views
12 min read

[Home](/cybersecurity-blog/)[Cybersecurity Lifehacks](/cybersecurity-blog/category/lifehacks/)

Major Cyber Attacks in February 2026: BQTLock, Thread-Hijack Phishing, and MFA Bypass Evolution

#### Recent posts

* [![](/cybersecurity-blog/wp-content/uploads/2026/03/5-Major-Cyber-Attacks-in-February-2026_cover-1024x497.png)

  #### Major Cyber Attacks in February 2026: BQTLock, Thread-Hijack Phishing, and MFA Bypass Evolution

  195
  0](/cybersecurity-blog/february-26-attacks/)
* [![](/cybersecurity-blog/wp-content/uploads/2026/03/ssl-1024x497.png)

  #### Expanding Phishing Detection at Scale with Automatic SSL Decryption

  482
  0](/cybersecurity-blog/automatic-ssl-decryption/)
* [![](/cybersecurity-blog/wp-content/uploads/2026/02/Splunk_ent_blog-1024x497.png)

  #### ANY.RUN & Splunk Enterprise: Stronger Detection, Faster Response in Your SOC

  1947
  0](/cybersecurity-blog/splunk-enterprise-integration/)

[Home](/cybersecurity-blog/)[Cybersecurity Lifehacks](/cybersecurity-blog/category/lifehacks/)

Major Cyber Attacks in February 2026: BQTLock, Thread-Hijack Phishing, and MFA Bypass Evolution

February 2026 brought a surge of sophisticated cyber threats targeting businesses across industries. ANY.RUN’s analysts exposed and explored several major cyber threats this month, providing early visibility into emerging malware families and evolving attack techniques.

From new ransomware strains capable of encrypting entire environments in minutes, to fully undetected remote access trojans — the threat landscape this February demands attention from every security team.

## Summary for Every Security Team to Focus

* Two new ransomware families, **GREENBLOOD and BQTLock**, capable of disrupting business operations within minutes and combining encryption with data theft, were identified this month.

* Two new RATs — **Moonrise and Karsto** — were caught with zero detections on VirusTotal at the time of analysis, illustrating the growing gap between static detection and real-world threats.

* **Thread-hijack phishing** reached a new level of sophistication, with attackers inserting themselves into real C-suite email conversations to deliver layered credential-theft campaigns using the EvilProxy phishing kit.

* **Enterprise phishing** infrastructure is now routinely hosted on trusted cloud platforms: Microsoft Azure, Google Firebase, and Cloudflare. This makes URL reputation checks and blocklists increasingly unreliable as standalone defenses.

## 1. The New Threats Nobody Had Signatures For

ANY.RUN analysts identified four new malicious families in February 2026 — two ransomware strains and two remote access trojans — all of which either evaded static detection entirely or compressed the window for defenders to respond.

### GREENBLOOD: Fast Encryption, Evidence Removal, and Immediate Business Exposure

GREENBLOOD is [a newly identified](https://any.run/cybersecurity-blog/emerging-ransomware-bqtlock-greenblood/) Go-based ransomware built for speed, stealth, and pressure. Rather than relying on encryption alone, it combines rapid file locking with self-deletion to reduce forensic visibility, and adds data-leak threats through a TOR-based site — transforming a technical incident into a full business crisis involving downtime, regulatory exposure, reputational damage, and recovery cost.

[ANY.RUN’s Interactive Sandbox](https://any.run/features/?utm_source=anyrunblog&utm_medium=article&utm_campaign=february-26-attacks&utm_term=030326&utm_content=linktosandboxlanding) captured the full attack chain in real time.

[View detonation](https://app.any.run/tasks/6f5d3098-14c0-45ed-916e-863ef4ba354d/?utm_source=anyrunblog&utm_medium=article&utm_campaign=february-26-attacks&utm_term=030326&utm_content=linktoservice)

![](/cybersecurity-blog/wp-content/uploads/2026/03/febr_1-1024x576.png)

Analysts observed:

    • ChaCha8-based **encryption** capable of disrupting operations within minutes of initial execution.

    • Attempts to delete the original executable, limiting post-incident **forensic visibility**.

    • A TOR-based leak site to add **extortion** leverage beyond file recovery.

Teams using TI Lookup can search for other GREENBLOOD sample analyses to uncover variants and expand detection coverage across environments:

[commandLine:”greenblood”](https://intelligence.any.run/analysis/lookup?utm_source=anyrunblog&utm_medium=article&utm_campaign=february-26-attacks&utm_term=030326&utm_content=linktotilookup#%7B%22query%22:%22commandLine:%5C%22greenblood%5C%22%22,%22dateRange%22:180%7D)

![](/cybersecurity-blog/wp-content/uploads/2026/03/febr_2-1024x488.png)

### BQTLock: The Ransomware That Steals Your Data Before You Even Know It’s There

[BQTLock is a](https://any.run/cybersecurity-blog/emerging-ransomware-bqtlock-greenblood/) stealthy ransomware-linked chain. Instead of triggering obvious alerts immediately, it blends into trusted Windows processes and delays visible damage — making early detection difficult and increasing the chance of data exposure, operational disruption, and financial loss.

Minimize  financial exposure, breach costs
 and regulatory risk.
Build an early detection workflow with ANY.RUN solutions

[Contact us](https://any.run/enterprise/?utm_source=anyrunblog&utm_medium=article&utm_campaign=february-26-attacks&utm_term=030326&utm_content=linktoenterprise#contact-sales)

Sandbox detonation revealed the complete kill chain,...
---
title: From Fake Purchase Orders to Remote Access: Analyzing the JS.MonoGlyphRAT Threat to US Enterprises
url: https://any.run/cybersecurity-blog/monoglyphrat-attacks-us-enterprise/
source: Over Security
date: 2026-06-02
fetch_date: 2026-06-03T06:46:49.998546
---

# From Fake Purchase Orders to Remote Access: Analyzing the JS.MonoGlyphRAT Threat to US Enterprises

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

![From Fake Purchase Orders to Remote Access: Analyzing the JS.MonoGlyphRAT Threat to US Enterprises](https://any.run/cybersecurity-blog/wp-content/uploads/2026/06/Global-Alert-scaled.png)

[Malware Analysis](https://any.run/cybersecurity-blog/category/malware-analysis/)

# From Fake Purchase Orders to Remote Access: Analyzing the JS.MonoGlyphRAT Threat to US Enterprises

June 2, 2026

[Add comment](#comments-21343)
458 views
17 min read

[Home](https://any.run/cybersecurity-blog/)[Malware Analysis](https://any.run/cybersecurity-blog/category/malware-analysis/)

From Fake Purchase Orders to Remote Access: Analyzing the JS.MonoGlyphRAT Threat to US Enterprises

#### Recent posts

* [![](https://any.run/cybersecurity-blog/wp-content/uploads/2026/06/Global-Alert-1024x497.png)

  #### From Fake Purchase Orders to Remote Access: Analyzing the JS.MonoGlyphRAT Threat to US Enterprises

  458
  0](https://any.run/cybersecurity-blog/monoglyphrat-attacks-us-enterprise/)
* [![](https://any.run/cybersecurity-blog/wp-content/uploads/2026/05/Interview-1024x497.png)

  #### Inside ANY.RUN’s 10-Year Evolution: An Interview with CEO Aleksey Lapshin

  6684
  0](https://any.run/cybersecurity-blog/ceo-interview-anyrun-10-years/)
* [![](https://any.run/cybersecurity-blog/wp-content/uploads/2026/05/5-Major-Cyber-Attacks-in-May-2026-1024x497.png)

  #### Major Cyber Attacks in May 2026: Fake Invitations, Agent Tesla, BlobPhish, and More

  7046
  0](https://any.run/cybersecurity-blog/major-cyber-attacks-may-2026/)

[Home](https://any.run/cybersecurity-blog/)[Malware Analysis](https://any.run/cybersecurity-blog/category/malware-analysis/)

From Fake Purchase Orders to Remote Access: Analyzing the JS.MonoGlyphRAT Threat to US Enterprises

A previously unidentified cyberattack is quietly spreading through US businesses — and most security tools are not catching it. Researchers at [ANY.RUN](http://any.run/?utm_source=anyrunblog&utm_medium=article&utm_campaign=monoglyphrat-attacks-us-enterprise&utm_term=020626&utm_content=linktolanding) have identified a new backdoor called JS.MonoGlyphRAT, an advanced piece of malware delivered as an ordinary-looking JavaScript file disguised as a purchase order, quote, or business proposal. Once an employee opens the file, the attacker gains silent, persistent access to the company’s systems.

This threat is currently active and primarily targeting organizations in the United States, with victims confirmed across the technology sector, managed security service providers (MSSPs), telecommunications, and education. It has also been observed in Germany, Sweden, Australia, and several other countries.

The financial consequences can quickly escalate beyond incident response costs. Organizations may face operational downtime, regulatory penalties, contractual liabilities, lost business opportunities, reputational damage, and increased cyber insurance expenses. Because MonoGlyphRAT functions as a loader capable of delivering additional malware, even a seemingly minor infection can become the first step toward a large-scale breach with significant business impact.

## Key Takeaways

* **It is actively targeting US businesses.** JS.MonoGlyphRAT is an operational threat, with confirmed victims in the US technology, MSSP, and telecom sectors, delivered via convincing sales-themed phishing lures.
* **Most security tools are blind to it.** The malware is currently classified as ‘Unknown malware’ on VirusTotal and ThreatFox. Standard signature-based antivirus provides little to no protection.
* **It is designed for persistence and deep access.** The RAT establishes a permanent foothold via the Windows registry, runs silently in the background, and can pivot to download ransomware, exfiltrate data, or deploy further stages.
* **The attack begins with a single click.** Employees in procurement, sales, and finance are the primary targets. A .js file disguised as a purchase order or quote is all it takes to compromise a machine.
* **The financial exposure is real and immediate.** From ransomware deployment to data breach fines and incident response costs, a successful compromise can cost a mid-sized US business millions of dollars — plus reputational damage that is harder to quantify.
* **Behavioral detection is the key defense.** The malware’s most reliable detection artifacts are behavioral: unusual wscript.exe activity, PowerShell chains launched from a user directory, suspicious registry writes, and HTTP beaconing to non-standard ports. Hunt for these patterns actively.
* **ANY.RUN detects and analyzes this threat in real time.** ANY.RUN’s [Interactive Sandbox](https://any.run/features/?utm_source=anyrunblog&utm_medium=article&utm_campaign=monoglyphrat-attacks-us-enterprise&utm_term=020626&utm_content=linktosandboxlanding) first identified and documented JS.MonoGlyphRAT, providing full behavioral analysis, C2 traffic capture, and MITRE ATT&CK mapping. ANY.RUN [Threat Intelligence](https://intelligence.any.run/?utm_source=anyrunblog&utm_medium=article&utm_campaign=monoglyphrat-attacks-us-enterprise&utm_term=020626&utm_content=linktoti) allows defenders to query related IOCs — including C2 IPs, domains, URI patterns, and Suricata rule IDs — to proactively hunt for this threat across their environments. Organizations using ANY.RUN can analyze suspicious .js files in seconds before they reach endpoints, dramatically reducing the window of exposure.

## Wh...
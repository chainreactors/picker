---
title: LATAM Businesses Hit by XWorm via Fake Financial Receipts: Full Campaign Analysis
url: https://any.run/cybersecurity-blog/xworm-latam-campaign/
source: Over Security - Cybersecurity news aggregator
date: 2026-02-17
fetch_date: 2026-02-18T04:15:56.534286
---

# LATAM Businesses Hit by XWorm via Fake Financial Receipts: Full Campaign Analysis

[![ANY.RUN's Cybersecurity Blog](/cybersecurity-blog/wp-content/uploads/2026/02/anyrun-logo.svg)](http://any.run)
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

[![ANY.RUN's Cybersecurity Blog](/cybersecurity-blog/wp-content/uploads/2026/02/anyrun-logo.svg)](http://any.run)
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

[![ANY.RUN's Cybersecurity Blog](/cybersecurity-blog/wp-content/uploads/2026/02/anyrun-logo.svg)](http://any.run)
/
[BLOG](/cybersecurity-blog/)

* + Search

![LATAM Businesses Hit by XWorm via Fake Financial Receipts: Full Campaign Analysis ](/cybersecurity-blog/wp-content/uploads/2026/02/XWorm-Attacks-LATAM.png)

[Malware Analysis](/cybersecurity-blog/category/malware-analysis/)

# LATAM Businesses Hit by XWorm via Fake Financial Receipts: Full Campaign Analysis

February 17, 2026

[Add comment](#comments-18515)
1031 views
10 min read

[Home](/cybersecurity-blog/)[Malware Analysis](/cybersecurity-blog/category/malware-analysis/)

LATAM Businesses Hit by XWorm via Fake Financial Receipts: Full Campaign Analysis

#### Recent posts

* [![](/cybersecurity-blog/wp-content/uploads/2026/02/XWorm-Attacks-LATAM-1024x497.png)

  #### LATAM Businesses Hit by XWorm via Fake Financial Receipts: Full Campaign Analysis

  1031
  0](/cybersecurity-blog/xworm-latam-campaign/)
* [![](/cybersecurity-blog/wp-content/uploads/2026/02/Driving-Stronger-Triage-and-Response-1024x497.png)

  #### Fortune 500 Tech Enterprise Speeds up Triage and Response with ANY.RUN's Solutions

  2431
  0](/cybersecurity-blog/fortune-500-enterprise-success-story/)
* [![](/cybersecurity-blog/wp-content/uploads/2026/02/Green-Blood-and-BQTLock-Ransomware-1024x497.png)

  #### Emerging Ransomware BQTLock & GREENBLOOD Disrupt Businesses in Minutes

  4212
  0](/cybersecurity-blog/emerging-ransomware-bqtlock-greenblood/)

[Home](/cybersecurity-blog/)[Malware Analysis](/cybersecurity-blog/category/malware-analysis/)

LATAM Businesses Hit by XWorm via Fake Financial Receipts: Full Campaign Analysis

***Editor’s note:** The current article is authored by Moises Cerqueira, malware researcher and threat hunter. You can find [Moises on LinkedIn](https://www.linkedin.com/in/moises-cerqueira/)*.

Malware campaigns targeting Latin America (LATAM) are evolving. While the final payloads, often commodity RATs like [XWorm](https://any.run/malware-trends/xworm/), remain consistent, delivery mechanisms are becoming increasingly sophisticated to bypass region-specific defenses and increase the chance of reaching real business users.

In this analysis, we dissect a recent campaign targeting Brazilian users. What starts as a **deceptive “banking receipt”** quickly turns into a multi-stage infection chain that leverages steganography, Cloudinaryabuse, and a dedicated .NET persistence module designed to bypass traditional schtasks monitoring, reducing early visibility for security teams and prolonging dwell time.

![](/cybersecurity-blog/wp-content/uploads/2026/02/Fig01_Full_ProcessGraph-1024x559.png)

## Key Takeaways

**Built to blend into finance workflows:** A “receipt” lure is optimized for real corporate inboxes and shared drives across LATAM.

**High click potential in real operations:** Payment and receipt themes map to everyday processes, which raises the chance of execution on work machines.

**The chain is designed to stay quiet:**WMI execution, fileless loading, and .NET-based persistence reduce early detection signals and increase dwell time.

**One endpoint can become an identity problem:**XWorm access can lead to credential/session theft and downstream compromise of email, SaaS, and finance systems.

**Trusted services and binaries are part of the evasion:** Cloud-hosted payload delivery and CasPol.exe abuse help the activity blend in.

**Early detection is an operational advantage:** Better monitoring + faster triage + [regional hunting](https://any.run/cybersecurity-blog/threat-hunting-for-soc-and-mssp/) can keep his attack from escalating into fraud, data exposure, or ransomware.

74% of Fortune 100 companies
rely on ANY.RUN
for earlier detection and faster SOC response

[Power your SOC now](https://any.run/enterprise/?utm_source=anyrunblog&utm_medium=article&utm_campaign=xworm-latam-campaign&utm_term=170226&utm_content=linktoenterprise#contact-sales)

## Stage 1: The Deceptive Delivery

This campaign begins with a classic but effective technique aimed at Brazilian users: a malicious file masquerading as a bank receipt (“Comprovante-Bradesco…”). While it abuses the double-extension trick (.pdf.js) to look like a document, it is, in reality, a Windows Script Host (WSH) dropper designed for direct execution

![The file tries to masquerade as a PDF document](/cybersecurity-blog/wp-content/uploads/2026/02/Fig02_FileProperties.png)

Although the file size is unusually large (~1.2MB) for a simple script, this is intentional. The attackers padded it with junk data to inflate entropy and evade static analysis scanners that may skip larger files, helping the lure pass through initial controls and delaying detection.

### Analyzing the Obfuscated JavaScript

Upon opening the file, there’s no readable code. Instead, the script uses heavy obfuscation via Unicode “junk injection.” The malicious logic is buried inside massive string variables packed with emojis, homoglyphs, and other non-ASCII characters

![Heavily obfuscated code using Unicode characters and emojis](/cybersecurity-blog/wp-content/uploads/2026/02/Fig03_ObfuscatedCode-1024x134.png)

As seen above, the script uses a delimiter-based reconstruction method. Rather than relying on complex cryptography, it applies a simple .replace() function at runtime to strip away the injected Unicode noise (the delimiters) and reconstruct the payload

### Deobfuscation and Payload Extraction

To understand the dropper’s intent, we replicated the deobfuscation logic using CyberChef. By stripping the specific Unicode delimiters and decoding the resulting Base64 and UTF-16LE text, we revealed the core payload.

![Using CyberChef to strip Unicode delimiters](/cybersecurity-blog/wp-content/uploads/2026/02/1-1024x490.png)

The deobfuscated payload confirms that this is a pure dropper. It constructs a PowerShell command responsible for downloading the next stage.

Speed up
alert triage
Validate real threats in minutes

[Register now](http...
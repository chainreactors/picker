---
title: Emerging Ransomware BQTLock & GREENBLOOD Disrupt Businesses in Minutes
url: https://any.run/cybersecurity-blog/emerging-ransomware-bqtlock-greenblood/
source: Over Security - Cybersecurity news aggregator
date: 2026-02-11
fetch_date: 2026-02-12T04:23:05.868052
---

# Emerging Ransomware BQTLock & GREENBLOOD Disrupt Businesses in Minutes

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

![Emerging Ransomware BQTLock & GREENBLOOD Disrupt Businesses in Minutes ](/cybersecurity-blog/wp-content/uploads/2026/02/Green-Blood-and-BQTLock-Ransomware.png)

[Malware Analysis](/cybersecurity-blog/category/malware-analysis/)

# Emerging Ransomware BQTLock & GREENBLOOD Disrupt Businesses in Minutes

February 11, 2026

[Add comment](#comments-18417)
1693 views
7 min read

[Home](/cybersecurity-blog/)[Malware Analysis](/cybersecurity-blog/category/malware-analysis/)

Emerging Ransomware BQTLock & GREENBLOOD Disrupt Businesses in Minutes

#### Recent posts

* [![](/cybersecurity-blog/wp-content/uploads/2026/02/Green-Blood-and-BQTLock-Ransomware-1024x497.png)

  #### Emerging Ransomware BQTLock & GREENBLOOD Disrupt Businesses in Minutes

  1693
  0](/cybersecurity-blog/emerging-ransomware-bqtlock-greenblood/)
* [![](/cybersecurity-blog/wp-content/uploads/2026/02/hunting_blog-1024x497.png)

  #### How to Build Threat Hunting that Defends Your Organization Against Real Attacks

  1013
  0](/cybersecurity-blog/threat-hunting-for-soc-and-mssp/)
* [![](/cybersecurity-blog/wp-content/uploads/2026/02/cti_finance_blog-1024x497.png)

  #### How Threat Intelligence Helps Protect Financial Organizations from Business Risk

  736
  0](/cybersecurity-blog/cyber-threat-intelligence-for-finance/)

[Home](/cybersecurity-blog/)[Malware Analysis](/cybersecurity-blog/category/malware-analysis/)

Emerging Ransomware BQTLock & GREENBLOOD Disrupt Businesses in Minutes

How long would it take your team to realize ransomware is already running?

The newly identified ransomware families are already causing real business disruption. These threats can disrupt operations fast while also reducing visibility through stealth or cleanup activity, shrinking the time teams have to detect and contain the attack.

Here’s what you should know about BQTLock and GREENBLOOD, and how your team can detect and contain them before the impact escalates.

**TL;DR**

* **BQTLock** is a stealthy ransomware-linked chain. It injects Remcos into explorer.exe, performs UAC bypass via fodhelper.exe, and sets autorun persistence to keep elevated access after reboot, then shifts into credential theft / screen capture, turning the incident into both ransomware + data breach risk.

* **GREENBLOOD** is a **Go-based** ransomware built for rapid impact: ChaCha8-based encryption can disrupt operations in minutes, followed by self-deletion / cleanup attempts to reduce forensic visibility, plus TOR leak-site pressure to add extortion leverage beyond recovery.

* In both cases, the critical window is **pre-encryption / early execution**: stealth setup (BQTLock) and fast encryption (GREENBLOOD) compress response time and raise cost fast.

* Behavior-first triage in ANY.RUN’s [Interactive Sandbox](https://any.run/features/?utm_source=anyrunblog&utm_medium=article&utm_campaign=emerging-ransomware-bqtlock-greenblood&utm_term=110226&utm_content=linktosandboxlanding) lets teams confirm key actions (process injection, UAC bypass, persistence, encryption, self-delete) during execution, extract IOCs immediately, and pivot into [Threat Intelligence Lookup](https://any.run/threat-intelligence-lookup/?utm_source=anyrunblog&utm_medium=article&utm_campaign=emerging-ransomware-bqtlock-greenblood&utm_term=110226&utm_content=linktotilookuplanding) (e.g., commandLine:”greenblood”) to find related runs/variants and harden detections faster.

## BQTLock: A Stealth Attack That Escalates into Data Theft and Business Risk

[Original post on LinkedIn](https://www.linkedin.com/posts/any-run_bqtlock-remcos-anyrun-activity-7422972134806687744-URZY)

BQTLock is a ransomware-linked threat designed to hide in normal system activity, gain elevated privileges, and quietly prepare for deeper impact before defenders can react.

Instead of triggering obvious alerts immediately, it blends into trusted Windows processes and delays visible damage. This makes early detection difficult and increases the chance of **data exposure, operational disruption, and financial loss** for affected organizations.

### How the Attack Was Revealed Through Behavioral Analysis

Using the [ANY.RUN interactive sandbox](https://any.run/features/?utm_source=anyrunblog&utm_medium=article&utm_campaign=emerging-ransomware-bqtlock-greenblood&utm_term=110226&utm_content=linktosandboxlanding), analysts were able to observe the full behavioral chain in real time.

[See full execution chain of BQTLock](https://app.any.run/tasks/90be5f16-fdde-4aca-9482-86e2aa43fba0/?utm_source=anyrunblog&utm_medium=article&utm_campaign=emerging-ransomware-bqtlock-greenblood&utm_term=110226&utm_content=linktoservice)

![BQTLock ransomware analysis](/cybersecurity-blog/wp-content/uploads/2026/02/BQTLock-1024x568.png)

The analysis revealed that the malware:

* Injects the Remcos payload into **explorer.exe** to remain hidden inside legitimate system activity

* Performs a **UAC bypass via fodhelper.exe** to obtain elevated privileges

* Establishes [autorun persistence](https://any.run/cybersecurity-blog/6-persistence-mechanisms-in-malware/) to survive system restarts with higher access rights

Faster detection and lower incident risk

Uncover stealthy ransomware early with ANY.RUN

[Integrate in your SOC](https://any.run/enterprise/?utm_source=anyrunblog&utm_medium=article&utm_campaign=emerging-ransomware-bqtlock-greenblood&utm_term=110226&utm_content=linktoenterprise#contact-sales)

Once privilege escalation is complete, the threat moves beyond stealth and into active harm, including:

* **data theft capabilities** that increase breach severity

* **screen capture activity** that may expose sensitive corporate information

![Credentials stealing by BQTLock](/cybersecurity-blog/wp-content/uploads/2026/02/Credentials-stealing-1024x669.png)

This sequence shows how quickly a seemingly quiet infection can evolve ...
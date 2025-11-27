---
title: Major Cyber Attacks in November 2025: XWorm, JSGuLdr Loader, Phoenix Backdoor, Mobile Threats, and More
url: https://any.run/cybersecurity-blog/major-cyber-attacks-november-2025/
source: Over Security - Cybersecurity news aggregator
date: 2025-11-26
fetch_date: 2025-11-27T03:13:00.383291
---

# Major Cyber Attacks in November 2025: XWorm, JSGuLdr Loader, Phoenix Backdoor, Mobile Threats, and More

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

![Major Cyber Attacks in November 2025: XWorm, JSGuLdr Loader, Phoenix Backdoor, Mobile Threats, and More ](/cybersecurity-blog/wp-content/uploads/2025/11/5-Major-Cyber-Attacks-in-November-2025_cover.png)

[Malware Analysis](/cybersecurity-blog/category/malware-analysis/)

# Major Cyber Attacks in November 2025: XWorm, JSGuLdr Loader, Phoenix Backdoor, Mobile Threats, and More

November 26, 2025

[Add comment](#comments-17015)
401 views
8 min read

[Home](/cybersecurity-blog/)[Malware Analysis](/cybersecurity-blog/category/malware-analysis/)

Major Cyber Attacks in November 2025: XWorm, JSGuLdr Loader, Phoenix Backdoor, Mobile Threats, and More

#### Recent posts

* [![](/cybersecurity-blog/wp-content/uploads/2025/11/5-Major-Cyber-Attacks-in-November-2025_cover-1024x497.png)

  #### Major Cyber Attacks in November 2025: XWorm, JSGuLdr Loader, Phoenix Backdoor, Mobile Threats, and More

  401
  0](/cybersecurity-blog/major-cyber-attacks-november-2025/)
* [![](/cybersecurity-blog/wp-content/uploads/2025/11/Detecting-Critical-Incidents-in-Alert-Overload-1024x497.png)

  #### How to See Critical Incidents in Alert Overload: A Guide for SOCs and MSSPs

  332
  0](/cybersecurity-blog/fixing-alert-overload/)
* [![](/cybersecurity-blog/wp-content/uploads/2025/11/Detected-in-60-Seconds-1024x497.png)

  #### Detected in 60 Seconds: How to Identify Phishing with a Malware Sandbox

  846
  0](/cybersecurity-blog/60-seconds-phishing-analysis/)

[Home](/cybersecurity-blog/)[Malware Analysis](/cybersecurity-blog/category/malware-analysis/)

Major Cyber Attacks in November 2025: XWorm, JSGuLdr Loader, Phoenix Backdoor, Mobile Threats, and More

Stealers, loaders, and targeted campaigns dominated November’s activity. [ANY.RUN](https://any.run/?utm_source=anyrunblog&utm_medium=article&utm_campaign=major-cyber-attacks-november-2025&utm_term=261125&utm_content=linktolanding) analysts examined cases ranging from PNG-based in-memory loading used to deploy XWorm to JSGuLdr, a three-stage JavaScript-to-PowerShell loader pushing PhantomStealer.

Alongside these public cases, three Threat Intelligence Reports detailed new activity across Windows, Linux, and Android, including loader-enabled hijackers, Tor-based cryptotrojan communication, Linux ransomware in Go, MaaS stealers, and a WhatsApp-propagating campaign with geofencing controls.

Each case was analyzed inside [ANY.RUN’s Interactive Sandbox](https://any.run/features/?utm_source=anyrunblog&utm_medium=article&utm_campaign=major-cyber-attacks-november-2025&utm_term=261125&utm_content=linksandboxlanding), revealing execution flows, persistence mechanisms, and behavioral indicators that help teams tune detections and trace related activity.

Let’s break down how these attacks unfolded, where they hit, and what security teams can take away to strengthen their defenses before the next wave arrives.

## 1. XWorm: PNG Files Used as Containers for an In-Memory Loader

[Post on X](https://x.com/anyrun_app/status/1986072813984240018)

ANY.RUN analysts observed a new wave of XWorm infections in November, delivered through phishing pages and emails that distribute a JavaScript dropper named **PurchaseOrder\_25005092.js**. While it appears benign at first glance, the script unpacks a full multi-stage chain designed to bypass quick checks, hide payloads inside PNG files, and execute a .NET assembly directly in memory.

### How the attack begins

The campaign begins with a phishing lure **(T1566.001)** delivering a heavily obfuscated JavaScript installer **(T1027)**. Once executed, the script checks whether the required components exist on the system and writes the missing files to **C:\Users\PUBLIC** using Base64-encoded and AES-encrypted data **(T1027.013)**. The staged components are later used during the PowerShell-driven decryption and in-memory execution stages.

The three staged files are:

* **Kile.cmd:**A heavily obfuscated batch script filled with variable noise, percent-encoding, and fragmented Base64

* **Vile.png:**Not an image but a Base64-encoded and AES-encrypted payload

* **Mands.png**: Another encrypted data blob used during the second stage

Attackers deliberately use the “.png” extension (**T1036.008**) to make the files look harmless and evade quick manual reviews.

![](/cybersecurity-blog/wp-content/uploads/2025/11/image-1024x1024.jpg)

### In-memory execution chain

After writing the staged components to **C:\Users\PUBLIC**, the JavaScript dropper reconstructs readable commands from its fragments and launches a PowerShell payload **(T1059)**. This PowerShell script operates as a two-stage AES-CBC loader.

**Stage 1: Command runner**

Reads C:\Users\PUBLIC\Mands.png as Base64 → AES-decrypt → yields Base64-encoded commands. Each command is decoded and executed via Invoke-Expression, enabling the script to run attacker-controlled instructions without a traditional executable.

**Stage 2: In-memory assembly load**

Reads C:\Users\PUBLIC\Vile.png as Base64 → AES-decrypt → raw bytes. Loader attempts to execute the resulting .NET assembly directly from memory **(T1620)**.

This creates an in-memory loader that launches XWorm without dropping a traditional executable. A successful compromise enables credential theft, remote...
---
title: DBatLoader Delivers Remcos via UAC Bypass in New Phishing Campaign
url: https://any.run/cybersecurity-blog/dbatloader-drops-remcos/
source: Over Security - Cybersecurity news aggregator
date: 2025-05-23
fetch_date: 2025-10-06T22:30:13.935010
---

# DBatLoader Delivers Remcos via UAC Bypass in New Phishing Campaign

[![ANY.RUN's Cybersecurity Blog](/cybersecurity-blog/wp-content/uploads/2020/07/Logo-1.png)](/cybersecurity-blog/)

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

[![ANY.RUN's Cybersecurity Blog](/cybersecurity-blog/wp-content/uploads/2020/07/Logo-1.png)](/cybersecurity-blog/)

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

[![ANY.RUN's Cybersecurity Blog](/cybersecurity-blog/wp-content/uploads/2022/10/mini-logo.png)](/cybersecurity-blog/)

* + Search

![DBatLoader Delivers Remcos via .pif Files and UAC Bypass in New Phishing Campaign ](/cybersecurity-blog/wp-content/uploads/2025/05/dbatload_blog.jpg)

[News](/cybersecurity-blog/category/news/)

# DBatLoader Delivers Remcos via .pif Files and UAC Bypass in New Phishing Campaign

May 22, 2025

[Add comment](#comments-13839)
2830 views
4 min read

[Home](/cybersecurity-blog/)[News](/cybersecurity-blog/category/news/)

DBatLoader Delivers Remcos via .pif Files and UAC Bypass in New Phishing Campaign

#### Recent posts

* [![](/cybersecurity-blog/wp-content/uploads/2025/09/Release-notes-1024x497.png)

  #### Release Notes: Palo Alto Networks, Microsoft, IBM Connectors and 2,300+ Suricata Rules

  1616
  0](/cybersecurity-blog/release-notes-september-2025/)
* [![](/cybersecurity-blog/wp-content/uploads/2025/10/FunkLocker_blog-1024x497.jpg)

  #### FunkSec’s FunkLocker: How AI Is Powering the Next Wave of Ransomware

  3164
  0](/cybersecurity-blog/funklocker-malware-analysis/)
* [![](/cybersecurity-blog/wp-content/uploads/2025/09/defender_blog-1024x497.jpg)

  #### ANY.RUN & MS Defender: Enrich Alerts Faster, Stop Attacks Early

  3181
  0](/cybersecurity-blog/ms-defender-connectors/)

[Home](/cybersecurity-blog/)[News](/cybersecurity-blog/category/news/)

DBatLoader Delivers Remcos via .pif Files and UAC Bypass in New Phishing Campaign

A new phishing campaign is spreading the [Remcos](https://any.run/malware-trends/remcos) Remote Access Trojan ([RAT](https://any.run/malware-trends/rat)) through [DBatLoader](https://any.run/malware-trends/dbatloader). It employs User Account Control ([UAC](https://any.run/cybersecurity-blog/windows11-uac-bypass/)) bypass, obfuscated scripts, Living Off the Land Binaries (LOLBAS) abuse, and persistence mechanisms.

Here’s an analysis of the infection chain, key techniques, and detection tips.

## How the Attack Works

To see how the attack unfolds, we analyzed the sample inside [ANY.RUN’s Interactive Sandbox](https://any.run/?utm_source=anyrunblog&utm_medium=article&utm_campaign=dbatloader_phish_campaign&utm_term=220525&utm_content=linktolanding).

[View full execution and analysis](https://app.any.run/tasks/c57ca499-51f5-4c50-a91f-70bc5a60b98d/?utm_source=anyrunblog&utm_medium=article&utm_campaign=dbatloader_phish_campaign&utm_term=220525&utm_content=linktoservice)

The attack likely starts with a [phishing](https://any.run/cybersecurity-blog/investigating-phishing-threats/) email containing an archive.

![](/cybersecurity-blog/wp-content/uploads/2025/05/image-21-1024x582.png)

Inside it, there is a malicious executable named “FAKTURA”, which deploys DBatLoader on the system.

### **Use of .pif Files for Disguise and UAC Bypass**

DBatLoader uses .pif (Program Information File) files as a method of disguise and execution.

Originally intended for configuring how DOS-based programs should run in early Windows systems, .pif files have become obsolete for legitimate use. However, they are still executable on modern Windows versions, making them useful for attackers.

Windows treats .pif files similarly to .exe files. When executed, they can run without triggering warning dialogs, depending on system configuration.

![](/cybersecurity-blog/wp-content/uploads/2025/05/image5-1.png)

In the analysis, the malicious alpha.pif (a Portable Executable file) bypassed UAC by creating fake directories like “C:\Windows “ (note the empty space), exploiting Windows’s folder name handling to gain elevated privileges.

Get extra sandbox licenses for your team as a gift
Take advantage of ANY.RUN’s special offers before May 31

[See all offers](https://app.any.run/plans/?utm_source=anyrunblog&utm_medium=article&utm_campaign=dbatloader_phish_campaign&utm_term=220525&utm_content=linktoplans)

### **Evasion and Persistence: Ping Command and Scheduled Task**

One observed command line uses PING.EXE to ping the local loopback address (127.0.0.1) ten times. While legitimate programs may use this to test network connectivity by sending ICMP echo requests, malware like DBatLoader uses it to introduce artificial delays for time-based evasion.

![](/cybersecurity-blog/wp-content/uploads/2025/05/image6-1-1024x557.png)

In some cases, this technique can also be repurposed for remote system discovery.

The malicious svchost.pif file launched NEO.cmd through CMD, which then executed extrac32.exe to add a specific path to Windows Defender’s exclusion list, allowing it to evade further detection.

![](/cybersecurity-blog/wp-content/uploads/2025/05/image7-1-1024x604.png)

To maintain persistence and survive following reboots, DBatLoader abuses a scheduled task to trigger a Cmwdnsyn.url file, which launches a .pif dropper.

### **Obfuscation and Remcos Deployment**

![](/cybersecurity-blog/wp-content/uploads/2025/05/image8-1-1024x625.png)

The loader used .cmd files obfuscated with BatCloak to download and run Remcos.

![](/cybersecurity-blog/wp-content/uploads/2025/05/image9-1-1024x601.png)

*The sandbox flags the injected process and detects Remcos*

Remcos injects into trusted system processes SndVol.exe, colorcpl.exe or others, varying on each new instance, blending in with the rest of the processes.

## Spot Similar Attacks with Proactive Sandbox Analysis

Multi-stage attacks that utilize different means ...
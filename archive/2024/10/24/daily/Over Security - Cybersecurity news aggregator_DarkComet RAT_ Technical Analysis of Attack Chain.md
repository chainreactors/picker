---
title: DarkComet RAT: Technical Analysis of Attack Chain
url: https://any.run/cybersecurity-blog/darkcomet-rat-technical-analysis/
source: Over Security - Cybersecurity news aggregator
date: 2024-10-24
fetch_date: 2025-10-06T18:55:44.549204
---

# DarkComet RAT: Technical Analysis of Attack Chain

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

![DarkComet RAT: <br>Technical Analysis of Attack Chain](/cybersecurity-blog/wp-content/uploads/2024/10/darkcomet_blog.jpg)

[Malware Analysis](/cybersecurity-blog/category/malware-analysis/)

# DarkComet RAT: Technical Analysis of Attack Chain

October 23, 2024

[Add comment](#comments-9342)
6428 views
10 min read

[Home](/cybersecurity-blog/)[Malware Analysis](/cybersecurity-blog/category/malware-analysis/)

DarkComet RAT:
Technical Analysis of Attack Chain

#### Recent posts

* [![](/cybersecurity-blog/wp-content/uploads/2025/09/Release-notes-1024x497.png)

  #### Release Notes: Palo Alto Networks, Microsoft, IBM Connectors and 2,300+ Suricata Rules

  1395
  0](/cybersecurity-blog/release-notes-september-2025/)
* [![](/cybersecurity-blog/wp-content/uploads/2025/10/FunkLocker_blog-1024x497.jpg)

  #### FunkSec’s FunkLocker: How AI Is Powering the Next Wave of Ransomware

  3020
  0](/cybersecurity-blog/funklocker-malware-analysis/)
* [![](/cybersecurity-blog/wp-content/uploads/2025/09/defender_blog-1024x497.jpg)

  #### ANY.RUN & MS Defender: Enrich Alerts Faster, Stop Attacks Early

  3038
  0](/cybersecurity-blog/ms-defender-connectors/)

[Home](/cybersecurity-blog/)[Malware Analysis](/cybersecurity-blog/category/malware-analysis/)

DarkComet RAT:
Technical Analysis of Attack Chain

*Editor’s note: The current article is authored by Mostafa ElSheimy, a malware reverse engineer and threat intelligence analyst. You can find Mostafa on* [*X*](https://x.com/M4lcode) *and* [*LinkedIn*](https://www.linkedin.com/in/m4lcode)*.*

In this malware analysis report, we take an in-depth look at how the Remote Access Trojan (RAT) [DarkComet](https://any.run/malware-trends/darkcomet) has been used by attackers to remotely control systems, steal sensitive data, and execute various malicious activities.

## Overview

DarkComet is a Remote Access Trojan (RAT) initially developed by Jean-Pierre Lesueur in 2008. This malware runs silently in the background, collecting sensitive information about the system, users, and network activity.

It attempts to steal stored credentials, usernames, passwords, and other personal data, transmitting this information to a destination specified by the attacker.

Backdoor.DarkComet allows attackers to install further malicious software on the infected machine or enlist it in a botnet for sending spam or other malicious activities.

Symptoms of an infection may not be noticeable to the user, as it can disable antivirus programs and other Windows security features.

### Distribution methods include:

* Bundling with free software.

* Disguising as harmless programs in [emails](https://any.run/cybersecurity-blog/spearphishing-explained/).

* Exploiting software vulnerabilities on websites.

DarkComet became widely used due to its user-friendly graphical interface, which contributed to its popularity.

## Technical Details

Let’s run a sandbox analysis session using [ANY.RUN](https://any.run/?utm_source=anyrunblog&utm_medium=article&utm_campaign=darkcomet_analysis&utm_term=231024&utm_content=linktolanding) to discover the technical details of this malware.

[View analysis session](https://app.any.run/tasks/7f5f43ce-f9db-405a-8e4c-17e7bd3bfc19/?utm_source=anyrunblog&utm_medium=article&utm_campaign=darkcomet_analysis&utm_term=231024&utm_content=linktoservice)

### Changing file attributes

DarkComet uses a command-line operation to alter file attributes, making its components more difficult to detect.

![](/cybersecurity-blog/wp-content/uploads/2024/10/image-3-1024x758.png)

It uses **attrib** to display or change file attributes

1. **+s (System Attribute)**: Marks the file as a system file, making it appear as a critical part of the operating system.

2. **+h (Hidden Attribute)**: Hides the file from regular view in Windows Explorer, making it invisible to most users.

![](/cybersecurity-blog/wp-content/uploads/2024/10/image2-4-1024x743.png)

It drops an executable at C:\Users\admin\Documents\MSDCSC\msdcsc.exe and executes it, making it harder to detect.

Try advanced malware analysis with ANY.RUN for free

[Get 14-day trial](https://any.run/demo/?utm_source=anyrunblog&utm_medium=article&utm_campaign=darkcomet_analysis&utm_term=231024&utm_content=linktodemo)

### Contacting Malicious Domains

The malware establishes communication with a specified malicious domain, enabling remote control and data exfiltration.

![](/cybersecurity-blog/wp-content/uploads/2024/10/image3-5-1024x117.png)

### Modifying Process Privileges

The malware interacts with the Windows APIs **LookupPrivilegeValueA** and **AdjustTokenPrivileges** to modify the privileges associated with the current process’s access token (not the process itself).

This is done by obtaining a handle to the process’s access token, which allows the malware to modify its security context.

![](/cybersecurity-blog/wp-content/uploads/2024/10/image4-2-1024x487.png)

* If a2 is 0, the privilege is removed (Attributes = 0).

* If a2 is 1, the privilege is enabled (Attributes = 2).

## Gathering System Information

### Retrieving Hardware Profile

![](/cybersecurity-blog/wp-content/uploads/2024/10/image5-3-1024x313.png)

DarkComet uses the **GetCurrentHwProfileA** API to collect detailed information about the infected system’s hardware:

* **Har...
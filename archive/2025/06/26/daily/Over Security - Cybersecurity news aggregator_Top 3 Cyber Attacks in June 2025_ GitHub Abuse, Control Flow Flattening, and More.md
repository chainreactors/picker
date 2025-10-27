---
title: Top 3 Cyber Attacks in June 2025: GitHub Abuse, Control Flow Flattening, and More
url: https://any.run/cybersecurity-blog/cyber-attacks-june-2025/
source: Over Security - Cybersecurity news aggregator
date: 2025-06-26
fetch_date: 2025-10-06T22:55:02.523555
---

# Top 3 Cyber Attacks in June 2025: GitHub Abuse, Control Flow Flattening, and More

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

![Top 3 Cyber Attacks in June 2025: GitHub Abuse, Control Flow Flattening, and More ](/cybersecurity-blog/wp-content/uploads/2025/06/june_attacks_blog.jpg)

[Malware Analysis](/cybersecurity-blog/category/malware-analysis/)

# Top 3 Cyber Attacks in June 2025: GitHub Abuse, Control Flow Flattening, and More

June 25, 2025

[Add comment](#comments-14463)
36287 views
7 min read

[Home](/cybersecurity-blog/)[Malware Analysis](/cybersecurity-blog/category/malware-analysis/)

Top 3 Cyber Attacks in June 2025: GitHub Abuse, Control Flow Flattening, and More

#### Recent posts

* [![](/cybersecurity-blog/wp-content/uploads/2025/09/Release-notes-1024x497.png)

  #### Release Notes: Palo Alto Networks, Microsoft, IBM Connectors and 2,300+ Suricata Rules

  1637
  0](/cybersecurity-blog/release-notes-september-2025/)
* [![](/cybersecurity-blog/wp-content/uploads/2025/10/FunkLocker_blog-1024x497.jpg)

  #### FunkSec’s FunkLocker: How AI Is Powering the Next Wave of Ransomware

  3168
  0](/cybersecurity-blog/funklocker-malware-analysis/)
* [![](/cybersecurity-blog/wp-content/uploads/2025/09/defender_blog-1024x497.jpg)

  #### ANY.RUN & MS Defender: Enrich Alerts Faster, Stop Attacks Early

  3197
  0](/cybersecurity-blog/ms-defender-connectors/)

[Home](/cybersecurity-blog/)[Malware Analysis](/cybersecurity-blog/category/malware-analysis/)

Top 3 Cyber Attacks in June 2025: GitHub Abuse, Control Flow Flattening, and More

June 2025 saw several sophisticated and stealthy cyber attacks that relied heavily on obfuscated scripts, abuse of legitimate services, and multi-stage delivery techniques. Among the key threats observed by ANY.RUN’s analysts were malware campaigns using GitHub for payload hosting, JavaScript employing control-flow flattening to drop Remcos, and obfuscated BAT scripts delivering NetSupport RAT. Let’s see how ANY.RUN’s [Interactive Sandbox](https://any.run/?utm_source=anyrunblog&utm_medium=article&utm_campaign=cyberattacks_june_25&utm_term=250625&utm_content=linktolanding) and [Threat Intelligence Lookup](https://any.run/threat-intelligence-lookup/?utm_source=anyrunblog&utm_medium=article&utm_campaign=cyberattacks_june_25&utm_term=250625&utm_content=linktotilookupanding) can help security teams detect, investigate, and understand these threats.

## 1. Braodo Stealer Abuses GitHub for Payload Staging and Hosting

[Original post on X](https://x.com/anyrun_app/status/1935359366036635915/photo/1) and [LinkedIn](https://www.linkedin.com/posts/any-run_braodo-malware-github-activity-7341125061149454355-KKBC?utm_source=share&utm_medium=member_desktop&rcm=ACoAAE8fxWoBjRQuEUnJBJlt9oH6kqphHT7Telw)

A new campaign distributing Braodo stealer leverages public GitHub repository, including raw file content, to host payloads. The primary goal of this stealer is data exfiltration, and at the time of analysis, its detection rate was low. The BAT files used in the campaign include misleading comments to complicate analysis.

ANY.RUN’s [Script Tracer](https://any.run/cybersecurity-blog/script-tracer/) simplifies the analysis by logging the multi-stage execution flow step by step, without the need for manual deobfuscation. Let’s take a closer look at this threat’s behavior using ANY.RUN Interactive Sandbox, which provides full visibility into process activity and persistence mechanisms.

[View analysis](https://app.any.run/tasks/75be7fd8-8984-4b54-bd18-c98305cc94a8/?utm_source=anyrunblog&utm_medium=article&utm_campaign=cyberattacks_june_25&utm_term=250625&utm_content=linktoservice)

![](/cybersecurity-blog/wp-content/uploads/2025/06/imagec-6-1024x497.png)

The first BAT file executes a CMD command that launches [PowerShell](https://any.run/cybersecurity-blog/powershell-script-tracer/) in hidden mode to avoid displaying a visible window. It then downloads a second BAT file from github[.]com, disguised as a .PNG file, saves it to the %temp% folder, and executes it.

![This image has an empty alt attribute; its file name is image2-7.png](/cybersecurity-blog/wp-content/uploads/2025/06/image2-7.png)

The second BAT file launches a new PowerShell script file, that removes components from the earlier stages, enforces TLS 1.2, retrieves an additional payload from raw.githubusercontent[.]com, saving it in the Startup folder, and downloads main payload in a ZIP file. This behavior is captured in ANY.RUN’s Script Tracer.

![](/cybersecurity-blog/wp-content/uploads/2025/06/image3-7.png)

The final payload, Braodo Stealer, is extracted from a ZIP file, stored in the Public directory, and executed using python.exe. After execution, it deletes the initial archive to reduce artifacts. The Python file is obfuscated with pyobfuscate and contains non-encrypted, custom Base64-encoded payload strings appended to the script.

![](/cybersecurity-blog/wp-content/uploads/2025/06/image4-—-крупный-размер-768x1024.png)

ANY.RUN’s Threat Intelligence Lookup allows analysts to discover recent Braodo attacks and fresh samples of this stealer dissected by the users of the Interactive Sandbox. Search by the malware’s name and view analyses:

[threatName:”Braodo”](https://intelligence.any.run/analysis/lookup/?utm_source=anyrunblog&utm_medium=article&utm_campaign=cyberattacks_june_25&utm_term=250625&utm_content=linktotilookup#%7B%2522query%2522:%2522t...
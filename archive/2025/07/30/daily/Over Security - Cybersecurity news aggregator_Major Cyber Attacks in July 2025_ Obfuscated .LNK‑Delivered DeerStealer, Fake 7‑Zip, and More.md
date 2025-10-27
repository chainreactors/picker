---
title: Major Cyber Attacks in July 2025: Obfuscated .LNK‑Delivered DeerStealer, Fake 7‑Zip, and More
url: https://any.run/cybersecurity-blog/cyber-attacks-july-2025/
source: Over Security - Cybersecurity news aggregator
date: 2025-07-30
fetch_date: 2025-10-06T23:54:01.053811
---

# Major Cyber Attacks in July 2025: Obfuscated .LNK‑Delivered DeerStealer, Fake 7‑Zip, and More

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

![Major Cyber Attacks in July 2025: Obfuscated .LNK‑Delivered DeerStealer, Fake 7‑Zip, and More](/cybersecurity-blog/wp-content/uploads/2025/07/july_attacks_25_blog.jpg)

[Malware Analysis](/cybersecurity-blog/category/malware-analysis/)

# Major Cyber Attacks in July 2025: Obfuscated .LNK‑Delivered DeerStealer, Fake 7‑Zip, and More

July 29, 2025

[Add comment](#comments-15111)
6092 views
7 min read

[Home](/cybersecurity-blog/)[Malware Analysis](/cybersecurity-blog/category/malware-analysis/)

Major Cyber Attacks in July 2025: Obfuscated .LNK‑Delivered DeerStealer, Fake 7‑Zip, and More

#### Recent posts

* [![](/cybersecurity-blog/wp-content/uploads/2025/09/Release-notes-1024x497.png)

  #### Release Notes: Palo Alto Networks, Microsoft, IBM Connectors and 2,300+ Suricata Rules

  1763
  0](/cybersecurity-blog/release-notes-september-2025/)
* [![](/cybersecurity-blog/wp-content/uploads/2025/10/FunkLocker_blog-1024x497.jpg)

  #### FunkSec’s FunkLocker: How AI Is Powering the Next Wave of Ransomware

  3178
  0](/cybersecurity-blog/funklocker-malware-analysis/)
* [![](/cybersecurity-blog/wp-content/uploads/2025/09/defender_blog-1024x497.jpg)

  #### ANY.RUN & MS Defender: Enrich Alerts Faster, Stop Attacks Early

  3267
  0](/cybersecurity-blog/ms-defender-connectors/)

[Home](/cybersecurity-blog/)[Malware Analysis](/cybersecurity-blog/category/malware-analysis/)

Major Cyber Attacks in July 2025: Obfuscated .LNK‑Delivered DeerStealer, Fake 7‑Zip, and More

While cybercriminals were working overtime this July, so were we at ANY.RUN — and, dare we say, with better results. As always, we’ve picked the most dangerous and intriguing attacks of the month. But this time, there’s more.

Alongside the monthly top, we are highlighting a key trend that’s been powering campaigns throughout 2025: the top 5 Remote Access Tools most abused by threat actors in the first half of the year.

The threats were investigated with ANY.RUN’s [Interactive Sandbox](https://any.run/?utm_source=anyrunblog&utm_medium=article&utm_campaign=major_attacks_july_25&utm_term=290725&utm_content=linktolanding), where you can trace the full attack chain and see malware behavior in action, and our [Threat Intelligence Lookup](https://intelligence.any.run/analysis/lookup/?utm_source=anyrunblog&utm_medium=article&utm_campaign=major_attacks_july_25&utm_term=290725&utm_content=linktolookup) (available now for free), which helps you turn raw IOCs into actionable intelligence to better protect your organization.

## DeerStealer Delivered via Obfuscated .LNK and LOLBin Abuse

[Post On X](https://x.com/anyrun_app/status/1945836857431834957)

![](/cybersecurity-blog/wp-content/uploads/2025/07/image-1-768x1024.jpg)

The recent phishing campaign delivers malware through a fake PDF shortcut (*Report.lnk*) that leverages *mshta.exe* for script execution, which is a known LOLBin technique ([MITRE T1218.005](https://attack.mitre.org/techniques/T1218/005/)).

ANY.RUN’s [Script Tracer](https://any.run/cybersecurity-blog/script-tracer/) reveals the full chain, including wildcard LOLBin execution, encoded payloads, and network exfiltration, without requiring manual deobfuscation.

[View analysis session in the Sandbox](https://app.any.run/tasks/02dd6096-b621-49a0-a7ef-4758cc957c0f/?utm_source=anyrunblog&utm_medium=article&utm_campaign=major_attacks_july_25&utm_term=290725&utm_content=linktoservice)

The attack begins with a *.lnk* file that covertly invokes *mshta.exe* to drop scripts for the next stages. The execution command is heavily obfuscated using wildcard paths.

![](/cybersecurity-blog/wp-content/uploads/2025/07/image-14-1024x499.png)

To evade signature-based detection, PowerShell dynamically resolves the full path to *mshta.exe* in the System32 directory. It is launched with flags, followed by obfuscated Base64 strings. Both logging and profiling are disabled to reduce forensic visibility during execution.

Characters are decoded in pairs, converted from hex to ASCII, reassembled into a script, and executed via IEX. This ensures the malicious logic stays hidden until runtime.

The script dynamically resolves URLs and binary content from obfuscated arrays, downloads a fake PDF to distract the user, writes the main executable into *AppData*, and silently runs it. The PDF is opened in Adobe Acrobat to distract the user.

You can use Threat Intelligence Lookup to find malware samples using similar techniques with fake *.lnk* files and PowerShell commands to enrich your company’s detection systems.

Search for suspicious shortcut attachments: [threatName:”susp-lnk”](https://intelligence.any.run/analysis/lookup/?utm_source=anyrunblog&utm_medium=article&utm_campaign=major_attacks_july_25&utm_term=290725&utm_content=linktotilookup#%7B%2522query%2522:%2522threatName:%255C%2522susp-lnk%255C%2522%2522,%2522dateRange%2522:180%7D)

![](/cybersecurity-blog/wp-content/uploads/2025/07/image2-8-1024x391.png)

Query TI Lookup for a snippet in PowerShell command: [commandLine:”| IEX”](https://intelligence.any.run/analysis/lookup#{%22query%22:%22commandLine:%5C%22|%20IEX%5C%22%22,%22dateRange%22:180})

![](/cybersecurity-blog/wp-content/uploads/2025/07/image3-3-1024x538.png)

IOC for the threat detection and research:

* https[:]//tripplefury[.]com/

* Fd5a2f9eed065c...
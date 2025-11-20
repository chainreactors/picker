---
title: LOLBin Attacks Explained with Examples: Everything SOC Teams Need to Know
url: https://any.run/cybersecurity-blog/lolbin-attacks-soc-detection-guide/
source: Over Security - Cybersecurity news aggregator
date: 2025-11-19
fetch_date: 2025-11-20T03:10:06.532821
---

# LOLBin Attacks Explained with Examples: Everything SOC Teams Need to Know

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

![LOLBin Attacks Explained with Examples: Everything SOC Teams Need to Know ](/cybersecurity-blog/wp-content/uploads/2025/11/LOLBin-Attacks-101.png)

[Malware Analysis](/cybersecurity-blog/category/malware-analysis/)

# LOLBin Attacks Explained with Examples: Everything SOC Teams Need to Know

November 19, 2025

[Add comment](#comments-16931)
659 views
9 min read

[Home](/cybersecurity-blog/)[Malware Analysis](/cybersecurity-blog/category/malware-analysis/)

LOLBin Attacks Explained with Examples: Everything SOC Teams Need to Know

#### Recent posts

* [![](/cybersecurity-blog/wp-content/uploads/2025/11/LOLBin-Attacks-101-1024x497.png)

  #### LOLBin Attacks Explained with Examples: Everything SOC Teams Need to Know

  659
  0](/cybersecurity-blog/lolbin-attacks-soc-detection-guide/)
* [![](/cybersecurity-blog/wp-content/uploads/2025/11/Success-story-about-healthcare-1024x497.png)

  #### Healthcare MSSP Cuts Phishing Triage by 76% and Launches Proactive Defense with ANY.RUN

  358
  0](/cybersecurity-blog/healthcare-mssp-success-story/)
* [![](/cybersecurity-blog/wp-content/uploads/2025/11/Solve-Alert-Fatigue-in-Your-SOC-1024x497.png)

  #### Solve Alert Fatigue, Focus on High-Risk Incidents: An Action Plan for CISOs

  931
  0](/cybersecurity-blog/solve-alert-fatigue-in-your-soc/)

[Home](/cybersecurity-blog/)[Malware Analysis](/cybersecurity-blog/category/malware-analysis/)

LOLBin Attacks Explained with Examples: Everything SOC Teams Need to Know

Some attacks smash the door open. LOLBins just borrow your keys and walk right in.

They’re tricky because tools everyone trusts suddenly start doing things that don’t match their usual job; loading odd-looking modules, decoding files that shouldn’t need decoding, or quietly handing work off to hidden [PowerShell scripts](https://any.run/cybersecurity-blog/powershell-script-tracer/). At first glance it all feels normal, but a closer look shows a payload slowly being set up in the background.

For analysts, the real challenge is noticing that shift before it grows into a full incident.

Let’s take a closer look at what’s hiding behind LOLBin attacks, and how advanced SOC teams uncover them in minutes without much effort.

## What Are LOLBin Attacks?

LOLBin attacks occur when threat actors repurpose legitimate Windows system binaries (rundll32, certutil, mshta, powershell, regsvr32, etc.) to carry out malicious actions. These tools are built into every system, signed by Microsoft, and widely used by normal applications, which is why attackers rely on them.

Using LOLBins, adversaries can:

* Load disguised or renamed DLLs

* Decode or unpack payloads using built-in utilities

* Trigger PowerShell or script execution indirectly

* Execute code completely in memory

* Blend malicious steps into routine system activity

This approach lets attackers avoid dropping obvious malware and makes early-stage execution appear clean and legitimate.

## Why LOLBin Attacks Are a Real Risk for Businesses?

![](/cybersecurity-blog/wp-content/uploads/2025/11/2-1-1024x576.png)

The real problem isn’t the binaries themselves but how much **visibility your SOC loses** when attackers hide behind them. When malicious activity runs inside trusted system tools, the early signs of an intrusion become dramatically harder to catch.

Here’s what makes them dangerous:

* **Normal on the surface:** Activity is routed through tools the environment already trusts.

* **Minimal forensic evidence:** In-memory execution leaves few files to investigate.

* **Weak signature coverage:** Microsoft-signed binaries rarely trigger basic detection rules.

* **Extended dwell time:** Attackers gain more space for lateral movement and credential access.

* **Harder investigations:** Clean-looking events force analysts to dig deeper to find the real issue.

* **Higher SOC workload:** The team must identify subtle behavior shifts instead of relying on clear indicators.

This means attackers can establish footholds, unpack payloads, or run loaders while the environment still appears clean, leading to late detection and higher incident impact.

## The Fastest Way to Reveal LOLBin Abuse: How ANY.RUN Makes It Obvious

LOLBin attacks only work when no one can see what’s really happening behind those trusted Windows binaries. [ANY.RUN](https://any.run/?utm_source=anyrunblog&utm_medium=article&utm_campaign=LOLBin_attacks_101&utm_term=191125&utm_content=linktolanding) removes that advantage by showing analysts the full behavior in real time; not just the file name or the process label, but the actual actions taking place underneath.

With [ANY.RUN’s sandbox](https://any.run/features/?utm_source=anyrunblog&utm_medium=article&utm_campaign=LOLBin_attacks_101&utm_term=191125&utm_content=linksandboxlanding), “normal-looking” activity turns into something you can spot immediately:

* **Process behavior becomes clear at a glance:** rundll32 loading a strange module, certutil decoding an unexpected file, mshta spawning hidden PowerShell… every unusual step is visible right away.

* **Parent–child chains tell the full story:** Instead of digging through logs, you see exactly who launched what, and whether it fits normal usage patterns.

* **Command lines show the truth:** E...
---
title: How DFIR Analysts Use ANY.RUN Sandbox
url: https://any.run/cybersecurity-blog/sandbox-use-cases-for-dfir/
source: Over Security - Cybersecurity news aggregator
date: 2024-12-19
fetch_date: 2025-10-06T19:41:18.029561
---

# How DFIR Analysts Use ANY.RUN Sandbox

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

![How DFIR Analysts Use ANY.RUN Sandbox](/cybersecurity-blog/wp-content/uploads/2024/12/dfir_blog.jpg)

[Cybersecurity Lifehacks](/cybersecurity-blog/category/lifehacks/)

# How DFIR Analysts Use ANY.RUN Sandbox

December 18, 2024

[Add comment](#comments-10532)
1649 views
8 min read

[Home](/cybersecurity-blog/)[Cybersecurity Lifehacks](/cybersecurity-blog/category/lifehacks/)

How DFIR Analysts Use ANY.RUN Sandbox

#### Recent posts

* [![](/cybersecurity-blog/wp-content/uploads/2025/09/Release-notes-1024x497.png)

  #### Release Notes: Palo Alto Networks, Microsoft, IBM Connectors and 2,300+ Suricata Rules

  1416
  0](/cybersecurity-blog/release-notes-september-2025/)
* [![](/cybersecurity-blog/wp-content/uploads/2025/10/FunkLocker_blog-1024x497.jpg)

  #### FunkSec’s FunkLocker: How AI Is Powering the Next Wave of Ransomware

  3028
  0](/cybersecurity-blog/funklocker-malware-analysis/)
* [![](/cybersecurity-blog/wp-content/uploads/2025/09/defender_blog-1024x497.jpg)

  #### ANY.RUN & MS Defender: Enrich Alerts Faster, Stop Attacks Early

  3061
  0](/cybersecurity-blog/ms-defender-connectors/)

[Home](/cybersecurity-blog/)[Cybersecurity Lifehacks](/cybersecurity-blog/category/lifehacks/)

How DFIR Analysts Use ANY.RUN Sandbox

Recently, DFIR consultant & content creator/educator [Steven from the YouTube channel MyDFIR](https://www.youtube.com/%40MyDFIR/videos)released a [new video](https://www.youtube.com/watch?v=6csFShaEHrk) showing how DFIR professionals can leverage the [ANY.RUN Sandbox](https://any.run/?utm_source=anyrunblog&utm_medium=article&utm_campaign=dfir_use_cases&utm_term=181224&utm_content=linktolanding) to efficiently analyze malware and extract actionable intelligence.

The video provides a step-by-step guide on investigating real-world threats, including how to quickly identify and analyze [Indicators of Compromise](https://any.run/cybersecurity-blog/how-to-collect-iocs-in-sandbox/) (IOCs) and uncover key behavioral insights.

If you’re looking to improve your investigation workflows and see practical examples of malware analysis in action, we highly recommend watching the video to follow along with the expert’s process.

Here’s our overview of the key highlights covered in the video.

## About ANY.RUN Sandbox

The [ANY.RUN Sandbox](https://any.run/?utm_source=anyrunblog&utm_medium=article&utm_campaign=dfir_use_cases&utm_term=181224&utm_content=linktolanding) is an [interactive](https://any.run/cybersecurity-blog/interactive-malware-sandbox/) malware analysis platform that enables security professionals to analyze malicious files in a live, user-driven environment. It allows DFIR professionals to:

* Uncover the behaviors and tactics of malware.
* Quickly gather critical Indicators of Compromise (IOCs).
* Explore malware configurations and identify threats in real time.

By providing detailed insights through features like process trees, network monitoring, and integrated [ATT&CK mapping](https://any.run/cybersecurity-blog/mitre-ttps-in-ti-lookup/), ANY.RUN helps analysts stay ahead of emerging threats and streamline investigations.

Analyze malware and phishing threats
in ANY.RUN’s Interactive Sandbox for free

[Sign up now](https://app.any.run/?utm_source=anyrunblog&utm_medium=article&utm_campaign=dfir_use_cases&utm_term=181224&utm_content=linktoregistration#register)

## Use Case 1: Investigating Formbook Infostealer

Formbook is a widespread infostealer that targets credentials, cookies, and other sensitive data. Here’s how DFIR professionals can use [ANY.RUN](https://app.any.run/?utm_source=anyrunblog&utm_medium=article&utm_campaign=dfir_use_cases&utm_term=181224&utm_content=linktoregistration#register) to analyze it.

Imagine you have received the following alert: malware detected and quarantined.

The alert also provides details such as:

* Hostname: SALESPC-01
* User: Bobby
* Filename: suchost.exe
* Current Directory: C:\Users\Bobby\Downloads
* SHA256: 472a703381c8fe89f83b0fe4d7960b0942c5694054ba94dd85c249c4c702e0cd

Use this information to initiate your investigation.

### Check Previous Analyses

The first thing you should do is check if ANY.RUN analyzed this file previously. Navigate to ANY.RUN’s [*Reports* section](https://app.any.run/submissions/?utm_source=anyrunblog&utm_medium=article&utm_campaign=dfir_use_cases&utm_term=181224&utm_content=linktoreports), located on the left-hand side.

![](/cybersecurity-blog/wp-content/uploads/2024/12/image-10-1024x580.png)

Search for the hash of the flagged file. If the file has already been analyzed, review the existing reports. Otherwise, upload the file to initiate a fresh analysis.

In our case, there are 2 analysis sessions found from October 2024. Let’s choose the first report and look closer at what’s inside.

After clicking on the existing entry, you’ll be redirected to the ANY.RUN sandbox presented with a lot of useful information.

![](/cybersecurity-blog/wp-content/uploads/2024/12/imagea-1-1024x603.png)

Let’s use [this analysis](https://app.any.run/tasks/488981a6-2681-4efc-ab96-00215d866a56) to see how the sandbox can help us.

### Examine Initial Results

ANY.RUN provides an overview of the analysis, including malicious activity indicators, the operating system used for analysis (e.g., Windows 10 64-bit), and a suit...
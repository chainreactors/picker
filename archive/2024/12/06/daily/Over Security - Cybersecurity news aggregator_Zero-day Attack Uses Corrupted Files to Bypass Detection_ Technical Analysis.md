---
title: Zero-day Attack Uses Corrupted Files to Bypass Detection: Technical Analysis
url: https://any.run/cybersecurity-blog/corrupted-files-attack/
source: Over Security - Cybersecurity news aggregator
date: 2024-12-06
fetch_date: 2025-10-06T19:41:21.614916
---

# Zero-day Attack Uses Corrupted Files to Bypass Detection: Technical Analysis

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

![Zero-day Attack Uses Corrupted Files to Bypass Detection: Technical Analysis](/cybersecurity-blog/wp-content/uploads/2024/12/zeroday_blog_new.jpg)

[Malware Analysis](/cybersecurity-blog/category/malware-analysis/)

# Zero-day Attack Uses Corrupted Files to Bypass Detection: Technical Analysis

December 5, 2024

[Add comment](#comments-10226)
10227 views
7 min read

[Home](/cybersecurity-blog/)[Malware Analysis](/cybersecurity-blog/category/malware-analysis/)

Zero-day Attack Uses Corrupted Files to Bypass Detection: Technical Analysis

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

[Home](/cybersecurity-blog/)[Malware Analysis](/cybersecurity-blog/category/malware-analysis/)

Zero-day Attack Uses Corrupted Files to Bypass Detection: Technical Analysis

Recently, our analyst team [shared their research](https://x.com/anyrun_app/status/1861024182210900357) into a **zero-day attack** involving the use of corrupted malicious files to bypass static detection systems. Now, we present a technical analysis of this method and its mechanics.

In this article, we will:

* Demonstrate how attackers corrupt archives, office documents, and other files
* Explain how this method successfully evades detection by security systems
* Show how corrupted files get recovered by their native applications

Let’s get started.

## Sandbox Analysis of a Corrupted File Attack

To first see how such attacks unfold, we can upload one of the corrupted filles used by attackers to [ANY.RUN’s sandbox](https://any.run/?utm_source=anyrunblog&utm_medium=article&utm_campaign=corrupted_files&utm_term=051224&utm_content=linktolanding).

[View analysis session](https://app.any.run/tasks/f0c1fe95-8165-4015-bb58-d9b38a8e9486/?utm_source=anyrunblog&utm_medium=article&utm_campaign=corrupted_files&utm_term=051224&utm_content=linktoservice).

![](/cybersecurity-blog/wp-content/uploads/2024/12/image-2-1024x579.png)

Thanks to its interactivity, the sandbox lets us simulate a real scenario of user opening the broken malicious file inside the file’s **corresponding application**.

![](/cybersecurity-blog/wp-content/uploads/2024/12/image2-2.png)

In our case, it’s a docx file. When we open it with Word, the program immediately offers us the option to **recover the content of the file** and successfully does it.

![](/cybersecurity-blog/wp-content/uploads/2024/12/image3-1-1024x579.png)

Inside, we find a **QR code with a phishing link**. The sandbox also automatically detects malicious activity and notifies us about this.

Analyze emerging and persistent cyber threats safely

with ANY.RUN’s Interactive Sandbox

[Sign up free](https://app.any.run/?utm_source=anyrunblog&utm_medium=article&utm_campaign=corrupted_files&utm_term=051224&utm_content=linktoregistration#register/)

## How Corrupted Files Bypass Antivirus Software and Other Automated Solutions

Analysis inside the ANY.RUN sandbox showed how a corrupted file gets restored thanks to Word’s **built-in recovery mechanisms**, which allows us to identify its malicious nature.

![](/cybersecurity-blog/wp-content/uploads/2024/12/image4-2-1024x153.png)

Yet, [if we submit the same corrupted file to VirusTotal](https://www.virustotal.com/gui/file/3245ca6c7f9f78e6b8fc0f05e7821e4b4e0d1abf24719d9457a7640f3f447c58?nocache=1), which provides verdicts from numerous security solutions, we will see **zero threat detections**. The question is why?

The answer is simple: **most antivirus software and automated tools are** **not equipped with the recovery functionality** that is found in applications, such as Word. This prevents them from accurately identifying the type of the corrupted file, resulting in a **failure to detect and mitigate the threat**.

Docx is not the only file format used by attackers. There are also **corrupted archives with malicious files inside**, which easily bypass spam filters because security systems cannot view their contents due to corruption.

Once downloaded onto a system, tools like **WinRAR easily restore the damaged archive**, making its contents available to the victim.

Now, let’s see how exactly it works on a technical level.

## Technical Analysis of a Corrupted Word Document

### The Structure of a Word Document

Since the mid-2000s, office documents (OpenOffice.org 2.0 — released in 2005) have been **structured as archives** containing the document’s content.

In the image below, you can see the structure of a Word document.

![](/cybersecurity-blog/wp-content/uploads/2024/12/zeroday_info_one-794x1024.png)

As we can see, all structures within this archive are interconnected, and this relationship **begins from the end**.

At the end of ...
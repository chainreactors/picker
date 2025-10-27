---
title: AsyncRAT’s Infection Tactics via Open Directories: Technical Analysis
url: https://any.run/cybersecurity-blog/asyncrat-open-directories-infection-analysis/
source: Over Security - Cybersecurity news aggregator
date: 2024-11-08
fetch_date: 2025-10-06T19:22:55.580593
---

# AsyncRAT’s Infection Tactics via Open Directories: Technical Analysis

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

![AsyncRAT’s Infection Tactics <br>via Open Directories: Technical Analysis ](/cybersecurity-blog/wp-content/uploads/2024/11/asyrat_blog.jpg)

[Malware Analysis](/cybersecurity-blog/category/malware-analysis/)

# AsyncRAT’s Infection Tactics via Open Directories: Technical Analysis

November 7, 2024

[Add comment](#comments-9695)
4035 views
8 min read

[Home](/cybersecurity-blog/)[Malware Analysis](/cybersecurity-blog/category/malware-analysis/)

AsyncRAT’s Infection Tactics
via Open Directories: Technical Analysis

#### Recent posts

* [![](/cybersecurity-blog/wp-content/uploads/2025/09/Release-notes-1024x497.png)

  #### Release Notes: Palo Alto Networks, Microsoft, IBM Connectors and 2,300+ Suricata Rules

  1408
  0](/cybersecurity-blog/release-notes-september-2025/)
* [![](/cybersecurity-blog/wp-content/uploads/2025/10/FunkLocker_blog-1024x497.jpg)

  #### FunkSec’s FunkLocker: How AI Is Powering the Next Wave of Ransomware

  3024
  0](/cybersecurity-blog/funklocker-malware-analysis/)
* [![](/cybersecurity-blog/wp-content/uploads/2025/09/defender_blog-1024x497.jpg)

  #### ANY.RUN & MS Defender: Enrich Alerts Faster, Stop Attacks Early

  3055
  0](/cybersecurity-blog/ms-defender-connectors/)

[Home](/cybersecurity-blog/)[Malware Analysis](/cybersecurity-blog/category/malware-analysis/)

AsyncRAT’s Infection Tactics
via Open Directories: Technical Analysis

*Editor’s note: The current article is authored by RacWatchin8872, who is a threat intelligence analyst. You can find him on* [*X*](https://x.com/RacWatchin8872)*.*

This article covers two distinct methods used to infect systems with AsyncRAT via open directories. These techniques show how attackers are constantly adapting, finding new ways to use publicly accessible files to broaden AsyncRAT’s impact and reach.

## Overview

[AsyncRAT](https://any.run/malware-trends/asyncrat) is a type of [Remote Access Trojan](https://any.run/malware-trends/rat) (RAT) malware designed to stealthily infiltrate systems and give attackers remote control over infected devices. It is commonly used for spying, data theft, and manipulation of compromised systems.

Recently, two open directories surfaced, each employing unique methods to distribute and infect victims with AsyncRAT. These techniques highlight the persistent threat posed by this malware and its diverse infection strategies.

## First Technique

### Open Directory

While investigating malicious open directories exposed to the internet, I discovered one with an unusual structure.

The directory contained the following files:

* A text file with an extensive string that turned out to be a [VBS script](https://any.run/cybersecurity-blog/macros-in-malware/)

* A JPG file that was actually a disguised ZIP archive

![](/cybersecurity-blog/wp-content/uploads/2024/11/image1.png)

### Analysis of the Txt file

The text file’s extensive string conceals an obfuscated VBS script. It uses random variables to store parts of the text that will be used to download the JPG file.

![](/cybersecurity-blog/wp-content/uploads/2024/11/image2-2-1024x417.png)

To make it easier to read we just need to make a few changes:

1. Replace the variables with the actual text

2. Use intuitive names for variables that are used to write or download files

![](/cybersecurity-blog/wp-content/uploads/2024/11/image3-3-1024x498.png)

Now we see that the VBS script creates an XML file **OMjRRRRRRRRRRRRRRRRRRRRvbK.xml** located at **C:\Users\Public**. The content of the XML file contains a PowerShell script that downloads the disguised JPG file, saves it, and extracts it to the same directory.

Once extracted, the process continues by executing another script, **TesKKKeLAvaYdAfbBS.vbs.** Then, it cleans up by deleting both the XML and ZIP files.

### Analysis of the VBS file

The VBS script is also obfuscated and uses the same technique as the other text file. By examining the file, we can understand a few parts of its execution:

![](/cybersecurity-blog/wp-content/uploads/2024/11/image4-2-1024x450.png)

To make it simple to read, we just need to make a few changes:

1. Replace the variables with the actual text

2. Use intuitive names for variables that are in use

3. Delete all the If statements that execute the same code regardless of the result

By making these changes, we can transform a 34-line VBS script into a simpler 6-line version that is easier to read.

![](/cybersecurity-blog/wp-content/uploads/2024/11/image5-1.png)

The VBS script will then execute the **KKKKKKllLavIOOOOOtesAA.bat**, which is the next stage.

Analyze malware and see detailed script execution
inside ANY.RUN’s Interactive Sandbox

[Try it now](https://app.any.run/?utm_source=anyrunblog&utm_medium=article&utm_campaign=asyncrat_analysis&utm_term=071124&utm_content=linktoregistration#register/)

### Analysis of the Bat file

The BAT script is also obfuscated, but it is possible to understand its purpose by reading the values stored inside the variables vertically.

![](/cybersecurity-blog/wp-content/uploads/2024/11/image6-1-1024x491.png)

*Figure *6*: KKKKKKllLavIOOOOOtesAA.bat file*

Its role is to execute PowerShell without a prompt window. It initiates the next stage by running **KiLOvBeRNdautESaatnENn.ps1**

### Analysis of the PowerShell (PS1) file

The PS1 fil...
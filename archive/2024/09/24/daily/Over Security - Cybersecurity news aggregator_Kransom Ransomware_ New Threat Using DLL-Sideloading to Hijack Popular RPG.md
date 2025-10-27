---
title: Kransom Ransomware: New Threat Using DLL-Sideloading to Hijack Popular RPG
url: https://any.run/cybersecurity-blog/kransom-abuses-rpg/
source: Over Security - Cybersecurity news aggregator
date: 2024-09-24
fetch_date: 2025-10-06T18:29:52.693658
---

# Kransom Ransomware: New Threat Using DLL-Sideloading to Hijack Popular RPG

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

![Kransom Ransomware: New Threat Using DLL-Sideloading to Hijack Popular RPG](/cybersecurity-blog/wp-content/uploads/2024/09/kransom_blog.jpg)

[News](/cybersecurity-blog/category/news/)

# Kransom Ransomware: New Threat Using DLL-Sideloading to Hijack Popular RPG

September 23, 2024

[Add comment](#comments-8868)
3056 views
4 min read

[Home](/cybersecurity-blog/)[News](/cybersecurity-blog/category/news/)

Kransom Ransomware: New Threat Using DLL-Sideloading to Hijack Popular RPG

#### Recent posts

* [![](/cybersecurity-blog/wp-content/uploads/2025/09/Release-notes-1024x497.png)

  #### Release Notes: Palo Alto Networks, Microsoft, IBM Connectors and 2,300+ Suricata Rules

  1380
  0](/cybersecurity-blog/release-notes-september-2025/)
* [![](/cybersecurity-blog/wp-content/uploads/2025/10/FunkLocker_blog-1024x497.jpg)

  #### FunkSec’s FunkLocker: How AI Is Powering the Next Wave of Ransomware

  3018
  0](/cybersecurity-blog/funklocker-malware-analysis/)
* [![](/cybersecurity-blog/wp-content/uploads/2025/09/defender_blog-1024x497.jpg)

  #### ANY.RUN & MS Defender: Enrich Alerts Faster, Stop Attacks Early

  3023
  0](/cybersecurity-blog/ms-defender-connectors/)

[Home](/cybersecurity-blog/)[News](/cybersecurity-blog/category/news/)

Kransom Ransomware: New Threat Using DLL-Sideloading to Hijack Popular RPG

Recently, our team of analysts discovered a sample of a yet-unknown ransomware that they dubbed Kransom. The malware employed the malicious DLL-sideloading technique to hijack the execution flow of an .exe file belonging to the popular game Honkai: Star Rail. Here is everything we have on the threat so far.

## Initial Infection Vector

[View the sandbox session for detailed analysis](https://app.any.run/tasks/9835858b-9f4c-4013-bad7-93ca6bf7645c/?utm_source=mtt&utm_medium=article&utm_campaign=deerstealer&utm_term=230924&utm_content=linktoservice).

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXe-JbzJs-qeYQtvc-_aQYGkaYzeP2b1Hz4ilUdkOo_ohuSg7TS-zUcnci9UQ_Lz92wX0f7CUe9k4XsKSNwHrn5YHzVNKbYUhC9bUK7vZZslkukjH4027NDuPKzI1AEcFhtwRGW9nVIXppwCTdU-tPbyH0ZE?key=YFuxOOksK5xcTx_NXFYhSQ)

The Kransom ransomware attack began with a deceptive archive containing two files: an executable and a DLL (Dynamic Link Library) file.

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcMkG6UuzNZRrUHOHHsWdoKc4-fRW7cd-HHVtfwsJx9lj4axg2Ws_F_QF_iUzvfW7l27ntrDWrpZuC3a6uGcWSLqBq8MB7knE1eJLX7sa5-vy_0oRWfWmchCfkHDtuCAm0WEUOF_TvZqGkaz0DUsqmj-Cg?key=YFuxOOksK5xcTx_NXFYhSQ)

The executable was signed with a valid certificate from COGNOSPHERE PTE. LTD, the publishing company for Honkai: Star Rail, a popular RPG.

Easily analyze malware and phishing in ANY.RUN sandbox

[Sign up for free](https://app.any.run/?utm_source=mtt&utm_medium=article&utm_campaign=deerstealer&utm_term=230924&utm_content=linktoregistration#register/)

## DLL Side-Loading Technique

![](/cybersecurity-blog/wp-content/uploads/2024/09/krans_five-1024x576.jpeg)

Kransom employs a technique known as DLL side-loading to evade detection and inject its malicious payload. The method involves loading a malicious DLL into the process of a legitimate application.

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfzFsOzarr8CFefh1ggC4-z8BPyiPRZECSXMXvY38kd9w4B8gsd4ov4fxrsg96b9BRZ5Fd7ko6F4vXLqgJnoJ9-x7-6V3PXZFQPrQa8ENLXITRIcFG4TIcJpDWnpM_afBKidMUBYipaa5lYSVigpB7_3t1C?key=YFuxOOksK5xcTx_NXFYhSQ)

Upon launching the legitimate executable named “StarRail.exe”, the user triggers the loading of the malicious DLL ([see analysis of StarRailBase.dll](https://app.any.run/tasks/b6366c04-7527-4c13-a5f8-e0a496a84dc1/?utm_source=mtt&utm_medium=article&utm_campaign=deerstealer&utm_term=230924&utm_content=linktoservice)), which is responsible for initiating the infection and encrypting the victim’s files.

## File Encryption Method

Kransom utilizes a simple XOR encryption algorithm with a weak key (0xaa) to encrypt files on the infected system.

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcdL0BXZQXxgvZ1N0PO4JyF0cKndEArW-WhXtktELMeZcixVCfbhnZ6CfXph0ZNZaVh-bCHWdXni7FKlOYSmEUy7V5rwpeCNvD6O452oLSXu_aRGzMH4qf9gFvJh-GORVQI3sQHE4BFZ0boUHhQmQT-oT_R?key=YFuxOOksK5xcTx_NXFYhSQ)

ANY.RUN’s sandbox helps you track all the encrypted files and see their contents.

## Ransom Note

Following successful file encryption, Kransom drops a ransom note that instructs the user to contact “hoyoverse” for solutions.

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXeDiV_sGXJjzU_yuZJ792K6_lPlVb3nDmYyxJffeHtdOQYTwzHltjfTR6i93BoUqHnAHAKIMOvkAgYX0OjCG7pT1zppdFOtWxL0SopsAAo3qVkiewtU1MamQCkkCuXhI01mDHEkQOpFcZAeWItwvzQtfCg?key=YFuxOOksK5xcTx_NXFYhSQ)

*The ransom note shared with victims*

This is a social engineering tactic designed to impersonate the game’s legitimate developer, Hoyoverse.

## Collecting Threat Intelligence on Kransom Ransomware

To stay updated on the latest Kransom attacks and enrich your investigations to this and other threats, use [Threat intelligence Lookup](https://any.run/threat-intelligence-lookup/?utm_source=mtt&utm_medium=article&utm_campaign=deerstealer&utm_term=230924&utm_content=linktolookuplanding).

The [service](https://any.run/cybersecurity-blog/introducing-any-run-threat-intelligence-lookup/) pulls threat data from thousands of public malware and phishing sam...
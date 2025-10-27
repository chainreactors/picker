---
title: Mamona: Technical Analysis of a New Ransomware Strain
url: https://any.run/cybersecurity-blog/mamona-ransomware-analysis/
source: Over Security - Cybersecurity news aggregator
date: 2025-05-07
fetch_date: 2025-10-06T22:29:33.140444
---

# Mamona: Technical Analysis of a New Ransomware Strain

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

![Mamona: Technical Analysis of a New Ransomware Strain](/cybersecurity-blog/wp-content/uploads/2025/05/mamona_blog.jpg)

[Malware Analysis](/cybersecurity-blog/category/malware-analysis/)

# Mamona: Technical Analysis of a New Ransomware Strain

May 6, 2025

[Add comment](#comments-13267)
7760 views
10 min read

[Home](/cybersecurity-blog/)[Malware Analysis](/cybersecurity-blog/category/malware-analysis/)

Mamona: Technical Analysis of a New Ransomware Strain

#### Recent posts

* [![](/cybersecurity-blog/wp-content/uploads/2025/09/Release-notes-1024x497.png)

  #### Release Notes: Palo Alto Networks, Microsoft, IBM Connectors and 2,300+ Suricata Rules

  1616
  0](/cybersecurity-blog/release-notes-september-2025/)
* [![](/cybersecurity-blog/wp-content/uploads/2025/10/FunkLocker_blog-1024x497.jpg)

  #### FunkSec’s FunkLocker: How AI Is Powering the Next Wave of Ransomware

  3163
  0](/cybersecurity-blog/funklocker-malware-analysis/)
* [![](/cybersecurity-blog/wp-content/uploads/2025/09/defender_blog-1024x497.jpg)

  #### ANY.RUN & MS Defender: Enrich Alerts Faster, Stop Attacks Early

  3181
  0](/cybersecurity-blog/ms-defender-connectors/)

[Home](/cybersecurity-blog/)[Malware Analysis](/cybersecurity-blog/category/malware-analysis/)

Mamona: Technical Analysis of a New Ransomware Strain

*Editor’s note:****The current article is authored by Mauro Eldritch, offensive security expert and threat intelligence analyst. You can***[***find Mauro on X***](https://x.com/MauroEldritch)***.***

These days, it’s easy to come across new [ransomware strains](https://any.run/malware-trends/ransomware) without much effort. But the ransomware threat landscape is far broader than it seems, especially when you dive into the commodity ransomware scene. This type of ransomware is developed by a group that sells a builder to third-party operators, with no formal agreement or contract between them, unlike the more organized Ransomware-as-a-Service (RaaS) model.

On this side of the fence, we see countless new products appearing on the cybercrime shelf every day. They’re much harder to track, as victims, strains, infrastructure, and builds often have no direct connection to each other.

Let’s take a look at one of them: Mamona Ransomware. Never heard of it? That’s probably because it’s a new strain but despite its short lifespan, it has already made some noise. It’s been spotted in campaigns run by BlackLock affiliates (who are also linked to Embargo), one of its online builders was exposed and later leaked on the clearnet, and the DragonForce group even stole the main website’s .env file, publishing it on their Dedicated Leak Site on Tor under the headline: *“Is this your .env file?”*

So, let’s find out what this is all about.

![](/cybersecurity-blog/wp-content/uploads/2025/05/1-1024x542.png)

## Mamona Ransomware: Key Takeaways

* **Emerging threat:** Mamona is a newly identified commodity ransomware strain.

* **No external communication:** The malware operates entirely offline, with no observed Command and Control (C2) channels or data exfiltration.

* **Local encryption only:** All cryptographic processes are executed locally using custom routines, with no reliance on standard libraries.

* **Obfuscated delay technique:** A ping to 127[.]0.0[.]7 is used as a timing mechanism, followed by a self-deletion command to minimize forensic traces.

* **False extortion claims:** The ransom note threatens data leaks, but analysis confirms there is no actual data exfiltration.

* **File encryption behavior:** User files are encrypted and renamed with the .HAes extension; ransom notes are dropped in multiple directories.

* **Decryption available:** A working decryption tool was identified and successfully tested, enabling file recovery.

* **Functional, despite poor design:** The decrypter features an outdated interface but effectively restores encrypted files.

This emerging ransomware can be clearly observed within [ANY.RUN’s cloud-based sandbox environment](http://any.run/?utm_source=anyrunblog&utm_medium=article&utm_campaign=mamona_analysis&utm_term=060525&utm_content=linktolanding). You can explore a full analysis session below for a detailed visual breakdown.

[View analysis session with Mamona ransomware](https://app.any.run/tasks/cdcc75cd-d1f0-4fae-8924-d1aa44525e7e)

## Offline and Dangerous: Mamona’s Silent Tactics

When you hear about ransomware, your first educated guess is usually a threat that comes from the outside, exfiltrates sensitive files, encrypts the local versions, and then demands a ransom. Pretty much the full ransomware cycle. But this one is different. It has no network communication at all, acting surprisingly as a **mute ransomware**. So far, the only connections it attempts are local, plus one to port 80 (HTTP), where no data is actually sent or received.

![](/cybersecurity-blog/wp-content/uploads/2025/05/2-2-1024x367.png)

This lack of network communication strongly suggests that the encryption key is either generated locally on the fly or hardcoded within the binary itself. In the medium term, this increases the chances of reverse-engineering a working decrypter which, fortunately, we already have in this case.

A closer look reveals that the encryptor relies entirely on homemade routines. Th...
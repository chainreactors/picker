---
title: Recent Cyber Attacks Discovered by ANY.RUN: October 2024
url: https://any.run/cybersecurity-blog/cyber-attacks-october-2024/
source: Over Security - Cybersecurity news aggregator
date: 2024-10-29
fetch_date: 2025-10-06T18:54:26.330195
---

# Recent Cyber Attacks Discovered by ANY.RUN: October 2024

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

![Recent Cyber Attacks Discovered by ANY.RUN: October 2024](/cybersecurity-blog/wp-content/uploads/2024/10/cyber_att_blog.jpg)

[Malware Analysis](/cybersecurity-blog/category/malware-analysis/)

# Recent Cyber Attacks Discovered by ANY.RUN: October 2024

October 28, 2024

[Add comment](#comments-9427)
3374 views
6 min read

[Home](/cybersecurity-blog/)[Malware Analysis](/cybersecurity-blog/category/malware-analysis/)

Recent Cyber Attacks Discovered by ANY.RUN: October 2024

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

Recent Cyber Attacks Discovered by ANY.RUN: October 2024

Identifying new cyber threats is no simple task. They’re always evolving, adapting, and finding new ways to slip through the defenses.

But no stress—[ANY.RUN](https://any.run/?utm_source=anyrunblog&utm_medium=article&utm_campaign=phishing_in_october_2024&utm_term=281024&utm_content=linktolanding) has you covered!

Our team of researchers are always on the lookout, analyzing the latest attacks to keep you informed.

In this article, we’re sharing some of the most recent threats our team has uncovered over the past month. Let’s dive in and see what’s out there!

## APT-C-36, aka BlindEagle, Campaign in LATAM

[*Original post on X*](https://x.com/anyrun_app/status/1848335385660666334)

APT-C-36, better known as **BlindEagle**, is a group that has been actively targeting the **LATAM region** for years. Their primary goal? To gain remote control of victims’ devices through continuous phishing attacks, installing [Remote Access Tools](https://any.run/malware-trends/rat) **(RATs)** like [Remcos](https://any.run/malware-trends/remcos) and [AsyncRAT](https://any.run/malware-trends/asyncrat) for financial gain.

### Attack details

![](/cybersecurity-blog/wp-content/uploads/2024/10/apt36_intel-1024x576.jpeg)

We discovered that in recent cases attackers invite victims to an online court hearing via email. This official-sounding invitation creates a sense of urgency, pushing the target to download the malicious payload.

You can view [analysis](https://app.any.run/tasks/c03dd430-2d34-424e-83ba-d9efda45a32a/?utm_source=anyrunblog&utm_medium=article&utm_campaign=phishing_in_october_2024&utm_term=281024&utm_content=linktoservice) of this attack inside ANY.RUN’s sandbox.

![](/cybersecurity-blog/wp-content/uploads/2024/10/orig_email_phish-1024x576.jpeg)

To deliver their malware, BlindEagle often relies on well-known online services, such as:

* Discord
* Google Drive
* Bitbucket
* Pastee
* YDRAY

This tactic helps them bypass certain security filters since these services are typically trusted by users.

The malicious payload is stored in the archive, which is usually protected by a password that can be found in the initial email.

![](/cybersecurity-blog/wp-content/uploads/2024/10/image4-4-1024x586.png)

Thanks to ANY.RUN’s [interactivity](https://any.run/cybersecurity-blog/interactive-malware-sandbox/), you can manually enter the password right inside the sandbox.

Analyze malware and phishing threats
in ANY.RUN sandbox for free

[Set up free account](https://app.any.run/?utm_source=anyrunblog&utm_medium=article&utm_campaign=phishing_in_october_2024&utm_term=281024&utm_content=linktoregistration#register)

As mentioned, BlindEagle use **Remcos** and **AsyncRAT** as their primary tools for remote access. The current attack involved Remcos distribution.

![](/cybersecurity-blog/wp-content/uploads/2024/10/image5-4-1024x312.png)

In the current analysis session, we observed a Remcos RAT connection attempting communication with a Command and Control (C2) server.

![](/cybersecurity-blog/wp-content/uploads/2024/10/image6-3-1024x635.png)

This activity involves establishing TLS connection to an external server, which was immediately flagged by a Suricata IDS rule in the ANY.RUN sandbox.

### Threat Intelligence on APT-C-36 attacks

To collect intel on other attacks belonging to BlindEagle’s campaigns, you can use ANY.RUN’s **[Threat Intelligence Lookup](https://any.run/cybersecurity-blog/introducing-any-run-threat-intelligence-lookup/)**:

* Specify the country from where the phishing sample originated:
  **submissionCountry:”Co”**

* Filter for sessions that involve an email client, like Outlook:
  **commandLine:”OUTLOOK.EXE”**

* Since the payload is often stored in an archive, filter for an archiving tool, such as WinRAR:
  **commandLine:”WinRAR”**

* Look for sessions flagged as suspicious or malicious:
  **threatLevel:”malicious”**

* To find active RATs like Remcos, add a condition for Remote Access Tools:
  ...
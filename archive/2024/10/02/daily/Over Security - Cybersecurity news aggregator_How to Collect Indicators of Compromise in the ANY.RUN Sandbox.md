---
title: How to Collect Indicators of Compromise in the ANY.RUN Sandbox
url: https://any.run/cybersecurity-blog/how-to-collect-iocs-in-sandbox/
source: Over Security - Cybersecurity news aggregator
date: 2024-10-02
fetch_date: 2025-10-06T18:57:01.785431
---

# How to Collect Indicators of Compromise in the ANY.RUN Sandbox

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

![How to Collect Indicators of Compromise <br>in the ANY.RUN Sandbox](/cybersecurity-blog/wp-content/uploads/2024/10/iocs_blog.jpg)

[Instructions on ANY.RUN](/cybersecurity-blog/category/instructions/)

# How to Collect Indicators of Compromise in the ANY.RUN Sandbox

October 1, 2024

[Add comment](#comments-9013)
2674 views
4 min read

[Home](/cybersecurity-blog/)[Instructions on ANY.RUN](/cybersecurity-blog/category/instructions/)

How to Collect Indicators of Compromise
in the ANY.RUN Sandbox

#### Recent posts

* [![](/cybersecurity-blog/wp-content/uploads/2025/09/Release-notes-1024x497.png)

  #### Release Notes: Palo Alto Networks, Microsoft, IBM Connectors and 2,300+ Suricata Rules

  1396
  0](/cybersecurity-blog/release-notes-september-2025/)
* [![](/cybersecurity-blog/wp-content/uploads/2025/10/FunkLocker_blog-1024x497.jpg)

  #### FunkSec’s FunkLocker: How AI Is Powering the Next Wave of Ransomware

  3020
  0](/cybersecurity-blog/funklocker-malware-analysis/)
* [![](/cybersecurity-blog/wp-content/uploads/2025/09/defender_blog-1024x497.jpg)

  #### ANY.RUN & MS Defender: Enrich Alerts Faster, Stop Attacks Early

  3040
  0](/cybersecurity-blog/ms-defender-connectors/)

[Home](/cybersecurity-blog/)[Instructions on ANY.RUN](/cybersecurity-blog/category/instructions/)

How to Collect Indicators of Compromise
in the ANY.RUN Sandbox

Gathering [Indicators of Compromise (IOCs)](https://any.run/cybersecurity-blog/indicators-of-compromise/) is key to identifying and responding to threats. IOCs are pieces of forensic data that point to potential malicious activity, helping you detect, investigate, and prevent cyberattacks.

With [ANY.RUN](https://any.run/?utm_source=anyrunblog&utm_medium=article&utm_campaign=how_to_collect_iocs&utm_term=011024&utm_content=linktolanding), you can collect a wide variety of IOCs, giving you a complete picture of any threat.

Let’s dive into the types of IOCs you can collect in ANY.RUN’s Interactive Sandbox and where to find them.

## File System Indicators

### **Main Objects**

The Main Object is one of the most critical components when analyzing malware inside the ANY.RUN sandbox. This refers to the primary file that was loaded for analysis.

Once you’ve initiated a [sandbox analysis session](https://app.any.run/tasks/138ae7e8-9ae3-4f76-afd7-09671418e59b/?utm_source=anyrunblog&utm_medium=article&utm_campaign=how_to_collect_iocs&utm_term=011024&utm_content=linktoservice), simply click on the file name located in the upper-right corner of the screen.

![](/cybersecurity-blog/wp-content/uploads/2024/10/image8-1.png)

This action will give you quick access to the Main Object IOCs, which include basic details such as file paths, hashes, and more.

![](/cybersecurity-blog/wp-content/uploads/2024/10/image9-1024x299.png)

Analyze and collect IOCs of malware and phishing threats
in the ANY.RUN sandbox

[Start your first analysis](https://app.any.run/?utm_source=anyrunblog&utm_medium=article&utm_campaign=how_to_collect_iocs&utm_term=011024&utm_content=linktoregistration#register/)

### **Dropped Executable Files**

All files dropped during the malware’s execution are shown in the bottom panel under **Files**. This area demonstrates exactly what files the malware generated or modified, helping you track its propagation across the system.

![](/cybersecurity-blog/wp-content/uploads/2024/10/imagea-1024x253.png)

## Network Indicators

### **Domains (DNS Requests)**

Domains that the malware attempts to access can help you trace its communication with external servers, such as command-and-control (C2) infrastructure.

You can find these IOCs under **Network → DNS Requests** in the bottom panel of the sandbox interface.

By analyzing the DNS requests, you’ll get a clearer view of how the malware interacts with remote hosts, often revealing malicious infrastructure or other indicators that can assist in further threat investigation.

![](/cybersecurity-blog/wp-content/uploads/2024/10/imageb-1024x242.png)

### **Connections**

The malware’s active connections can be observed under **Network → Connections**.

This feature allows you to monitor the malware’s communication channels, tracking its interactions with command-and-control (C2) servers or other suspicious IP addresses.

Analyzing these connections enables you to identify data exfiltration routes or pinpoint where the malware is sending information.

![](/cybersecurity-blog/wp-content/uploads/2024/10/imagec-1024x251.png)

### **HTTP/HTTPS Requests**

HTTP and HTTPS requests initiated by the malware are logged under **Network** → **HTTP Requests**. This is crucial for identifying malicious websites or external servers the malware connects to.

![](/cybersecurity-blog/wp-content/uploads/2024/10/imaged-1024x185.png)

*HTTP requests displayed in ANY.RUN*

## Malware Configurations

In the ANY.RUN sandbox, you can gather IOCs specifically associated with malware configurations by clicking the **MalConf**button located in the upper right corner of the screen.

![](/cybersecurity-blog/wp-content/uploads/2024/10/imagee-1024x369.png)

*MalConf button inside ANY.RUN sandbox*

The feature specifically pulls IOCs from to the malware’s configurations, such as URLs, file hashes, and domains, providing key insights that are crucial for furthe...
---
title: Cyber Attacks on DeepSeek AI: What Really Happened? Full Timeline and Analysis
url: https://any.run/cybersecurity-blog/deepseek-cyber-attacks/
source: Over Security - Cybersecurity news aggregator
date: 2025-02-06
fetch_date: 2025-10-06T20:38:34.436096
---

# Cyber Attacks on DeepSeek AI: What Really Happened? Full Timeline and Analysis

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

![Cyber Attacks on DeepSeek AI: What Really Happened? Full Timeline and Analysis](/cybersecurity-blog/wp-content/uploads/2025/02/deep_blog.jpg)

[News](/cybersecurity-blog/category/news/)

# Cyber Attacks on DeepSeek AI: What Really Happened? Full Timeline and Analysis

February 5, 2025

[Add comment](#comments-11437)
4107 views
5 min read

[Home](/cybersecurity-blog/)[News](/cybersecurity-blog/category/news/)

Cyber Attacks on DeepSeek AI: What Really Happened? Full Timeline and Analysis

#### Recent posts

* [![](/cybersecurity-blog/wp-content/uploads/2025/09/Release-notes-1024x497.png)

  #### Release Notes: Palo Alto Networks, Microsoft, IBM Connectors and 2,300+ Suricata Rules

  1441
  0](/cybersecurity-blog/release-notes-september-2025/)
* [![](/cybersecurity-blog/wp-content/uploads/2025/10/FunkLocker_blog-1024x497.jpg)

  #### FunkSec’s FunkLocker: How AI Is Powering the Next Wave of Ransomware

  3041
  0](/cybersecurity-blog/funklocker-malware-analysis/)
* [![](/cybersecurity-blog/wp-content/uploads/2025/09/defender_blog-1024x497.jpg)

  #### ANY.RUN & MS Defender: Enrich Alerts Faster, Stop Attacks Early

  3084
  0](/cybersecurity-blog/ms-defender-connectors/)

[Home](/cybersecurity-blog/)[News](/cybersecurity-blog/category/news/)

Cyber Attacks on DeepSeek AI: What Really Happened? Full Timeline and Analysis

Less than a month after its launch, DeepSeek has already shaken up the industry, caused NVidia’s stock to shed $600 billion, and sparked political controversy.

Now, the AI company is dealing with the consequences of major cyber attacks. As of February 5, DeepSeek is still having trouble letting new users join.

Let’s review the entire timeline of the attacks and take a closer look at the two botnets, HailBot and RapperBot, responsible for the latest disruptions, using [ANY.RUN’s Interactive Sandbox](https://any.run/?utm_source=anyrunblog&utm_medium=article&utm_campaign=deepseek_cyber_attack&utm_term=050225&utm_content=linktolanding).

## What is DeepSeek

DeepSeek is an Artificial Intelligence company based in China and founded in late 2023. On January 20, 2025, it launched its first DeepSeek-R1 model, which instantly gained millions of app downloads worldwide.

The success of the release came down to several factors:

* DeepSeek achieved AI model performance comparable to OpenAI’s (the company behind ChatGPT) for under $6 million.
* DeepSeek uses less-advanced chips, making its AI operations [up to 50 times](https://www.usatoday.com/story/tech/news/2025/01/31/deepseek-ai-trump-wakeup-call/78097990007/) cheaper than competitors.
* DeepSeek’s AI is open source.

## Cyber Attacks on DeepSeek: Timeline

### January 27

DeepSeek paused new user registrations, citing “large-scale malicious attacks” on its infrastructure.

### January 28

Wiz.io [reported](https://www.wiz.io/blog/wiz-research-uncovers-exposed-deepseek-database-leak) discovering a leaked ClickHouse database linked to DeepSeek, which contained users’ chat histories and API keys. This leak was likely unrelated to the cyber attacks mentioned by DeepSeek.

### January 29

Global Times [revealed](https://www.globaltimes.cn/page/202501/1327676.shtml) that DeepSeek had been facing regular distributed denial-of-service (DDoS) attacks since early January, involving reflection amplification techniques.

Starting January 22, HTTP proxy attacks began, gradually increasing in frequency and peaking on January 28. These were further accompanied by brute-force attack attempts, which allegedly originated from IP addresses in the United States.

### January 30

Based on a report by XLab, Global Times [disclosed](https://www.globaltimes.cn/page/202501/1327697.shtml) that the latest wave of attacks on DeepSeek involved two botnets, HailBot and RapperBot, both variants of the infamous Mirai botnet.

The attacks launched early on January 30 used 16 command-and-control (C2) servers and over 100 C2 ports.

## Why Businesses Must Pay Attention

The cyber attacks on DeepSeek highlight that businesses of all sizes and industries, especially those dependent on extensive digital infrastructure, can be vulnerable to such threats. With botnets like HailBot and RapperBot available as a service, attackers can launch cyber assaults without needing advanced technical skills.

For companies that rely on AI services, the consequences can be even more severe, including service disruptions, data breaches, and loss of customer trust. As AI becomes more integral to business operations, it is crucial for companies to invest in robust cybersecurity measures.

## How HailBot and RapperBot Botnets Work

### **HailBot**

HailBot, named after the string “hail china mainland,” is known for its DDoS attack capabilities. This variant of Mirai exploits vulnerabilities such as CVE-2017-17215, which affects certain Huawei devices.

HailBot can compromise a wide range of devices and use them to launch distributed denial-of-service attacks.

![](/cybersecurity-blog/wp-content/uploads/2025/02/hailbot_sandbox-1024x579.png)

By uploading a sample of HailBot to ANY.RUN’s [Interactive Sandbox](https://any.run/?utm_source=anyrunblog&utm_medium=article&utm_campaign=deepseek_cyber_attack&utm_term=050225&utm_content=linktolanding), we can get a detailed view of how it operates.

[View a...
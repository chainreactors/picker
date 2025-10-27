---
title: Investigating Phishing Threats with TI Lookup: Use Cases from an Expert
url: https://any.run/cybersecurity-blog/investigating-phishing-threats/
source: Over Security - Cybersecurity news aggregator
date: 2024-11-27
fetch_date: 2025-10-06T19:20:47.572926
---

# Investigating Phishing Threats with TI Lookup: Use Cases from an Expert

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

![Investigating Phishing Threats with TI Lookup: Use Cases from an Expert](/cybersecurity-blog/wp-content/uploads/2024/11/phish_lookup_blog.jpg)

[Cybersecurity Lifehacks](/cybersecurity-blog/category/lifehacks/)

# Investigating Phishing Threats with TI Lookup: Use Cases from an Expert

November 26, 2024

[Add comment](#comments-10021)
2548 views
8 min read

[Home](/cybersecurity-blog/)[Cybersecurity Lifehacks](/cybersecurity-blog/category/lifehacks/)

Investigating Phishing Threats with TI Lookup: Use Cases from an Expert

#### Recent posts

* [![](/cybersecurity-blog/wp-content/uploads/2025/09/Release-notes-1024x497.png)

  #### Release Notes: Palo Alto Networks, Microsoft, IBM Connectors and 2,300+ Suricata Rules

  1406
  0](/cybersecurity-blog/release-notes-september-2025/)
* [![](/cybersecurity-blog/wp-content/uploads/2025/10/FunkLocker_blog-1024x497.jpg)

  #### FunkSec’s FunkLocker: How AI Is Powering the Next Wave of Ransomware

  3024
  0](/cybersecurity-blog/funklocker-malware-analysis/)
* [![](/cybersecurity-blog/wp-content/uploads/2025/09/defender_blog-1024x497.jpg)

  #### ANY.RUN & MS Defender: Enrich Alerts Faster, Stop Attacks Early

  3052
  0](/cybersecurity-blog/ms-defender-connectors/)

[Home](/cybersecurity-blog/)[Cybersecurity Lifehacks](/cybersecurity-blog/category/lifehacks/)

Investigating Phishing Threats with TI Lookup: Use Cases from an Expert

TI Lookup from [ANY.RUN](https://any.run/?utm_source=anyrunblog&utm_medium=article&utm_campaign=phish_investigations_with_jane&utm_term=261124&utm_content=linktolanding) is a versatile tool for gathering up-to-date intelligence on the latest cyber threats. The best way to demonstrate its effectiveness is to hear from actual security professionals about how they use the service in their daily work.

This time, we asked [Jane\_0sint](https://x.com/Jane_0sint), an accomplished network traffic analyst and the first ANY.RUN ambassador, for her real-world cases of using TI Lookup. Lucky for us, she agreed to share her insights and sent us a few examples, which include finding intel on phishing kits like Mamba2FA and Tycoon2FA.

## About Threat Intelligence Lookup

[TI Lookup](https://any.run/cybersecurity-blog/introducing-any-run-threat-intelligence-lookup/) is a searchable hub for investigating malware and phishing attacks and collecting fresh cyber threat data. Powered by a massive public database of millions of samples analyzed in ANY.RUN’s Interactive Sandbox, it contains various [Indicators of Compromise](https://any.run/cybersecurity-blog/how-to-collect-iocs-in-sandbox/) (IOCs), Indicators of Attack (IOAs), and Indicators of Behavior (IOBs), from threats’ network activity to system processes and beyond.

The service provides you with extensive search capabilities, allowing you to create custom requests that feature different data points to home in on specific threats. It offers:

* **Quick Results**: Searches for events and indicators from the past six months take just 5 seconds on average

* **Unique Data**: It contains over [40 types of threat data](https://any.run/cybersecurity-blog/ti-lookup-search-parameters/), including malicious IPs, URLs, command line contents, mutexes, and YARA rules

* **Large Database**: TI Lookup is updated daily with thousands of public samples uploaded to ANY.RUN’s sandbox by a global community of over 500,000 security professionals

Get 20 free requests to test TI Lookup

[Contact us](https://intelligence.any.run/plans/?utm_source=anyrunblog&utm_medium=article&utm_campaign=phish_investigations_with_jane&utm_term=261124&utm_content=linktotiplans/)

## Investigating the Mamba2FA Phishing Kit

Mamba2FA is a phishing kit that has seen a significant rise over the past several months. To investigate this threat and gather more context, we can utilize a typical URL pattern commonly found in its campaigns. This pattern follows the structure {domain}/{m,n,o}/?{Base64 string}.

When translating this into an actual query for TI Lookup, we can use the following search string:

|  |
| --- |
| [commandLine:" http\*\/?\/\?c3Y9"](https://intelligence.any.run/analysis/lookup/?utm_source=anyrunblog&utm_medium=article&utm_campaign=phish_investigations_with_jane&utm_term=261124&utm_content=linktolookup#%7B%2522query%2522:%2522commandLine:%255C%2522%2520http*%255C%255C/?%255C%255C/%255C%255C?c3Y9%255C%2522%25C2%25A0%2522,%2522dateRange%2522:180%7D) |

Let’s break down this query:

* **Asterisk (\*):** This wildcard character indicates any character string. It helps expand our search to include all domains used in Mamba2FA attacks, ensuring a comprehensive investigation

* **Question Mark (?):** This is another wildcard character that indicates exactly one character or none at all. In our case, there are two question marks in the query. The first one is the wildcard that serves as a stand-in for the characters “m”, “n”, and “o” that are commonly used in Mamba2FA URLs. The second question mark is a part of the address. To escape it, we use the \ slash symbol

* **c3Y9:** This is a Base64-encoded parameter found across Mamba2FA attacks. When decoded, it translates to sv=, which specifies the appearance of the phishing page

![](/cybersecurity-blog/wp-content/uploads/2024/11/image4-6-1024x435.png)

Submitting this search quer...
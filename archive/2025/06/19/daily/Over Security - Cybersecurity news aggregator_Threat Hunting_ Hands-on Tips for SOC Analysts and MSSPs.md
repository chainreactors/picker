---
title: Threat Hunting: Hands-on Tips for SOC Analysts and MSSPs
url: https://any.run/cybersecurity-blog/cyber-threat-hunting-tips/
source: Over Security - Cybersecurity news aggregator
date: 2025-06-19
fetch_date: 2025-10-06T22:55:28.248368
---

# Threat Hunting: Hands-on Tips for SOC Analysts and MSSPs

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

![Threat Hunting: Hands-on Tips for SOC Analysts and MSSPs ](/cybersecurity-blog/wp-content/uploads/2025/06/threat_hunt_blog.jpg)

[Cybersecurity Lifehacks](/cybersecurity-blog/category/lifehacks/)

# Threat Hunting: Hands-on Tips for SOC Analysts and MSSPs

June 18, 2025

[Add comment](#comments-14328)
2186 views
14 min read

[Home](/cybersecurity-blog/)[Cybersecurity Lifehacks](/cybersecurity-blog/category/lifehacks/)

Threat Hunting: Hands-on Tips for SOC Analysts and MSSPs

#### Recent posts

* [![](/cybersecurity-blog/wp-content/uploads/2025/09/Release-notes-1024x497.png)

  #### Release Notes: Palo Alto Networks, Microsoft, IBM Connectors and 2,300+ Suricata Rules

  1637
  0](/cybersecurity-blog/release-notes-september-2025/)
* [![](/cybersecurity-blog/wp-content/uploads/2025/10/FunkLocker_blog-1024x497.jpg)

  #### FunkSec’s FunkLocker: How AI Is Powering the Next Wave of Ransomware

  3168
  0](/cybersecurity-blog/funklocker-malware-analysis/)
* [![](/cybersecurity-blog/wp-content/uploads/2025/09/defender_blog-1024x497.jpg)

  #### ANY.RUN & MS Defender: Enrich Alerts Faster, Stop Attacks Early

  3197
  0](/cybersecurity-blog/ms-defender-connectors/)

[Home](/cybersecurity-blog/)[Cybersecurity Lifehacks](/cybersecurity-blog/category/lifehacks/)

Threat Hunting: Hands-on Tips for SOC Analysts and MSSPs

***Editor’s note**: The current article is authored by Clandestine, threat researcher and threat hunter. You can*[*find Clandestine on X*](https://x.com/akaclandestine)*.*

Threat actors today are continuously developing sophisticated techniques to evade traditional detection methods. ANY.RUN’s [Threat Intelligence Lookup](https://any.run/threat-intelligence-lookup/?utm_source=anyrunblog&utm_medium=article&utm_campaign=threat_hunting_tips&utm_term=180625&utm_content=linktolookuplanding) offers advanced capabilities for threat data gathering and analysis. As a specialized search engine, it allows security analysts to query [various indicators](https://any.run/cybersecurity-blog/iocs-iobs-ioas-explained/) of compromise (IOCs), behaviors (IOBs), and attacks (IOAs), providing valuable insights into real-world malware activity observed in sandboxed environments.

We shall review several advanced threat hunting techniques using [ANY.RUN](http://any.run/?utm_source=anyrunblog&utm_medium=article&utm_campaign=threat_hunting_tips&utm_term=180625&utm_content=linktolanding)’s TI Lookup to provide cybersecurity researchers and threat intelligence analysts of [SOC and MSSP teams](https://any.run/cybersecurity-blog/expertware-success-story/) with effective strategies to identify and analyze various types of threats.

## Threat Intelligence Lookup Key Capabilities

![](/cybersecurity-blog/wp-content/uploads/2025/06/ti_lookup_main-2-1024x602.png)

[Threat Intelligence Lookup](https://intelligence.any.run/?utm_source=anyrunblog&utm_medium=article&utm_campaign=threat_hunting_tips&utm_term=180625&utm_content=linktotilookup) provides analysts with access to a vast malware database topped up by over 500,000 users of the Interactive Sandbox, including [15,000 corporate SOC teams](https://any.run/cybersecurity-blog/threat-intelligence-from-organizations/). A single search request can deliver hundreds of relevant analysis sessions, malware samples, or indicators for further research and refining the results with more specific queries.

Besides the ability to instantly get a verdict and context on a potential indicator of compromise, TI Lookup offers a number of functions that enable effective threat hunting and analysis:

* **IOC Lookups**: Detailed searches of various indicators of compromise, including IP addresses, file hashes, URLs, and domain names.

* **Behavioral Lookups**: Beyond traditional IOCs, the service enables searches based on behavioral indicators, such as registry modifications, process activities, network communications, and mutex creations. It is particularly effective for identifying unknown or emerging threats that may not have established IOCs.

* **MITRE Techniques Detection**: The [incorporation of the MITRE ATT&CK](https://any.run/cybersecurity-blog/mitre-ttps-in-ti-lookup/) framework allows analysts to search for specific tactics, techniques, and procedures (TTPs) used by threat actors. This capability facilitates a more structured and comprehensive approach to threat hunting.

* **File/Event Correlation**: The ability to correlate files and events helps analysts identify relationships between different components of an attack and understand the broader context of malicious activities.

* **YARA-based Threat Hunting**: This capability allows for highly specific searches based on file characteristics and patterns.

* **Wildcards and Logical Operators**: The search supports various wildcards and logical operators for the construction of complex and precise queries.

The sophisticated query syntax of Threat Intelligence Lookup supports over 40 parameters, allowing for highly specific and contextualized searches. The basic structure of a query typically includes a parameter, a colon, and a value, often enclosed in quotation marks (e.g., submissionCountry:”us” ).

Logical [operators](https://any.run/cybersecurity-blog/search-operators-and-wildcards-in-ti-lookup/) play a crucial role in constructin...
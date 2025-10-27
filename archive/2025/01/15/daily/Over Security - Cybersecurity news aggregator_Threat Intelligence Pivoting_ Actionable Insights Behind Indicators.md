---
title: Threat Intelligence Pivoting: Actionable Insights Behind Indicators
url: https://any.run/cybersecurity-blog/threat-intelligence-pivoting/
source: Over Security - Cybersecurity news aggregator
date: 2025-01-15
fetch_date: 2025-10-06T20:13:25.269984
---

# Threat Intelligence Pivoting: Actionable Insights Behind Indicators

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

![Threat Intelligence Pivoting: Actionable Insights Behind Indicators](/cybersecurity-blog/wp-content/uploads/2025/01/pivoting_blog.jpg)

[Cybersecurity Lifehacks](/cybersecurity-blog/category/lifehacks/)

# Threat Intelligence Pivoting: Actionable Insights Behind Indicators

January 14, 2025

[Add comment](#comments-10937)
2201 views
7 min read

[Home](/cybersecurity-blog/)[Cybersecurity Lifehacks](/cybersecurity-blog/category/lifehacks/)

Threat Intelligence Pivoting: Actionable Insights Behind Indicators

#### Recent posts

* [![](/cybersecurity-blog/wp-content/uploads/2025/09/Release-notes-1024x497.png)

  #### Release Notes: Palo Alto Networks, Microsoft, IBM Connectors and 2,300+ Suricata Rules

  1432
  0](/cybersecurity-blog/release-notes-september-2025/)
* [![](/cybersecurity-blog/wp-content/uploads/2025/10/FunkLocker_blog-1024x497.jpg)

  #### FunkSec’s FunkLocker: How AI Is Powering the Next Wave of Ransomware

  3036
  0](/cybersecurity-blog/funklocker-malware-analysis/)
* [![](/cybersecurity-blog/wp-content/uploads/2025/09/defender_blog-1024x497.jpg)

  #### ANY.RUN & MS Defender: Enrich Alerts Faster, Stop Attacks Early

  3074
  0](/cybersecurity-blog/ms-defender-connectors/)

[Home](/cybersecurity-blog/)[Cybersecurity Lifehacks](/cybersecurity-blog/category/lifehacks/)

Threat Intelligence Pivoting: Actionable Insights Behind Indicators

Pivoting in cyber threat intelligence refers to using one piece of data to find and explore related information and expand your understanding of a threat. It lets you discover hidden connections between indicators of compromise and find potential vulnerabilities before they are exploited.

## Why pivoting matters

Cyber threat intelligence concentrates on indicators of compromise, [IOCs](https://any.run/cybersecurity-blog/malconf-in-ti-lookup/). These are data points or artifacts (like IP addresses, domain names, file hashes, email addresses, etc.) that indicate a potential or actual malicious activity. Pivoting is researching links and correlations between IOCs and thus discovering new IOCs relevant to the same attack, malware, or threat agent.

Pivoting helps make CTI proactive, helps predict and prevent the unfolding of an attack or the emergence of new threats.

Threat intelligence and pivoting are critical for [businesses and corporate security](https://any.run/cybersecurity-blog/ti-for-business/) because they enhance an organization’s ability to anticipate, detect, and respond to cyber threats. By leveraging actionable insights from threat intelligence and pivoting to discover deeper connections, businesses can protect their assets, reduce risk, and strengthen overall cybersecurity posture.

Note that the definition of pivoting in threat intelligence is different to that in cyber security. Generally, it’s a popular term used in many other fields.

In CS the term is usually used by pentesters and hackers. Here pivoting [is](https://csrc.nist.gov/glossary/term/pivot) *the act of an attacker moving from one compromised system to one or more other systems within the same or other organizations. Pivoting is fundamental to the success of advanced persistent threat (APT) attacks.*

## How it works

Pivoting for CTI shows its potential when IOCs are viewed not as “atomic” but rather as complex objects. Taken by themselves, they are, so to say, “backward-looking”, they lack context. IOCs are good forensic material, but not enough for predictive, proactive security effort.

Pivoting focuses on behaviors. Indicators are linked through their behavioral commonalities. This approach grasps IOC relationships, helps discover new ones, predict their behavior, generalize tendencies, and eventually build strong and adaptive defense based on the understanding of adversaries.

## Pivoting routine

Pivoting is not just about techniques and tools; it is rather about a certain approach or dare say a certain mindset. Once adopted, it’ll give your threat intelligence a new depth and perspective.

The most basic algorithm is:

* Select an initial indicator. For example, a suspicious IP. Or a domain name associated with a known threat or attack.
* Analyze the indicator with a tool of your choice.
* Decompose the indicator. Understand its parameters. Define which of them could signal malicious behavior or be linked to other artifacts.
* Find and analyze linked artifacts. Pay attention to those that haven’t been yet connected with a threat or an attack.
* Research the discovered data.
* Draw actionable insights.

## Where to start

You can start with network indicators pivoting.  Basic network IOCs are IPs, domains, SSL/TSL certificates. They all have certain parameters: for example, registrar and registrant for domains, hosting provider or server type for an IP address, issue date or issuer for a certificate.

One of the most powerful tools for IOC research is [ANY.RUN’s Threat Intelligence Lookup](https://any.run/cybersecurity-blog/introducing-any-run-threat-intelligence-lookup/). It lets you search threat artifacts with over [40 search parameters](https://any.run/cybersecurity-blog/ti-lookup-search-parameters/), including [YARA](https://any.run/cybersecurity-blog/yara-search-guide/) and [Suricata](https://any.run/cybersecurity-blog/suricata-search/) rules, combine them and ...
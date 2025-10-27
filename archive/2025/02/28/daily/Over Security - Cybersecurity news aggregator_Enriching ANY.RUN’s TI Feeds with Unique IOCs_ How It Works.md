---
title: Enriching ANY.RUN’s TI Feeds with Unique IOCs: How It Works
url: https://any.run/cybersecurity-blog/indicators-in-ti-feeds/
source: Over Security - Cybersecurity news aggregator
date: 2025-02-28
fetch_date: 2025-10-06T20:40:13.548376
---

# Enriching ANY.RUN’s TI Feeds with Unique IOCs: How It Works

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

![Enriching ANY.RUN’s TI Feeds with Unique IOCs: How It Works](/cybersecurity-blog/wp-content/uploads/2025/02/iocs_unique_blog.jpg)

[Cybersecurity Lifehacks](/cybersecurity-blog/category/lifehacks/)

# Enriching ANY.RUN’s TI Feeds with Unique IOCs: How It Works

February 27, 2025

[Add comment](#comments-11872)
2090 views
5 min read

[Home](/cybersecurity-blog/)[Cybersecurity Lifehacks](/cybersecurity-blog/category/lifehacks/)

Enriching ANY.RUN’s TI Feeds with Unique IOCs: How It Works

#### Recent posts

* [![](/cybersecurity-blog/wp-content/uploads/2025/09/Release-notes-1024x497.png)

  #### Release Notes: Palo Alto Networks, Microsoft, IBM Connectors and 2,300+ Suricata Rules

  1444
  0](/cybersecurity-blog/release-notes-september-2025/)
* [![](/cybersecurity-blog/wp-content/uploads/2025/10/FunkLocker_blog-1024x497.jpg)

  #### FunkSec’s FunkLocker: How AI Is Powering the Next Wave of Ransomware

  3042
  0](/cybersecurity-blog/funklocker-malware-analysis/)
* [![](/cybersecurity-blog/wp-content/uploads/2025/09/defender_blog-1024x497.jpg)

  #### ANY.RUN & MS Defender: Enrich Alerts Faster, Stop Attacks Early

  3087
  0](/cybersecurity-blog/ms-defender-connectors/)

[Home](/cybersecurity-blog/)[Cybersecurity Lifehacks](/cybersecurity-blog/category/lifehacks/)

Enriching ANY.RUN’s TI Feeds with Unique IOCs: How It Works

Threat Intelligence Feeds from [ANY.RUN](http://any.run/?utm_source=anyrunblog&utm_medium=article&utm_campaign=ti_feeds_iocs&utm_term=270225&utm_content=linktolanding) provide a continuously-updated stream of the latest indicators of compromise. They enable SOC teams to quickly detect and mitigate attacks, including emerging malware and persistent threats.

But how do ANY.RUN’s feeds get enriched with fresh and, most importantly, unique indicators?

Let’s find out.

## About ANY.RUN’s Threat Intelligence Feeds

ANY.RUN’s [Threat Intelligence (TI) Feeds](https://any.run/cybersecurity-blog/ti-feeds-integration/) offer an extensive collection of Indicators of Compromise ([IOCs](https://any.run/cybersecurity-blog/indicators-of-compromise/)) designed to enhance the threat detection capabilities of clients’ security systems. These feeds provide detailed information beyond the basics, including malicious IPs, URLs, domains.

### Where does this data come from?

An international community of over 500,000 researchers and cybersecurity pros who upload and analyze real-world malware and phishing samples every day to ANY.RUN’s [submissions repository](https://app.any.run/submissions/?utm_source=anyrunblog&utm_medium=article&utm_campaign=inside_ti_feeds&utm_term=161224&utm_content=linktoservice).

With TI Feeds from ANY.RUN, [organizations can](https://any.run/cybersecurity-blog/ti-feeds-for-organizational-performance/):

* Expand and speed up threat hunting with enriched up-to-date indicators
* Enhance alert triage and prioritize most urgent issues
* Improve incident response thanks to better understanding threats and their behaviors
* Proactively defend against new and evolving threats

Give TI Feeds from ANY.RUN a try
Start with a free demo sample in STIX or MISP

[Integrate via API](https://intelligence.any.run/feeds/?utm_source=anyrunblog&utm_medium=article&utm_campaign=ti_feeds_iocs&utm_term=270225&utm_content=linktofeeds)

## IOCs Provided by ANY.RUN TI Feeds

TI Feeds contain indicators along with additional info like the threat score, which signals IOCs’ reliability:

* 100: Highly reliable
* 50: Suspicious
* 75: Trustworthy

Here are the indicators you can find in ANY.RUN’s TI Feeds.

### IP addresses

Compromised IPs instantly signal of cybercriminal operations, they are often linked to Command-and-Control (C2) servers or phishing campaigns. By analyzing IP addresses, cybersecurity teams can proactively block malicious traffic and analyze attack patterns and tactics.

### Domains

Domains provide a higher-level view of malicious activity, often connecting multiple IPs or malware instances within a single campaign. ANY.RUN’s TI Feeds provide comprehensive information about domains, including all the details available for IP addresses, such as threat names, types, detection timestamps, and related file hashes.

### URLs

URL addresses serve as gateways to distribute malware, execute phishing campaigns, or redirect users to malicious content. By analyzing URLs, cybersecurity teams can uncover attack patterns, block harmful traffic, and prevent unauthorized access to systems and data.

## How ANY.RUN’s TI Feeds Are Enriched with Unique IOCs

There are several features of Threat Intelligence Feeds that make them stand out, one of them is the way we collect indicators. Here are the two methods we use to get the latest and the most accurate indicators that cannot be found elsewhere.

### IOCs Extracted from Malware Configurations

Configurations are a crucial part of any malware sample. They contain hardcoded IOCs such as command and control (C2) server addresses, encryption keys, and specific attack parameters. ANY.RUN’s Interactive Sandbox can automatically extract configs for dozens of malware families and pull out these valuable indicators.

[Take a look at this sandbox session](https://app.any.run/tasks/e5a0cb58-0b0a-4405-b09a-717913115fd3).

![](/cybersecurity-blog/wp-content/uploads...
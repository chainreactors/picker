---
title: From Forgotten Tool to Powerful Pivot: Using JA3 to Expose Attackers’ Infrastructure
url: https://any.run/cybersecurity-blog/ja3-hashes-threat-intelligence/
source: Over Security - Cybersecurity news aggregator
date: 2026-01-21
fetch_date: 2026-01-22T03:36:14.562548
---

# From Forgotten Tool to Powerful Pivot: Using JA3 to Expose Attackers’ Infrastructure

[![ANY.RUN's Cybersecurity Blog](/cybersecurity-blog/wp-content/uploads/2025/11/Logo-Blog_Header_238х46.svg)](/cybersecurity-blog/)

* [Register for free](https://app.any.run/#register)
* [Guides and tutorials](/cybersecurity-blog/guides/)
* [Research](/cybersecurity-blog/research/)
* Featured posts
  + [Malware Analysis in ANY.RUN:
    The Ultimate Guide](/cybersecurity-blog/malware-analysis-in-a-sandbox/)
  + [Salty2FA & Tycoon2FA Hybrid: A New Phishing Threat](/cybersecurity-blog/salty2fa-tycoon2fa-hybrid-phishing-2025/)
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

[![ANY.RUN's Cybersecurity Blog](/cybersecurity-blog/wp-content/uploads/2025/11/Logo-Blog_Header_238х46.svg)](/cybersecurity-blog/)

* [Register for free](https://app.any.run/#register)
* [Guides and tutorials](/cybersecurity-blog/guides/)
* [Research](/cybersecurity-blog/research/)
* Featured posts
  + [Malware Analysis in ANY.RUN:
    The Ultimate Guide](/cybersecurity-blog/malware-analysis-in-a-sandbox/)
  + [Salty2FA & Tycoon2FA Hybrid: A New Phishing Threat](/cybersecurity-blog/salty2fa-tycoon2fa-hybrid-phishing-2025/)
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

[![ANY.RUN's Cybersecurity Blog](/cybersecurity-blog/wp-content/uploads/2025/11/Logo-Blog_Header_238х46.svg)](/cybersecurity-blog/)

* + Search

![From Forgotten Tool to Powerful Pivot: Using JA3 to Expose Attackers’ Infrastructure ](/cybersecurity-blog/wp-content/uploads/2026/01/JA3_blog.png)

[Malware Analysis](/cybersecurity-blog/category/malware-analysis/)

# From Forgotten Tool to Powerful Pivot: Using JA3 to Expose Attackers’ Infrastructure

January 21, 2026

[Add comment](#comments-17852)
592 views
7 min read

[Home](/cybersecurity-blog/)[Malware Analysis](/cybersecurity-blog/category/malware-analysis/)

From Forgotten Tool to Powerful Pivot: Using JA3 to Expose Attackers’ Infrastructure

#### Recent posts

* [![](/cybersecurity-blog/wp-content/uploads/2026/01/JA3_blog-1024x497.png)

  #### From Forgotten Tool to Powerful Pivot: Using JA3 to Expose Attackers' Infrastructure

  592
  0](/cybersecurity-blog/ja3-hashes-threat-intelligence/)
* [![](/cybersecurity-blog/wp-content/uploads/2026/01/Malware-Trends-2025-1024x497.png)

  #### Malware Trends Report 2025: New Security Risks for Businesses in 2026

  1942
  0](/cybersecurity-blog/malware-trends-2025/)
* [![](/cybersecurity-blog/wp-content/uploads/2026/01/Intagration-ANYRUN-Tines-1024x497.png)

  #### ANY.RUN & Tines: Scale SOC and Meet SLAs with Powerful Automation

  2997
  0](/cybersecurity-blog/anyrun-tines-integration/)

[Home](/cybersecurity-blog/)[Malware Analysis](/cybersecurity-blog/category/malware-analysis/)

From Forgotten Tool to Powerful Pivot: Using JA3 to Expose Attackers’ Infrastructure

A growing skepticism around JA3 is evident, and quite understandable as well. Public lists are rarely updated, and initiatives like [JA3-fingerprints](https://sslbl.abuse.ch/ja3-fingerprints/) have been effectively frozen since 2021, creating the impression that this is a “yesterday’s technology.”

However, JA3 fingerprints have not disappeared. Sensors continue to collect them, they appear in reports and threat intelligence interfaces; it’s just that many teams treat them formally, as yet another field in logs without meaningful analysis.

## Key Takeaways

* JA3 fingerprints represent tool-level pyramid of pain, not disposable indicators like IPs or domains.

* Frequency analysis of JA3 hashes can surface new malicious tooling early, before signatures exist.

* JA3 can rarely be useful in isolation; context such as SNI, JA3S, URI, and host telemetry is critical.

* Threat hunting with JA3 enables analysts to cluster activity across samples, sessions, and campaigns.

* [Threat Intelligence Lookup](https://any.run/threat-intelligence-lookup/?utm_source=anyrunblog&utm_medium=article&utm_campaign=ja3-hashes-threat-intelligence&utm_term=200126&utm_content=linktotilookuplanding) operationalizes JA3 by enabling fast pivots from a hash to malware, infrastructure, and TTPs.

## JA3 Is Obsolete? That’s Only Half the Truth

Technically, JA3 is straightforward to compute. It is built from TLS ClientHello parameters (version, cipher suites, extensions, supported groups/elliptic curves, EC point formats), forming a JA3 string:

```
version,ciphers,extensions,groups,ec_point_formats
```

Lists are separated by “-”, fields by “,”, and an MD5 hash is calculated from this string. Unlike an IP, domain, or file hash, JA3 describes a long-term network profile of a tool that tends to repeat across many samples using the same network module.

This places JA3 at the Tools level in the Pyramid of Pain. The paradox is that threat intelligence feeds are often overloaded with “cheap” IOCs (IPs, domains, SHA256 hashes, etc.), while more resilient behavioral indicators like JA3 remain underutilized.

There is, however, a downside: the same JA3 can appear in both legitimate and malicious applications (if they share the same TLS library), and attackers can deliberately mimic the profiles of popular clients — Google Chrome, Firefox, or Edge. Treating JA3 as a classic [IOC](https://any.run/cybersecurity-blog/iocs-iobs-ioas-explained/) (“hash → malware family”) without context is therefore risky: without additional data (SNI, URI, JA3S, host information, or session behavior), it can confuse SOC analysts more than help them.

JA3 becomes truly powerful only when it is searchable, pivotable, and enriched with context. This is where ANY.RUN’s [Threat Intelligence Lookup](https://any.run/threat-intelligence-lookup/?utm_source=anyrunblog&utm_medium=article&utm_campaign=ja3-hashes-threat-intelligence&utm_term=200126&utm_content=linktotilookuplanding) can assist [SOC](https://any.run/cybersecurity-blog/threat-intel-board-cases/) and Threat Hunting (TH) teams in turning JA3 from a mere log field into a practical investigation driver: quickly finding related malware samples, [pivoting](https://any.run/cybersecurity-blog/threat-intelligence-pivoting/) across infrastructure, and validating hypotheses with context. The approach ANY.RUN offers — backed by real-world case studies — is described below.

## Applying JA3 in Practice

If a SOC systematically collects JA3 hashes and tracks their frequency, the dynamics of these values become informative on their own. A sudden spike in a previously rare JA3 hash often signals the emergence of a new tool, script, or automated client in the infrastructure. This anomalous growth enables early identification ...
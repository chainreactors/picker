---
title: Detecting Emerging Network Threats From Newly Observed Domains
url: https://buaq.net/go-131318.html
source: unSafe.sh - 不安全
date: 2022-10-18
fetch_date: 2025-10-03T20:04:26.200534
---

# Detecting Emerging Network Threats From Newly Observed Domains

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/c8c2b5fc7171ebf97e220f333e26e6cf.jpg)

Detecting Emerging Network Threats From Newly Observed Domains

This post is also available i
*2022-10-17 21:0:16
Author: [unit42.paloaltonetworks.com(查看原文)](/jump-131318.htm)
阅读量:33
收藏*

---

![DNS security conceptual image, covering topics including malicious newly observed domains](https://unit42.paloaltonetworks.com/wp-content/uploads/2022/10/Unit42-DNS-vulnerability-illustration_2.png)

This post is also available in:
[日本語 (Japanese)](https://unit42.paloaltonetworks.jp/malicious-newly-observed-domains/)

## Executive Summary

In May 2021, Palo Alto Networks launched a [proactive detector](https://unit42.paloaltonetworks.com/proactive-detector/) employing state-of-the-art methods to recognize malicious domains at the time of registration, with the aim of identifying them before they are able to engage in harmful activities. The system scans newly registered domains (NRDs) and detects potential network abuses. However, the proactive detector has limitations; created to only focus on new domains, it cannot obtain and analyze malicious indicators appearing after a domain's creation. In addition, in the cases of [adversaries leveraging or compromising aged domains to carry out attack traffic](https://unit42.paloaltonetworks.com/strategically-aged-domain-detection/), the proactive detector fails to capture the emerging threats because the malicious domains are out of the scope of being considered NRDs.

In addition to scanning for potential abuses at the time of registration, we have another great opportunity to detect malicious domains proactively when they start carrying attack traffic. A malicious domain may be registered long before it serves its attacking campaign and exposes indicators of abuse. Once the domain starts carrying malicious traffic, we can observe its DNS requests from passive DNS. To block network threats at this early stage, we developed a new proactive detector that ingests newly observed domains (NODs) to discover potential threats among them. The new detector leverages various machine learning techniques to expose suspicious behaviors based on various information about NODs, including their latest WHOIS records and DNS traffic.

This blog will illustrate how we collect and analyze the enriched features available for NODs to detect emerging threats. Our detector scans 2.6 million NODs and captures around 2,300 suspicious domains every day. To evaluate the performance, we cross-checked the detected domains against other threat intelligence from VirusTotal. 33.08% of the NODs detected by our system were also labeled as malicious by other sources later. But our detector's average discovery time is 4.79 days earlier than any VirusTotal vendor. Furthermore, we will explain the new system's benefits with case studies about various network abuses such as command and control (C2), phishing and unethical search engine optimization (SEO) practices. We will discuss how the proactive detector captured and blocked these threats based on different indicators for cybercriminal activities.

Once the proactive detector captures a potentially harmful domain, the knowledge is distributed from [DNS Security](https://www.paloaltonetworks.com/products/threat-detection-and-prevention/dns-security) to other [Palo Alto Networks Cloud-Delivered Security Services](https://www.paloaltonetworks.com/network-security/security-subscriptions), including [URL Filtering](https://docs.paloaltonetworks.com/pan-os/9-1/pan-os-admin/url-filtering) and [WildFire](https://www.paloaltonetworks.com/products/secure-the-network/wildfire).

## Table of Contents

[Detection Methods and High-level Statistics](#post-125343-_7o5fyycb25qw)

## Detection Methods and High-level Statistics

Palo Alto Networks collects passive DNS data from multiple sources, including our DNS Security service, as well as external providers from all around the world. Our cloud-based passive DNS system can ingest and process about 13 million DNS logs each day. The data ingestion pipeline catches the latest DNS data every hour and extracts the domains that haven't been seen carrying traffic before. These domains will be forwarded to the proactive detector to identify emerging threats. Our system can capture and scan about 2.6 million NODs daily.

![Number of newly observed domains shown in blue bars. Detection percentage shown in red line. Period covered is April 27, 2022-May 23, 2022](https://unit42.paloaltonetworks.com/wp-content/uploads/2022/10/chart.png)

Figure 1. Daily NOD amount and the percentage flagged as suspicious.

For each NOD, our centralized data collector will actively crawl all related information, including the latest WHOIS record and all DNS traffic requesting the domain and its subdomains. To leverage a variety of malicious indicators, we developed individual machine learning models to analyze different information. Specifically, we built a reputation system to evaluate WHOIS records, applied multiple classification models to DNS-related features, and used the bigram model to analyze hostnames. These models captured about 2,323 unique potentially malicious NODs every day. Figure 1 shows the daily NOD amount and detection rate from April 27-May 2, 2022.

![Number of days between when a domain is considered a newly registered domain (NRD) and when it is considered a newly observed domain (NOD). The graph shows the cumulative distribution function of their dormant periods. ](https://unit42.paloaltonetworks.com/wp-content/uploads/2022/10/chart-1.png)

Figure 2. Malicious NOD Dormant Period CDF.

To analyze attackers' behaviors, we compare the registration date of potentially malicious NODs and the date when they start hosting DNS traffic to see how long they keep silent before activation. Figure 2 presents the cumulative distribution function (CDF) of their dormant periods. The malicious domains start carrying traffic 5.57 days after their registration on average. However, during the period studied, our detector captured 152 NODs involving network abuses more than one year after creation – some domains can lie dormant for a significant amount of time before beginning malicious activity.

![The cumulative distribution function of how many days before any vendor of VirusTotal the proactive detector was able to flag malicious domains among newly observed domains. ](https://unit42.paloaltonetworks.com/wp-content/uploads/2022/10/chart-2.png)

Figure 3. Early discovery time CDF.

Of all suspicious NODs detected by the new proactive system, 37.11% were labeled as confirmed malicious 30 days later by Palo Alto Networks or other threat intelligence vendors in VirusTotal. Figure 3 shows the CDF of how many days before any vendor on VirusTotal the proactive detector was able to flag malicious domains. On average, our detector can capture these malicious domains and isolate their traffic 4.79 days before any VirusTotal vendor blocks them. Furthermore, we can discover 19.47% of malicious NODs more than a week earlier than others.

## Broader Visibility Into Emerging Internet Threats

One major benefit of our new proactive malicious NOD detector is that it extends visibility into emerging attacking domains. [The previous proactive detector](https://unit42.paloaltonetworks.com/proactive-detector/) scans threats among NRDs only. However, not all top-level domains (TLDs) disclose their new domains to the public. For example, hundreds of country-level TLDs are maintained by governments. Access to their complete domain list or WHOIS database is restricted.

Let's take a malicious domain...
---
title: AMD Warns of New Transient Scheduler Attacks Impacting a Wide Range of CPUs
url: https://thehackernews.com/2025/07/amd-warns-of-new-transient-scheduler.html
source: The Hacker News
date: 2025-07-11
fetch_date: 2025-10-06T23:51:32.689815
---

# AMD Warns of New Transient Scheduler Attacks Impacting a Wide Range of CPUs

#1 Trusted Cybersecurity News Platform

Followed by 5.20+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Subscribe – Get Latest News](#email-outer)

* [** Home](/)
* [** Newsletter](#email-outer)
* [** Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Data Breaches](/search/label/data%20breach)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Vulnerabilities](/search/label/Vulnerability)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Contact](/p/submit-news.html)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Free eBooks](https://thehackernews.tradepub.com)

About Site

* [About THN](/p/about-us.html)
* [Jobs](/p/careers-technical-writer-designer-and.html)
* [Advertise with us](/p/advertising-with-hacker-news.html)

Contact/Tip Us

[**

Reach out to get featured—contact us to send your exclusive story idea, research, hacks, or ask us a question or leave a comment/feedback!](/p/submit-news.html)

Follow Us On Social Media

[**](https://www.facebook.com/thehackernews)
[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.youtube.com/c/thehackernews?sub_confirmation=1)
[**](https://www.instagram.com/thehackernews/)

[** RSS Feeds](https://feeds.feedburner.com/TheHackersNews)
[** Email Alerts](#email-outer)

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjWa8tsMNqlevi1HGF1ALQRGIq7hROPFAbHd3R1RTEOe73T8_Q2xW_-91t2jSGjU5peiPb8QYblGp4igNW-u2Qmlxbp2BKzTVMSvyXDZJmC-BYpiiJHrcnG5drmSP97iZ9PVIf1DeEr7U-7vWpe4HXwfMjt8FGNgq5mOycOJluYr9wF7YOKrQY9MfArwgjt/s728-e100/ai-agent-security-d.png)](https://thehackernews.uk/ai-agent-security-d)

# [AMD Warns of New Transient Scheduler Attacks Impacting a Wide Range of CPUs](https://thehackernews.com/2025/07/amd-warns-of-new-transient-scheduler.html)

**Jul 10, 2025**Ravie LakshmananVulnerability / Hardware Security

[![AMD Transient Scheduler Attacks](data:image/png;base64... "AMD Transient Scheduler Attacks")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhhzU14QrbBVvoSlsDUEGP1kH6Owyx44EAsfefvjJegC6X7S-AKzqGyHCFHmZZTtCNirnBR4AEtTTKPI_YSa_djMPd0s41_wzcdCrKPKM4wwvDhJa8QPy1bGoEIzzqc5s_61q_SpM8m9K0t-Ju8wU8tfRgTx9QP9q5Ypa_7K5Xw24oyjm_qnipxh3u2sNtB/s790-rw-e365/amd.jpg)

Semiconductor company AMD is warning of a new set of vulnerabilities affecting a broad range of chipsets that could lead to information disclosure.

The flaws, collectively called Transient Scheduler Attacks (TSA), manifest in the form of a speculative side channel in its CPUs that leverage execution timing of instructions under specific microarchitectural conditions.

"In some cases, an attacker may be able to use this timing information to infer data from other contexts, resulting in information leakage," AMD [said](https://www.amd.com/en/resources/product-security/bulletin/amd-sb-7029.html) in an advisory.

The company said issues were uncovered as part of a study [published](https://www.microsoft.com/en-us/research/publication/enter-exit-page-fault-leak-testing-isolation-boundaries-for-microarchitectural-leaks/) by Microsoft and ETH Zurich researchers about [testing](https://github.com/microsoft/sca-fuzzer) modern CPUs against speculative execution attacks like [Meltdown](https://thehackernews.com/2025/05/researchers-expose-new-intel-cpu-flaws.html) and [Foreshadow](https://thehackernews.com/2020/08/foreshadow-processor-vulnerability.html) by stress testing isolation between security domains such as virtual machines, kernel, and processes.

Following responsible disclosure in June 2024, the issues have been assigned the below CVE identifiers -

* **CVE-2024-36350** (CVSS score: 5.6) - A transient execution vulnerability in some AMD processors may allow an attacker to infer data from previous stores, potentially resulting in the leakage of privileged information
* **CVE-2024-36357** (CVSS score: 5.6) - A transient execution vulnerability in some AMD processors may allow an attacker to infer data in the L1D cache, potentially resulting in the leakage of sensitive information across privileged boundaries
* **CVE-2024-36348** (CVSS score: 3.8) - A transient execution vulnerability in some AMD processors may allow a user process to infer the control registers speculatively even if UMIP[3] feature is enabled, potentially resulting in information leakage
* **CVE-2024-36349** (CVSS score: 3.8) - A transient execution vulnerability in some AMD processors may allow a user process to infer TSC\_AUX even when such a read is disabled, potentially resulting in information leakage

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

AMD has described TSA as a "new class of speculative side channels" affecting its CPUs, stating it has released microcode updates for impacted processors -

* 3rd Gen AMD EPYC Processors
* 4th Gen AMD EPYC Processors
* AMD Instinct MI300A
* AMD Ryzen 5000 Series Desktop Processors
* AMD Ryzen 5000 Series Desktop Processors with Radeon Graphics
* AMD Ryzen 7000 Series Desktop Processors
* AMD Ryzen 8000 Series Processors with Radeon Graphics
* AMD Ryzen Threadripper PRO 7000 WX-Series Processors
* AMD Ryzen 6000 Series Processors with Radeon Graphics
* AMD Ryzen 7035 Series Processors with Radeon Graphics
* AMD Ryzen 5000 Series Processors with Radeon Graphics
* AMD Ryzen 7000 Series Processors with Radeon Graphics
* AMD Ryzen 7040 Series Processors with Radeon Graphics
* AMD Ryzen 8040 Series Mobile Processors with Radeon Graphics
* AMD Ryzen 7000 Series Mobile Processors
* AMD EPYC Embedded 7003
* AMD EPYC Embedded 8004
* AMD EPYC Embedded 9004
* AMD EPYC Embedded 97X4
* AMD Ryzen Embedded 5000
* AMD Ryzen Embedded 7000
* AMD Ryzen Embedded V3000

The company also noted that instructions that read data from memory may experience what's referred to as "false completion," which occurs when CPU hardware expects the load instructions to complete quickly, but there exists a condition that prevents it from happening –

*In this case, dependent operations may be scheduled for execution before the false completion is detected. As the load did not actually complete, data associated with that load is considered invalid. The load will be re-executed later in order to complete successfully, and any dependent operations will re-execute with the valid data when it is ready.*

*Unlike other speculative behavior such as Predictive Store Forwarding, loads that experience a false completion do not result in an eventual pipeline flush. While the invalid data associated with a false completion may be forwarded to dependent operations, load and store instructions which consume this data will not attempt to fetch data or update any cache or TLB state. As such, the value of this invalid data cannot be inferred using standard transient side channel methods.*

*In processors affected by TSA, the invalid data may however affect the timing of other instructions being executed by the CPU in a way that may be detectable by an attacker.*

The chipmaker said it has identified two variants of TSA, TSA-L1 and TSA-SQ, based on the source of the invalid data associated with a false completion: either the L1 data cache or the CPU store queue.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

In a worst-case scenario, successful attacks carried out using TSA-L1 or TSA-SQ flaws could lead to information leakage from the operating system kernel to a user application, from a hypervisor to a guest virtual machine, or between two user applications.

While TSA-L1 is caused by an error in the way the L1 cache uses microtags for data-cache lookups, TSA-SQ vulnerabilities arise when a...
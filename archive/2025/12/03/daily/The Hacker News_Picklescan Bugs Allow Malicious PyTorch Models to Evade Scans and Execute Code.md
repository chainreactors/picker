---
title: Picklescan Bugs Allow Malicious PyTorch Models to Evade Scans and Execute Code
url: https://thehackernews.com/2025/12/picklescan-bugs-allow-malicious-pytorch.html
source: The Hacker News
date: 2025-12-03
fetch_date: 2025-12-04T03:19:40.850511
---

# Picklescan Bugs Allow Malicious PyTorch Models to Evade Scans and Execute Code

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

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi4PKjL50qMNKKq6z8Ofu7tXpz51soFtMEKzX6_qMTj-_Exp3EctK0Z7KiOlubgst1DxPrrk8TgthgjViGZmg4FlcOYG8L63G_dX8731tRGkOc42mbtdMv6KDyjdNKRdCPHkhUQJmcoxcFKLcQjeILTu-wEtAOXsTp7JyWMIuP0k1RJo9sZjTo5dYL8CyFQ/s728-e100/z-dd.png)](https://thehackernews.uk/zz--header-d)

# [Picklescan Bugs Allow Malicious PyTorch Models to Evade Scans and Execute Code](https://thehackernews.com/2025/12/picklescan-bugs-allow-malicious-pytorch.html)

**Dec 03, 2025**Ravie LakshmananMachine Learning / Vulnerability

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgtJ6D3cf9n4d0wB-0nReoF_JEgEraaVECS6V41EWkvsqwoa8YOSI5EnrHQ2MBHew0VbYvNg1pXuVpV7OQKTDKH4IWhlqyPZnVjA7RcLW_drNT2MVy3jupLSFT2ePAxBj0GaI3z3tNd4E2-gCBisHYhFUWXzyXocF0wGQCCLjV5W4Wl8FS5gLJX2GlQdGRZ/s790-rw-e365/pytorch.jpg)

Three critical security flaws have been disclosed in an open-source utility called Picklescan that could allow malicious actors to execute arbitrary code by loading untrusted PyTorch models, effectively bypassing the tool's protections.

[Picklescan](https://github.com/mmaitre314/picklescan), developed and maintained by Matthieu Maitre (@mmaitre314), is a security scanner that's designed to parse Python pickle files and detect suspicious imports or function calls, before they are executed. Pickle is a widely used serialization format in machine learning, including [PyTorch](https://docs.pytorch.org/tutorials/beginner/saving_loading_models.html), which uses the format to save and load models.

But pickle files can also be a [huge security risk](https://huggingface.co/docs/hub/en/security-pickle), as they can be used to automatically trigger the [execution of arbitrary Python code](https://thehackernews.com/2024/06/new-attack-technique-sleepy-pickle.html) when they are loaded. This necessitates that users and organizations load trusted models, or load model weights from TensorFlow and Flax.

The issues discovered by JFrog essentially make it possible to bypass the scanner, present the scanned model files as safe, and enable malicious code to be executed, which could then pave the way for a supply chain attack.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ransomware_dragon_d)

"Each discovered vulnerability enables attackers to evade PickleScan's malware detection and potentially execute a large-scale supply chain attack by distributing malicious ML models that conceal undetectable malicious code," security researcher David Cohen [said](https://jfrog.com/blog/unveiling-3-zero-day-vulnerabilities-in-picklescan/).

Picklescan, at its core, works by examining the pickle files at bytecode level and checking the results against a blocklist of known hazardous imports and operations to flag similar behavior. This approach, as opposed to allowlisting, also means that it prevents the tools from detecting any new attack vector and requires the developers to take into account all possible malicious behaviors.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEguE6W7IfUZK44IA2c0TKwrGeXRXcFAWP4Ru6NElYofJKLMiBkWnBQlt4TBI-AcBMX0pgDJxJYUIZ3X2S4pXntNerJarSf1-vF2tJ5PYJ3R6R-BBNnleSl_SvofL5wXEqAB5NLv3katx86D7w0_lsqTJG-kJG9DaO95ordcP_ep8BXJluk3vyqxfWGZv4j3/s790-rw-e365/poc.jpg)

The identified flaws are as follows -

* **[CVE-2025-10155](https://github.com/mmaitre314/picklescan/security/advisories/GHSA-jgw4-cr84-mqxg)** (CVSS score: 9.3/7.8) - A file extension bypass vulnerability that can be used to undermine the scanner and load the model when providing a standard pickle file with a PyTorch-related extension such as .bin or .pt
* **[CVE-2025-10156](https://github.com/mmaitre314/picklescan/security/advisories/GHSA-mjqp-26hc-grxg)** (CVSS score: 9.3/7.5) - A bypass vulnerability that can be used to disable ZIP archive scanning by introducing a Cyclic Redundancy Check (CRC) error
* **[CVE-2025-10157](https://github.com/mmaitre314/picklescan/security/advisories/GHSA-f7qq-56ww-84cr)** (CVSS score: 9.3/8.3) - A bypass vulnerability that can be used to undermine Picklescan's unsafe globals check, leading to arbitrary code execution by getting around a blocklist of dangerous imports

Successful exploitation of the aforementioned flaws could allow attackers to conceal malicious pickle payloads within files using common PyTorch extensions, deliberately introduce CRC errors into ZIP archives containing malicious models, or craft malicious PyTorch models with embedded pickle payloads to bypass the scanner.

Following responsible disclosure on June 29, 2025, the three vulnerabilities have been addressed in Picklescan [version 0.0.31](https://github.com/mmaitre314/picklescan/releases/tag/v0.0.31) released on September 9.

The development comes as SecDim and DCODX detailed another high-severity security flaw in the same utility ([CVE-2025-46417](https://nvd.nist.gov/vuln/detail/CVE-2025-46417), CVSS score: 7.5/7.1) that could be abused to bypass the tool's blocklist and [allow malicious pickle files](https://github.com/mmaitre314/picklescan/security/advisories/GHSA-93mv-x874-956g) to exfiltrate sensitive information via DNS when the model is loaded.

In a hypothetical attack scenario, an attacker can repurpose legitimate Python modules like linecache and ssl to read sensitive data from files like "/etc/passwd" using "linecache.getline()" and leverage "ssl.get\_server\_certificate()" to transmit the data to a domain under their control.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-security-insights-d)

"The leaked content appears in DNS logs. Scanning this payload with Picklescan 0.0.24 returns 'no issues found,' because linecache and ssl were not on the deny-list," SecDim [said](https://secdim.com/blog/post/cve-2025-46417-bypassing-ai-model-scanners-and-exfiltrate-sensitive-data-15594/).

The findings illustrate some key systemic issues, including the reliance on a single scanning tool, discrepancies in file-handling behavior between security tools and PyTorch, thereby rendering security architectures vulnerable to attacks.

"AI libraries like PyTorch grow more complex by the day, introducing new features, model formats, and execution pathways faster than security scanning tools can adapt," Cohen said. "This widening gap between innovation and protection leaves ...
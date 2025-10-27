---
title: SilentSync RAT Delivered via Two Malicious PyPI Packages Targeting Python Developers
url: https://thehackernews.com/2025/09/silentsync-rat-delivered-via-two.html
source: The Hacker News
date: 2025-09-19
fetch_date: 2025-10-02T20:23:43.650130
---

# SilentSync RAT Delivered via Two Malicious PyPI Packages Targeting Python Developers

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

# [SilentSync RAT Delivered via Two Malicious PyPI Packages Targeting Python Developers](https://thehackernews.com/2025/09/silentsync-rat-delivered-via-two.html)

**Sep 18, 2025**Ravie LakshmananMalware / Supply Chain Attack

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhAbjw1B2M-4If7F3tFoqS9Ra3GqczXVQOAbTf0vTt6qhOxIgMMtyiF1yqZhxx8rl12vpRQ0AyJgmwreH83TJuqiNzEGCAP3XFCMVvY1w6l8FVWXWfQHy27UkRx38y-wLYHoGOfTx-lOJ7yMYidbCR2dkQv4wDolBiHz8k_7z23Z5QHBarkSazwWc9oSlv1/s790-rw-e365/python.jpg)

Cybersecurity researchers have discovered two new malicious packages in the Python Package Index (PyPI) repository that are designed to deliver a remote access trojan called SilentSync on Windows systems.

"SilentSync is capable of remote command execution, file exfiltration, and screen capturing," Zscaler ThreatLabz's Manisha Ramcharan Prajapati and Satyam Singh [said](https://www.zscaler.com/blogs/security-research/malicious-pypi-packages-deliver-silentsync-rat). "SilentSync also extracts web browser data, including credentials, history, autofill data, and cookies from web browsers like Chrome, Brave, Edge, and Firefox."

The packages, now no longer available for download from PyPI, are listed below. They were both uploaded by a user named "CondeTGAPIS."

* sisaws (201 Downloads)
* secmeasure (627 Downloads)

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Zscaler said the package sisaws mimics the behavior of the legitimate Python package sisa, which is associated with Argentina's national health information system, Sistema Integrado de Información Sanitaria Argentino (SISA).

However, present in the library is a function called "gen\_token()" in the initialization script (\_\_init\_\_.py) that acts as a downloader for a next-stage malware. To achieve this, it sends a hard-coded token as input, and receives as response a secondary static token in a manner that's similar to the legitimate SISA API.

"If a developer imports the sisaws package and invokes the gen\_token function, the code will decode a hexadecimal string that reveals a curl command, which is then used to fetch an additional Python script," Zscaler said. "The Python script retrieved from PasteBin is written to the filename helper.py in a temporary directory and executed."

Secmeasure, in a similar fashion, masquerades as a "library for cleaning strings and applying security measures," but harbors embedded functionality to drop SilentSync RAT.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhca-YUpoK1wKFx2MQEwEQLWuzUpm7620c9Bn_OAai1VATi3a7WF-yuAhyhYHI9OilpFvu0d91Q0bO-bCSoYR5c-8aS5GJ94MUPBP4bcsaw2MgaPu5neuoeC2J65SdOJ_hklw6GPZ_1p8cZXCnR_CcBnaefXXJ_uOqICV8vzUDLYy4Hugh5Gr6K1EWY6XlF/s790-rw-e365/z-blog.jpg)

SilentSync is mainly geared towards infecting Windows systems at this stage, but the malware is also equipped with built-in features for Linux and macOS as well, making Registry modifications on Windows, altering the crontab file on Linux to execute the payload on system startup, and registering a LaunchAgent on macOS.

The package relies on the secondary token's presence to send an HTTP GET request to a hard-coded endpoint ("200.58.107[.]25") in order to receive Python code that's directly executed in memory. The server supports four different endpoints -

* /checkin, to verify connectivity
* /comando, to request commands to execute
* /respuesta, to send a status message
* /archivo, to send command output or stolen data

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The malware is capable of harvesting browser data, executing shell commands, capturing screenshots, and stealing files. It can also exfiltrate files and entire directories in the form of ZIP archives. Once the data is transmitted, all the artifacts are deleted from the host to sidestep detection efforts.

"The discovery of the malicious PyPI packages sisaws and secmeasure highlight the growing risk of supply chain attacks within public software repositories," Zscaler said. "By leveraging typosquatting and impersonating legitimate packages, threat actors can gain access to personally identifiable information (PII)."

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/) to read more exclusive content we post.

SHARE
[**](#link_share)
[**](#link_share)
[**](#link_share)
**

[**Tweet](#link_share)

[**Share](#link_share)

[**Share](#link_share)

**Share

**
[**Share on Facebook](#link_share)
[**Share on Twitter](#link_share)
[**Share on Linkedin](#link_share)
[**Share on Reddit](#link_share)
[**Share on Hacker News](#link_share)
[**Share on Email](#link_share)
[**Share on WhatsApp](#link_share)
[![Facebook Messenger](data:image/png;base64...)Share on Facebook Messenger](#link_share)
[**Share on Telegram](#link_share)

SHARE **

[Browser Data Theft](https://thehackernews.com/search/label/Browser%20Data%20Theft)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[Linux security](https://thehackernews.com/search/label/Linux%20security)[macos security](https://thehackernews.com/search/label/macos%20security)[Malware](https://thehackernews.com/search/label/Malware)[PyPI](https://thehackernews.com/search/label/PyPI)[Python](https://thehackernews.com/search/label/Python)[Remote Access Trojan](https://thehackernews.com/search/label/Remote%20Access%20Trojan)[supply chain attack](https://thehackernews.com/search/label/supply%20chain%20attack)[windows security](https://thehackernews.com/search/label/windows%20security)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:ima...
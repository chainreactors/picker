---
title: New Java-Based QuimaRAT MaaS Built to Run on Windows, Linux, and macOS
url: https://thehackernews.com/2026/07/new-java-based-quimarat-maas-built-to.html
source: The Hacker News
date: 2026-07-06
fetch_date: 2026-07-07T06:05:05.908487
---

# New Java-Based QuimaRAT MaaS Built to Run on Windows, Linux, and macOS

#1 Trusted Cybersecurity News Platform

Followed by 5.70+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Get the Latest News](#email-outer)

* [Home](/)
* [Newsletter](#email-outer)
* [Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Threat Intelligence](/search/label/Threat%20Intelligence)
* [Vulnerabilities](/search/label/Vulnerability)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Awards](https://awards.thehackernews.com/)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Awards](https://awards.thehackernews.com/)
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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgrKWHErc__Wn0forfQ5eJ5sIR1hVKCHCTeNQOaAX4lbygJ8S1Xpemx6JXl78dpwiT65DDBGURp48A3EemKzmli-jXPI3v1928MnJm-1j2ZPUaFXCvuySFhyphenhyphenKR-Li6fAinFT2bhLgsqUSNUR_ggMAnOHi3jD1qYWHXvueX8WdtxAd6GYety9cBGYABo18hX/s728-e100/tt-d.jpg)](https://thehackernews.uk/ai-zero-trust-h-d)

# [New Java-Based QuimaRAT MaaS Built to Run on Windows, Linux, and macOS](https://thehackernews.com/2026/07/new-java-based-quimarat-maas-built-to.html)

**Ravie Lakshmanan**Jul 06, 2026Malware / Endpoint Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhVcOvCD8qFylCqOCpN8Rnl9cnxNkIeGxNbVKzlsKXY_7Nuw2xvYsckNEHKVM5ntvT2JAureArFIyApOvGLu52wpCG1xbHO8Y5xBmOAkSI3RoyEegmlNxs_gJip32Uzv_inXS7seOeRB1d3mw9SNIggoqgIApupRF2etBx5U_IFkuQz4_WNBL0Q1oi1l77q/s1700-e365/javarat.jpg)

Cybersecurity researchers have flagged a novel Java-based remote access trojan (RAT) called **QuimaRAT** that's capable of targeting Windows, Linux, and macOS environments.

According to LevelBlue, the cross-platform malware is advertised under a malware-as-a-service (MaaS) model, costing anywhere between $150 for one month to $1,200 for lifetime access. Other subscription tiers include $300 for three months, $500 for six months, and $700 for twelve months.

"Built around a modular architecture, the RAT supports dynamic capability expansion through encrypted plugins that can be delivered, loaded, unloaded, and updated directly from its command-and-control (C2) infrastructure," the cybersecurity company [said](https://www.levelblue.com/blogs/spiderlabs-blog/novel-java-based-quimarat-targets-windows-macos-and-linux) in an analysis of the malware.

The malware author also advertises a builder capable of generating multiple output formats, including JAR, EXE, APP, SH, BAT, and VBS, indicating an attempt to help prospective customers package the client tailored for different environments and delivery scenarios.

The seller's post guarantees complete stealth on Windows and Linux, noting there are no visible user interface elements or desktop entries. On macOS, however, the threat actor includes a caveat that certain features like screen capture and input control require "user-granted admin permissions."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-vuln-protection-d)

Visiting their website, users are greeted by a pop-up message that states the platform "provides offensive security tooling intended exclusively for professional security research, authorized penetration testing, and controlled educational environments," warning them against using it for "malicious, unauthorized, or illegal purposes."

In all, the threat actor offers four tools -

* **Quima Control** (aka QuimaRAT), a remote administration tool with 74 Windows and 46 macOS and Linux modules
* **Quima Builder**, a modular builder and launcher toolkit with support for XLL, LNK, VBS, JS, BAT, DOCM, XLSM, MSC, CPL, and CHM file formats
* **Quima Loader**, a browser-cache payload delivery service to stage and deliver the malware payload
* **Quima Dropper**, an HTML/SVG payload generator

Quima Loader, particularly, is noteworthy, as it allows an operator to upload an EXE file through a dedicated panel and select a delivery format (e.g., HTA or LNK) and a landing page template (e.g., fake CAPTCHA check or software update alerts), after which the tool generates a stager link that, when opened by the victim in the browser, initiates the following sequence of actions, per the malware developer -

* The landing page is loaded, and the payload is fetched and held in the browser cache.
* A download button appears on the page.
* Clicking it saves a "small, clean loader file" that's trusted by the browser.
* Target runs the loader, which reads the cached payload.
* The main payload gets executed on the system, while bypassing SmartScreen protections on Windows.

"A RAT, a builder suite, a web loader, and an HTML dropper — each built around what Windows already trusts," the author behind the Quima suite claims on their website. "Native execution paths, system-owned resources, clean outputs. AV [antivirus] sees nothing unusual. Neither does the user."

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi46Hj1MqYMlfOtXufRJ0mDqPiqVRJ8hhQ4wWOUZcU7lHATjVLRYRcehU9phY0KLjYRWr4VFWCk25AMF1rjpc4Fkk2Dikg_rfxZldMj8m_QRsp5TNlw_eFPdrFWk5SzhyphenhyphenswwATBYuk73KsDi8IvyFwmsGFzKC8LnT9iII4RweIKvnIb8rkbUrEek2YytQBp/s1700-e365/quimat.jpg)

LevelBlue's [analysis](https://www.virustotal.com/gui/file/bb0fbcb1e47ec04aa55555f3769fbc6f09694de1e9baae59260356b26b5af6a7) suggests that QuimaRAT is organized as a modular Java project built using Apache Maven, while containing embedded Java Native Access (JNA) native libraries for Windows, Linux, and macOS across various architectures. It also decodes and parses an internal configuration file necessary for environment validation, persistence installation, and C2 initialisation.

"These native components allow the RAT to interact directly with low-level operating system APIs through C/C++ code, indicating intentional support for broad multi-platform deployment," researchers Chen Aviani and Nikita Kazymirskyi said.

Before execution, the malware ensures only one instance of the trojan is running on the infected machine at any given point in time. It achieves this by creating a lock file within the operating system's temporary directory and preventing other processes from using it simultaneously. If it detects that another RAT instance is already holding the lock to the file, it terminates execution.

QuimaRAT is designed to determine the current operating system name, using it to dictate the next course of action, including evading sandboxed and virtual environments, establishing persistence, and serving the main payload. Furthermore, it supports the ability to execute an additional embedded payload or decoy application along with the main RAT process if the functionality, named Binder, is enabled through the configuration.

[![Cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhr7HGzx4ULDSqwnN820pPGxlPxqqVxKgIrI5II1iWdspOL6yHZsdB5lWoXU3LmhIU4dtnph89fLZ0CxrQSs-ufs6Mo4eD-d-Cpx-DsV1G15eC-phLACF7hyaKSIH1zIdj3AuD7lHSHnVelmKVMoVV-_zvtJuod...
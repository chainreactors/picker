---
title: New Linux Rootkit PUMAKIT Uses Advanced Stealth Techniques to Evade Detection
url: https://thehackernews.com/2024/12/new-linux-rootkit-pumakit-uses-advanced.html
source: The Hacker News
date: 2024-12-14
fetch_date: 2025-10-06T19:43:43.579755
---

# New Linux Rootkit PUMAKIT Uses Advanced Stealth Techniques to Evade Detection

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

# [New Linux Rootkit PUMAKIT Uses Advanced Stealth Techniques to Evade Detection](https://thehackernews.com/2024/12/new-linux-rootkit-pumakit-uses-advanced.html)

**Dec 13, 2024**Ravie LakshmananLinux / Threat Analysis

[![Linux Rootkit PUMAKIT](data:image/png;base64... "Linux Rootkit PUMAKIT")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgHXY1PJ6CzHF7vXl-bcJc6Jh4utuRjvZQIQgG9CsGM4v_V-QfHNR5yx2BCf6R1YS9rij9zz-28Xd7TnSprXlvwc-7yqPUAXRM5c_V0Pq6u4GGKdr_CRlvhRBv5EmpSZ2xtwFpx9fyUQzISCqhmDdIWN004Ff82esgq9hTpG1URZx38M5iPvNUX8vtbIVtt/s790-rw-e365/malware.png)

Cybersecurity researchers have uncovered a new Linux rootkit called **PUMAKIT** that comes with capabilities to escalate privileges, hide files and directories, and conceal itself from system tools, while simultaneously evading detection.

"PUMAKIT is a sophisticated loadable kernel module (LKM) rootkit that employs advanced stealth mechanisms to hide its presence and maintain communication with command-and-control servers," Elastic Security Lab researchers Remco Sprooten and Ruben Groenewoud [said](https://www.elastic.co/security-labs/declawing-pumakit) in a technical report published Thursday.

The company's analysis [comes](https://www.virustotal.com/gui/file/30b26707d5fb407ef39ebee37ded7edeea2890fb5ec1ebfa09a3b3edfc80db1f) from [artifacts](https://www.virustotal.com/gui/file/71cc6a6547b5afda1844792ace7d5437d7e8d6db1ba995e1b2fb760699693f24) uploaded to the VirusTotal malware scanning platform earlier this September.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The internals of the malware is based on a multi-stage architecture that comprises a dropper component named "cron," two memory-resident executables ("/memfd:tgt" and "/memfd:wpn"), an LKM rootkit ("puma.ko"), and a shared object (SO) userland rootkit called Kitsune ("lib64/libs.so").

It also uses the internal Linux function tracer ([ftrace](https://www.kernel.org/doc/html/latest/trace/ftrace.html)) to hook into as many as 18 different system calls and various kernel functions such as "prepare\_creds," and "commit\_creds" to alter core system behaviors and accomplish its goals.

[![Linux Rootkit PUMAKIT](data:image/png;base64... "Linux Rootkit PUMAKIT")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiF2ULuMPvmCBSXfU1fBuMuDVGwItFriYDrhpIVCwsmnGXLE5QsACaceNuv_KCyuTUdMuh-bcWlES-d2_3U6K0RCWDVnhNH0pWqFvD4RY2Nf_TFk_2wAUei3bZ-D-w6hL-f_sl7xX2U5mb55r-qlkljT-tAVtWcs1wRU7sIg17nNpW5Dt5RysMOU-m1p3D7/s790-rw-e365/chart.png)

"Unique methods are used to interact with PUMA, including using the rmdir() syscall for privilege escalation and specialized commands for extracting configuration and runtime information," the researchers said.

"Through its staged deployment, the LKM rootkit ensures it only activates when specific conditions, such as secure boot checks or kernel symbol availability, are met. These conditions are verified by scanning the Linux kernel, and all necessary files are embedded as ELF binaries within the dropper."

The executable "/memfd:tgt" is the default Ubuntu Linux Cron binary sans any modifications, whereas "/memfd:wpn" is a loader for the rootkit assuming the conditions are satisfied. The LKM rootkit, for its part, contains an embedded SO file that's used to interact with the rookie from userspace.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Elastic noted that every stage of the infection chain is designed to hide the malware's presence and take advantage of memory-resident files and specific checks prior to unleashing the rootkit. The company told The Hacker News that it's not attributing PUMAKIT to any known threat actor or group at this stage.

"PUMAKIT is a complex and stealthy threat that uses advanced techniques like syscall hooking, memory-resident execution, and unique privilege escalation methods. Its multi-architectural design highlights the growing sophistication of malware targeting Linux systems," the researchers concluded.

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

[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[Elastic Security](https://thehackernews.com/search/label/Elastic%20Security)[linux](https://thehackernews.com/search/label/linux)[Malware](https://thehackernews.com/search/label/Malware)[privilege escalation](https://thehackernews.com/search/label/privilege%20escalation)[rootkit](https://thehackernews.com/search/label/rootkit)[Threat Analysis](https://thehackernews.com/search/label/Threat%20Analysis)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop Alert Chaos: Context Is the Key to Effective Incident Response](data:image/svg+xml;base64... "Stop Alert Chaos: Context Is the Key to Effective Incident Response")

Stop Alert Chaos: Context Is the Key to Effective Incident Response](https://thehackernews.com/2025/09/stop-alert-chaos-context-is-key-to.html)

[![Evolving Enterprise Defense to Secure the Modern AI Supply Chain](data:image/svg+xml;base64... "Evolving Enterprise Defense to Secure the Modern AI Supply Chain")

Evolving Enterprise Defense to Secure the Modern AI Supply Chain](https:/...
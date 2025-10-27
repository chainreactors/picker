---
title: GhostWrite: New T-Head CPU Bugs Expose Devices to Unrestricted Attacks
url: https://thehackernews.com/2024/08/ghostwrite-new-t-head-cpu-bugs-expose.html
source: The Hacker News
date: 2024-08-14
fetch_date: 2025-10-06T18:13:18.570075
---

# GhostWrite: New T-Head CPU Bugs Expose Devices to Unrestricted Attacks

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

# [GhostWrite: New T-Head CPU Bugs Expose Devices to Unrestricted Attacks](https://thehackernews.com/2024/08/ghostwrite-new-t-head-cpu-bugs-expose.html)

**Aug 13, 2024**Ravie LakshmananVulnerability / Hardware Security

[![CPU Bugs](data:image/png;base64... "CPU Bugs")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhW6zDUeW2wiVtgKzftxRDm_aRQd6NgLzcPCeu1oIW95Nf7yRURx9_lShRyD9yFOYQ8FOA-74lvxTwcand7fr0oxGMuv2DARo5dBSkl2QyqaM5TAO-qZ8vEMQVLtHU8eJkC9K6oFl9gXtxzTHH550w6A0KL_dODHyaalGyjbYoZJr53oZdOTv34UOhbBlEC/s790-rw-e365/chip.jpg)

A team of researchers from the CISPA Helmholtz Center for Information Security in Germany has disclosed an architectural bug impacting Chinese chip company T-Head's XuanTie C910 and C920 [RISC-V CPUs](https://riscv.org) that could allow attackers to gain unrestricted access to susceptible devices.

The vulnerability has been codenamed GhostWrite. It has been described as a direct CPU bug embedded in the hardware, as opposed to a side-channel or transient execution attack.

"This vulnerability allows unprivileged attackers, even those with limited access, to read and write any part of the computer's memory and to control peripheral devices like network cards," the researchers [said](https://ghostwriteattack.com). "GhostWrite renders the CPU's security features ineffective and cannot be fixed without disabling around half of the CPU's functionality."

CISPA found that the CPU has faulty instructions in its vector extension, an add-on to the RISC-V ISA designed to handle larger data values than the base Instruction Set Architecture (ISA).

These faulty instructions, which the researchers said operate directly on physical memory rather than virtual memory, could bypass the process isolation normally enforced by the operating system and hardware.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

As a result, an unprivileged attacker could weaponize this loophole to write to any memory location and sidestep security and isolation features to obtain full, unrestricted access to the device. It could be also be leak any memory content from a machine, including passwords.

"The attack is 100% reliable, deterministic, and takes only microseconds to execute," the researchers said. "Even security measures like Docker containerization or sandboxing cannot stop this attack. Additionally, the attacker can hijack hardware devices that use memory-mapped input/output (MMIO), allowing them to send any commands to these devices."

The most effective countermeasure for GhostWrite is to disable the entire vector functionality, which, however, severely impacts the CPU's performance and capabilities as it turns off roughly 50% of the instruction set.

"Luckily, the vulnerable instructions lie in the vector extension, which can be disabled by the operating system," the researchers noted. "This fully mitigates GhostWrite, but also fully disables vector instructions on the CPU."

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEicronanzKn_Il1dIbLj6qhz4GOPXKXB2Arh6YzN2N97ofcmZ93J7ZRPjiOMvrTt1L0Yvj_QKYgqWY0RGQCIxOfyoPFVbe-PqPf9N2ZGnzm3-noU8D1udRPSS8wLVhZAiXfRWvyUryW5-dR4qwWVGn_mV4lp-QHWbhJYGLZkeap-pA0BrtBb1sXTQ411Nt8/s790-rw-e365/demo.png)

"Disabling the vector extension significantly reduces the CPU's performance, especially for tasks that benefit from parallel processing and handling large data sets. Applications relying heavily on these features may experience slower performance or reduced functionality."

The disclosure comes as the Android Red Team at Google [revealed](https://defcon.org/html/defcon-32/dc-32-speakers.html#54457) more than nine flaws in Qualcomm's Adreno GPU that could permit an attacker with local access to a device to achieve privilege escalation and code execution at the kernel level. The weaknesses have since been patched by the chipset maker.

It also follows the discovery of a new [security flaw in AMD processors](https://labs.ioactive.com/2024/02/exploring-amd-platform-secure-boot.html) that could be potentially exploited by an attacker with kernel (aka Ring-0) access to elevate privileges and modify the configuration of System Management Mode ([SMM](https://thehackernews.com/2022/09/high-severity-firmware-security-flaws.html) or Ring-2) even when SMM Lock is enabled.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Dubbed [Sinkclose](https://ioactive.com/event/def-con-talk-amd-sinkclose-universal-ring-2-privilege-escalation/) by IOActive (aka CVE-2023-31315, CVSS score: 7.5), the vulnerability is said to have [remained undetected](https://defcon.org/html/defcon-32/dc-32-speakers.html#54490) for nearly two decades. Access to the highest privilege levels on a computer means it allows for disabling security features and installing persistent malware that can go virtually under the radar.

Speaking to WIRED, the company [said](https://www.wired.com/story/amd-chip-sinkclose-flaw/) the only way to remediate an infection would be to physically connect to the CPUs using a hardware-based tool known as SPI Flash programmer and scan the memory for malware installed using SinkClose.

"Improper validation in a model specific register (MSR) could allow a malicious program with ring0 access to modify SMM configuration while SMI lock is enabled, potentially leading to arbitrary code execution," AMD [noted](https://www.amd.com/en/resources/product-security/bulletin/amd-sb-7014.html) in an advisory, stating it intends to release updates to Original Equipment Manufacturers (OEM) to mitigate the issue.

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/) to read more exclusive content we post.

SHARE
[**](#link_share)
[**](#link_share)
[**](#link_share)
**

...
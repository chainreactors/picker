---
title: 9 Critical IP KVM Flaws Enable Unauthenticated Root Access Across Four Vendors
url: https://thehackernews.com/2026/03/9-critical-ip-kvm-flaws-enable.html
source: The Hacker News
date: 2026-03-18
fetch_date: 2026-03-19T04:21:06.460096
---

# 9 Critical IP KVM Flaws Enable Unauthenticated Root Access Across Four Vendors

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

[![Security Service Edge](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEguiZ85S7494GyqhFt9uP48C8ggEnb3bp9Qmsdv4LOYjNWfa98MKx17Dk7o1nJrEV3ai3edIGIgwt6oO5iJMmYLcyu6PojcvJnO4IfLhVK2dzGKFyEroFjKQhnp2hd5Cc6G4CynJRfb55aclnGwj7rse9jMncn_vu_tFqQZtHZH3Sb5dMXwRKN-kSVYUMzD/s1700-e365/ai-d.png)](https://thehackernews.uk/wiz-ai-security-d)

# [9 Critical IP KVM Flaws Enable Unauthenticated Root Access Across Four Vendors](https://thehackernews.com/2026/03/9-critical-ip-kvm-flaws-enable.html)

**Ravie Lakshmanan**Mar 18, 2026Network Security / Vulnerability

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg1w0kzOmqTtztN-mHI2uI1lo8OnX3r0r6sB1FuwEKJAIX3zudBP_BkZiFk5f3RbtXjTiARWWhhKkLp2szjQk5-IVk_sOHkyGlIAof66_UIY595IhcdGZQR2xjTHKQSqWAV0bkjCPlfqBdJqokmSkZID1kQxcI8M-LX2aWSDErd63Y86_UTo321Fm45dcDC/s1700-e365/ip.jpg)

Cybersecurity researchers have warned about the risks posed by low-cost IP KVM (Keyboard, Video, Mouse over Internet Protocol) devices, which can grant attackers extensive control over compromised hosts.

The nine vulnerabilities, discovered by **Eclypsium**, span four different products from GL-iNet Comet RM-1, Angeet/Yeeso ES3 KVM, Sipeed NanoKVM, and JetKVM. The most severe of them allow unauthenticated actors to gain root access or run malicious code.

"The common themes are damning: missing firmware signature validation, no brute-force protection, broken access controls, and exposed debug interfaces," researchers Paul Asadoorian and Reynaldo Vasquez Garcia [said](https://eclypsium.com/blog/your-kvm-is-the-weak-link-how-30-dollar-devices-can-own-your-entire-network/) in an analysis.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/not-fast-enough-d)

With IP KVM devices enabling remote access to the target machine's keyboard, video output, and mouse input at the BIOS/UEFI level, successful exploitation of vulnerabilities in these products can expose systems to potential takeover risks, undermining security controls put in place. The list of shortcomings is as follows -

* **[CVE-2026-32290](https://www.cve.org/CVERecord?id=CVE-2026-32290)** (CVSS score: 4.2) - An insufficient verification of firmware authenticity in GL-iNet Comet KVM (Fix being planned)
* **[CVE-2026-32291](https://www.cve.org/CVERecord?id=CVE-2026-32291)** (CVSS score: 7.6) - A Universal Asynchronous Receiver-Transmitter (UART) root access vulnerability in GL-iNet Comet KVM (Fix being planned)
* **[CVE-2026-32292](https://www.cve.org/CVERecord?id=CVE-2026-32292)** (CVSS score: 5.3) - An insufficient brute-force protection vulnerability in GL-iNet Comet KVM (Fixed in version 1.8.1 BETA)
* **[CVE-2026-32293](https://www.cve.org/CVERecord?id=CVE-2026-32293)** (CVSS score: 3.1) - An insecure initial provisioning via unauthenticated cloud connection vulnerability in GL-iNet Comet KVM (Fixed in version 1.8.1 BETA)
* **[CVE-2026-32294](https://www.cve.org/CVERecord?id=CVE-2026-32294)** (CVSS score: 6.7) - An insufficient update verification vulnerability in JetKVM (Fixed in version 0.5.4)
* **[CVE-2026-32295](https://www.cve.org/CVERecord?id=CVE-2026-32295)** (CVSS score: 7.3) - An insufficient rate limiting vulnerability in JetKVM (Fixed in version 0.5.4)
* **[CVE-2026-32296](https://www.cve.org/CVERecord?id=CVE-2026-32296)** (CVSS score: 5.4) - A configuration endpoint exposure vulnerability in Sipeed NanoKVM (Fixed in NanoKVM version 2.3.1 and NanoKVM Pro version 1.2.4)
* **[CVE-2026-32297](https://www.cve.org/CVERecord?id=CVE-2026-32297)** (CVSS score: 9.8) - A missing authentication for a critical function vulnerability in Angeet ES3 KVM leading to arbitrary code execution (No fix available)
* **[CVE-2026-32298](https://www.cve.org/CVERecord?id=CVE-2026-32298)** (CVSS score: 8.8) - An operating system command injection vulnerability in Angeet ES3 KVM leading to arbitrary command execution (No fix available)

"These are not exotic zero-days requiring months of reverse engineering," the researchers noted. "These are fundamental security controls that any networked device should implement. Input validation. Authentication. Cryptographic verification. Rate limiting. We are looking at the same class of failures that plagued early IoT devices a decade ago, but now on a device class that provides the equivalent of physical access to everything it connects to."

An adversary can weaponize these issues to inject keystrokes, boot from removable media to bypass disk encryption or Secure Boot protections, circumvent lock screens and access systems, and, more importantly, remain undetected by security software installed at the operating system level.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/fs-report-d)

This is not the first time vulnerabilities have been disclosed in IP KVM devices. In July 2025, Russian cybersecurity vendor Positive Technologies [flagged five flaws](https://global.ptsecurity.com/en/about/news/vulnerabilities-in-aten-international-switches-patched-with-the-assistance-of-pt-experts/) in ATEN International switches (CVE-2025-3710, CVE-2025-3711, CVE-2025-3712, CVE-2025-3713, and CVE-2025-3714) that could pave the way for denial-of-service or remote code execution.

What's more, such IP KVM switches like PiKVM or TinyPilot [have been put to use](https://thehackernews.com/2025/07/us-arrests-key-facilitator-in-north.html) by North Korean IT workers residing in countries like China to remotely connect to company-issued laptops hosted on laptop farms.

As mitigations, it's recommended to enforce multi-factor authentication (MFA) where supported, isolate KVM devices on a dedicated management VLAN, restrict internet access, use tools like Shodan to check for external exposure, monitor for unexpected network traffic to/from the devices, and keep the firmware up-to-date.

"A compromised KVM is not like a compromised IoT device sitting on your network. It is a direct, silent channel to every machine it controls," Eclypsium said. "An attacker who compromises the KVM can hide tools and backdoors on the device itself, consistently re-infecting host systems even after remediation."

"Since some firmware updates lack signature verification on most of these devices, a supply-chain attacker could tamper with the firmware at distribution time and have it per...
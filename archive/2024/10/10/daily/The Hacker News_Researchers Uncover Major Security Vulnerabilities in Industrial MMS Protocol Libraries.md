---
title: Researchers Uncover Major Security Vulnerabilities in Industrial MMS Protocol Libraries
url: https://thehackernews.com/2024/10/researchers-uncover-major-security.html
source: The Hacker News
date: 2024-10-10
fetch_date: 2025-10-06T18:58:51.036652
---

# Researchers Uncover Major Security Vulnerabilities in Industrial MMS Protocol Libraries

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

# [Researchers Uncover Major Security Vulnerabilities in Industrial MMS Protocol Libraries](https://thehackernews.com/2024/10/researchers-uncover-major-security.html)

**Oct 09, 2024**Ravie LakshmananIndustrial Security / Critical Infrastructure

[![Industrial MMS Protocol Libraries](data:image/png;base64... "Industrial MMS Protocol Libraries")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiEvdYu2KWcfkeisOEk5wr_l3J5EOYdKriWexaULjynaT0Y_GpRKHt2g54E-ohqRcaHPgPZs8HBm_J3HBIwhfnN7c3dAPG5gW7lBI44G-iM73P8ZcMXf2L01M_w_Tik6Ikd0cM3d0jiwIIHFWLwqd44aKrdl8Ygennd4uwPhLYcnCmJwaBJO-ryeWxMD-9t/s790-rw-e365/hackers.png)

Details have emerged about multiple security vulnerabilities in two implementations of the Manufacturing Message Specification ([MMS](https://en.wikipedia.org/wiki/Manufacturing_Message_Specification)) protocol that, if successfully exploited, could have severe impacts in industrial environments.

"The vulnerabilities could allow an attacker to crash an industrial device or in some cases, enable remote code execution," Claroty researchers Mashav Sapir and Vera Mens said in a new analysis.

MMS is an [OSI application layer messaging protocol](https://sisconet.com/wp-content/uploads/2016/03/mmsovrlg.pdf) that enables remote control and monitoring of industrial devices by exchanging supervisory control information in an application-agnostic manner.

Specifically, it allows for communication between intelligent electronic devices ([IEDs](https://en.wikipedia.org/wiki/Intelligent_electronic_device)) and supervisory control and data acquisition (SCADA) systems or programmable logic controllers (PLCs).

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The five shortcomings identified by the operational technology security company impact MZ Automation's [libIEC61850](https://libiec61850.com) library and Triangle MicroWorks' [TMW IEC 61850](https://www.trianglemicroworks.com/products/source-code-libraries/iec-61850-scl-pages/overview) library, and were patched in September and October 2022 following responsible disclosure -

* **[CVE-2022-2970](https://www.cisa.gov/news-events/ics-advisories/icsa-22-251-01)** (CVSS score: 10.0) - A stack-based buffer overflow vulnerability in libIEC61850 that could lead to a crash or remote code execution

* **[CVE-2022-2971](https://www.cisa.gov/news-events/ics-advisories/icsa-22-251-01)** (CVSS score: 8.6) - A type confusion vulnerability in libIEC61850 that could allow an attacker to crash the server with a malicious payload

* **[CVE-2022-2972](https://www.cisa.gov/news-events/ics-advisories/icsa-22-251-01)** (CVSS score: 10.0) - A stack-based buffer overflow vulnerability in libIEC61850 that could lead to a crash or remote code execution

* **[CVE-2022-2973](https://www.cisa.gov/news-events/ics-advisories/icsa-22-251-01)** (CVSS score: 8.6) - A null pointer deference vulnerability that could allow an attacker to crash the server

* **[CVE-2022-38138](https://www.cisa.gov/news-events/ics-advisories/icsa-22-249-01)** (CVSS score:7.5) - An access of uninitialized pointer vulnerability that allows an attacker to cause a denial-of-service (DoS) condition

Claroty's analysis also found that Siemens [SIPROTEC 5 IED](https://www.siemens.com/global/en/products/energy/energy-automation-and-smart-grid/protection-relays-and-control/siprotec-5.html) relied on an outdated version of SISCO's MMS-EASE stack for MMS support, which is susceptible to a DoS condition via a specially crafted packet ([CVE-2015-6574](https://nvd.nist.gov/vuln/detail/CVE-2015-6574), CVSS score: 7.5).

The German company has since updated its firmware with an updated version of the protocol stack as of December 2022, according to an [advisory](https://www.cisa.gov/news-events/ics-advisories/icsa-22-349-14) released by the U.S. Cybersecurity and Infrastructure Security Agency (CISA).

The research highlights the "gap between modern technology's security demands and the outdated, hard-to-replace protocols," Claroty said, urging vendors to follow security guidelines issued by CISA.

The disclosure comes weeks after Nozomi Networks detailed two vulnerabilities in the reference implementation of Espressif's ESP-NOW wireless protocol (CVE-2024-42483 and CVE-2024-42484) that could allow replay attacks and cause a DoS condition.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"Depending on the system being targeted, this vulnerability [CVE-2024-42483] can have profound consequences," it [said](https://www.nozominetworks.com/blog/flaws-in-espressif-esp-now-allow-attackers-to-replay-communications). "ESP-NOW is used in security systems such as building alarms, allowing them to communicate with motion sensors."

"In such a scenario, an attacker could exploit this vulnerability to replay a previously intercepted legitimate 'OFF' command, thereby disabling a motion sensor at will."

Alternatively, ESP-NOW's use in remote door openers, such as automatic gates and garage doors, could be weaponized to intercept an "OPEN" command and replay it at a later time to gain unauthorized access to buildings.

Back in August, Nozomi Networks also shed light on a set of unpatched 37 vulnerabilities in the OpenFlow libfluid\_msg parsing library, collectively dubbed FluidFaults, that an adversary could exploit to crash Software-Defined Networking (SDN) applications.

"An attacker with network visibility to an OpenFlow controller/forwarder can send a malicious OpenFlow network packet that leads to a denial-of-service (DoS) attack," the company [said](https://www.nozominetworks.com/blog/37-vulnerabilities-in-openflow-libfluid-msg-parsing-library).

In recent months, security flaws have also been [uncovered](https://www.nozominetworks.com/blog/four-vulnerabilities-in-beckhoff-twincat-bsd-could-allow-plc-logic-tampering-dos) in Beckhoff Automation's TwinCAT/BSD operating system that could expose PLCs to logic tampering, DoS attacks, and even command execution with roo...